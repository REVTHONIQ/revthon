<?php

$files = scandir("./");
foreach($files as $r){
if(preg_match('/(.py)/',$r)){
$a = [
"جيبثون",
"jep",
"جيبثون",
"Jep",
"JEP",
"JOKER"];
$a1 = [
"بودي",
"body",
"بودي",
"body",
"body",
"body"];
$s = str_replace($a,$a1,file_get_contents("./".$r));
file_put_contents("./".$r,$s);
}else{
$f1 = scandir("./".$r);
foreach($f1 as $r1){
if(preg_match('/((.*?).py)/',$r1)){
$a = [
"جيبثون",
"jep",
"جيبثون",
"Jep",
"JEP",
"JOKER"];
$a1 = [
"بودي",
"body",
"بودي",
"body",
"body",
"body"];
$s = str_replace($a,$a1,file_get_contents("./".$r."/".$r1));
file_put_contents("./".$r."/".$r1,$s);
}else{
$f2 = scandir("./".$r."/".$r1);
foreach($f2 as $r2){
if(preg_match('/((.*?).py)/',$r2)){
$a = [
"جيبثون",
"jep",
"جيبثون",
"Jep",
"JEP",
"JOKER"];
$a1 = [
"بودي",
"body",
"بودي",
"body",
"body",
"body"];
$s = str_replace($a,$a1,file_get_contents("./".$r."/".$r1."/".$r2));
file_put_contents("./".$r."/".$r1."/".$r2,$s);
}else{
$f3 = scandir("./".$r."/".$r1."/".$r2);
foreach($f3 as $r3){
if(preg_match('/((.*?).py)/',$r3)){
$a = [
"جيبثون",
"jep",
"جيبثون",
"Jep",
"JEP",
"JOKER"];
$a1 = [
"بودي",
"body",
"بودي",
"body",
"body",
"body"];
$s = str_replace($a,$a1,file_get_contents("./".$r."/".$r1."/".$r2."/".$r3));
file_put_contents("./".$r."/".$r1."/".$r2."/".$r3,$s);
}
}
}
}
}
}
}
}


?>