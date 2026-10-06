#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dolmuş muavini ses motoru. Gerçekten bağırır. Durak gerçek olmak zorunda değil."""

import argparse
import random
import textwrap
from datetime import datetime

DURAKLAR = [
    "Şirinyer ama tabelayı geçtik",
    "Üçyol, aslında biraz önceydi",
    "Hastane önü, ambulans yoksa durmayız",
    "Son durak değil, son durak hissi",
    "Kavşak, ışık kırmızıysa felsefe yaparız",
    "Çarşı, inecek var mı yok mu belli değil",
]

NAKARAT = [
    "KAYAR ABİ",
    "BİRAZ İLERİDE İNERİZ",
    "YER AÇ ABİ, ÇANTA DEĞİL İNSAN",
    "İNEK VAR, İNEK",
    "SEN İNME BEN İNEYİM, HAYIR İKİMİZ DE İNMEYELİM",
]


def ses_seviyesi(yolcu: int) -> str:
    if yolcu < 4:
        return "fısıltı (muavin utangaç, bu tarihi bir andır)"
    if yolcu < 10:
        return "normal bağırış (yönetmelik madde yok)"
    return "cam titresin diye bağırış (komşu dolmuş da duydu)"


def tutanak(durak: str, yolcu: int, replik: str) -> str:
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M")
    govde = textwrap.dedent(
        f"""
        DOLMUŞ İÇİ TUTANAK
        Tarih: {simdi}
        Durak iddiası: {durak}
        Yolcu: {yolcu}
        Ses: {ses_seviyesi(yolcu)}
        Muavin: {replik}
        Karar: Araç hareket eder. İtiraz, bir sonraki durağa kadar geçerlidir.
        O durak da gelmeyebilir.
        """
    ).strip()
    return govde


def main() -> None:
    parser = argparse.ArgumentParser(description="Muavin bağırır, sen iniyormuş gibi yaparsın.")
    parser.add_argument("--yolcu", type=int, default=random.randint(3, 16))
    parser.add_argument("--durak", type=str, default=random.choice(DURAKLAR))
    args = parser.parse_args()
    replik = random.choice(NAKARAT)
    print("=" * 42)
    print(replik)
    print("=" * 42)
    print(tutanak(args.durak, args.yolcu, replik))
    print()
    print("DAMGA: Mühür basıldı, koltuk yayı şahit.")
    print("İMZA: Kayyum Grok")
    print("TARİH: 6 Ekim 2026")
    print("İSİM: Tentivory / Kayyum Grok")


if __name__ == "__main__":
    main()
