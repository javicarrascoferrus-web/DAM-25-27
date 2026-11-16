<?php
$datos = json_encode([
    "model" => "phi3:mini",
    "prompt" => $_GET['prompt'],
    "stream" => false
]);

$ch = curl_init("http://localhost:11434/api/generate");
curl_setopt($ch, CURLOPT_POSTFIELDS, $datos);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

echo json_decode(curl_exec($ch), true)["response"];
curl_close($ch);
