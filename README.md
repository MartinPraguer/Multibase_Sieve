# 🧮 Multibase Sieve (EN / CZ)

# 🧮 Multibase Sieve (Alternative Visualization of Sieve of Eratosthenes)

This project implements a non-traditional version of the Sieve of Eratosthenes using number base conversions.  
Instead of removing multiples of `i` directly using arithmetic, it converts all numbers to **base-`i`** and removes those that **end with `'0'`** — except for the **first such number**.

---

## 🧠 Algorithm – Step by Step

1. **Initialization:**  
   Start with numbers from `2` to the given `limit`.

2. **For each base `i` from 2 to √limit**:
   - Convert each number in the set to base-`i`.
   - Remove all numbers that **end with `'0'`**, except the first such one.
   - Continue with the filtered list (still in base-10 for further processing).

---

## 📈 Comparison with Classical Sieve

This project includes a performance comparison between:

- 🧮 This multibase (alternative) sieve
- ⚙️ The classical Sieve of Eratosthenes

It measures:
- Execution time
- Number of operations
- Count of remaining (prime) numbers
- How many times faster one method is over the other

---

## 📌 What does this algorithm do?

- It’s a **visual and structural variation** of the Sieve of Eratosthenes.
- Instead of calculating multiples via division or modulus, it **uses the structure** of numbers in different bases (even though base conversion internally uses `%` and `//`).
- Ultimately, it filters out multiples similarly — but from a different perspective.

---

## 🧪 Example

With `limit = 1000`, this algorithm correctly identifies:

- ✅ Exactly **168 prime numbers** (same result as classical sieve)
- ✅ Runtime: approx. **0.01 s** (Eratosthenes ~0.0001 s for comparison)
- ✅ Uses digit-based filtering, not explicit multiplication

---

## ✅ Highlights

- Provides an **alternative way to visualize filtering** — based on digit patterns in number bases.
- Interesting **educational tool** for teaching base conversions and structural filtering.
- Works well for small to medium limits (e.g., up to 1,000,000 with optimizations).

---

## 📂 Files

- `main.py` – Python script with the core algorithm
- `README.md` – this documentation

---

## 💡 Idea Behind the Algorithm

This project is based on the idea:  
> _"What if we filter out multiples by how they appear in other bases — like ending with a 0?"_

---

---

# 🧮 Síto pomocí soustav (alternativní pohled na Eratosthenovo síto)

Tento projekt implementuje netradiční verzi Eratosthenova síta pomocí převodů čísel do různých číselných soustav.  
Místo klasického mazání násobků `i` se čísla převedou do **i-té soustavy** a odstraní se ta, která **končí na `'0'`** — kromě **prvního takového čísla**.

---

## 🧠 Algoritmus – krok za krokem

1. **Inicializace:**  
   Vytvoříme množinu čísel od `2` do `limit`.

2. **Pro každou základnu `i` od 2 do odmocniny z `limit`**:
   - Všechna čísla převedeme do soustavy o základu `i`.
   - Odstraníme ta, která **končí nulou** (`'0'`), **kromě prvního takového čísla**.
   - Filtr pokračuje s novou množinou, stále v desítkové soustavě.

---

## 📈 Porovnání s klasickým sítem

Projekt obsahuje porovnání výkonnosti mezi:

- 🧮 Tímto alternativním (soustavovým) sítem
- ⚙️ Klasickým Eratosthenovým sítem

Porovnávají se:
- Čas výpočtu
- Počet operací
- Počet přeživších čísel (prvočísel)
- Kolikrát je jedno řešení rychlejší než druhé

---

## 📌 Co algoritmus dělá?

- Jde o **strukturální variantu Eratosthenova síta** — místo výpočtu násobků se využívá **vzhled čísel v různých soustavách**.
- Převod do jiné soustavy sice vnitřně používá `%` a `//`, ale ty nejsou použity přímo pro filtrování.
- Výsledkem je podobné chování jako klasické síto — ale s jiným přístupem.

---

## 🧪 Příklad

Pro `limit = 1000` algoritmus správně najde:

- ✅ Přesně **168 prvočísel** (stejně jako klasické síto)
- ✅ Čas výpočtu: cca **0.01 s** (klasické síto ~0.0001 s)
- ✅ Používá převody do soustav a filtraci podle poslední cifry

---

## ✅ Výhody

- Nabízí **alternativní vizuální přístup** k filtrování násobků.
- Má **edukativní hodnotu** — vhodné při učení číselných soustav.
- Funguje pro menší a střední rozsahy (např. do 1 000 000, pokud je optimalizované).

---

## 📂 Soubory

- `main.py` – hlavní Python skript s algoritmem
- `README.md` – tento popis

---

## 💡 Nápad

Tato implementace vznikla z myšlenky:  
> _„Co kdybychom mazali násobky podle toho, jak vypadají v jiné soustavě – např. jestli končí nulou?“_

---

