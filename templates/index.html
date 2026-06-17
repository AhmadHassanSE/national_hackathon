<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HAALAT — Pakistan's Emergency Intelligence System</title>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;900&family=Noto+Nastaliq+Urdu:wght@400..700&family=JetBrains+Mono:wght@400;700&display=swap"
    rel="stylesheet">
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    :root {
      --bg-deep: #06080d;
      --bg-card: rgba(15, 19, 32, 0.8);
      --bg-card-hover: rgba(22, 28, 46, 0.9);
      --bg-input: #0e111d;
      --accent-red: #ff3b30;
      --accent-red-glow: rgba(255, 59, 48, 0.45);
      --accent-green: #00e676;
      --accent-green-glow: rgba(0, 230, 118, 0.4);
      --accent-gold: #ffb300;
      --accent-gold-glow: rgba(255, 179, 0, 0.45);
      --accent-blue: #00e5ff;
      --accent-blue-glow: rgba(0, 229, 255, 0.35);
      --text-primary: #f5f6fa;
      --text-muted: #808b9c;
      --border-glow: rgba(255, 255, 255, 0.05);
      --font-main: 'Outfit', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-deep);
      color: var(--text-primary);
      font-family: var(--font-main);
      overflow-x: hidden;
      min-height: 100vh;
      position: relative;
      transition: var(--transition);
    }

    /* Screen-flashing Red Border Glow for Critical Emergencies */
    body.panic-mode {
      animation: viewportAlert 1.5s infinite;
    }

    @keyframes viewportAlert {

      0%,
      100% {
        box-shadow: inset 0 0 15px rgba(255, 59, 48, 0.25);
      }

      50% {
        box-shadow: inset 0 0 35px rgba(255, 59, 48, 0.65);
      }
    }

    /* Ambient shifting background highlights */
    body::before {
      content: '';
      position: absolute;
      top: -20%;
      left: -20%;
      width: 140%;
      height: 140%;
      background:
        radial-gradient(circle at 10% 20%, rgba(255, 59, 48, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(0, 230, 118, 0.04) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(0, 229, 255, 0.03) 0%, transparent 50%);
      z-index: -1;
      pointer-events: none;
      animation: pulseBg 15s ease-in-out infinite alternate;
    }

    @keyframes pulseBg {
      0% {
        transform: scale(1) translate(0, 0);
      }

      100% {
        transform: scale(1.05) translate(1%, 1%);
      }
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }

    ::-webkit-scrollbar-track {
      background: transparent;
    }

    ::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 999px;
    }

    ::-webkit-scrollbar-thumb:hover {
      background: rgba(255, 255, 255, 0.2);
    }

    /* Layout framework */
    .container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 20px;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding: 14px 20px;
      background: var(--bg-card);
      border: 1px solid var(--border-glow);
      border-radius: 16px;
      backdrop-filter: blur(16px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .logo-container {
      background: linear-gradient(135deg, var(--accent-red), #b31414);
      width: 44px;
      height: 44px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 16px var(--accent-red-glow);
    }

    .logo-container i {
      font-size: 20px;
      color: #fff;
    }

    .brand-text h1 {
      font-size: 24px;
      font-weight: 900;
      letter-spacing: -0.02em;
      line-height: 1;
    }

    .urdu-logo-text {
      font-family: 'Noto Nastaliq Urdu', 'Urdu Typesetting', serif;
      font-size: 24px;
      font-weight: 700;
      background: linear-gradient(135deg, var(--accent-green), var(--accent-blue));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 8px rgba(0, 230, 118, 0.35));
      margin-left: 8px;
    }

    .brand-text span {
      font-size: 11px;
      color: var(--text-muted);
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }

    .system-status {
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .status-indicator {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 230, 118, 0.05);
      border: 1px solid rgba(0, 230, 118, 0.15);
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 600;
      color: var(--accent-green);
    }

    .status-dot {
      width: 6px;
      height: 6px;
      background-color: var(--accent-green);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--accent-green);
      animation: pulseDot 2s infinite;
    }

    @keyframes pulseDot {
      0% {
        transform: scale(0.95);
        opacity: 0.6;
      }

      50% {
        transform: scale(1.1);
        opacity: 1;
        box-shadow: 0 0 12px var(--accent-green);
      }

      100% {
        transform: scale(0.95);
        opacity: 0.6;
      }
    }

    .dashboard-grid {
      display: grid;
      grid-template-columns: 1.15fr 1.35fr;
      gap: 20px;
    }

    @media(max-width: 1024px) {
      .dashboard-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Glass Panels */
    .panel-card {
      background: var(--bg-card);
      border: 1px solid var(--border-glow);
      border-radius: 16px;
      backdrop-filter: blur(12px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
      padding: 20px;
      margin-bottom: 20px;
      transition: var(--transition);
    }

    .panel-card:hover {
      border-color: rgba(255, 255, 255, 0.08);
      background: var(--bg-card-hover);
    }

    .panel-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      padding-bottom: 10px;
    }

    .panel-title {
      font-size: 15px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .panel-title i {
      color: var(--accent-red);
    }

    /* Location Routing Block */
    .location-box {
      background: rgba(255, 255, 255, 0.015);
      border: 1px solid rgba(255, 255, 255, 0.04);
      border-radius: 12px;
      padding: 14px;
      margin-bottom: 16px;
    }

    .location-controls {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .btn-auto-detect {
      background: linear-gradient(135deg, #181d2f, #111422);
      color: var(--text-primary);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 14px;
      font-weight: 700;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: var(--transition);
    }

    .btn-auto-detect:hover {
      background: linear-gradient(135deg, var(--accent-blue), #00b0ff);
      color: #030408;
      border-color: transparent;
      box-shadow: 0 0 16px rgba(0, 229, 255, 0.35);
      transform: translateY(-1.5px);
    }

    .btn-auto-detect.loading {
      pointer-events: none;
      opacity: 0.85;
      background: #111422;
    }

    .btn-auto-detect.loading i {
      animation: spin 1s linear infinite;
    }

    @keyframes spin {
      100% {
        transform: rotate(360deg);
      }
    }

    .location-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      font-weight: 600;
      padding: 8px 12px;
      border-radius: 8px;
      margin-top: 8px;
      display: none;
    }

    .location-badge.verified {
      background: rgba(0, 230, 118, 0.07);
      border: 1px solid rgba(0, 230, 118, 0.2);
      color: var(--accent-green);
      display: flex;
    }

    .location-badge.error {
      background: rgba(255, 59, 48, 0.07);
      border: 1px solid rgba(255, 59, 48, 0.2);
      color: var(--accent-red);
      display: flex;
    }

    .manual-toggle {
      font-size: 12px;
      color: var(--accent-blue);
      text-decoration: underline;
      cursor: pointer;
      background: none;
      border: none;
      align-self: flex-start;
      margin-top: 2px;
      outline: none;
    }

    .manual-dropdowns {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-top: 10px;
      display: none;
    }

    .input-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .input-label {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }

    select,
    textarea,
    input[type="text"] {
      background: var(--bg-input);
      color: var(--text-primary);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 10px 12px;
      font-family: var(--font-main);
      font-size: 13px;
      transition: var(--transition);
      outline: none;
    }

    select:focus,
    textarea:focus,
    input[type="text"]:focus {
      border-color: var(--accent-blue);
      box-shadow: 0 0 12px rgba(0, 229, 255, 0.2);
    }

    /* Emergency description */
    .textarea-container {
      position: relative;
      margin-bottom: 16px;
    }

    textarea {
      width: 100%;
      resize: vertical;
      min-height: 100px;
      font-size: 14px;
      line-height: 1.5;
    }

    .input-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 10px;
      gap: 12px;
    }

    .record-controls {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn-record {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: var(--text-primary);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition);
    }

    .btn-record:hover {
      background: rgba(255, 59, 48, 0.12);
      border-color: var(--accent-red);
      color: var(--accent-red);
      transform: scale(1.05);
    }

    .btn-record.recording {
      background: var(--accent-red);
      color: #fff;
      border-color: transparent;
      animation: recordPulse 1.2s infinite alternate;
    }

    @keyframes recordPulse {
      0% {
        box-shadow: 0 0 4px var(--accent-red-glow);
      }

      100% {
        box-shadow: 0 0 16px var(--accent-red);
      }
    }

    .mic-status {
      font-size: 12px;
      color: var(--text-muted);
      max-width: 140px;
    }

    .success-text {
      color: var(--accent-green);
    }

    /* Web waveform indicator */
    .waveform {
      display: flex;
      align-items: center;
      gap: 3px;
      height: 20px;
      margin-left: 6px;
      display: none;
    }

    .waveform.active {
      display: flex;
    }

    .wave-bar {
      width: 3px;
      height: 6px;
      background: var(--accent-red);
      border-radius: 99px;
      animation: bounceWave 0.8s ease-in-out infinite alternate;
    }

    .wave-bar:nth-child(2) {
      animation-delay: 0.15s;
    }

    .wave-bar:nth-child(3) {
      animation-delay: 0.3s;
    }

    .wave-bar:nth-child(4) {
      animation-delay: 0.45s;
    }

    .wave-bar:nth-child(5) {
      animation-delay: 0.6s;
    }

    @keyframes bounceWave {
      0% {
        height: 4px;
      }

      100% {
        height: 16px;
      }
    }

    .btn-submit {
      flex: 1;
      background: linear-gradient(135deg, var(--accent-red), #cc1d15);
      color: #fff;
      border: none;
      border-radius: 10px;
      padding: 14px 20px;
      font-weight: 900;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      cursor: pointer;
      transition: var(--transition);
      box-shadow: 0 4px 16px var(--accent-red-glow);
    }

    .btn-submit:hover {
      box-shadow: 0 6px 24px rgba(255, 59, 48, 0.55);
      transform: translateY(-1.5px);
    }

    /* Mono multi-agent logger console */
    .console-card {
      background: #040508;
      border: 1px solid rgba(0, 229, 255, 0.12);
      border-radius: 12px;
      padding: 14px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      line-height: 1.6;
      height: 170px;
      overflow-y: auto;
      box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.75);
    }

    .console-line {
      margin-bottom: 5px;
      opacity: 0;
      transform: translateY(3px);
      animation: consoleFade 0.35s forwards;
    }

    @keyframes consoleFade {
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .console-timestamp {
      color: var(--accent-blue);
    }

    .console-agent {
      color: var(--accent-gold);
      font-weight: bold;
    }

    .console-message {
      color: var(--text-primary);
    }

    /* Right operational details */
    .operation-grid {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Triage Severity styling */
    .severity-widget {
      border-radius: 12px;
      padding: 16px;
      text-align: center;
      border: 1px solid var(--border-glow);
      background: rgba(255, 255, 255, 0.01);
      transition: var(--transition);
    }

    .severity-widget.sev-5 {
      background: linear-gradient(135deg, rgba(255, 59, 48, 0.15), rgba(0, 0, 0, 0.45));
      border: 2px solid var(--accent-red);
      box-shadow: 0 0 24px rgba(255, 59, 48, 0.2);
    }

    .severity-widget.sev-3-4 {
      background: linear-gradient(135deg, rgba(255, 179, 0, 0.12), rgba(0, 0, 0, 0.45));
      border: 2px solid var(--accent-gold);
      box-shadow: 0 0 16px rgba(255, 179, 0, 0.15);
    }

    .severity-widget.sev-1-2 {
      background: linear-gradient(135deg, rgba(0, 230, 118, 0.08), rgba(0, 0, 0, 0.45));
      border: 1px solid var(--accent-green);
    }

    .severity-widget .title {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-bottom: 4px;
    }

    .severity-widget.sev-5 .title {
      color: var(--accent-red);
    }

    .severity-widget.sev-3-4 .title {
      color: var(--accent-gold);
    }

    .severity-widget.sev-1-2 .title {
      color: var(--accent-green);
    }

    .severity-score {
      font-size: 36px;
      font-weight: 900;
      line-height: 1;
    }

    .severity-label {
      font-size: 13px;
      font-weight: 700;
      margin-top: 4px;
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }

    /* Coordinated dispatch widgets */
    .dispatch-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }

    @media(max-width: 600px) {
      .dispatch-container {
        grid-template-columns: 1fr;
      }
    }

    .resource-card {
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 170px;
      transition: var(--transition);
      background: rgba(255, 255, 255, 0.015);
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .resource-card.service-matched {
      background: linear-gradient(145deg, rgba(0, 229, 255, 0.06), rgba(0, 0, 0, 0.4));
      border: 1px solid rgba(0, 229, 255, 0.3);
      box-shadow: 0 4px 16px rgba(0, 229, 255, 0.05);
    }

    .resource-card.volunteer-matched {
      background: linear-gradient(145deg, rgba(0, 230, 118, 0.06), rgba(0, 0, 0, 0.4));
      border: 1px solid rgba(0, 230, 118, 0.3);
      box-shadow: 0 4px 16px rgba(0, 230, 118, 0.05);
    }

    .resource-badge {
      align-self: flex-start;
      font-size: 9.5px;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }

    .resource-badge.service {
      background: rgba(0, 229, 255, 0.1);
      color: var(--accent-blue);
      border: 1px solid rgba(0, 229, 255, 0.15);
    }

    .resource-badge.volunteer {
      background: rgba(0, 230, 118, 0.1);
      color: var(--accent-green);
      border: 1px solid rgba(0, 230, 118, 0.15);
    }

    .resource-name {
      font-size: 15px;
      font-weight: 800;
      margin-bottom: 5px;
      color: #fff;
    }

    .resource-meta {
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .resource-meta i {
      width: 14px;
    }

    .resource-call-btn {
      background: #0b0d14;
      border: 1px solid rgba(255, 255, 255, 0.06);
      color: var(--text-primary);
      text-decoration: none;
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 12px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: var(--transition);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .resource-card.service-matched .resource-call-btn {
      color: var(--accent-blue);
      border-color: rgba(0, 229, 255, 0.2);
    }

    .resource-card.service-matched .resource-call-btn:hover {
      background: var(--accent-blue);
      color: #030408;
      border-color: transparent;
      box-shadow: 0 4px 14px rgba(0, 229, 255, 0.35);
    }

    .resource-card.volunteer-matched .resource-call-btn {
      color: var(--accent-green);
      border-color: rgba(0, 230, 118, 0.2);
    }

    .resource-card.volunteer-matched .resource-call-btn:hover {
      background: var(--accent-green);
      color: #030408;
      border-color: transparent;
      box-shadow: 0 4px 14px rgba(0, 230, 118, 0.35);
    }

    /* Red Grounded Medical Protocol Checklist Card */
    .protocol-card {
      background: linear-gradient(135deg, rgba(255, 59, 48, 0.08), rgba(0, 0, 0, 0.6));
      border: 2px solid var(--accent-red);
      box-shadow: 0 4px 20px rgba(255, 59, 48, 0.1);
      border-radius: 12px;
      padding: 18px;
    }

    .protocol-title {
      font-size: 15px;
      font-weight: 800;
      color: var(--accent-red);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .protocol-steps {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .step-item {
      display: flex;
      gap: 12px;
      font-size: 14px;
      line-height: 1.5;
      color: var(--text-primary);
      cursor: pointer;
      user-select: none;
      padding: 8px 10px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.01);
      border: 1px solid rgba(255, 255, 255, 0.02);
      transition: var(--transition);
    }

    .step-item:hover {
      background: rgba(255, 59, 48, 0.04);
      border-color: rgba(255, 59, 48, 0.2);
    }

    .step-checkbox {
      width: 20px;
      height: 20px;
      border-radius: 6px;
      border: 2px solid rgba(255, 255, 255, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
      transition: var(--transition);
    }

    .step-item:hover .step-checkbox {
      border-color: var(--accent-green);
      background: rgba(0, 230, 118, 0.06);
    }

    .step-item.checked {
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.005);
      border-color: transparent;
    }

    .step-item.checked span {
      text-decoration: line-through;
      color: var(--text-muted);
    }

    .step-item.checked .step-checkbox {
      background-color: var(--accent-green);
      border-color: transparent;
    }

    .step-item.checked .step-checkbox i {
      color: #030408;
      font-size: 11px;
      display: block;
    }

    .step-checkbox i {
      display: none;
    }

    /* Radar Scanning Map display Container */
    .map-container {
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.06);
      height: 300px;
      background: #0b0d14;
      position: relative;
    }

    .map-container iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    /* Radar scan sweeps */
    .radar-sweep {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: linear-gradient(90deg, transparent, var(--accent-blue), transparent);
      z-index: 10;
      pointer-events: none;
      animation: radarSweep 2.2s linear infinite;
      box-shadow: 0 0 8px var(--accent-blue);
      display: none;
    }

    .map-container.scanning::after {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle, transparent 40%, rgba(0, 229, 255, 0.15) 100%);
      pointer-events: none;
      z-index: 9;
      animation: radarPulse 1.5s ease-out infinite;
    }

    .map-container.scanning .radar-sweep {
      display: block;
    }

    @keyframes radarPulse {
      0% {
        opacity: 0.3;
      }

      50% {
        opacity: 0.75;
      }

      100% {
        opacity: 0.3;
      }
    }

    @keyframes radarSweep {
      0% {
        top: 0;
      }

      100% {
        top: 100%;
      }
    }

    /* City incidents */
    .recent-incidents {
      max-height: 220px;
      overflow-y: auto;
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 12px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
    }

    th {
      padding: 10px 14px;
      text-align: left;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent-green);
      background: rgba(0, 230, 118, 0.03);
      position: sticky;
      top: 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      z-index: 2;
    }

    td {
      padding: 10px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.03);
      color: var(--text-muted);
    }

    tr:hover td {
      color: var(--text-primary);
      background: rgba(255, 255, 255, 0.01);
    }

    /* Report text box */
    .sitrep-box {
      background: rgba(255, 179, 0, 0.015);
      border-left: 3px solid var(--accent-gold);
      border-radius: 0 8px 8px 0;
      padding: 12px 16px;
      font-family: var(--font-mono);
      font-size: 11px;
      line-height: 1.6;
      white-space: pre-wrap;
      color: var(--text-muted);
      max-height: 180px;
      overflow-y: auto;
    }

    /* Event alert banners */
    .mass-alert-banner {
      background: linear-gradient(90deg, rgba(255, 59, 48, 0.15), rgba(255, 179, 0, 0.08));
      border: 1px solid var(--accent-gold);
      border-radius: 8px;
      padding: 12px 18px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      color: #fff;
      font-weight: 700;
      font-size: 13px;
      animation: alertFlash 1s infinite alternate;
      display: none;
    }

    @keyframes alertFlash {
      0% {
        box-shadow: 0 0 4px rgba(255, 179, 0, 0.2);
      }

      100% {
        box-shadow: 0 0 16px rgba(255, 179, 0, 0.5);
      }
    }

    /* Out of Service Modal */
    .unsupported-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(4, 5, 8, 0.96);
      backdrop-filter: blur(12px);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.4s ease;
    }

    .unsupported-overlay.active {
      opacity: 1;
      pointer-events: all;
    }

    .unsupported-card {
      background: linear-gradient(145deg, #121524, #0a0b12);
      border: 2px solid var(--accent-red);
      border-radius: 24px;
      padding: 36px;
      max-width: 500px;
      width: 90%;
      text-align: center;
      box-shadow: 0 0 40px rgba(255, 59, 48, 0.35);
      transform: scale(0.9);
      transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .unsupported-overlay.active .unsupported-card {
      transform: scale(1);
    }

    .unsupported-icon {
      font-size: 50px;
      color: var(--accent-red);
      margin-bottom: 16px;
      animation: heartBeat 1.5s infinite;
    }

    @keyframes heartBeat {

      0%,
      100% {
        transform: scale(1);
      }

      50% {
        transform: scale(1.08);
      }
    }

    .unsupported-card h2 {
      font-size: 22px;
      font-weight: 900;
      margin-bottom: 10px;
      letter-spacing: -0.01em;
    }

    .unsupported-card p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 24px;
    }

    .emergency-hotlines {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 24px;
    }

    .hotline-btn {
      background: rgba(255, 59, 48, 0.07);
      border: 1px solid rgba(255, 59, 48, 0.25);
      border-radius: 12px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      color: #fff;
      font-weight: 700;
      transition: var(--transition);
    }

    .hotline-btn:hover {
      background: var(--accent-red);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(255, 59, 48, 0.45);
      border-color: transparent;
    }

    .hotline-number {
      font-size: 20px;
      font-weight: 900;
    }

    .hotline-label {
      font-size: 11px;
      text-transform: uppercase;
      color: var(--text-muted);
    }

    .hotline-btn:hover .hotline-label {
      color: #fff;
    }

    .btn-close-modal {
      background: #151a2d;
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: var(--text-primary);
      border-radius: 8px;
      padding: 10px 18px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      transition: var(--transition);
    }

    .btn-close-modal:hover {
      background: rgba(255, 255, 255, 0.08);
    }
    .admin-btn:hover {
      background: rgba(0, 229, 255, 0.15) !important;
      border-color: var(--accent-blue) !important;
      box-shadow: 0 0 12px rgba(0, 229, 255, 0.3);
      transform: translateY(-1px);
    }
  </style>
</head>

<body>

  <!-- Geolocation Modal -->
  <div class="unsupported-overlay" id="unsupported-modal">
    <div class="unsupported-card">
      <div class="unsupported-icon">
        <i class="fa-solid fa-triangle-exclamation"></i>
      </div>
      <h2>Out of Service Region</h2>
      <p id="unsupported-modal-text">We detected coordinates outside our active coverage grid. We currently serve
        Karachi and Islamabad/Rawalpindi. Please immediately dial national emergency authorities.</p>

      <div class="emergency-hotlines">
        <a href="tel:1122" class="hotline-btn">
          <span class="hotline-number">1122</span>
          <span class="hotline-label">Rescue 1122</span>
        </a>
        <a href="tel:115" class="hotline-btn">
          <span class="hotline-number">115</span>
          <span class="hotline-label">Edhi Ambulance</span>
        </a>
        <a href="tel:1020" class="hotline-btn">
          <span class="hotline-number">1020</span>
          <span class="hotline-label">Chhipa Rescue</span>
        </a>
        <a href="tel:16" class="hotline-btn">
          <span class="hotline-number">16</span>
          <span class="hotline-label">Fire Brigade</span>
        </a>
      </div>

      <button class="btn-close-modal" id="close-modal-btn">Manual Override</button>
    </div>
  </div>

  <div class="container">

    <!-- Header -->
    <header>
      <div class="brand">
        <div class="logo-container">
          <i class="fa-solid fa-truck-medical"></i>
        </div>
        <div class="brand-text">
          <div style="display: flex; align-items: center;">
            <h1>HAALAT</h1>
            <span class="urdu-logo-text">حالت</span>
          </div>
          <span>Emergency Intelligence Console</span>
        </div>
      </div>
      <div class="system-status" style="display: flex; align-items: center; gap: 16px;">
        <a href="/admin" class="nav-link admin-btn" style="color: var(--accent-blue); text-decoration: none; font-size: 12px; font-weight: 700; border: 1px solid rgba(0, 229, 255, 0.2); padding: 6px 12px; border-radius: 8px; background: rgba(0, 229, 255, 0.05); display: flex; align-items: center; gap: 6px; transition: all 0.3s ease;">
          <i class="fa-solid fa-user-shield"></i> Admin Dashboard
        </a>
        <div class="status-indicator">
          <div class="status-dot"></div>
          7-AGENT SYSTEM ONLINE
        </div>
      </div>
    </header>

    <!-- Dashboard Grid -->
    <div class="dashboard-grid">

      <!-- Input Panel -->
      <div class="operation-grid">

        <!-- Submission block -->
        <div class="panel-card">
          <div class="panel-header">
            <h2 class="panel-title"><i class="fa-solid fa-bullhorn"></i> Submit Emergency Report</h2>
          </div>

          <!-- GPS detection box -->
          <div class="location-box">
            <div class="location-controls">
              <button class="btn-auto-detect" id="detect-btn" type="button">
                <i class="fa-solid fa-location-crosshairs"></i> Auto-Detect My Location
              </button>

              <div class="location-badge" id="location-badge"></div>

              <button class="manual-toggle" id="manual-toggle-btn" type="button">Manually select area</button>

              <div class="manual-dropdowns" id="manual-dropdowns">
                <div class="input-group">
                  <label class="input-label">Region</label>
                  <select id="region-select">
                    <option value="karachi">Karachi</option>
                    <option value="islamabad">Islamabad</option>
                    <option value="rawalpindi">Rawalpindi</option>
                  </select>
                </div>
                <div class="input-group">
                  <label class="input-label">Area / Sector</label>
                  <select id="area-select">
                    <!-- Dynamically loaded -->
                  </select>
                </div>
              </div>
            </div>
          </div>

          <!-- Message entry -->
          <div class="textarea-container">
            <label class="input-label" style="display:block; margin-bottom: 6px;">Describe symptoms or situation</label>
            <textarea id="text-input"
              placeholder="Describe symptoms or incident context in Urdu, Roman Urdu or English... e.g. Humare padosi ki dukan me aag lag gayi hai, or dhuan uth raha hai Garden East me."></textarea>
          </div>

          <div class="input-actions">
            <div class="record-controls">
              <button class="btn-record" id="record-btn" type="button" title="Record Voice Audio">
                <i class="fa-solid fa-microphone"></i>
              </button>
              <div class="waveform" id="waveform">
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
                <div class="wave-bar"></div>
              </div>
              <span class="mic-status" id="mic-status">Ready</span>
            </div>

            <input type="hidden" id="audio-path-input" value="">
            <input type="hidden" id="lat-input" value="">
            <input type="hidden" id="lng-input" value="">

            <button class="btn-submit" id="submit-btn">🚨 Dispatch Report</button>
          </div>
        </div>

        <!-- Logging Terminal -->
        <div class="panel-card" style="margin-bottom: 0;">
          <div class="panel-header">
            <h2 class="panel-title" style="color: var(--accent-blue);"><i class="fa-solid fa-terminal"></i> Multi-Agent
              Command Console</h2>
          </div>
          <div class="console-card" id="console-display">
            <div class="console-line">
              <span class="console-timestamp">[SYSTEM]</span>
              <span class="console-agent">SYSTEM:</span>
              <span class="console-message">Awaiting incident report submission...</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Operational outputs -->
      <div class="operation-grid">

        <!-- Result summary -->
        <div class="panel-card" id="results-panel" style="display: none;">
          <div class="panel-header">
            <h2 class="panel-title"><i class="fa-solid fa-truck-ramp-box"></i> Emergency Dispatch Details</h2>
          </div>

          <div style="display:flex; flex-direction:column; gap:14px;">
            <!-- Severity Display -->
            <div class="severity-widget" id="severity-widget">
              <div class="title" id="severity-widget-title">Triage Status</div>
              <div class="severity-score" id="severity-score">--</div>
              <div class="severity-label" id="severity-label">Awaiting Assessment</div>
            </div>

            <!-- Report Description -->
            <div class="report-desc-card" id="report-desc-card" style="display:none; background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; padding: 14px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
                <span style="font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 700; letter-spacing: 0.05em;"><i class="fa-solid fa-file-invoice"></i> Report Description</span>
                <span class="badge" id="report-lang-badge" style="font-size: 10px; background: rgba(0, 229, 255, 0.1); color: var(--accent-blue); padding: 2px 6px; border-radius: 4px; font-weight: 700;">English</span>
              </div>
              <p id="report-desc-text" style="margin: 0; font-size: 13px; line-height: 1.5; color: #fff;"></p>
            </div>

            <!-- Mass Event alert -->
            <div class="mass-alert-banner" id="mass-alert-banner">
              <i class="fa-solid fa-triangle-exclamation"></i>
              <span>MASS EVENT CLUSTER TRIGGERED IN AREA</span>
            </div>

            <!-- Dispatch Cards -->
            <div class="dispatch-container">
              <!-- Service Card -->
              <div class="resource-card" id="service-card">
                <div>
                  <div class="resource-badge service">Emergency Service</div>
                  <div class="resource-name" id="service-name">---</div>
                  <div class="resource-meta">
                    <span id="service-type"><i class="fa-solid fa-hospital"></i> Hospital</span>
                    <span id="service-distance"><i class="fa-solid fa-route"></i> Distance: ---</span>
                  </div>
                </div>
                <a href="tel:" class="resource-call-btn" id="service-call-btn">
                  <i class="fa-solid fa-phone"></i> Dial Dispatch
                </a>
              </div>

              <!-- Volunteer Card -->
              <div class="resource-card" id="volunteer-card">
                <div>
                  <div class="resource-badge volunteer">First Responder</div>
                  <div class="resource-name" id="volunteer-name">---</div>
                  <div class="resource-meta">
                    <span id="volunteer-skills"><i class="fa-solid fa-user-doctor"></i> Skills: ---</span>
                    <span id="volunteer-distance"><i class="fa-solid fa-route"></i> Distance: ---</span>
                  </div>
                </div>
                <a href="tel:" class="resource-call-btn" id="volunteer-call-btn">
                  <i class="fa-solid fa-phone"></i> Call Volunteer
                </a>
              </div>
            </div>

            <!-- Red First Aid Checklist Card -->
            <div class="protocol-card" id="protocol-card" style="display:none;">
              <div class="protocol-title">
                <i class="fa-solid fa-kit-medical"></i>
                <span>First Aid Guidance: <span id="protocol-name">Protocol</span></span>
              </div>
              <div class="protocol-steps" id="protocol-steps-list">
                <!-- Populated dynamically -->
              </div>
            </div>

          </div>
        </div>

        <!-- Operations Map -->
        <div class="panel-card">
          <div class="panel-header" style="display: flex; justify-content: space-between; align-items: center;">
            <h2 class="panel-title" style="margin: 0;"><i class="fa-solid fa-map-location-dot"></i> Real-Time Operations Map</h2>
            <div class="map-view-toggle" style="display: flex; gap: 4px; background: rgba(255,255,255,0.04); padding: 3px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.06);">
              <button class="toggle-btn active" id="btn-show-map" style="background: var(--accent-blue); color: #000; border: none; border-radius: 6px; padding: 4px 10px; font-size: 11px; font-weight: 700; cursor: pointer; transition: all 0.2s ease;">Map</button>
              <button class="toggle-btn" id="btn-show-streetview" style="background: transparent; color: var(--text-muted); border: none; border-radius: 6px; padding: 4px 10px; font-size: 11px; font-weight: 700; cursor: pointer; transition: all 0.2s ease;">Street View</button>
            </div>
          </div>
          <div class="map-container" id="map-container">
            <div class="radar-sweep"></div>
            <div
              style="display:flex; align-items:center; justify-content:center; height:100%; color:var(--text-muted); font-size:13px; flex-direction:column; gap:10px;">
              <i class="fa-solid fa-location-dot" style="font-size:24px; color:var(--accent-red);"></i>
              Detect location or report emergency to initialize live operations map.
            </div>
          </div>
        </div>

        <!-- Memory tracking -->
        <div class="panel-card" style="margin-bottom: 0;">
          <div class="panel-header">
            <h2 class="panel-title"><i class="fa-solid fa-database"></i> City Memory incident logs</h2>
          </div>
          <div class="recent-incidents" id="recent-incidents-display">
            <table>
              <thead>
                <tr>
                  <th>Time</th>
                  <th>Area</th>
                  <th>Type</th>
                  <th>Severity</th>
                </tr>
              </thead>
              <tbody id="incidents-table-body">
                <!-- Populated dynamically -->
              </tbody>
            </table>
          </div>

          <div style="margin-top:16px;">
            <div class="input-label" style="margin-bottom:6px;">Civil Defense SITREP Escalation Log</div>
            <div class="sitrep-box" id="sitrep-display">No mass-event clusters flagged.</div>
          </div>
        </div>

      </div>

    </div>

  </div>

  <script>
    const KNOWN_LOCATIONS = {
      "karachi": {
        "Garden": [24.8665, 67.0235],
        "Saddar": [24.8550, 67.0050],
        "Clifton": [24.8325, 67.0430],
        "Gulshan": [24.8770, 67.0412],
        "Gulshan-e-Iqbal": [24.9100, 67.0900],
        "North Nazimabad": [24.9300, 67.0400],
        "PECHS": [24.8900, 67.0450],
        "Lyari": [24.8800, 66.9800],
        "Korangi": [24.8300, 67.1400],
        "Malir": [24.9000, 67.2000],
        "DHA": [24.8100, 67.0500],
        "Federal B Area": [24.9200, 67.0550],
        "Soldier Bazaar": [24.8681, 67.0261],
        "Garden East": [24.8662, 67.0239],
        "Garden West": [24.8648, 67.0207]
      },
      "islamabad": {
        "Blue Area": [33.7167, 73.0587],
        "G-8": [33.6933, 73.0586],
        "G-9": [33.6830, 73.0600],
        "F-8": [33.7200, 73.0650],
        "F-7": [33.7240, 73.0720],
        "I-8": [33.7100, 73.0500],
        "H-8": [33.6880, 73.0650],
        "G-10": [33.6720, 73.0700],
        "F-10": [33.6950, 73.0620],
        "E-7": [33.7280, 73.0800],
        "I-10": [33.6980, 73.0420]
      },
      "rawalpindi": {
        "Saddar": [33.6010, 73.0510],
        "Rawalpindi Cantt": [33.5980, 73.0460],
        "Westridge": [33.6080, 73.0380],
        "Committee Chowk": [33.6120, 73.0420],
        "Chandni Chowk": [33.6050, 73.0550],
        "Satellite Town": [33.6180, 73.0600],
        "Dhoke Choudharian": [33.5960, 73.0480],
        "Lalazar": [33.6100, 73.0360]
      }
    };

    const regionSelect = document.getElementById('region-select');
    const areaSelect = document.getElementById('area-select');
    const manualDropdowns = document.getElementById('manual-dropdowns');
    const manualToggleBtn = document.getElementById('manual-toggle-btn');
    const detectBtn = document.getElementById('detect-btn');
    const locationBadge = document.getElementById('location-badge');

    const recordBtn = document.getElementById('record-btn');
    const micStatus = document.getElementById('mic-status');
    const waveform = document.getElementById('waveform');

    const submitBtn = document.getElementById('submit-btn');
    const textInput = document.getElementById('text-input');
    const audioPathInput = document.getElementById('audio-path-input');

    const consoleDisplay = document.getElementById('console-display');
    const resultsPanel = document.getElementById('results-panel');
    const mapContainer = document.getElementById('map-container');
    const sitrepDisplay = document.getElementById('sitrep-display');
    const incidentsTableBody = document.getElementById('incidents-table-body');
    const massAlertBanner = document.getElementById('mass-alert-banner');

    const unsupportedModal = document.getElementById('unsupported-modal');
    const unsupportedModalText = document.getElementById('unsupported-modal-text');
    const closeModalBtn = document.getElementById('close-modal-btn');

    let mediaRecorder;
    let audioChunks = [];
    let activeMapView = 'map';
    let currentLat = null;
    let currentLng = null;
    let mapsApiKey = '';
    let hasValidMapsKey = false;

    async function fetchConfig() {
      try {
        const res = await fetch('/api/config');
        const data = await res.json();
        mapsApiKey = data.google_maps_api_key;
        hasValidMapsKey = data.is_valid_key;
      } catch (err) {
        console.error("Failed to load config", err);
      }
    }
    fetchConfig();

    // Dropdown list populator
    function populateAreas(region) {
      areaSelect.innerHTML = "";
      const areas = Object.keys(KNOWN_LOCATIONS[region]);
      areas.forEach(area => {
        const opt = document.createElement('option');
        opt.value = area;
        opt.textContent = area;
        areaSelect.appendChild(opt);
      });
    }

    regionSelect.addEventListener('change', () => populateAreas(regionSelect.value));
    populateAreas('karachi');

    manualToggleBtn.addEventListener('click', () => {
      if (manualDropdowns.style.display === "grid") {
        manualDropdowns.style.display = "none";
        manualToggleBtn.textContent = "Manually select area";
      } else {
        manualDropdowns.style.display = "grid";
        manualToggleBtn.textContent = "Hide manual selection";
      }
    });

    // Haversine
    function getDistance(lat1, lon1, lat2, lon2) {
      const R = 6371;
      const dLat = (lat2 - lat1) * Math.PI / 180;
      const dLon = (lon2 - lon1) * Math.PI / 180;
      const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
      return R * c;
    }

    function findClosestArea(lat, lng, broadRegion) {
      let closestArea = "";
      let closestDist = Infinity;
      let finalRegion = broadRegion;

      const regionsToCheck = broadRegion === "karachi" ? ["karachi"] : ["islamabad", "rawalpindi"];

      for (let r of regionsToCheck) {
        for (let area in KNOWN_LOCATIONS[r]) {
          let coords = KNOWN_LOCATIONS[r][area];
          let dist = getDistance(lat, lng, coords[0], coords[1]);
          if (dist < closestDist) {
            closestDist = dist;
            closestArea = area;
            finalRegion = r;
          }
        }
      }

      return { area: closestArea, region: finalRegion };
    }

    // Geolocation trigger with radar scanner sweep animation
    detectBtn.addEventListener('click', () => {
      locationBadge.className = "location-badge";
      locationBadge.style.display = "none";
      detectBtn.classList.add('loading');
      detectBtn.innerHTML = `<i class="fa-solid fa-spinner"></i> Acquiring Location GPS...`;

      // Turn on radar scanning screen effect on the map panel
      mapContainer.classList.add('scanning');

      if (!navigator.geolocation) {
        detectBtn.classList.remove('loading');
        mapContainer.classList.remove('scanning');
        detectBtn.innerHTML = `<i class="fa-solid fa-location-crosshairs"></i> Auto-Detect My Location`;
        showLocationBadge(false, "Browser Geolocation is not supported.");
        return;
      }

      navigator.geolocation.getCurrentPosition(
        (pos) => {
          mapContainer.classList.remove('scanning');
          const lat = pos.coords.latitude;
          const lng = pos.coords.longitude;

          document.getElementById('lat-input').value = lat;
          document.getElementById('lng-input').value = lng;

          verifyCoordinates(lat, lng);
        },
        (err) => {
          detectBtn.classList.remove('loading');
          mapContainer.classList.remove('scanning');
          detectBtn.innerHTML = `<i class="fa-solid fa-location-crosshairs"></i> Auto-Detect My Location`;
          showLocationBadge(false, "Location query timed out or permission denied. Please select manually.");
        },
        { enableHighAccuracy: true, timeout: 8000 }
      );
    });

    function showLocationBadge(isVerified, message) {
      locationBadge.style.display = "flex";
      if (isVerified) {
        locationBadge.className = "location-badge verified";
        locationBadge.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${message}`;
      } else {
        locationBadge.className = "location-badge error";
        locationBadge.innerHTML = `<i class="fa-solid fa-circle-exclamation"></i> ${message}`;
      }
    }

    function verifyCoordinates(lat, lng) {
      detectBtn.classList.remove('loading');
      detectBtn.innerHTML = `<i class="fa-solid fa-location-crosshairs"></i> Auto-Detect My Location`;

      const inKarachi = (lat >= 24.7 && lat <= 25.25 && lng >= 66.7 && lng <= 67.35);
      const inIslamabadRawalpindi = (lat >= 33.45 && lat <= 33.8 && lng >= 72.8 && lng <= 73.25);

      if (!inKarachi && !inIslamabadRawalpindi) {
        showUnsupportedModal(lat, lng);
        showLocationBadge(false, `Coordinates outside coverage bounds: Lat ${lat.toFixed(4)}, Lng ${lng.toFixed(4)}`);
        return;
      }

      const broadRegion = inKarachi ? "karachi" : "islamabad";
      const result = findClosestArea(lat, lng, broadRegion);

      regionSelect.value = result.region;
      populateAreas(result.region);
      areaSelect.value = result.area;

      showLocationBadge(true, `Verified: Auto-routed to ${result.area}, ${result.region.toUpperCase()}`);
      updateMapIframe(result.region, result.area);
    }

    function showUnsupportedModal(lat, lng) {
      unsupportedModalText.innerHTML = `Your detected location (<strong>Lat: ${lat.toFixed(4)}, Lng: ${lng.toFixed(4)}</strong>) is outside our active coverage grid in Karachi or Islamabad/Rawalpindi.<br><br><strong>In emergencies, please directly call local agencies:</strong>`;
      unsupportedModal.classList.add('active');
    }

    closeModalBtn.addEventListener('click', () => {
      unsupportedModal.classList.remove('active');
      manualDropdowns.style.display = "grid";
      manualToggleBtn.textContent = "Hide manual selection";
    });

     function loadStreetView() {
      if (!currentLat || !currentLng) {
        mapContainer.innerHTML = `
          <div style="display:flex; align-items:center; justify-content:center; height:100%; color:var(--text-muted); font-size:13px; flex-direction:column; gap:10px; padding: 20px; text-align: center;">
            <i class="fa-solid fa-street-view" style="font-size:24px; color:var(--accent-blue);"></i>
            Street View not initialized. Detect location or select an area first.
          </div>`;
        return;
      }
      
      const streetViewLink = `https://www.google.com/maps?layer=c&cbll=${currentLat},${currentLng}`;
      
      if (hasValidMapsKey) {
        const embedUrl = `https://www.google.com/maps/embed/v1/streetview?key=${mapsApiKey}&location=${currentLat},${currentLng}`;
        mapContainer.innerHTML = `
          <div style="position: relative; width: 100%; height: 100%;">
            <iframe src="${embedUrl}" style="width:100%; height:100%; border:none;"></iframe>
            <a href="${streetViewLink}" target="_blank" style="position: absolute; bottom: 10px; right: 10px; background: rgba(0, 0, 0, 0.85); color: #fff; padding: 6px 12px; border-radius: 6px; font-size: 11px; font-weight: bold; text-decoration: none; border: 1px solid rgba(255,255,255,0.15); display: flex; align-items: center; gap: 5px; z-index: 100;">
              <i class="fa-solid fa-street-view"></i> Open Google Maps ↗
            </a>
          </div>`;
      } else {
        mapContainer.innerHTML = `
          <div style="display:flex; align-items:center; justify-content:center; height:100%; color:var(--text-muted); font-size:13.5px; flex-direction:column; gap:12px; padding: 24px; text-align: center; background: #0c0e17;">
            <i class="fa-solid fa-street-view" style="font-size:32px; color:var(--accent-red); animation: pulse 2s infinite;"></i>
            <div>
              <strong style="color: #fff; display: block; margin-bottom: 4px;">Street View Available</strong>
              Interactive Street View embed requires a Google Maps API Key in <code>.env</code>.
            </div>
            <a href="${streetViewLink}" target="_blank" style="background: var(--accent-red); color: #fff; padding: 10px 18px; border-radius: 8px; font-size: 12px; font-weight: bold; text-decoration: none; display: flex; align-items: center; gap: 8px; border: none; box-shadow: 0 4px 12px rgba(255, 59, 48, 0.3); transition: all 0.2s ease;">
              <i class="fa-solid fa-location-arrow"></i> Open Street View in Google Maps ↗
            </a>
          </div>`;
      }
    }

    function updateMapIframe(region, area) {
      let lat = document.getElementById('lat-input').value;
      let lng = document.getElementById('lng-input').value;
      
      if (!lat || !lng) {
        if (KNOWN_LOCATIONS[region] && KNOWN_LOCATIONS[region][area]) {
          lat = KNOWN_LOCATIONS[region][area][0];
          lng = KNOWN_LOCATIONS[region][area][1];
        }
      }
      
      currentLat = lat ? parseFloat(lat) : null;
      currentLng = lng ? parseFloat(lng) : null;
      
      let iframeUrl = `/api/map?region=${region}&area=${area}`;
      if (lat && lng) {
        iframeUrl += `&lat=${lat}&lng=${lng}`;
      }
      
      if (activeMapView === 'street') {
        loadStreetView();
      } else {
        mapContainer.innerHTML = `<div class="radar-sweep"></div><iframe src="${iframeUrl}"></iframe>`;
      }
    }

    // Audio capture record
    recordBtn.addEventListener('click', async () => {
      if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop();
        recordBtn.classList.remove('recording');
        waveform.classList.remove('active');
        micStatus.innerText = "Transmitting Audio...";
        return;
      }

      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];
        mediaRecorder.ondataavailable = event => {
          audioChunks.push(event.data);
        };
        mediaRecorder.onstop = async () => {
          const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
          const formData = new FormData();
          formData.append('file', audioBlob, 'recording.wav');

          try {
            const res = await fetch('/api/upload-audio', {
              method: 'POST',
              body: formData
            });
            const data = await res.json();
            if (data.file_path) {
              audioPathInput.value = data.file_path;
              micStatus.innerText = "Audio Locked";
              micStatus.classList.add('success-text');
              textInput.value = "[AUDIO REPORT TRANSMITTED]";
            } else {
              micStatus.innerText = "Upload failed.";
            }
          } catch (err) {
            micStatus.innerText = "Server upload error.";
          }
        };
        mediaRecorder.start();
        recordBtn.classList.add('recording');
        waveform.classList.add('active');
        micStatus.innerText = "Recording... click again to stop";
        micStatus.classList.remove('success-text');
      } catch (err) {
        console.error(err);
        micStatus.innerText = "Microphone access blocked.";
      }
    });

    // Logger streamer
    let logInterval;
    function printConsoleStream(logs, callback) {
      clearInterval(logInterval);
      consoleDisplay.innerHTML = "";
      let index = 0;

      function addLine() {
        if (index >= logs.length) {
          clearInterval(logInterval);
          if (callback) callback();
          return;
        }
        const timeStr = new Date().toLocaleTimeString();
        const rawLog = logs[index];
        let agentName = "SYSTEM";
        let message = rawLog;

        if (rawLog.includes(':')) {
          const parts = rawLog.split(':');
          agentName = parts[0].trim();
          message = parts.slice(1).join(':').trim();
        }

        const div = document.createElement('div');
        div.className = "console-line";
        div.innerHTML = `<span class="console-timestamp">[${timeStr}]</span> <span class="console-agent">${agentName}:</span> <span class="console-message">${message}</span>`;
        consoleDisplay.appendChild(div);
        consoleDisplay.scrollTop = consoleDisplay.scrollHeight;

        index++;
      }

      addLine();
      logInterval = setInterval(addLine, 600);
    }

    // Recent database incidents loader
    async function loadIncidentHistory() {
      try {
        const res = await fetch('/api/incidents');
        const incidents = await res.json();
        incidentsTableBody.innerHTML = "";

        if (incidents.length === 0) {
          incidentsTableBody.innerHTML = `<tr><td colspan="4" style="text-align:center;">No recent logs in memory.</td></tr>`;
          return;
        }

        incidents.slice(-8).reverse().forEach(inc => {
          const tr = document.createElement('tr');
          const timeVal = inc.time || "Live";
          const areaVal = inc.area || "Unknown";
          const typeVal = inc.type || "Emergency";
          const sevVal = inc.severity || "?";

          tr.innerHTML = `<td>${timeVal}</td><td>${areaVal}</td><td>${typeVal}</td><td>${sevVal}/5</td>`;
          incidentsTableBody.appendChild(tr);
        });
      } catch (err) {
        console.error("Failed to load memory history", err);
      }
    }

    // Submit handler
    submitBtn.addEventListener('click', async () => {
      const message = textInput.value.trim();
      const audioPath = audioPathInput.value;
      const region = regionSelect.value;
      const area = areaSelect.value;
      const lat = document.getElementById('lat-input').value;
      const lng = document.getElementById('lng-input').value;

      if (!message && !audioPath) {
        alert("Please input details or record a voice file first.");
        return;
      }

      submitBtn.disabled = true;
      submitBtn.innerText = "Dispatching...";

      const loadingLogs = [
        "SYSTEM: Dispatch payload received. Handing off to AI router network...",
        "Language Router: Scanning input contents for audio path or text strings...",
        "Language Router: Initiated dialection check (English, Urdu, Sindhi, Pashto)...",
        "Language Router: Language verified. Instruction pipeline set.",
        "Emergency Classifier: Requesting emergency category taxonomy index from local RAG...",
        "Emergency Classifier: Grounding symptoms and calculating priority index...",
        "Emergency Classifier: Severity assessment complete.",
        "Resource Locator: Matching geo coordinates against services.json & volunteers.json...",
        "Resource Locator: Identifying nearest skill-matched volunteer responders...",
        "Pattern Detector: Querying temporal event window logic...",
        "City Memory: Recording logs and compiling dashboard resources..."
      ];

      printConsoleStream(loadingLogs, async () => {
        try {
          const res = await fetch('/api/report', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              message: message,
              audio_path: audioPath || null,
              region: region,
              area: area,
              lat: lat ? parseFloat(lat) : null,
              lng: lng ? parseFloat(lng) : null
            })
          });
          const data = await res.json();

          // Render details
          resultsPanel.style.display = "block";

          // Severity
          const sev = data.severity || 3;
          const severityWidget = document.getElementById('severity-widget');
          const severityScore = document.getElementById('severity-score');
          const severityLabel = document.getElementById('severity-label');

          severityWidget.className = "severity-widget";
          severityScore.textContent = `${sev}/5`;

          // Apply/Remove Flashing Red Alert border style to body
          if (sev >= 4) {
            document.body.classList.add('panic-mode');
            severityWidget.classList.add('sev-5');
            severityLabel.textContent = "CRITICAL — EMERGENCY UNIT EN ROUTE";
          } else if (sev === 3) {
            document.body.classList.remove('panic-mode');
            severityWidget.classList.add('sev-3-4');
            severityLabel.textContent = "ELEVATED — FIELD ASSIST ADVISED";
          } else {
            document.body.classList.remove('panic-mode');
            severityWidget.classList.add('sev-1-2');
            severityLabel.textContent = "STABLE — MONITOR & ADVISE";
          }

          // Service Card matches styling
          const serviceCard = document.getElementById('service-card');
          if (data.nearest_service.name && data.nearest_service.name !== "None available") {
            serviceCard.className = "resource-card service-matched";
            document.getElementById('service-name').textContent = data.nearest_service.name;
            document.getElementById('service-type').innerHTML = `<i class="fa-solid fa-hospital"></i> ${data.nearest_service.type || 'N/A'}`;
            document.getElementById('service-distance').innerHTML = `<i class="fa-solid fa-route"></i> Distance: ${data.nearest_service.distance_km || '---'} km`;
            document.getElementById('service-call-btn').href = `tel:${data.nearest_service.phone || ''}`;
          } else {
            serviceCard.className = "resource-card";
            document.getElementById('service-name').textContent = "None available";
            document.getElementById('service-type').innerHTML = `<i class="fa-solid fa-hospital"></i> ---`;
            document.getElementById('service-distance').innerHTML = `<i class="fa-solid fa-route"></i> Distance: ---`;
            document.getElementById('service-call-btn').href = `tel:`;
          }

          // Volunteer Card matches styling
          const volunteerCard = document.getElementById('volunteer-card');
          if (data.nearest_volunteer.name && data.nearest_volunteer.name !== "None in radius") {
            volunteerCard.className = "resource-card volunteer-matched";
            document.getElementById('volunteer-name').textContent = data.nearest_volunteer.name;
            document.getElementById('volunteer-skills').innerHTML = `<i class="fa-solid fa-user-doctor"></i> Skills: ${data.nearest_volunteer.skills || 'First Aid'}`;
            document.getElementById('volunteer-distance').innerHTML = `<i class="fa-solid fa-route"></i> Distance: ${data.nearest_volunteer.distance_km || '---'} km`;
            document.getElementById('volunteer-call-btn').href = `tel:${data.nearest_volunteer.phone || ''}`;
          } else {
            volunteerCard.className = "resource-card";
            volunteerCard.innerHTML = `---`;
            document.getElementById('volunteer-name').textContent = "None in radius";
            document.getElementById('volunteer-skills').innerHTML = `<i class="fa-solid fa-user-doctor"></i> Skills: ---`;
            document.getElementById('volunteer-distance').innerHTML = `<i class="fa-solid fa-route"></i> Distance: ---`;
            document.getElementById('volunteer-call-btn').href = `tel:`;
          }

          // First aid checklist
          const protocolCard = document.getElementById('protocol-card');
          const stepsList = document.getElementById('protocol-steps-list');
          stepsList.innerHTML = "";

          if (data.first_aid_steps) {
            protocolCard.style.display = "block";
            document.getElementById('protocol-name').textContent = data.type;

            const steps = data.first_aid_steps.split(/\n+/).filter(line => line.trim().match(/^\d+\./));
            if (steps.length > 0) {
              steps.forEach(stepText => {
                const cleanText = stepText.replace(/^\d+\.\s*/, "");
                const stepDiv = document.createElement('div');
                stepDiv.className = "step-item";
                stepDiv.innerHTML = `<div class="step-checkbox"><i class="fa-solid fa-check"></i></div><span>${cleanText}</span>`;
                stepDiv.addEventListener('click', () => {
                  stepDiv.classList.toggle('checked');
                });
                stepsList.appendChild(stepDiv);
              });
            } else {
              stepsList.innerHTML = `<p style="font-size:13.5px; line-height:1.6;">${data.first_aid_steps}</p>`;
            }
          } else {
            protocolCard.style.display = "none";
          }
          
          // Render translated description
          const descCard = document.getElementById('report-desc-card');
          const descText = document.getElementById('report-desc-text');
          const langBadge = document.getElementById('report-lang-badge');
          
          if (data.description) {
            descCard.style.display = "block";
            descText.textContent = data.description;
            textInput.value = data.description;
            
            if (data.detected_language) {
              langBadge.textContent = data.detected_language;
              langBadge.style.display = "inline-block";
            } else {
              langBadge.style.display = "none";
            }
          } else {
            descCard.style.display = "none";
          }

          updateMapIframe(region, area);

          if (data.is_mass_event) {
            massAlertBanner.style.display = "flex";
            sitrepDisplay.textContent = data.sitrep;
          } else {
            massAlertBanner.style.display = "none";
            sitrepDisplay.textContent = "No active mass-event clusters flagged in district.";
          }

          loadIncidentHistory();

          const executionLogs = data.agent_log || [];
          printConsoleStream(executionLogs);

        } catch (err) {
          console.error(err);
          const errorLogs = ["SYSTEM ERROR: Target pipeline execution failure.", "Check API keys or network connection."];
          printConsoleStream(errorLogs);
        } finally {
          submitBtn.disabled = false;
          submitBtn.innerHTML = `🚨 Dispatch Report`;
        }
      });
    });

    const btnShowMap = document.getElementById('btn-show-map');
    const btnShowStreetView = document.getElementById('btn-show-streetview');
    
    btnShowMap.addEventListener('click', () => {
      activeMapView = 'map';
      btnShowMap.classList.add('active');
      btnShowMap.style.background = 'var(--accent-blue)';
      btnShowMap.style.color = '#000';
      btnShowStreetView.classList.remove('active');
      btnShowStreetView.style.color = 'var(--text-muted)';
      btnShowMap.style.color = '#000';
      const region = regionSelect.value;
      const area = areaSelect.value;
      updateMapIframe(region, area);
    });
    
    btnShowStreetView.addEventListener('click', () => {
      activeMapView = 'street';
      btnShowStreetView.classList.add('active');
      btnShowMap.classList.remove('active');
      btnShowMap.style.color = 'var(--text-muted)';
      btnShowStreetView.style.color = '#000';
      loadStreetView();
    });

    loadIncidentHistory();
  </script>
</body>

</html>