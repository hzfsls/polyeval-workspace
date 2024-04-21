from polyeval import *

github_popular = [
    "csharp", "cpp", "coffeescript", "dart", "elixir", 
    "go", "groovy", "java", "javascript", "kotlin", 
    "objectivec", "perl", "php", "python", "ruby",
    "rust", "scala", "swift", "typescript"
]

other_popular = [
    "clojure", "commonlisp", "d", "elm", "erlang",
    "fsharp", "hack", "haskell", "julia", "lua", 
    "ocaml", "racket", "visualbasic"
]

def get_signatures(lang: str, question) -> str:
    return find_target(lang).code_generator.gen_all_signature(question.functions).strip()


ped_dsl = """\
def Example1
    fun substr_len_prod(words: list<str>, word: str) -> int
        (["ab", "dcb", "ffe", "def", "abd"], "abdcb") -> 18
        (["apple", "banana", "cherry", "date", "elderberry"], "applebanana") -> 30
        (["010", "110", "101", "001", "111"], "010110") -> 27
        ([], "abcde") -> 1
        (["a", "bcd", "e"], "abcde") -> 3

def Example2
    fun fizz_buzz_str(num: int) -> str
    fun fizz_buzz(num: int) -> str
        (1) -> "1"
        (3) -> "12Fizz"
        (5) -> "12Fizz4Buzz"
        (15) -> "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz"
        (100) -> "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19BuzzFizz2223FizzBuzz26Fizz2829FizzBuzz3132Fizz34BuzzFizz3738FizzBuzz41Fizz4344FizzBuzz4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FizzBuzz6162Fizz64BuzzFizz6768FizzBuzz71Fizz7374FizzBuzz7677Fizz79BuzzFizz8283FizzBuzz86Fizz8889FizzBuzz9192Fizz94BuzzFizz9798FizzBuzz"
"""

questions = parse_questions(ped_dsl)

# Python Solutions
lang = "python"

imp_e1 = """\
def substr_len_prod(words: list[str], word: str) -> int:
    result = 1
    for x in words:
        if x in word:
            result *= len(x)
    return result
"""

fun_e1 = """\
def substr_len_prod(words: list[str], word: str) -> int:
    return functools.reduce(lambda x, y: x*y, [len(x) for x in words if x in word], 1)
"""

imp_e2 = """\
def fizz_buzz_str(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)

def fizz_buzz(num: int) -> str:
    result = ""
    for x in range(1, num+1):
        result += fizz_buzz_str(x)
    return result
"""

fun_e2 = """\
def fizz_buzz_str(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)

def fizz_buzz(num: int) -> str:
    return "".join([fizz_buzz_str(x) for x in range(1, num+1)])
"""

# C# Solutions

lang = "csharp"

imp_e1 = """\
static int SubstrLenProd(List<string> words, string word) {
    int result = 1;
    foreach (string x in words) {
        if (word.Contains(x)) {
            result *= x.Length;
        }
    }
    return result;
}
"""

fun_e1 = """\
static int SubstrLenProd(List<string> words, string word) {
    return words.Where(x => word.Contains(x))
                .Select(x => x.Length)
                .Aggregate(1, (x, y) => x * y);
}
"""

imp_e2 = """\
static string FizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return num.ToString();
}

static string FizzBuzz(int num) {
    string result = "";
    for (int x = 1; x <= num; x++) {
        result += FizzBuzzStr(x);
    }
    return result;
}
"""

fun_e2 = """\
static string FizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return num.ToString();
}

static string FizzBuzz(int num) {
    return string.Concat(Enumerable.Range(1, num).Select(x => FizzBuzzStr(x)));
}
"""

# C++ Solutions

lang = "cpp"

imp_e1 = """\
int substrLenProd(const vector<string>& words, const string& word) {
    int result = 1;
    for (const string& x : words) {
        if (word.find(x) != string::npos) {
            result *= x.size();
        }
    }
    return result;
}
"""

fun_e1 = """\
int substrLenProd(const vector<string>& words, const string& word) {
    return ranges::fold_left(words 
            | views::filter([&](auto& x) { return word.find(x) != string::npos; }) 
            | views::transform([](auto& x) { return x.size(); }),
            1, multiplies());
}
"""

imp_e2 = """\
string fizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return to_string(num);
}

string fizzBuzz(int num) {
    string result;
    for (int x = 1; x <= num; x++) {
        result += fizzBuzzStr(x);
    }
    return result;
}
"""

fun_e2 = """\
string fizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return to_string(num);
}

string fizzBuzz(int num) {
    return ranges::fold_left(
            views::iota(1, num+1) | views::transform(fizzBuzzStr) | views::join,
            string(), plus());
}
"""

# CoffeeScript Solutions

lang = "coffeescript"

imp_e1 = """\
substrLenProd = (words, word) ->
    result = 1
    for x in words
        if word.includes(x)
            result *= x.length
    result
"""

fun_e1 = """\
substrLenProd = (words, word) ->
    words.filter((x) -> word.includes(x))
            .map((x) -> x.length)
            .reduce(((x, y) -> x * y), 1)
"""

imp_e2 = """\
fizzBuzzStr = (num) ->
    if num % 3 is 0 and num % 5 is 0
        return "FizzBuzz"
    if num % 3 is 0
        return "Fizz"
    if num % 5 is 0
        return "Buzz"
    num.toString()

fizzBuzz = (num) ->
    result = ""
    for x in [1..num]
        result += fizzBuzzStr(x)
    result
"""

fun_e2 = """\
fizzBuzzStr = (num) ->
    if num % 3 is 0 and num % 5 is 0
        return "FizzBuzz"
    if num % 3 is 0
        return "Fizz"
    if num % 5 is 0
        return "Buzz"
    num.toString()

fizzBuzz = (num) ->
    [1..num].map(fizzBuzzStr).join("")
"""

# Dart Solutions

lang = "dart"

imp_e1 = """\
int substrLenProd(List<String> words, String word) {
    int result = 1;
    for (String x in words) {
        if (word.contains(x)) {
            result *= x.length;
        }
    }
    return result;
}
"""

fun_e1 = """\
int substrLenProd(List<String> words, String word) {
    return words.where((x) => word.contains(x))
                .map((x) => x.length)
                .fold(1, (x, y) => x * y);
}
"""

imp_e2 = """\
String fizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return num.toString();
}

String fizzBuzz(int num) {
    String result = "";
    for (int x = 1; x <= num; x++) {
        result += fizzBuzzStr(x);
    }
    return result;
}
"""

fun_e2 = """\
String fizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return num.toString();
}

String fizzBuzz(int num) {
    return List.generate(num, (x) => x+1).map(fizzBuzzStr).join("");
}
"""

# Elixir Solutions

lang = "elixir"

fun_e1 = """\
def substr_len_prod(words, word) do
    words |> Enum.filter(&(String.contains?(word, &1))) 
            |> Enum.map(&(String.length(&1))) 
            |> Enum.reduce(1, &(&1*&2))
end
"""

fun_e2 = """\
def fizz_buzz_str(num) do
    cond do
        rem(num, 3) == 0 and rem(num, 5) == 0 -> "FizzBuzz"
        rem(num, 3) == 0 -> "Fizz"
        rem(num, 5) == 0 -> "Buzz"
        true -> Integer.to_string(num)
    end
end

def fizz_buzz(num) do
    1..num |> Enum.map(&fizz_buzz_str/1) |> Enum.join()
end
"""

# Go Solutions

lang = "go"

imp_e1 = """\
func substrLenProd(words []string, word string) int {
    result := 1
    for _, x := range words {
        if strings.Contains(word, x) {
            result *= len(x)
        }
    }
    return result
}
"""

imp_e2 = """\
func fizzBuzzStr(num int) string {
    if num % 3 == 0 && num % 5 == 0 {
        return "FizzBuzz"
    }
    if num % 3 == 0 {
        return "Fizz"
    }
    if num % 5 == 0 {
        return "Buzz"
    }
    return strconv.Itoa(num)
}

func fizzBuzz(num int) string {
    result := ""
    for x := 1; x <= num; x++ {
        result += fizzBuzzStr(x)
    }
    return result
}
"""

# Groovy Solutions

lang = "groovy"

imp_e1 = """\
def substrLenProd(words, word) {
    result = 1
    for (x in words) {
        if (word.contains(x)) {
            result *= x.size()
        }
    }
    result
}
"""

fun_e1 = """\
def substrLenProd(words, word) {
    words.findAll { word.contains(it) }
            .collect { it.size() }
            .inject(1) { x, y -> x * y }
}
"""

imp_e2 = """\
def fizzBuzzStr(num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz"
    }
    if (num % 3 == 0) {
        return "Fizz"
    }
    if (num % 5 == 0) {
        return "Buzz"
    }
    num.toString()
}

def fizzBuzz(num) {
    result = ""
    for (x in 1..num) {
        result += fizzBuzzStr(x)
    }
    result
}
"""

fun_e2 = """\
def fizzBuzzStr(num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz"
    }
    if (num % 3 == 0) {
        return "Fizz"
    }
    if (num % 5 == 0) {
        return "Buzz"
    }
    num.toString()
}

def fizzBuzz(num) {
    (1..num).collect { fizzBuzzStr(it) }.join()
}
"""

# Java Solutions

lang = "java"

imp_e1 = """\
static int substrLenProd(List<String> words, String word) {
    int result = 1;
    for (String x : words) {
        if (word.contains(x)) {
            result *= x.length();
        }
    }
    return result;
}
"""

fun_e1 = """\
static int substrLenProd(List<String> words, String word) {
    return words.stream()
            .filter(x -> word.contains(x))
            .map(x -> x.length())
            .reduce(1, (x, y) -> x * y);
}
"""

imp_e2 = """\
static String fizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return Integer.toString(num);
}

static String fizzBuzz(int num) {
    String result = "";
    for (int x = 1; x <= num; x++) {
        result += fizzBuzzStr(x);
    }
    return result;
}
"""

fun_e2 = """\
static String fizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return Integer.toString(num);
}

static String fizzBuzz(int num) {
    return IntStream.rangeClosed(1, num)
            .mapToObj(x -> fizzBuzzStr(x))
            .collect(Collectors.joining());
}
"""

# JavaScript Solutions

lang = "javascript"

imp_e1 = """\
function substrLenProd(words, word) {
    let result = 1;
    for (let x of words) {
        if (word.includes(x)) {
            result *= x.length;
        }
    }
    return result;
}
"""

fun_e1 = """\
function substrLenProd(words, word) {
    return words.filter(x => word.includes(x))
            .map(x => x.length)
            .reduce((x, y) => x * y, 1);
}
"""

imp_e2 = """\
function fizzBuzzStr(num) {
    if (num % 3 === 0 && num % 5 === 0) {
        return "FizzBuzz";
    }
    if (num % 3 === 0) {
        return "Fizz";
    }
    if (num % 5 === 0) {
        return "Buzz";
    }
    return num.toString();
}

function fizzBuzz(num) {
    let result = "";
    for (let x = 1; x <= num; x++) {
        result += fizzBuzzStr(x);
    }
    return result;
}
"""

fun_e2 = """\
function fizzBuzzStr(num) {
    if (num % 3 === 0 && num % 5 === 0) {
        return "FizzBuzz";
    }
    if (num % 3 === 0) {
        return "Fizz";
    }
    if (num % 5 === 0) {
        return "Buzz";
    }
    return num.toString();
}

function fizzBuzz(num) {
    return Array.from({length: num}, (_, x) => x+1)
            .map(x => fizzBuzzStr(x))
            .join("");
}
"""

# Kotlin Solutions

lang = "kotlin"

imp_e1 = """\
fun substrLenProd(words: List<String>, word: String): Int {
    var result = 1
    for (x in words) {
        if (word.contains(x)) {
            result *= x.length
        }
    }
    return result
}
"""

fun_e1 = """\
fun substrLenProd(words: List<String>, word: String): Int {
    return words.filter { word.contains(it) }
            .map { it.length }
            .fold(1) { x, y -> x * y }
}
"""

imp_e2 = """\
fun fizzBuzzStr(num: Int): String {
    return when {
        num % 3 == 0 && num % 5 == 0 -> "FizzBuzz"
        num % 3 == 0 -> "Fizz"
        num % 5 == 0 -> "Buzz"
        else -> num.toString()
    }
}

fun fizzBuzz(num: Int): String {
    var result = ""
    for (x in 1..num) {
        result += fizzBuzzStr(x)
    }
    return result
}
"""

fun_e2 = """\
fun fizzBuzzStr(num: Int): String {
    return when {
        num % 3 == 0 && num % 5 == 0 -> "FizzBuzz"
        num % 3 == 0 -> "Fizz"
        num % 5 == 0 -> "Buzz"
        else -> num.toString()
    }
}

fun fizzBuzz(num: Int): String {
    return (1..num).map { fizzBuzzStr(it) }.joinToString("")
}
"""

# Objective-C Solutions

lang = "objectivec"

imp_e1 = """\
+ (NSNumber *)substrLenProd:(NSArray<NSString *> *)words :(NSString *)word {
    NSNumber *result = @1;
    for (NSString *x in words) {
        if ([word containsString:x]) {
            result = @([result intValue] * x.length);
        }
    }
    return result;
}
"""

imp_e2 = """\
+ (NSString *)fizzBuzzStr:(NSNumber *)num {
    if ([num intValue] % 3 == 0 && [num intValue] % 5 == 0) {
        return @"FizzBuzz";
    }
    if ([num intValue] % 3 == 0) {
        return @"Fizz";
    }
    if ([num intValue] % 5 == 0) {
        return @"Buzz";
    }
    return [num stringValue];
}

+ (NSString *)fizzBuzz:(NSNumber *)num {
    NSMutableString *result = [NSMutableString new];
    for (int x = 1; x <= [num intValue]; x++) {
        [result appendString:[self fizzBuzzStr:@(x)]];
    }
    return result;
}
"""

# Perl Solutions

lang = "perl"

imp_e1 = """\
sub substr_len_prod($words, $word) {
    my $result = 1;
    for my $x (@$words) {
        if (index($word, $x) != -1) {
            $result *= length($x);
        }
    }
    return $result;
}
"""

fun_e1 = """\
sub substr_len_prod($words, $word) {
    return reduce { $a * $b } 1, map { length($_) } grep { index($word, $_) != -1 } @$words;
}
"""

imp_e2 = """\
sub fizz_buzz_str($num) {
    if ($num % 3 == 0 && $num % 5 == 0) {
        return "FizzBuzz";
    }
    if ($num % 3 == 0) {
        return "Fizz";
    }
    if ($num % 5 == 0) {
        return "Buzz";
    }
    return $num;
}

sub fizz_buzz($num) {
    my $result = "";
    for my $x (1..$num) {
        $result .= fizz_buzz_str($x);
    }
    return $result;
}
"""

fun_e2 = """\
sub fizz_buzz_str($num) {
    if ($num % 3 == 0 && $num % 5 == 0) {
        return "FizzBuzz";
    }
    if ($num % 3 == 0) {
        return "Fizz";
    }
    if ($num % 5 == 0) {
        return "Buzz";
    }
    return $num;
}

sub fizz_buzz($num) {
    return join "", map { fizz_buzz_str($_) } 1..$num;
}
"""

# PHP Solutions

lang = "php"

imp_e1 = """\
function substr_len_prod($words, $word) {
    $result = 1;
    foreach ($words as $x) {
        if (strpos($word, $x) !== false) {
            $result *= strlen($x);
        }
    }
    return $result;
}
"""

fun_e1 = """\
function substr_len_prod($words, $word) {
    return array_reduce(
            array_map('strlen', 
                    array_filter($words, fn($x) => strpos($word, $x) !== false)
            ), fn($a, $b) => $a * $b, 1);
}
"""

imp_e2 = """\
function fizz_buzz_str($num) {
    if ($num % 3 == 0 && $num % 5 == 0) {
        return "FizzBuzz";
    }
    if ($num % 3 == 0) {
        return "Fizz";
    }
    if ($num % 5 == 0) {
        return "Buzz";
    }
    return (string)$num;
}

function fizz_buzz($num) {
    $result = "";
    for ($x = 1; $x <= $num; $x++) {
        $result .= fizz_buzz_str($x);
    }
    return $result;
}
"""

fun_e2 = """\
function fizz_buzz_str($num) {
    if ($num % 3 == 0 && $num % 5 == 0) {
        return "FizzBuzz";
    }
    if ($num % 3 == 0) {
        return "Fizz";
    }
    if ($num % 5 == 0) {
        return "Buzz";
    }
    return (string)$num;
}

function fizz_buzz($num) {
    return implode("", array_map('fizz_buzz_str', range(1, $num)));
}
"""

# Ruby Solutions

lang = "ruby"

imp_e1 = """\
def substr_len_prod(words, word)
    result = 1
    words.each do |x|
        if word.include?(x)
            result *= x.length
        end
    end
    result
end
"""

fun_e1 = """\
def substr_len_prod(words, word)
    words.select { |x| word.include?(x) }
            .map { |x| x.length }
            .reduce(1, :*)
end
"""

imp_e2 = """\
def fizz_buzz_str(num)
    if num % 3 == 0 && num % 5 == 0
        return "FizzBuzz"
    end
    if num % 3 == 0
        return "Fizz"
    end
    if num % 5 == 0
        return "Buzz"
    end
    num.to_s
end

def fizz_buzz(num)
    result = ""
    (1..num).each do |x|
        result += fizz_buzz_str(x)
    end
    result
end
"""

fun_e2 = """\
def fizz_buzz_str(num)
    if num % 3 == 0 && num % 5 == 0
        return "FizzBuzz"
    end
    if num % 3 == 0
        return "Fizz"
    end
    if num % 5 == 0
        return "Buzz"
    end
    num.to_s
end

def fizz_buzz(num)
    (1..num).map { |x| fizz_buzz_str(x) }.join
end
"""

# Rust Solutions

lang = "rust"

imp_e1 = """\
fn substr_len_prod(words: &Vec<String>, word: &String) -> i32 {
    let mut result = 1;
    for x in words.iter() {
        if word.contains(x) {
            result *= x.len() as i32;
        }
    }   
    result
}
"""

fun_e1 = """\
fn substr_len_prod(words: &Vec<String>, word: &String) -> i32 {
    words.iter()
            .filter(|x| word.contains(*x))
            .map(|x| x.len() as i32)
            .fold(1, |x, y| x * y)
}
"""

imp_e2 = """\
fn fizz_buzz_str(num: i32) -> String {
    if num % 3 == 0 && num % 5 == 0 {
        return "FizzBuzz".to_string();
    }
    if num % 3 == 0 {
        return "Fizz".to_string();
    }
    if num % 5 == 0 {
        return "Buzz".to_string();
    }
    num.to_string()
}

fn fizz_buzz(num: i32) -> String {
    let mut result = String::new();
    for x in 1..=num {
        result.push_str(&fizz_buzz_str(x));
    }
    result
}
"""

fun_e2 = """\
fn fizz_buzz_str(num: i32) -> String {
    if num % 3 == 0 && num % 5 == 0 {
        return "FizzBuzz".to_string();
    }
    if num % 3 == 0 {
        return "Fizz".to_string();
    }
    if num % 5 == 0 {
        return "Buzz".to_string();
    }
    num.to_string()
}

fn fizz_buzz(num: i32) -> String {
    (1..=num).map(fizz_buzz_str).collect()
}
"""

# Scala Solutions

lang = "scala"

imp_e1 = """\
def substrLenProd(words: Seq[String], word: String): Int = {
    var result = 1
    for (x <- words) {
        if (word.contains(x)) {
            result *= x.length
        }
    }
    result
}
"""

fun_e1 = """\
def substrLenProd(words: Seq[String], word: String): Int = {
    words.filter(word.contains(_))
            .map(_.length)
            .fold(1)(_ * _)
}
"""

imp_e2 = """\
def fizzBuzzStr(num: Int): String = {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz"
    } else if (num % 3 == 0) {
        return "Fizz"
    } else if (num % 5 == 0) {
        return "Buzz"
    }
    num.toString
}

def fizzBuzz(num: Int): String = {
    var result = ""
    for (x <- 1 to num) {
        result += fizzBuzzStr(x)
    }
    result
}
"""

fun_e2 = """\
def fizzBuzzStr(num: Int): String = {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz"
    } else if (num % 3 == 0) {
        return "Fizz"
    } else if (num % 5 == 0) {
        return "Buzz"
    }
    num.toString
}

def fizzBuzz(num: Int): String = {
    (1 to num).map(fizzBuzzStr).mkString
}
"""

# Swift Solutions

lang = "swift"

imp_e1 = """\
func substrLenProd(_ words: [String], _ word: String) -> Int {
    var result = 1
    for x in words {
        if word.contains(x) {
            result *= x.count
        }
    }
    return result
}
"""

fun_e1 = """\
func substrLenProd(_ words: [String], _ word: String) -> Int {
    return words.filter { word.contains($0) }
            .map { $0.count }
            .reduce(1, *)
}
"""

imp_e2 = """\
func fizzBuzzStr(_ num: Int) -> String {
    if num % 3 == 0 && num % 5 == 0 {
        return "FizzBuzz"
    }
    if num % 3 == 0 {
        return "Fizz"
    }
    if num % 5 == 0 {
        return "Buzz"
    }
    return String(num)
}

func fizzBuzz(_ num: Int) -> String {
    var result = ""
    for x in 1...num {
        result += fizzBuzzStr(x)
    }
    return result
}
"""

fun_e2 = """\
func fizzBuzzStr(_ num: Int) -> String {
    if num % 3 == 0 && num % 5 == 0 {
        return "FizzBuzz"
    }
    if num % 3 == 0 {
        return "Fizz"
    }
    if num % 5 == 0 {
        return "Buzz"
    }
    return String(num)
}

func fizzBuzz(_ num: Int) -> String {
    return (1...num).map(fizzBuzzStr).joined()
}
"""

# TypeScript Solutions

lang = "typescript"

imp_e1 = """\
function substrLenProd(words: string[], word: string): number {
    let result = 1;
    for (const x of words) {
        if (word.includes(x)) {
            result *= x.length;
        }
    }
    return result;
}
"""

fun_e1 = """\
function substrLenProd(words: string[], word: string): number {
    return words.filter(x => word.includes(x))
            .map(x => x.length)
            .reduce((x, y) => x * y, 1);
}
"""

imp_e2 = """\
function fizzBuzzStr(num: number): string {
    if (num % 3 === 0 && num % 5 === 0) {
        return "FizzBuzz";
    }
    if (num % 3 === 0) {
        return "Fizz";
    }
    if (num % 5 === 0) {
        return "Buzz";
    }
    return num.toString();
}

function fizzBuzz(num: number): string {
    let result = "";
    for (let x = 1; x <= num; x++) {
        result += fizzBuzzStr(x);
    }
    return result;
}
"""

fun_e2 = """\
function fizzBuzzStr(num: number): string {
    if (num % 3 === 0 && num % 5 === 0) {
        return "FizzBuzz";
    }
    if (num % 3 === 0) {
        return "Fizz";
    }
    if (num % 5 === 0) {
        return "Buzz";
    }
    return num.toString();
}

function fizzBuzz(num: number): string {
    return Array.from({length: num}, (_, x) => x+1)
            .map(x => fizzBuzzStr(x))
            .join("");
}
"""

# Clojure Solutions

lang = "clojure"

fun_e1 = """\
(defn substr-len-prod [words word]
    (reduce * 1 
        (map count 
            (filter #(clojure.string/includes? word %) words))))
"""

fun_e2 = """\
(defn fizz-buzz-str [num]
    (cond
        (and (zero? (mod num 3)) (zero? (mod num 5))) "FizzBuzz"
        (zero? (mod num 3)) "Fizz"
        (zero? (mod num 5)) "Buzz"
        :else (str num)))

(defn fizz-buzz [num]
    (clojure.string/join 
        (map fizz-buzz-str 
            (range 1 (inc num)))))
"""

# Common Lisp Solutions

lang = "commonlisp"

fun_e1 = """\
(defun substr-len-prod (words word)
    (reduce #'* 
        (mapcar #'length 
            (remove-if-not (lambda (x) (search x word)) words))))
"""

fun_e2 = """\
(defun fizz-buzz-str (num)
    (cond
        ((and (zerop (mod num 3)) (zerop (mod num 5))) "FizzBuzz")
        ((zerop (mod num 3)) "Fizz")
        ((zerop (mod num 5)) "Buzz")
        (t (write-to-string num))))

(defun fizz-buzz (num)
    (apply #'concatenate 'string
        (mapcar #'fizz-buzz-str 
            (loop for x from 1 to num collect x))))
"""

# D Solutions

lang = "d"

imp_e1 = """\
int substrLenProd(string[] words, string word) {
    int result = 1;
    foreach (x; words) {
        if (word.canFind(x)) {
            result *= x.length;
        }
    }
    return result;
}
"""

fun_e1 = """\
int substrLenProd(string[] words, string word) {
    return words.filter!(x => word.canFind(x))
            .map!(x => cast(int)x.length)
            .fold!((a, b) => a * b)(1);
}
"""

imp_e2 = """\
string fizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return to!string(num);
}

string fizzBuzz(int num) {
    string result = "";
    foreach (x; 1..num+1) {
        result ~= fizzBuzzStr(x);
    }
    return result;
}
"""

fun_e2 = """\
string fizzBuzzStr(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
        return "FizzBuzz";
    }
    if (num % 3 == 0) {
        return "Fizz";
    }
    if (num % 5 == 0) {
        return "Buzz";
    }
    return to!string(num);
}

string fizzBuzz(int num) {
    return iota(1, num+1).map!(x => fizzBuzzStr(x)).join("");
}
"""

# Elm Solutions

lang = "elm"

fun_e1 = """\
substrLenProd : List String -> String -> Int
substrLenProd words word =
    words |> List.filter (\\x -> String.contains x word)
            |> List.map String.length
            |> List.foldl (*) 1
"""

fun_e2 = """\
fizzBuzzStr : Int -> String
fizzBuzzStr num =
    case (modBy 3 num, modBy 5 num) of
        (0, 0) -> "FizzBuzz"
        (0, _) -> "Fizz"
        (_, 0) -> "Buzz"
        _ -> String.fromInt num

fizzBuzz : Int -> String
fizzBuzz num =
    List.range 1 num
            |> List.map fizzBuzzStr
            |> String.concat
"""

# Erlang Solutions

lang = "erlang"

fun_e1 = """\
substr_len_prod(Words, Word) ->
    lists:foldl(fun(X, Acc) -> Acc * X end, 1, 
        lists:map(fun(X) -> string:length(X) end,
            lists:filter(fun(X) -> string:str(Word, X) > 0 end, Words))).
"""

fun_e2 = """\
fizz_buzz_str(Num) ->
    case {Num rem 3, Num rem 5} of
        {0, 0} -> "FizzBuzz";
        {0, _} -> "Fizz";
        {_, 0} -> "Buzz";
        _ -> integer_to_list(Num)
    end.

fizz_buzz(Num) ->
    lists:join("",
        lists:map(fun(X) -> fizz_buzz_str(X) end,
            lists:seq(1, Num))).
"""

# F# Solutions

lang = "fsharp"

fun_e1 = """\
let substrLenProd (words: list<string>) (word: string) =
    words |> List.filter (fun x -> word.Contains(x))
            |> List.map (fun x -> x.Length)
            |> List.fold (fun acc x -> acc * x) 1
"""

fun_e2 = """\
let fizzBuzzStr (num: int) =
    match num % 3, num % 5 with
    | 0, 0 -> "FizzBuzz"
    | 0, _ -> "Fizz"
    | _, 0 -> "Buzz"
    | _, _ -> num.ToString()

let fizzBuzz (num: int) =
    [1..num] |> List.map fizzBuzzStr |> List.reduce (+)
"""

# Hack Solutions

lang = "hack"

imp_e1 = """\
function substr_len_prod(vec<string> $words, string $word): int {
    $result = 1;
    foreach ($words as $x) {
        if (Str\\contains($word, $x)) {
            $result *= Str\\length($x);
        }
    }
    return $result;
}
"""

fun_e1 = """\
function substr_len_prod(vec<string> $words, string $word): int {
    return $words |> Vec\\filter($$, $x ==> Str\\contains($word, $x))
            |> Vec\\map($$, $x ==> Str\\length($x))
            |> C\\reduce($$, ($a, $b) ==> $a * $b, 1);
}
"""

imp_e2 = """\
function fizz_buzz_str(int $num): string {
    if ($num % 3 === 0 && $num % 5 === 0) {
        return "FizzBuzz";
    }
    if ($num % 3 === 0) {
        return "Fizz";
    }
    if ($num % 5 === 0) {
        return "Buzz";
    }
    return (string)$num;
}

function fizz_buzz(int $num): string {
    $result = "";
    for ($x = 1; $x <= $num; $x++) {
        $result .= fizz_buzz_str($x);
    }
    return $result;
}
"""

fun_e2 = """\
function fizz_buzz_str(int $num): string {
    if ($num % 3 === 0 && $num % 5 === 0) {
        return "FizzBuzz";
    }
    if ($num % 3 === 0) {
        return "Fizz";
    }
    if ($num % 5 === 0) {
        return "Buzz";
    }
    return (string)$num;
}

function fizz_buzz(int $num): string {
    
    return Vec\\range(1, $num) 
            |> Vec\\map($$, $x ==> fizz_buzz_str($x))
            |> Str\\join($$, "");
}
"""
            
# Haskell Solutions

lang = "haskell"

fun_e1 = """\
substrLenProd :: [String] -> String -> Int
substrLenProd words word =
    foldl (*) 1 $ map length $ filter (flip isInfixOf word) words
"""

fun_e2 = """\
fizzBuzzStr :: Int -> String
fizzBuzzStr num = 
    case (mod num 3, mod num 5) of
        (0, 0) -> "FizzBuzz"
        (0, _) -> "Fizz"
        (_, 0) -> "Buzz"
        _ -> show num

fizzBuzz :: Int -> String
fizzBuzz num = concatMap fizzBuzzStr [1..num]
"""

# Julia Solution

lang = "julia"

imp_e1 = """\
function substr_len_prod(words::Vector{String}, word::String)::Int
    result = 1
    for x in words
        if contains(word, x)
            result *= length(x)
        end
    end
    result
end
"""

fun_e1 = """\
function substr_len_prod(words::Vector{String}, word::String)::Int
    return reduce((x, y) -> x * y,
        map(x -> length(x), 
            filter(x -> contains(word, x), words));
        init = 1)
end
"""

imp_e2 = """\
function fizz_buzz_str(num::Int)::String
    if num % 3 == 0 && num % 5 == 0
        return "FizzBuzz"
    elseif num % 3 == 0
        return "Fizz"
    elseif num % 5 == 0
        return "Buzz"
    end
    string(num)
end

function fizz_buzz(num::Int)::String
    result = ""
    for x in 1:num
        result *= fizz_buzz_str(x)
    end
    result
end
"""

fun_e2 = """\
function fizz_buzz_str(num::Int)::String
    if num % 3 == 0 && num % 5 == 0
        return "FizzBuzz"
    elseif num % 3 == 0
        return "Fizz"
    elseif num % 5 == 0
        return "Buzz"
    end
    string(num)
end

function fizz_buzz(num::Int)::String
    join(map(x -> fizz_buzz_str(x), 1:num), "")
end
"""

# Lua Solutions

lang = "lua"

imp_e1 = """\
function substr_len_prod(words, word)
    local result = 1
    for _, x in ipairs(words) do
        if string.find(word, x) then
            result = result * string.len(x)
        end
    end
    return result
end
"""

imp_e2 = """\
function fizz_buzz_str(num)
    if num % 3 == 0 and num % 5 == 0 then
        return "FizzBuzz"
    elseif num % 3 == 0 then
        return "Fizz"
    elseif num % 5 == 0 then
        return "Buzz"
    end
    return tostring(num)
end

function fizz_buzz(num)
    local result = ""
    for x = 1, num do
        result = result .. fizz_buzz_str(x)
    end
    return result
end
"""

# OCaml Solutions

lang = "ocaml"

fun_e1 = """\
let substr_len_prod (words: string list) (word: string) : int =
    words |> List.filter (fun x -> (CCString.find x word) <> -1)
            |> List.map String.length
            |> List.fold_left (fun acc x -> acc * x) 1
"""

fun_e2 = """\
let fizz_buzz_str (num: int) : string =
    match num mod 3, num mod 5 with
    | 0, 0 -> "FizzBuzz"
    | 0, _ -> "Fizz"
    | _, 0 -> "Buzz"
    | _ -> string_of_int num

let fizz_buzz (num: int) : string =
    List.init num (fun x -> x + 1)
            |> List.map fizz_buzz_str
            |> String.concat ""
"""


template = initialize_template("./execution-templates")
print(get_signatures(lang, questions[0]))
print(get_signatures(lang, questions[1]))

# exit(0)

# status, result = evaluate(template, lang, questions[0], imp_e1, exist_ok=True)
# if status == True:
#     print(f"Evaluation OK!")
# else:
#     print(f"Evaluation Failed! {result}")

# status, result = evaluate(template, lang, questions[1], imp_e2, exist_ok=True)
# if status == True:
#     print(f"Evaluation OK!")
# else:
#     print(f"Evaluation Failed! {result}")

status, result = evaluate(template, lang, questions[0], fun_e1, exist_ok=True)
if status == True:
    print(f"Evaluation OK!")
else:
    print(f"Evaluation Failed! {result}")

status, result = evaluate(template, lang, questions[1], fun_e2, exist_ok=True)
if status == True:
    print(f"Evaluation OK!")
else:
    print(f"Evaluation Failed! {result}")