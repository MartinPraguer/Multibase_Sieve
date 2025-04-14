# 🧮 Multibase Sieve (EN / CZ)

## 🇬🇧 English
# 🧮 Multibase Sieve (Alternative to the Sieve of Eratosthenes)

This project implements a non-traditional version of the Sieve of Eratosthenes using base conversions.  
Instead of removing multiples of `i` directly, it converts all numbers to **base-`i`** and removes those that **end with `'0'`** — except for the **first occurrence**.

---

## 🧠 Algorithm – Step by Step

1. **Initialization:**  
   Start with the full set of numbers from `2` to `limit`.

2. **For each integer `i` from `2` up to `sqrt(limit)`**:
   - Convert all numbers in the current set to base `i`.
   - Remove all numbers that **end with `'0'`** in that base, **except for the first such number**.
   - Convert the filtered set back to base 10 (effectively, just keep using base 10 for processing).

3. **Repeat the process for all `i` from `2` to `sqrt(limit)`**

---

## 📌 What does this algorithm do?

- This is effectively a **variation of the Sieve of Eratosthenes**, where "multiples of `i`" are filtered by detecting numbers ending in `'0'` in base `i`.
- In each iteration, the algorithm removes all multiples of the current `i`, without using division.
- As a result, **prime numbers** survive all filtering steps.

---

## 🧪 Example

With `limit = 1000`, this algorithm correctly identifies:

- ✅ Exactly **168 prime numbers** (same as the classical sieve)
- ✅ Runtime: approx. **0.01 seconds** (Eratosthenes: ~0.0001 s, for comparison)
- ✅ Uses only string operations and base conversions

---

## ✅ Advantages

- Offers an alternative way to think about filtering without modulus or multiplication.
- Great educational tool for learning number bases and algorithmic thinking.
- Works for any positive integer limit.

---

## 📂 Files

- `main.py` – Python script with the core algorithm
- `README.md` – this documentation

---

## 💡 Idea Behind the Algorithm

This implementation is based on the thought:  
> _"What if we filter out multiples by how they appear in another number base — like ending with zero?"_

---

## 🇨🇿 Čeština
# 🧮 Síto s vícenásobnými soustavami (Varianta Eratosthenova síta)

Tento projekt implementuje netradiční verzi Eratosthenova síta, která využívá převody do různých číselných soustav.  
Místo klasického mazání násobků `i` se čísla převedou do **i-té soustavy** a vymažou se ta, která **končí na `'0'`** — kromě **prvního takového výskytu**.

---

## 🧠 Algoritmus – krok za krokem

1. **Inicializace:**  
   Vytvoříme množinu čísel od `2` do `limit`.

2. **Pro každé `i` od `2` po `sqrt(limit)`**:
   - Všechna čísla v aktuální množině převedeme do `i`-té soustavy.
   - Odstraníme ta, která **v této soustavě končí na `'0'`**, **kromě prvního**.
   - Množinu pak znovu zpracováváme jako běžná celá čísla (v desítkové soustavě).

3. **Iterace pokračuje pro všechna `i` od `2` do odmocniny z `limit`.**

---

## 📌 Co algoritmus dělá?

- V podstatě jde o **variantu Eratosthenova síta**, kde se **mazání násobků** realizuje přes převody do `i`-tých soustav.
- Každá iterace „odstraní“ násobky aktuálního `i` tím, že rozpozná čísla končící nulou.
- Díky tomu přežijí pouze **prvočísla**.

---

## 🧪 Příklad

Pro `limit = 1000` algoritmus najde přesně:

- ✅ 168 prvočísel (stejně jako klasické síto)
- ✅ Čas výpočtu: cca **0.01 s** (Eratosthenovo síto: cca 0.0001 s)
- ✅ Používá pouze převody a práci se stringy

---

## ✅ Výhody

- Nabízí alternativní způsob filtrování bez dělení a zbytků.
- Výborný nástroj pro výuku číselných soustav a algoritmického myšlení.
- Funguje pro libovolně velký `limit`.

---

## 📂 Soubory

- `main.py` – hlavní Python skript s implementací
- `README.md` – tento popis

---

## 💡 Nápad

Tato implementace vznikla na základě otázky:  
> _„Co kdybychom mazali násobky tím, že v jiné soustavě končí nulou?“_

---