# This Challenge: http://codegolf.stackexchange.com/questions/84380/help-me-figure-out-what-tex-i-can-use
import re;A=lambda f:re.fullmatch('TeX Live|(La|LuaLa|Lua|Bib|pdf|XeLa|Xe|Mac|MiK)?TeX|Lyx|MakeIndex|Meta(Post|FUN)|PostScript|ConTeXt',f)
print(A('MetaFUN'))