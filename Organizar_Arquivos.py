import shutil
from pathlib import Path

print("---> BACKUP ORGANIZADO <---")
print()

pasta_base = Path(__file__).parent
pasta_alvo = pasta_base / "arquivos"
pasta_pdf = pasta_base / "Backup_Organizado" / "PDF"
pasta_py = pasta_base / "Backup_Organizado" / "PY"
pasta_docx = pasta_base / "Backup_Organizado" / "DOCX"
pasta_xlsx = pasta_base / "Backup_Organizado" / "XLSX"
pasta_txt = pasta_base / "Backup_Organizado" / "TXT"
pasta_final = pasta_base / "Backup_Organizado"

# Criando as pastas, caso não existam
pasta_pdf.mkdir(parents=True, exist_ok=True)
pasta_py.mkdir(parents=True, exist_ok=True)
pasta_docx.mkdir(parents=True, exist_ok=True)
pasta_xlsx.mkdir(parents=True, exist_ok=True)
pasta_txt.mkdir(parents=True, exist_ok=True)

lista_arquivos = list(pasta_alvo.glob("*"))

for item in lista_arquivos:
    if item.suffix == ".pdf":
        shutil.copyfile(item, pasta_pdf / item.name)
    elif item.suffix == ".py":
        shutil.copyfile(item, pasta_py / item.name)
    elif item.suffix == ".docx":
        shutil.copyfile(item, pasta_docx / item.name)
    elif item.suffix == ".xlsx":
        shutil.copyfile(item, pasta_xlsx / item.name)
    elif item.suffix == ".txt":
        shutil.copyfile(item, pasta_txt / item.name)

nome_arquivo = pasta_base / "Compactado"
shutil.make_archive(nome_arquivo, "zip", pasta_final)