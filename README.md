<h1 align="center">🎯 sentinelone-hunting-queries</h1>

<p align="center">
  Threat hunting queries for <b>SentinelOne Singularity</b> (S1QL 2.0 / PowerQuery), mapped to <b>MITRE ATT&CK</b>.<br>
  <sub>Queries de threat hunting para SentinelOne, mapeadas no MITRE ATT&CK.</sub>
</p>

<p align="center">
  <img src="https://github.com/Gustavobaldwin/sentinelone-hunting-queries/actions/workflows/validate.yml/badge.svg" alt="validate">
  <img src="https://img.shields.io/badge/S1QL-2.0-6c2dc7" alt="S1QL 2.0">
  <img src="https://img.shields.io/badge/MITRE-ATT%26CK-red" alt="MITRE ATT&CK">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT">
</p>

---

## 🇺🇸 English

A personal, growing collection of hunting queries I use as a solo IT/security admin in a Microsoft-centric environment (M365, Entra ID, Intune, hybrid AD). Each query is a YAML file with metadata, MITRE mapping, known false positives and tuning tips, validated automatically by CI.

**How to use:** open **Event Search** in the SentinelOne console, switch to **PowerQuery / S1QL 2.0**, paste the `query` field, pick a time range and run. Lines starting with `|` are PowerQuery pipes (aggregation); remove them if you only want raw events.

> ⚠️ Queries marked 🧪 `experimental` were written against the documented schema but have **not yet been validated in a live console**. Field names can vary between console versions — test, tune, and treat hits as leads, not verdicts.

## 🇧🇷 Português

Coleção pessoal (e crescente) de queries de caça que eu uso como admin de TI/segurança num ambiente Microsoft (M365, Entra ID, Intune, AD híbrido). Cada query é um arquivo YAML com metadados, mapeamento MITRE, falsos positivos conhecidos e dicas de ajuste, validado automaticamente pelo CI.

**Como usar:** abre o **Event Search** no console do SentinelOne, muda pra **PowerQuery / S1QL 2.0**, cola o campo `query`, escolhe o período e roda. Linhas que começam com `|` são pipes do PowerQuery (agregação); tira elas se quiser só os eventos crus.

> ⚠️ Queries marcadas 🧪 `experimental` foram escritas com base no schema documentado mas **ainda não foram validadas num console real**. Os nomes de campo podem variar entre versões. Testa, ajusta e trata os resultados como pista, não como veredito.

---

## 📚 Index

<!-- INDEX:START -->
| ID | Query | Tactic | Techniques | Status |
|----|-------|--------|------------|--------|
| S1H-0001 | [PowerShell with encoded command](queries/execution/powershell-encoded-command.yaml)<br><sub>PowerShell com comando codificado</sub> | execution | [T1059.001](https://attack.mitre.org/techniques/T1059/001/), [T1027](https://attack.mitre.org/techniques/T1027/) | 🧪 experimental |
| S1H-0002 | [Office application spawning a shell or script host](queries/initial-access/office-spawning-shell.yaml)<br><sub>Aplicativo do Office abrindo shell ou interpretador de script</sub> | initial-access | [T1566.001](https://attack.mitre.org/techniques/T1566/001/), [T1204.002](https://attack.mitre.org/techniques/T1204/002/) | 🧪 experimental |
| S1H-0003 | [LSASS memory dump via comsvcs.dll or ProcDump](queries/credential-access/lsass-dump-comsvcs.yaml)<br><sub>Dump de memória do LSASS via comsvcs.dll ou ProcDump</sub> | credential-access | [T1003.001](https://attack.mitre.org/techniques/T1003/001/) | 🧪 experimental |
| S1H-0004 | [Scheduled task created by a script host or Office app](queries/persistence/scheduled-task-suspicious-parent.yaml)<br><sub>Tarefa agendada criada por interpretador de script ou Office</sub> | persistence | [T1053.005](https://attack.mitre.org/techniques/T1053/005/) | 🧪 experimental |
| S1H-0005 | [Run/RunOnce registry key set from a user-writable path](queries/persistence/registry-run-key.yaml)<br><sub>Chave Run/RunOnce gravada por processo em pasta do usuário</sub> | persistence | [T1547.001](https://attack.mitre.org/techniques/T1547/001/) | 🧪 experimental |
| S1H-0006 | [Certutil used to download or decode files](queries/defense-evasion/certutil-download.yaml)<br><sub>Certutil usado para baixar ou decodificar arquivos</sub> | defense-evasion | [T1105](https://attack.mitre.org/techniques/T1105/), [T1140](https://attack.mitre.org/techniques/T1140/) | 🧪 experimental |
| S1H-0007 | [Mshta executing remote or inline script](queries/defense-evasion/mshta-remote.yaml)<br><sub>Mshta executando script remoto ou inline</sub> | defense-evasion | [T1218.005](https://attack.mitre.org/techniques/T1218/005/) | 🧪 experimental |
| S1H-0008 | [Microsoft Defender disabled via PowerShell](queries/defense-evasion/defender-tampering.yaml)<br><sub>Microsoft Defender desativado via PowerShell</sub> | defense-evasion | [T1562.001](https://attack.mitre.org/techniques/T1562/001/) | 🧪 experimental |
| S1H-0009 | [Active Directory reconnaissance burst per endpoint](queries/discovery/ad-recon-burst.yaml)<br><sub>Rajada de reconhecimento de Active Directory por endpoint</sub> | discovery | [T1087.002](https://attack.mitre.org/techniques/T1087/002/), [T1069.002](https://attack.mitre.org/techniques/T1069/002/), [T1482](https://attack.mitre.org/techniques/T1482/) | 🧪 experimental |
| S1H-0010 | [Local account created or added to Administrators](queries/persistence/local-account-created.yaml)<br><sub>Conta local criada ou adicionada aos Administradores</sub> | persistence | [T1136.001](https://attack.mitre.org/techniques/T1136/001/), [T1098](https://attack.mitre.org/techniques/T1098/) | 🧪 experimental |
| S1H-0011 | [PsExec-style remote service execution](queries/lateral-movement/psexec-service.yaml)<br><sub>Execução remota via serviço estilo PsExec</sub> | lateral-movement | [T1021.002](https://attack.mitre.org/techniques/T1021/002/), [T1569.002](https://attack.mitre.org/techniques/T1569/002/) | 🧪 experimental |
| S1H-0012 | [Shadow copies or backups deleted (ransomware precursor)](queries/impact/inhibit-system-recovery.yaml)<br><sub>Shadow copies ou backups apagados (precursor de ransomware)</sub> | impact | [T1490](https://attack.mitre.org/techniques/T1490/) | 🧪 experimental |
| S1H-0013 | [Unapproved remote access / RMM tool execution](queries/command-and-control/rmm-tool-execution.yaml)<br><sub>Execução de ferramenta de acesso remoto não homologada</sub> | command-and-control | [T1219](https://attack.mitre.org/techniques/T1219/), [T1572](https://attack.mitre.org/techniques/T1572/) | 🧪 experimental |

**13 queries** · **9 tactics** · **21 ATT&CK techniques**
<!-- INDEX:END -->

**Status:** 🧪 experimental · ✅ tested · 🛡️ production (also deployed as STAR rule) · ⚠️ deprecated

---

## 🗂️ Structure

```
queries/<mitre-tactic>/<query-name>.yaml   # one hunt per file
schema/query.schema.json                   # required fields & formats
scripts/validate.py                        # validates + rebuilds this index
.github/workflows/validate.yml             # runs on every push / PR
```

## ➕ Adding a query / Adicionando uma query

1. Copy any YAML under `queries/` into the folder of its MITRE tactic.
2. Give it the next free `id` (`S1H-00XX`), fill in EN + PT fields.
3. Run `pip install pyyaml jsonschema && python scripts/validate.py --write`.
4. Commit. CI fails if the schema is broken or the index is stale.

## 🙏 Credits

Format inspired by the official [SentineLabs S1QL-Queries](https://github.com/SentineLabs/S1QL-Queries) repository. Technique references from [MITRE ATT&CK®](https://attack.mitre.org/).

## ⚖️ Disclaimer

For defensive use only. No customer or tenant data is included in this repository. Use at your own risk.
