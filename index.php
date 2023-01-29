<?php

$files = scandir("ALJoker");
foreach($files as $r){
if(preg_match('/(.py)/',$r)){
$a = [
"جيبثون",
"Jep",
"الجوكر",
"jep",
"JEP",
"ALJoker"];
$a1 = [
"بودي",
"Body",
"بودي",
"body",
"BODY",
"ALBODY"];
$s = str_replace($a,$a1,file_get_contents("ALJoker/".$r));
file_put_contents("ALJoker/".$r,$s);
}else{
$f1 = scandir("ALJoker/".$r);
foreach($f1 as $r1){
if(preg_match('/((.*?).py)/',$r1)){
$a = [
"جيبثون",
"Jep",
"الجوكر",
"jep",
"JEP",
"ALJoker"];
$a1 = [
"بودي",
"Body",
"بودي",
"body",
"BODY",
"ALBODY"];
$s = str_replace($a,$a1,file_get_contents("ALJoker/".$r."/".$r1));
file_put_contents("ALJoker/".$r."/".$r1,$s);
}else{
$f2 = scandir("ALJoker/".$r."/".$r1);
foreach($f2 as $r2){
if(preg_match('/((.*?).py)/',$r2)){
$a = [
"جيبثون",
"Jep",
"الجوكر",
"jep",
"JEP",
"ALJoker"];
$a1 = [
"بودي",
"Body",
"بودي",
"body",
"BODY",
"ALBODY"];
$s = str_replace($a,$a1,file_get_contents("ALJoker/".$r."/".$r1."/".$r2));
file_put_contents("ALJoker/".$r."/".$r1."/".$r2,$s);
}else{
$f3 = scandir("ALJoker/".$r."/".$r1."/".$r2);
foreach($f3 as $r3){
if(preg_match('/((.*?).py)/',$r3)){
$a = [
"جيبثون",
"Jep",
"الجوكر",
"jep",
"JEP",
"ALJoker"];
$a1 = [
"بودي",
"Body",
"بودي",
"body",
"BODY",
"ALBODY"];
$s = str_replace($a,$a1,file_get_contents("ALJoker/".$r."/".$r1."/".$r2."/".$r3));
file_put_contents("ALJoker/".$r."/".$r1."/".$r2."/".$r3,$s);
}
}
}
}
}
}
}
}


?>