# Python e Animações Matemáticas

## O que é Manim?

---

## Instalação do Manim

### Windows
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

scoop install python ffmpeg latex

python -m pip install manim setuptools
```

### MacOS
```bash
brew install py3cairo ffmpeg

brew install pango pkg-config scipy

pip3 install manim

brew install --cask mactex-no-gui
```

---


## Teste de Instalação
```python
# arquivo teste.py

from manim import *

class Teste(Scene):

    def construct(self):

        s = Square()

        self.play(Create(s))

        self.wait(2)
```

### Execução
```bash
manim -pqh -r 1080,1920 teste.py Teste
```