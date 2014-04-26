<?php
// dead simple files index
header('Content-Type: text/plain');
foreach (glob('*.txt') as $f) { echo "$f:".filemtime($f)."\n"; }
