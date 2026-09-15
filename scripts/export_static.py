"""Exporta el mockup Django a HTML estatico para GitHub Pages.

Uso (desde la carpeta AccionProtege/):
    python ../scripts/export_static.py [--base /MockupAccionProtege] [--out ../dist]

- Renderiza con el test Client de Django (sin servidor).
- Reescribe links absolutos ("/servicios/") y estaticos relativos
  ("static/...") con el prefijo BASE del Pages del repositorio.
- Copia AccionProtege/static/ a dist/static/ y crea .nojekyll.
- En /contacto/ inyecta un aviso: el formulario no envia en la demo
  estatica (necesita el backend Django).
"""
import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DJANGO_DIR = REPO_ROOT / "AccionProtege"

sys.path.insert(0, str(DJANGO_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AccionProtege.settings")

import django  # noqa: E402

django.setup()

from django.test import Client  # noqa: E402

BASE = sys.argv[sys.argv.index("--base") + 1] if "--base" in sys.argv else "/MockupAccionProtege"
OUT = Path(sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else REPO_ROOT / "dist").resolve()

PAGES = [
    "/",
    "/nosotros/",
    "/mision/",
    "/atencion-personalizada/",
    "/garantia/",
    "/vigilancia-especializada/",
    "/servicios/",
    "/servicios/instalaciones-industriales-mineras/",
    "/servicios/guardias-vip/",
    "/servicios/alarmas/",
    "/servicios/control-acceso/",
    "/servicios/cctv-monitoreo/",
    "/servicios/proyectos/",
    "/contacto/",
    "/contacto/ok/",
    "/contacto/privacidad/",
]

CONTACTO_AVISO = (
    '<div class="alert alert-info" role="note">'
    "Demo estática en GitHub Pages: el formulario no envía desde aquí. "
    "Escríbenos al +56 2 2335 9125 o usa el Django local con "
    "<code>python manage.py runserver</code>.</div>"
)


def rewrite(html: str, url: str) -> str:
    html = html.replace('href="/', f'href="{BASE}/')
    html = html.replace('src="/', f'src="{BASE}/')
    html = html.replace('href="static/', f'href="{BASE}/static/')
    html = html.replace('src="static/', f'src="{BASE}/static/')
    if url == "/contacto/":
        html = html.replace("<h1>Contáctanos</h1>", "<h1>Contáctanos</h1>" + CONTACTO_AVISO)
    return html


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    client = Client()
    for url in PAGES:
        resp = client.get(url)
        assert resp.status_code == 200, f"{url} -> {resp.status_code}"
        rel = url.lstrip("/")
        target = OUT / rel / "index.html" if rel else OUT / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rewrite(resp.content.decode(), url), encoding="utf-8")
        print(f"OK {url} -> {target.relative_to(REPO_ROOT)}")
    shutil.copytree(DJANGO_DIR / "static", OUT / "static")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Listo: {len(PAGES)} paginas en {OUT}")


if __name__ == "__main__":
    main()
