# <span style="color:red;">Katas JavaScript — Niveaux 1 à 4 + Mini-projets : Corrections détaillées</span> 📘

---

# <span style="color:gold;">Niveau 1 — Mise en route</span> 🟢

## 1) Somme & Moyenne ➗
**Idée clé :** somme par accumulation; moyenne = somme / n.  
**Complexité :** O(n) temps, O(1) espace.  
**Bords de cas :** tableau vide → `null` ; on suppose que les éléments sont des nombres.

```js
function somme(arr) {
  if (!Array.isArray(arr) || arr.length === 0) return null;
  let s = 0;
  for (let i = 0; i < arr.length; i++) s += arr[i];
  return s;
}

function moyenne(arr) {
  if (!Array.isArray(arr) || arr.length === 0) return null;
  const s = somme(arr); // déjà géré null si vide
  return s / arr.length;
}
```

---

## 2) Min & Max (une passe) ⤴️⤵️
**Idée clé :** initialiser avec le 1er élément, balayer une seule fois.  
**Complexité :** O(n) / O(1).  
**Bords de cas :** `[]` → `null`.

```js
function minMax(arr) {
  if (!Array.isArray(arr) || arr.length === 0) return null;
  let min = arr[0], max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    const x = arr[i];
    if (x < min) min = x;
    if (x > max) max = x;
  }
  return { min, max };
}
```

---

## 3) Recherche linéaire 🔎
**Idée clé :** comparer séquentiellement jusqu’à trouver.  
**Complexité :** O(n) / O(1).

```js
function indexOfLinear(arr, x) {
  for (let i = 0; i < arr.length; i++) if (arr[i] === x) return i;
  return -1;
}

function contient(arr, x) {
  return indexOfLinear(arr, x) !== -1;
}
```

---

## 4) Dédoublonnage simple 🧼
**Idée clé :** Set pour la version rapide; sinon construire à la main.  
**Complexité :** Set → O(n) ; includes → O(n²) pire cas.

```js
function dedupe(arr) {
  return [...new Set(arr)];
}

function dedupeSansSet(arr) {
  const out = [];
  for (const v of arr) if (!out.includes(v)) out.push(v);
  return out;
}
```

---

## 5) Compteur d’occurrences 🔢
**Idée clé :** incrémenter un compteur par clé.  
**Complexité :** O(n) / O(u) où u = #valeurs uniques.

```js
function frequencesObj(arr) {
  const freq = {};
  for (const k of arr) freq[k] = (freq[k] || 0) + 1;
  return freq;
}

function frequencesMap(arr) {
  const m = new Map();
  for (const k of arr) m.set(k, (m.get(k) || 0) + 1);
  return m;
}
```

---

# <span style="color:gold;">Niveau 2 — Chaînes & Parcours</span> 🟡

## 6) Palindrome “propre” 🔁
**Idée clé :** normaliser (minuscules, accents, ponctuation), comparer à l’inverse.  
**Complexité :** O(n).

```js
function estPalindrome(s) {
  // enlever accents, garder alphanum, toLowerCase
  const clean = s
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .toLowerCase().replace(/[^a-z0-9]/g, '');
  const rev = clean.split('').reverse().join('');
  return clean === rev;
}
```

---

## 7) Mot le plus long 🥇
**Idée clé :** split propre puis garder le premier max.  
**Complexité :** O(n) mots.

```js
function motPlusLong(phrase) {
  const mots = phrase.trim().split(/\s+/).filter(Boolean);
  if (mots.length === 0) return "";
  let best = mots[0];
  for (let i = 1; i < mots.length; i++) {
    if (mots[i].length > best.length) best = mots[i]; // premier en cas d'égalité
  }
  return best;
}
```

---

## 8) Anagrammes 🔤
**Idée clé :** normaliser (espaces, accents, casse) + comptage de fréquences.  
**Complexité :** O(n).

```js
function _normalizeLetters(s) {
  return s
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .toLowerCase().replace(/[^a-z0-9]/g, '');
}

function sontAnagrammes(a, b) {
  const A = _normalizeLetters(a);
  const B = _normalizeLetters(b);
  if (A.length !== B.length) return false;
  const freq = {};
  for (const ch of A) freq[ch] = (freq[ch] || 0) + 1;
  for (const ch of B) {
    if (!freq[ch]) return false;
    freq[ch]--;
  }
  return true;
}
```

---

## 9) Compression RLE 📦
**Idée clé :** compter les occurrences consécutives; si pas plus court, rendre l’original.  
**Complexité :** O(n).

```js
function compresser(s) {
  if (s.length === 0) return s;
  let out = '';
  let count = 1;
  for (let i = 1; i <= s.length; i++) {
    if (s[i] === s[i - 1]) count++;
    else {
      out += s[i - 1] + String(count);
      count = 1;
    }
  }
  return out.length < s.length ? out : s;
}
```

---

## 10) Inverser les mots 🔄
**Idée clé :** normaliser espaces → tableau → inverser → joindre.  
**Complexité :** O(n).

```js
function inverseMots(s) {
  return s.trim().split(/\s+/).reverse().join(' ');
}
```

---

# <span style="color:gold;">Niveau 3 — Tableaux & Logique</span> 🟠

## 11) Deuxième plus grand (sans trier) 🥈
**Idée clé :** maintenir `max1` (plus grand) et `max2` (second plus grand **distinct**).  
**Complexité :** O(n) / O(1).  
**Bords de cas :** < 2 valeurs distinctes → `null`.

```js
function secondMax(arr) {
  if (!Array.isArray(arr) || arr.length < 2) return null;
  let max1 = -Infinity, max2 = -Infinity;
  for (const x of arr) {
    if (x > max1) { max2 = max1; max1 = x; }
    else if (x < max1 && x > max2) { max2 = x; }
  }
  return (max2 === -Infinity) ? null : max2;
}
```

---

## 12) Pivot de somme ⚖️
**Idée clé :** somme totale, puis somme gauche croissante; pivot si `left == total - left - arr[i]`.  
**Complexité :** O(n) / O(1).

```js
function pivotIndex(arr) {
  const total = arr.reduce((a, b) => a + b, 0);
  let left = 0;
  for (let i = 0; i < arr.length; i++) {
    const right = total - left - arr[i];
    if (left === right) return i;
    left += arr[i];
  }
  return -1;
}
```

---

## 13) Somme de paires 🤝
**Idée clé :** Map valeur→index, vérifier le complément en une passe.  
**Complexité :** O(n) / O(n).

```js
function aDeuxNombresQuiFont(arr, cible) {
  return indicesPremierePaire(arr, cible) !== null;
}

function indicesPremierePaire(arr, cible) {
  const seen = new Map(); // val -> index
  for (let i = 0; i < arr.length; i++) {
    const v = arr[i];
    const need = cible - v;
    if (seen.has(need)) return [seen.get(need), i]; // première paire
    if (!seen.has(v)) seen.set(v, i);
  }
  return null;
}
```

---

## 14) Fusion de deux triés (deux pointeurs) 🧷
**Idée clé :** avancer le pointeur du plus petit; en cas d’égalité, prendre de `a` (stabilité).  
**Complexité :** O(n+m).

```js
function fusionTries(a, b) {
  const out = [];
  let i = 0, j = 0;
  while (i < a.length && j < b.length) {
    if (a[i] <= b[j]) out.push(a[i++]); // stabilité si égal
    else out.push(b[j++]);
  }
  while (i < a.length) out.push(a[i++]);
  while (j < b.length) out.push(b[j++]);
  return out;
}
```

---

## 15) Fenêtre glissante — somme max (taille k) 🪟
**Idée clé :** somme initiale des k premiers, puis glisser (retirer gauche, ajouter droite).  
**Complexité :** O(n) / O(1).

```js
function sommeMax(arr, k) {
  const res = sommeMaxInterval(arr, k);
  return res ? res.somme : null;
}

function sommeMaxInterval(arr, k) {
  if (k <= 0 || k > arr.length) return null;
  let sum = 0;
  for (let i = 0; i < k; i++) sum += arr[i];
  let best = sum, start = 0;
  for (let i = k; i < arr.length; i++) {
    sum += arr[i] - arr[i - k];
    if (sum > best) { best = sum; start = i - k + 1; }
  }
  return { somme: best, start, end: start + k - 1 };
}
```

---

# <span style="color:gold;">Niveau 4 — Structures & Décisions</span> 🔴

## 16) Parenthèses bien formées 🧮
**Idée clé (simple) :** compteur jamais négatif, finit à 0.  
**Idée clé (multi) :** pile + correspondances.  
**Complexité :** O(n).

```js
function valideParenthesesSimple(s) {
  let c = 0;
  for (const ch of s) {
    if (ch === '(') c++;
    else if (ch === ')') { c--; if (c < 0) return false; }
  }
  return c === 0;
}

function valideParenthesesMulti(s) {
  const open = new Set(['(', '[', '{']);
  const match = new Map([[')','('], [']','['], ['}','{']]);
  const stack = [];
  for (const ch of s) {
    if (open.has(ch)) stack.push(ch);
    else if (match.has(ch)) {
      if (stack.pop() !== match.get(ch)) return false;
    }
  }
  return stack.length === 0;
}
```

---

## 17) Regrouper par clé 🧱
**Idée clé :** `reduce` en objet de groupes; clé manquante → `"inconnu"`.  
**Complexité :** O(n).

```js
function groupBy(arr, key) {
  const getKey = (typeof key === 'function')
    ? key
    : (item) => (item && item[key] != null ? String(item[key]) : 'inconnu');

  return arr.reduce((acc, item) => {
    const k = getKey(item);
    (acc[k] ||= []).push(item);
    return acc;
  }, {});
}
```

---

## 18) Tri par comptage (Count sort “lite”) 📊
**Idée clé :** compter les fréquences jusqu’au max, puis reconstruire.  
**Complexité :** O(n + k) où k = max+1.

```js
function countSortLite(arr) {
  if (arr.length === 0) return { sorted: [], freq: [] };
  const max = Math.max(...arr);
  if (arr.some(x => x < 0 || !Number.isInteger(x))) {
    throw new Error("Seulement entiers non négatifs pour count sort lite.");
  }
  const freq = Array(max + 1).fill(0);
  for (const x of arr) freq[x]++;
  const out = [];
  for (let v = 0; v < freq.length; v++) {
    for (let c = 0; c < freq[v]; c++) out.push(v);
  }
  return { sorted: out, freq };
}
```

---

## 19) Racine digitale (digital root) 🔂
**Idée clé :** sommer les chiffres jusqu’à un seul chiffre.  
**Complexité :** O(d * itérations) d = #chiffres.

```js
function racineDigitale(n) {
  n = Math.abs(n|0);
  while (n >= 10) {
    let s = 0, x = n;
    while (x > 0) { s += x % 10; x = (x / 10) | 0; }
    n = s;
  }
  return n;
}
```

---

## 20) Zigzag (up/down) 📈📉
**Idée clé :** alterner strictement `>` et `<`.  
**Complexité :** O(n).

```js
function estZigzag(arr) {
  return estZigzagAvecRupture(arr).ok;
}

function estZigzagAvecRupture(arr) {
  const n = arr.length;
  if (n <= 2) return { ok: n <= 1 ? true : arr[0] !== arr[1], ruptureIndex: null };
  // déterminer la première direction non nulle
  let dir = 0; // +1 : up, -1 : down
  for (let i = 1; i < n; i++) {
    const diff = arr[i] - arr[i-1];
    if (diff === 0) return { ok: false, ruptureIndex: i-1 };
    if (dir === 0) dir = diff > 0 ? +1 : -1;
    else {
      // doit alterner
      const curr = diff > 0 ? +1 : -1;
      if (curr === dir) return { ok: false, ruptureIndex: i-1 };
      dir = curr;
    }
  }
  return { ok: true, ruptureIndex: null };
}
```

---

# <span style="color:gold;">Mini-projets (bonus fun)</span> ⭐

## 21) Bulls & Cows 🐂🐄
**Idée clé :** 1ère passe → bulls; 2ème → cows via fréquences des non-bulls.  
**Complexité :** O(n).

```js
function bullsAndCows(secret, guess) {
  if (secret.length !== guess.length) throw new Error("Tailles différentes");
  let bulls = 0;
  const countS = new Map(), countG = new Map(); // pour cows
  for (let i = 0; i < secret.length; i++) {
    const s = secret[i], g = guess[i];
    if (s === g) bulls++;
    else {
      countS.set(s, (countS.get(s) || 0) + 1);
      countG.set(g, (countG.get(g) || 0) + 1);
    }
  }
  let cows = 0;
  for (const [ch, cS] of countS) cows += Math.min(cS, countG.get(ch) || 0);
  return `${bulls}A${cows}B`;
}
```

---

## 22) Horloge mots ⏰
**Idée clé :** dictionnaire 0..59; cas spéciaux : `minuit`, `midi`, `et quart`, `et demie`, `moins le quart`.  
**Convention :** 13:05 → “une heure cinq” (mode 12h).  
**Complexité :** O(1) (tables).

```js
function enMots(h, m) {
  const mots = ["zéro","une","deux","trois","quatre","cinq","six","sept","huit","neuf","dix",
    "onze","douze","treize","quatorze","quinze","seize","dix-sept","dix-huit","dix-neuf",
    "vingt","vingt et un","vingt-deux","vingt-trois","vingt-quatre","vingt-cinq","vingt-six","vingt-sept","vingt-huit","vingt-neuf",
    "trente","trente et un","trente-deux","trente-trois","trente-quatre","trente-cinq","trente-six","trente-sept","trente-huit","trente-neuf",
    "quarante","quarante et un","quarante-deux","quarante-trois","quarante-quatre","quarante-cinq","quarante-six","quarante-sept","quarante-huit","quarante-neuf",
    "cinquante","cinquante et un","cinquante-deux","cinquante-trois","cinquante-quatre","cinquante-cinq","cinquante-six","cinquante-sept","cinquante-huit","cinquante-neuf"
  ];
  const h12 = ((h % 12) + 12) % 12; // 0..11
  if (h === 0 && m === 0) return "minuit";
  if (h === 12 && m === 0) return "midi";
  const heureWord = h12 === 1 ? "une heure" : (h12 === 0 ? "douze heures" : `${mots[h12]} heures`);
  if (m === 0) return heureWord;
  if (m === 15) return `${heureWord} et quart`;
  if (m === 30) return `${heureWord} et demie`; // 'demie' accordée à 'heure' (fém.)
  if (m === 45) {
    const nextH12 = (h12 + 1) % 12 || 12;
    const nextHeure = nextH12 === 1 ? "une heure" : `${mots[nextH12]} heures`;
    return `${nextHeure} moins le quart`;
  }
  if (m < 30) return `${heureWord} ${mots[m]}`;
  // m > 30 et != 45
  const reste = 60 - m;
  const nextH12 = (h12 + 1) % 12 || 12;
  const nextHeure = nextH12 === 1 ? "une heure" : `${mots[nextH12]} heures`;
  return `${nextHeure} moins ${mots[reste]}`;
}
```

---

## 23) Romain ↔ Décimal (borné) 🏛️
**Idée clé :** lecture avec paires soustractives; génération gloutonne.  
**Validation simple :** ré-encoder et comparer.

```js
function romainVersInt(s) {
  if (typeof s !== 'string' || s.length === 0) return null;
  const val = new Map([['I',1],['V',5],['X',10],['L',50],['C',100],['D',500],['M',1000]]);
  s = s.toUpperCase();
  let total = 0;
  for (let i = 0; i < s.length; i++) {
    const v = val.get(s[i]);
    const next = val.get(s[i+1]) || 0;
    if (!v) return null;
    if (v < next) { total += next - v; i++; }
    else total += v;
  }
  if (total < 1 || total > 3999) return null;
  // validation : doit re-mapper à la forme canonique
  return intVersRomain(total) === s ? total : null;
}

function intVersRomain(n) {
  if (!Number.isInteger(n) || n < 1 || n > 3999) return null;
  const pairs = [
    [1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],
    [100,'C'],[90,'XC'],[50,'L'],[40,'XL'],
    [10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']
  ];
  let out = '';
  for (const [v, sym] of pairs) {
    while (n >= v) { out += sym; n -= v; }
  }
  return out;
}
```

---

## 24) Tableaux 2D — îles de 1 🏝️
**Version simple :** compter les segments **horizontaux** de `1` par ligne (pas d’union verticale).  
**Version DFS :** composantes connexes en 4-directions.

```js
// Simple : uniquement segments horizontaux
function compterIlesSimple(grid) {
  let count = 0;
  for (const row of grid) {
    let inRun = false;
    for (const cell of row) {
      if (cell === 1 && !inRun) { count++; inRun = true; }
      else if (cell === 0) inRun = false;
    }
  }
  return count;
}

// DFS 4-dir
function compterIlesDFS(grid) {
  const R = grid.length, C = grid[0]?.length || 0;
  const vis = Array.from({length: R}, () => Array(C).fill(false));
  const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
  let count = 0;

  function dfs(r,c) {
    vis[r][c] = true;
    for (const [dr,dc] of dirs) {
      const nr = r+dr, nc = c+dc;
      if (nr>=0 && nr<R && nc>=0 && nc<C && grid[nr][nc]===1 && !vis[nr][nc]) dfs(nr,nc);
    }
  }

  for (let r=0; r<R; r++) for (let c=0; c<C; c++) {
    if (grid[r][c]===1 && !vis[r][c]) { count++; dfs(r,c); }
  }
  return count;
}
```

---

## 25) Validateur de mot de passe 🔐
**Règles :** longueur ≥ 8, au moins 1 maj, 1 min, 1 chiffre, 1 spécial.  
**Sortie :** `{ ok, raisons[], score }` où `score ∈ [0..5]`.

```js
function validerMotDePasse(pwd) {
  const raisons = [];
  if (pwd.length < 8) raisons.push("Longueur < 8");
  if (!/[A-Z]/.test(pwd)) raisons.push("Manque une majuscule");
  if (!/[a-z]/.test(pwd)) raisons.push("Manque une minuscule");
  if (!/[0-9]/.test(pwd)) raisons.push("Manque un chiffre");
  if (!/[^A-Za-z0-9]/.test(pwd)) raisons.push("Manque un caractère spécial");
  const score = 5 - raisons.length;
  return { ok: score === 5, raisons, score };
}
```
