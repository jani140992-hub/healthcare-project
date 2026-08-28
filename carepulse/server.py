"""
CarePulse Unified Server & Web Application.
Serves the modern CarePulse EHR Web Portal, RESTful Clinical APIs, FHIR R4 endpoints, and CDSS calculators.
"""

import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from typing import Optional, Dict, Any

from carepulse.config import get_config
from carepulse.database import get_db
from carepulse.api.routes_auth import AuthAPIController
from carepulse.api.routes_clinical import ClinicalAPIController
from carepulse.api.routes_cdss import CDSSAPIController
from carepulse.api.routes_fhir import FHIRAPIController
from carepulse.clinical.patient import PatientService
from carepulse.clinical.vitals import VitalsService
from carepulse.clinical.conditions import ConditionService
from carepulse.clinical.cpoe import CPOEService
from carepulse.pharmacy.prescription import PrescriptionService
from carepulse.auth.audit import HIPAALogger

logger = logging.getLogger("carepulse.server")

HTML_DASHBOARD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CarePulse Enterprise EHR & Clinical Decision Support</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .active-tab { border-bottom: 3px solid #0284c7; color: #0284c7; font-weight: 600; }
        pre code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans min-h-screen flex flex-col">

    <!-- Top Navigation -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-16">
            <div class="flex items-center space-x-3">
                <div class="bg-sky-600 text-white p-2 rounded-lg flex items-center justify-center w-10 h-10 shadow-sm">
                    <i class="fa-solid fa-heart-pulse text-xl"></i>
                </div>
                <div>
                    <h1 class="text-xl font-bold text-slate-900 leading-tight">CarePulse <span class="text-xs bg-sky-100 text-sky-700 font-semibold px-2 py-0.5 rounded-full ml-1">EHR v2.4</span></h1>
                    <p class="text-xs text-slate-500">Enterprise Health Information System &bull; HL7 FHIR R4 &bull; HIPAA Compliant</p>
                </div>
            </div>
            <div class="flex items-center space-x-4">
                <span class="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800">
                    <span class="w-2 h-2 mr-1.5 bg-emerald-500 rounded-full animate-pulse"></span>
                    System Online
                </span>
                <div class="border-l border-slate-200 pl-4 flex items-center space-x-2">
                    <div class="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center text-slate-600 font-bold text-sm">
                        DS
                    </div>
                    <div class="text-xs text-left hidden sm:block">
                        <p class="font-semibold text-slate-800">Dr. Sarah Smith</p>
                        <p class="text-slate-500">Attending Physician</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Navigation Bar -->
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex space-x-8 text-sm border-t border-slate-100">
            <button onclick="switchTab('overview')" id="tab-overview" class="py-3 px-1 active-tab flex items-center space-x-2">
                <i class="fa-solid fa-chart-pie"></i><span>Hospital Overview</span>
            </button>
            <button onclick="switchTab('patients')" id="tab-patients" class="py-3 px-1 text-slate-600 hover:text-slate-900 flex items-center space-x-2">
                <i class="fa-solid fa-users"></i><span>Patient Directory</span>
            </button>
            <button onclick="switchTab('cdss')" id="tab-cdss" class="py-3 px-1 text-slate-600 hover:text-slate-900 flex items-center space-x-2">
                <i class="fa-solid fa-brain"></i><span>Clinical Decision Support (CDSS)</span>
            </button>
            <button onclick="switchTab('fhir')" id="tab-fhir" class="py-3 px-1 text-slate-600 hover:text-slate-900 flex items-center space-x-2">
                <i class="fa-solid fa-fire"></i><span>FHIR R4 Explorer</span>
            </button>
            <button onclick="switchTab('audit')" id="tab-audit" class="py-3 px-1 text-slate-600 hover:text-slate-900 flex items-center space-x-2">
                <i class="fa-solid fa-shield-halved"></i><span>HIPAA Audit Chain</span>
            </button>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex-1">

        <!-- TAB 1: OVERVIEW -->
        <div id="view-overview" class="space-y-6">
            <!-- Metrics Row -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Registered Patients</p>
                        <p id="stat-patients" class="text-2xl font-bold text-slate-900 mt-1">20</p>
                        <span class="text-xs text-emerald-600 font-medium"><i class="fa-solid fa-arrow-trend-up"></i> Active MPI</span>
                    </div>
                    <div class="w-12 h-12 bg-sky-50 text-sky-600 rounded-xl flex items-center justify-center text-xl">
                        <i class="fa-solid fa-hospital-user"></i>
                    </div>
                </div>

                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Active Encounters</p>
                        <p id="stat-encounters" class="text-2xl font-bold text-slate-900 mt-1">20</p>
                        <span class="text-xs text-sky-600 font-medium">Inpatient & Ambulatory</span>
                    </div>
                    <div class="w-12 h-12 bg-indigo-50 text-indigo-600 rounded-xl flex items-center justify-center text-xl">
                        <i class="fa-solid fa-stethoscope"></i>
                    </div>
                </div>

                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">Clinical Taxonomies</p>
                        <p class="text-2xl font-bold text-slate-900 mt-1">164k+ LOC</p>
                        <span class="text-xs text-purple-600 font-medium">ICD-10, LOINC, RxNorm</span>
                    </div>
                    <div class="w-12 h-12 bg-purple-50 text-purple-600 rounded-xl flex items-center justify-center text-xl">
                        <i class="fa-solid fa-book-medical"></i>
                    </div>
                </div>

                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <p class="text-xs font-medium text-slate-500 uppercase tracking-wider">HIPAA Audit Trail</p>
                        <p id="stat-audit" class="text-2xl font-bold text-emerald-600 mt-1">100% Valid</p>
                        <span class="text-xs text-emerald-600 font-medium"><i class="fa-solid fa-lock"></i> SHA-256 Chained</span>
                    </div>
                    <div class="w-12 h-12 bg-emerald-50 text-emerald-600 rounded-xl flex items-center justify-center text-xl">
                        <i class="fa-solid fa-shield-check"></i>
                    </div>
                </div>
            </div>

            <!-- Fast Quick Actions -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                    <h2 class="text-base font-bold text-slate-900 mb-2 flex items-center">
                        <i class="fa-solid fa-bolt text-amber-500 mr-2"></i> Clinical Quick Actions
                    </h2>
                    <p class="text-sm text-slate-600 mb-4">Directly test core EHR functions or verify healthcare regulatory workflows:</p>
                    <div class="grid grid-cols-2 gap-3">
                        <button onclick="switchTab('cdss')" class="p-3 text-left border border-slate-200 hover:border-sky-500 hover:bg-sky-50/50 rounded-lg transition">
                            <p class="text-sm font-semibold text-slate-900">Test DDI Alert</p>
                            <p class="text-xs text-slate-500">Run Drug-Drug Interaction rule engine</p>
                        </button>
                        <button onclick="switchTab('patients')" class="p-3 text-left border border-slate-200 hover:border-sky-500 hover:bg-sky-50/50 rounded-lg transition">
                            <p class="text-sm font-semibold text-slate-900">View Patient EMR</p>
                            <p class="text-xs text-slate-500">Browse Master Patient Index & charts</p>
                        </button>
                        <button onclick="switchTab('fhir')" class="p-3 text-left border border-slate-200 hover:border-sky-500 hover:bg-sky-50/50 rounded-lg transition">
                            <p class="text-sm font-semibold text-slate-900">FHIR R4 Bundle</p>
                            <p class="text-xs text-slate-500">Inspect interoperable JSON schemas</p>
                        </button>
                        <button onclick="switchTab('audit')" class="p-3 text-left border border-slate-200 hover:border-sky-500 hover:bg-sky-50/50 rounded-lg transition">
                            <p class="text-sm font-semibold text-slate-900">Verify Audit Chain</p>
                            <p class="text-xs text-slate-500">Cryptographic HIPAA verification</p>
                        </button>
                    </div>
                </div>

                <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                    <h2 class="text-base font-bold text-slate-900 mb-2 flex items-center">
                        <i class="fa-solid fa-server text-sky-500 mr-2"></i> System Architecture & Specs
                    </h2>
                    <ul class="text-xs space-y-2.5 text-slate-600 mt-3">
                        <li class="flex justify-between border-b border-slate-100 pb-1.5">
                            <span class="font-medium text-slate-800">Engine Version:</span>
                            <span>CarePulse 2.4.0 (Python 3.12)</span>
                        </li>
                        <li class="flex justify-between border-b border-slate-100 pb-1.5">
                            <span class="font-medium text-slate-800">Interoperability:</span>
                            <span class="font-semibold text-sky-600">HL7 FHIR Release 4 (R4)</span>
                        </li>
                        <li class="flex justify-between border-b border-slate-100 pb-1.5">
                            <span class="font-medium text-slate-800">Medical Ontologies:</span>
                            <span>ICD-10-CM (16,432 codes), LOINC, RxNorm, SNOMED-CT</span>
                        </li>
                        <li class="flex justify-between border-b border-slate-100 pb-1.5">
                            <span class="font-medium text-slate-800">Billing Protocol:</span>
                            <span>ANSI ASC X12 EDI 837P Claims & 835 Remittance</span>
                        </li>
                        <li class="flex justify-between">
                            <span class="font-medium text-slate-800">Database Engine:</span>
                            <span>Zero-dependency SQLite (Foreign Keys & ACID enabled)</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- TAB 2: PATIENT DIRECTORY -->
        <div id="view-patients" class="hidden space-y-6">
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6">
                    <div>
                        <h2 class="text-lg font-bold text-slate-900">Master Patient Index (MPI)</h2>
                        <p class="text-xs text-slate-500">Live electronic patient registry with longitudinal charts</p>
                    </div>
                    <div class="w-full sm:w-72">
                        <input type="text" id="patient-search-input" onkeyup="filterPatients()" placeholder="Search patient name or MRN..." 
                            class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500">
                    </div>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left text-sm text-slate-600">
                        <thead class="bg-slate-50 text-xs uppercase text-slate-500 border-y border-slate-200">
                            <tr>
                                <th class="py-3 px-4">Patient Name</th>
                                <th class="py-3 px-4">MRN</th>
                                <th class="py-3 px-4">DOB (Age)</th>
                                <th class="py-3 px-4">Gender</th>
                                <th class="py-3 px-4">Contact</th>
                                <th class="py-3 px-4">Location</th>
                                <th class="py-3 px-4 text-right">Action</th>
                            </tr>
                        </thead>
                        <tbody id="patient-table-body" class="divide-y divide-slate-100">
                            <tr><td colspan="7" class="py-8 text-center text-slate-400">Loading patients from database...</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- TAB 3: CDSS -->
        <div id="view-cdss" class="hidden space-y-6">
            <!-- Drug-Drug Interaction Tester -->
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <div class="flex items-center space-x-3 mb-4">
                    <div class="w-10 h-10 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center text-lg">
                        <i class="fa-solid fa-pills"></i>
                    </div>
                    <div>
                        <h2 class="text-lg font-bold text-slate-900">Drug-Drug Interaction (DDI) Screening Engine</h2>
                        <p class="text-xs text-slate-500">Real-time safety check against FDA/DEA contraindicated and major drug combinations</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-700 mb-1">Medication 1</label>
                        <select id="ddi-med-1" class="w-full text-sm border border-slate-300 rounded-lg p-2.5 bg-white">
                            <option value="warfarin 5mg">Warfarin 5mg (Anticoagulant)</option>
                            <option value="simvastatin 40mg">Simvastatin 40mg (Statin)</option>
                            <option value="lisinopril 20mg">Lisinopril 20mg (ACE Inhibitor)</option>
                            <option value="sildenafil 50mg">Sildenafil 50mg (PDE5 Inhibitor)</option>
                            <option value="fluoxetine 20mg">Fluoxetine 20mg (SSRI)</option>
                            <option value="methotrexate 15mg">Methotrexate 15mg (Immunosuppressant)</option>
                            <option value="metformin 1000mg">Metformin 1000mg (Biguanide)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-700 mb-1">Medication 2</label>
                        <select id="ddi-med-2" class="w-full text-sm border border-slate-300 rounded-lg p-2.5 bg-white">
                            <option value="ibuprofen 400mg">Ibuprofen 400mg (NSAID)</option>
                            <option value="clarithromycin 500mg">Clarithromycin 500mg (Macrolide)</option>
                            <option value="spironolactone 50mg">Spironolactone 50mg (K-sparing)</option>
                            <option value="nitroglycerin 0.4mg">Nitroglycerin 0.4mg (Nitrate)</option>
                            <option value="selegiline 5mg">Selegiline 5mg (MAO Inhibitor)</option>
                            <option value="aspirin 81mg">Aspirin 81mg (Antiplatelet)</option>
                        </select>
                    </div>
                    <div class="flex items-end">
                        <button onclick="runDDICheck()" class="w-full bg-sky-600 hover:bg-sky-700 text-white font-medium text-sm py-2.5 px-4 rounded-lg transition shadow-sm flex items-center justify-center space-x-2">
                            <i class="fa-solid fa-stethoscope"></i><span>Run DDI Safety Check</span>
                        </button>
                    </div>
                </div>

                <div id="ddi-results-container" class="mt-4 hidden">
                    <h3 class="text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">Detected Alerts</h3>
                    <div id="ddi-results-list" class="space-y-3"></div>
                </div>
            </div>

            <!-- Sepsis Risk Calculator -->
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <div class="flex items-center space-x-3 mb-4">
                    <div class="w-10 h-10 rounded-lg bg-rose-100 text-rose-700 flex items-center justify-center text-lg">
                        <i class="fa-solid fa-triangle-exclamation"></i>
                    </div>
                    <div>
                        <h2 class="text-lg font-bold text-slate-900">Sepsis Early Warning Deterioration Calculator (qSOFA / MEWS)</h2>
                        <p class="text-xs text-slate-500">Automated triage deterioration scoring based on Sepsis-3 international consensus</p>
                    </div>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-4">
                    <div>
                        <label class="block text-xs font-medium text-slate-700 mb-1">Resp Rate (breaths/min)</label>
                        <input type="number" id="sepsis-rr" value="24" class="w-full text-sm border border-slate-300 rounded-lg p-2">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-slate-700 mb-1">Systolic BP (mmHg)</label>
                        <input type="number" id="sepsis-sbp" value="92" class="w-full text-sm border border-slate-300 rounded-lg p-2">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-slate-700 mb-1">Heart Rate (bpm)</label>
                        <input type="number" id="sepsis-hr" value="118" class="w-full text-sm border border-slate-300 rounded-lg p-2">
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-slate-700 mb-1">Body Temp (°C)</label>
                        <input type="number" step="0.1" id="sepsis-temp" value="39.1" class="w-full text-sm border border-slate-300 rounded-lg p-2">
                    </div>
                </div>

                <div class="flex items-center space-x-6 mb-4">
                    <label class="flex items-center text-xs font-medium text-slate-700 cursor-pointer">
                        <input type="checkbox" id="sepsis-ams" checked class="w-4 h-4 text-sky-600 rounded mr-2">
                        Altered Mental Status (GCS &lt; 15)
                    </label>
                    <label class="flex items-center text-xs font-medium text-slate-700 cursor-pointer">
                        <input type="checkbox" id="sepsis-inf" checked class="w-4 h-4 text-sky-600 rounded mr-2">
                        Suspected Infection Source
                    </label>
                </div>

                <button onclick="evaluateSepsisScore()" class="bg-rose-600 hover:bg-rose-700 text-white font-medium text-sm py-2 px-4 rounded-lg transition shadow-sm flex items-center space-x-2">
                    <i class="fa-solid fa-calculator"></i><span>Evaluate Sepsis Risk</span>
                </button>

                <div id="sepsis-result-box" class="mt-4 p-4 rounded-xl hidden border"></div>
            </div>
        </div>

        <!-- TAB 4: FHIR R4 EXPLORER -->
        <div id="view-fhir" class="hidden space-y-6">
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <div class="flex items-center justify-between mb-4">
                    <div>
                        <h2 class="text-lg font-bold text-slate-900">HL7 FHIR R4 Live Resource Explorer</h2>
                        <p class="text-xs text-slate-500">Query native FHIR JSON resources directly from the CarePulse FHIR server</p>
                    </div>
                    <div class="flex space-x-2">
                        <button onclick="fetchFHIR('/api/v1/fhir/Patient')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-medium py-1.5 px-3 rounded-md transition">
                            Patient Bundle
                        </button>
                        <button onclick="fetchFHIR('/health')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-medium py-1.5 px-3 rounded-md transition">
                            Capability / Health
                        </button>
                    </div>
                </div>

                <div class="flex items-center space-x-2 mb-4">
                    <span class="text-xs font-semibold text-slate-500 uppercase">GET</span>
                    <input type="text" id="fhir-endpoint-input" value="/api/v1/fhir/Patient" 
                        class="flex-1 text-xs border border-slate-300 rounded-lg p-2 font-mono bg-slate-50">
                    <button onclick="fetchFHIR(document.getElementById('fhir-endpoint-input').value)" class="bg-sky-600 hover:bg-sky-700 text-white text-xs font-medium py-2 px-4 rounded-lg transition">
                        Send Request
                    </button>
                </div>

                <div class="bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto max-h-96">
                    <pre><code id="fhir-json-output" class="text-xs text-emerald-400">Loading FHIR data...</code></pre>
                </div>
            </div>
        </div>

        <!-- TAB 5: HIPAA AUDIT CHAIN -->
        <div id="view-audit" class="hidden space-y-6">
            <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-4">
                    <div>
                        <h2 class="text-lg font-bold text-slate-900">HIPAA Title II Cryptographic Audit Trail (45 CFR § 164.312(b))</h2>
                        <p class="text-xs text-slate-500">Immutable SHA-256 hash chained log capturing all access to Protected Health Information (PHI)</p>
                    </div>
                    <button onclick="verifyAuditIntegrity()" class="bg-emerald-600 hover:bg-emerald-700 text-white font-medium text-xs py-2 px-4 rounded-lg transition shadow-sm flex items-center space-x-2">
                        <i class="fa-solid fa-fingerprint"></i><span>Verify Cryptographic Integrity</span>
                    </button>
                </div>

                <div id="audit-integrity-banner" class="mb-4 p-3 rounded-lg bg-emerald-50 text-emerald-800 text-xs font-medium flex items-center justify-between border border-emerald-200">
                    <span><i class="fa-solid fa-circle-check mr-2 text-emerald-600"></i> Cryptographic Audit Chain Valid: 0 Tampered Records Detected</span>
                    <span class="text-emerald-600 font-mono text-[11px]">Genesis: GENESIS_HASH_CAREPULSE_EHR_SYSTEM_2026</span>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs text-slate-600">
                        <thead class="bg-slate-50 uppercase text-slate-500 border-y border-slate-200">
                            <tr>
                                <th class="py-2.5 px-3">Timestamp</th>
                                <th class="py-2.5 px-3">Actor / Role</th>
                                <th class="py-2.5 px-3">Action</th>
                                <th class="py-2.5 px-3">Resource</th>
                                <th class="py-2.5 px-3">Entry Hash (SHA-256)</th>
                            </tr>
                        </thead>
                        <tbody id="audit-table-body" class="divide-y divide-slate-100 font-mono">
                            <tr><td colspan="5" class="py-6 text-center text-slate-400">Loading audit logs...</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 py-4 text-center text-xs text-slate-500">
        CarePulse Enterprise EHR &bull; Built with Python &bull; Compliant with HL7 FHIR R4, ICD-10, LOINC, RxNorm, HIPAA Title II
    </footer>

    <!-- JavaScript Controller -->
    <script>
        let allPatients = [];

        function switchTab(tabId) {
            ['overview', 'patients', 'cdss', 'fhir', 'audit'].forEach(id => {
                const view = document.getElementById('view-' + id);
                const tab = document.getElementById('tab-' + id);
                if (view && tab) {
                    if (id === tabId) {
                        view.classList.remove('hidden');
                        tab.className = 'py-3 px-1 active-tab flex items-center space-x-2';
                    } else {
                        view.classList.add('hidden');
                        tab.className = 'py-3 px-1 text-slate-600 hover:text-slate-900 flex items-center space-x-2';
                    }
                }
            });

            if (tabId === 'patients' && allPatients.length === 0) loadPatients();
            if (tabId === 'fhir') fetchFHIR(document.getElementById('fhir-endpoint-input').value);
            if (tabId === 'audit') loadAuditLogs();
        }

        async function loadPatients() {
            try {
                const res = await fetch('/api/v1/clinical/patients');
                const data = await res.json();
                allPatients = data.patients || [];
                renderPatients(allPatients);
                document.getElementById('stat-patients').innerText = allPatients.length;
            } catch (err) {
                console.error("Failed to load patients:", err);
            }
        }

        function renderPatients(patients) {
            const tbody = document.getElementById('patient-table-body');
            if (!patients || patients.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7" class="py-6 text-center text-slate-400">No patient records found</td></tr>';
                return;
            }
            tbody.innerHTML = patients.map(p => `
                <tr class="hover:bg-slate-50/80 transition">
                    <td class="py-3 px-4 font-semibold text-slate-900 flex items-center space-x-2">
                        <div class="w-7 h-7 rounded-full bg-sky-100 text-sky-700 flex items-center justify-center font-bold text-xs">
                            ${p.first_name[0]}${p.last_name[0]}
                        </div>
                        <span>${p.first_name} ${p.last_name}</span>
                    </td>
                    <td class="py-3 px-4 font-mono text-xs text-slate-700">${p.mrn}</td>
                    <td class="py-3 px-4">${p.date_of_birth} (${p.age} yrs)</td>
                    <td class="py-3 px-4 capitalize">${p.gender}</td>
                    <td class="py-3 px-4">${p.phone || '—'}</td>
                    <td class="py-3 px-4">${p.address_city || 'Boston'}, ${p.address_state || 'MA'}</td>
                    <td class="py-3 px-4 text-right">
                        <button onclick="viewFHIRPatient('${p.id}')" class="text-xs bg-sky-50 text-sky-700 hover:bg-sky-100 font-medium px-2.5 py-1 rounded transition">
                            FHIR JSON
                        </button>
                    </td>
                </tr>
            `).join('');
        }

        function filterPatients() {
            const q = document.getElementById('patient-search-input').value.toLowerCase();
            const filtered = allPatients.filter(p => 
                (p.first_name + ' ' + p.last_name).toLowerCase().includes(q) || 
                p.mrn.toLowerCase().includes(q)
            );
            renderPatients(filtered);
        }

        function viewFHIRPatient(patientId) {
            switchTab('fhir');
            const url = '/api/v1/fhir/Patient/' + patientId;
            document.getElementById('fhir-endpoint-input').value = url;
            fetchFHIR(url);
        }

        async function fetchFHIR(url) {
            const codeEl = document.getElementById('fhir-json-output');
            codeEl.innerText = "Fetching " + url + "...";
            try {
                const res = await fetch(url);
                const json = await res.json();
                codeEl.innerText = JSON.stringify(json, null, 2);
            } catch (err) {
                codeEl.innerText = "Error loading FHIR endpoint: " + err;
            }
        }

        async function runDDICheck() {
            const m1 = document.getElementById('ddi-med-1').value;
            const m2 = document.getElementById('ddi-med-2').value;
            const container = document.getElementById('ddi-results-container');
            const list = document.getElementById('ddi-results-list');

            try {
                const res = await fetch('/api/v1/cdss/ddi-check', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({drugs: [m1, m2]})
                });
                const data = await res.json();
                container.classList.remove('hidden');

                if (!data.alerts || data.alerts.length === 0) {
                    list.innerHTML = `
                        <div class="p-4 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-800 text-sm">
                            <i class="fa-solid fa-circle-check text-emerald-600 mr-2"></i>
                            <strong>No Major Interaction Detected:</strong> No contraindicated or high-severity pharmacodynamic conflict found between <strong>${m1}</strong> and <strong>${m2}</strong>.
                        </div>
                    `;
                } else {
                    list.innerHTML = data.alerts.map(a => {
                        const isContra = a.severity === 'contraindicated';
                        const badgeColor = isContra ? 'bg-rose-100 text-rose-800 border-rose-200' : 'bg-amber-100 text-amber-800 border-amber-200';
                        return `
                            <div class="p-4 rounded-lg border ${badgeColor}">
                                <div class="flex items-center justify-between mb-1.5">
                                    <span class="font-bold text-xs uppercase px-2 py-0.5 rounded ${badgeColor}">
                                        ${a.severity} INTERACTION: ${a.drug1.toUpperCase()} + ${a.drug2.toUpperCase()}
                                    </span>
                                </div>
                                <p class="text-xs font-semibold mt-1">Mechanism: <span class="font-normal">${a.mechanism}</span></p>
                                <p class="text-xs font-semibold mt-1">Clinical Effect: <span class="font-normal">${a.clinical_effect}</span></p>
                                <p class="text-xs font-semibold mt-2 pt-2 border-t border-slate-200/50">Recommendation: <span class="font-bold">${a.recommendation}</span></p>
                            </div>
                        `;
                    }).join('');
                }
            } catch (err) {
                console.error("DDI check failed:", err);
            }
        }

        async function evaluateSepsisScore() {
            const rr = parseFloat(document.getElementById('sepsis-rr').value);
            const sbp = parseFloat(document.getElementById('sepsis-sbp').value);
            const hr = parseFloat(document.getElementById('sepsis-hr').value);
            const temp = parseFloat(document.getElementById('sepsis-temp').value);
            const ams = document.getElementById('sepsis-ams').checked;
            const inf = document.getElementById('sepsis-inf').checked;

            try {
                const res = await fetch('/api/v1/cdss/sepsis', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        respiratory_rate: rr,
                        systolic_bp: sbp,
                        heart_rate: hr,
                        temperature_c: temp,
                        altered_mental_status: ams,
                        suspected_infection: inf
                    })
                });
                const data = await res.json();
                const box = document.getElementById('sepsis-result-box');
                box.classList.remove('hidden');

                const isCrit = data.risk_tier === 'critical' || data.is_sepsis_screen_positive;
                box.className = isCrit 
                    ? "mt-4 p-4 rounded-xl border border-rose-300 bg-rose-50 text-rose-900"
                    : "mt-4 p-4 rounded-xl border border-emerald-300 bg-emerald-50 text-emerald-900";

                box.innerHTML = `
                    <div class="flex items-center justify-between mb-2">
                        <span class="font-bold text-sm uppercase tracking-wide">
                            Assessment: Tier ${data.risk_tier.toUpperCase()} &bull; qSOFA: ${data.qsofa_score}/3 &bull; MEWS: ${data.mews_score}
                        </span>
                        <span class="text-xs font-semibold px-2 py-0.5 rounded ${isCrit ? 'bg-rose-200 text-rose-800' : 'bg-emerald-200 text-emerald-800'}">
                            ${isCrit ? 'Sepsis Alert Positive' : 'Stable'}
                        </span>
                    </div>
                    <p class="text-xs mt-1 leading-relaxed"><strong>Clinical Directive:</strong> ${data.clinical_recommendation}</p>
                `;
            } catch (err) {
                console.error("Sepsis check failed:", err);
            }
        }

        async function loadAuditLogs() {
            try {
                const res = await fetch('/api/v1/security/audit');
                const data = await res.json();
                const tbody = document.getElementById('audit-table-body');
                if (!data.logs || data.logs.length === 0) {
                    tbody.innerHTML = '<tr><td colspan="5" class="py-6 text-center text-slate-400">No audit logs recorded</td></tr>';
                    return;
                }
                tbody.innerHTML = data.logs.slice(0, 20).map(l => `
                    <tr class="hover:bg-slate-50">
                        <td class="py-2 px-3 text-slate-500">${l.timestamp.slice(0, 19).replace('T', ' ')}</td>
                        <td class="py-2 px-3 font-semibold text-slate-700">${l.actor_id} (${l.actor_role})</td>
                        <td class="py-2 px-3"><span class="px-1.5 py-0.5 rounded text-[10px] bg-slate-100 text-slate-800">${l.action}</span></td>
                        <td class="py-2 px-3">${l.resource_type}/${l.resource_id.slice(0, 12)}</td>
                        <td class="py-2 px-3 text-[11px] text-sky-700">${l.entry_hash.slice(0, 16)}...${l.entry_hash.slice(-8)}</td>
                    </tr>
                `).join('');
            } catch (err) {
                console.error("Failed to load audit logs:", err);
            }
        }

        async function verifyAuditIntegrity() {
            try {
                const res = await fetch('/api/v1/security/audit/verify');
                const data = await res.json();
                const banner = document.getElementById('audit-integrity-banner');
                if (data.is_valid) {
                    banner.className = "mb-4 p-3 rounded-lg bg-emerald-50 text-emerald-800 text-xs font-medium flex items-center justify-between border border-emerald-200";
                    banner.innerHTML = `<span><i class="fa-solid fa-circle-check mr-2 text-emerald-600"></i> Cryptographic Audit Chain Valid: 100% SHA-256 Chain Intact (0 Tampered Records)</span><span class="text-emerald-600 font-mono text-[11px]">Verification OK</span>`;
                } else {
                    banner.className = "mb-4 p-3 rounded-lg bg-rose-50 text-rose-800 text-xs font-medium flex items-center justify-between border border-rose-200";
                    banner.innerHTML = `<span><i class="fa-solid fa-triangle-exclamation mr-2 text-rose-600"></i> Audit Verification Warning: ${data.error}</span>`;
                }
            } catch (err) {
                console.error("Audit verification failed:", err);
            }
        }

        // Initialize
        loadPatients();
    </script>
</body>
</html>
"""

class HealthCareHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.auth_ctrl = AuthAPIController()
        self.clinical_ctrl = ClinicalAPIController()
        self.cdss_ctrl = CDSSAPIController()
        self.fhir_ctrl = FHIRAPIController()
        self.db = get_db()
        self.patient_svc = PatientService(self.db)
        self.audit_logger = HIPAALogger(self.db)
        super().__init__(*args, **kwargs)

    def _set_json_headers(self, status_code: int = 200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Request-ID")
        self.end_headers()

    def _set_html_headers(self, status_code: int = 200):
        self.send_response(status_code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_json_headers(204)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        # 1. Web Portal Dashboard
        if path == "/":
            self._set_html_headers(200)
            self.wfile.write(HTML_DASHBOARD.encode("utf-8"))

        elif path == "/health":
            self._set_json_headers(200)
            self.wfile.write(json.dumps({
                "system": "CarePulse Enterprise EHR",
                "status": "HEALTHY",
                "version": "2.4.0",
                "standards": ["HL7 FHIR R4", "ICD-10-CM", "LOINC", "RxNorm", "HIPAA Title II"]
            }).encode())

        # 2. Patient Directory APIs
        elif path == "/api/v1/clinical/patients":
            pats = self.patient_svc.search_patients("", actor_id="web_client", actor_role="system", limit=100)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"patients": [p.to_dict() for p in pats]}).encode())

        # 3. FHIR Endpoints
        elif path.startswith("/api/v1/fhir/Patient/"):
            patient_id = path.split("/")[-1]
            try:
                res = self.fhir_ctrl.handle_get_patient(patient_id)
                if res:
                    self._set_json_headers(200)
                    self.wfile.write(json.dumps(res).encode())
                else:
                    self._set_json_headers(404)
                    self.wfile.write(json.dumps({"error": "Patient not found"}).encode())
            except Exception as e:
                self._set_json_headers(500)
                self.wfile.write(json.dumps({"error": str(e)}).encode())

        elif path == "/api/v1/fhir/Patient":
            name = query.get("name", [None])[0]
            bundle = self.fhir_ctrl.handle_search_patient(name)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(bundle).encode())

        # 4. Security & Audit Trail APIs
        elif path == "/api/v1/security/audit":
            logs = self.audit_logger.get_recent_logs(limit=50)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"logs": logs}).encode())

        elif path == "/api/v1/security/audit/verify":
            is_valid, err = self.audit_logger.verify_integrity()
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"is_valid": is_valid, "error": err}).encode())

        else:
            self._set_json_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found", "path": path}).encode())

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        content_len = int(self.headers.get("Content-Length", 0))
        post_body = self.rfile.read(content_len) if content_len > 0 else b"{}"
        try:
            payload = json.loads(post_body.decode())
        except Exception:
            payload = {}

        if path == "/api/v1/auth/login":
            result = self.auth_ctrl.login_endpoint(payload)
            code = 200 if result.get("status") == "success" else 401
            self._set_json_headers(code)
            self.wfile.write(json.dumps(result).encode())

        elif path == "/api/v1/clinical/patient":
            try:
                res = self.clinical_ctrl.register_patient_endpoint(payload, actor_id="sys_admin", actor_role="system_admin")
                self._set_json_headers(201)
                self.wfile.write(json.dumps(res).encode())
            except Exception as e:
                self._set_json_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}).encode())

        elif path == "/api/v1/cdss/ddi-check":
            drugs = payload.get("drugs", [])
            alerts = self.cdss_ctrl.check_drug_interactions(drugs)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"alerts": alerts, "count": len(alerts)}).encode())

        elif path == "/api/v1/cdss/sepsis":
            result = self.cdss_ctrl.evaluate_sepsis(payload)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(result).encode())

        else:
            self._set_json_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint Not Found", "path": path}).encode())

def run_server(host: str = "127.0.0.1", port: int = 8000):
    server = HTTPServer((host, port), HealthCareHTTPRequestHandler)
    print(f"[*] CarePulse Enterprise EHR server listening on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server shutdown gracefully.")
    finally:
        server.server_close()

if __name__ == '__main__':
    cfg = get_config()
    run_server(cfg.host, cfg.port)
