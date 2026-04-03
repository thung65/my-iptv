<?php
/**
 * Script xu ly ClearKey - Bao mat va Chan trinh duyet
 */

// 1. Thiet lap Header tra ve JSON
header('Content-Type: application/json; charset=utf-8');

// 2. Kiem tra User-Agent (Chan trinh duyet)
$userAgent = $_SERVER['HTTP_USER_AGENT'] ?? '';
$isIptvApp = (
    stripos($userAgent, 'Dalvik') !== false || 
    stripos($userAgent, 'TiviMate') !== false || 
    stripos($userAgent, 'OTT') !== false ||
    stripos($userAgent, 'Kodi') !== false
);

// Neu truy cap tu trinh duyet (khong phai app IPTV), hien thoi bao loi nhu anh mau
if (!$isIptvApp) {
    echo json_encode([
        "error" => "Access Denied",
        "message" => "This content is only available on IPTV Apps."
    ], JSON_UNESCAPED_SLASHES);
    exit;
}

// 3. Lay ID va xu ly Key (Neu la App IPTV thi tiep tuc chay)
$id = isset($_GET['id']) ? strtolower(trim($_GET['id'])) : '';

$channels = [
    // --- ALL ---
    'warnertv'       => '086d09a40bff3a00aa6dd4dbaf9c13b2:34f1908cfe2e05ee060046d40f14aec9',
    'hbo'            => '09ddfe3d63863cafaeb79d0546b098ab:3de0f38dcf014827dfd5bec38743c6a2',
    'cinemaworld'    => 'ee7915564d7439d09bd3556ffccc87a4:b35e12a75a42a6f9184723a90ff42d9c',
    'axn'            => '9d29f87efdec3c9fab368f724a62ad0e:6f1c09c035eab36323d60d1454db3d20',
    'cinemax'        => 'acb4c23471063327adc732e283c0847f:e9868f5f473d0fd8699ede48d531c2b0',
    'cartoonnetwork' => '3c20166660a93a75ac77db81567389f7:3cc1add43aecce3fe31c9c6a2a5b8c21',
    'cartoonito'     => 'b1f0d759e914369db388b3b0dc815971:5678d317e17007a88a9b9539e4526512',
    'bbccbeebies'    => 'cca73a006b4b39a595207ceb5ed9ca0a:b833d1f40c261ef78896f97e06f80cdc',
    'dmax'           => '53b26f904ae03a20b56477cfb9c5dca2:0c64ccfb978e7390bd33344075492aec',
    'dreamworks'     => '67dae20527c63dadaaae609aa91577cb:59328f621d56767bc5ff9404a8940683',
    'animalplanet'   => 'ec6f072c7125377a9bc0ae61598095f4:1d5388e0781415ebcec9914f5ad75875',
    'outdoorhd'      => 'a7c942778e874d43be92b8d0a0cd11b4:6d54358306571658ffdb952c6560688b',
    
    // --- INTERNATIONAL ---
    'discovery'      => 'eb4160ea553a321d899553e4e796fec2:bea5a07157e0c4d17b11ab399517f952',
    'tlc'            => 'b6908629732639ada4814a6208296d9c:7ca9bf03623f77b5e2f16df0b53f274d',
    'discoveryasia'  => '934907b134be3963a6263a453846924c:788e2835fb98568aed2f47bbdc091515',
    'fashiontv'      => 'c1d9f25701023508bfa6737e3a8c7001:30c3613e9b06e0f7cc201014f31bf5d8',
];

if (array_key_exists($id, $channels)) {
    // Neu la app thi tra ve chuoi Key thuan tuy de giai ma
    header('Content-Type: text/plain');
    echo $channels[$id];
} else {
    echo json_encode(["error" => "Not Found", "message" => "ID channel khong hop le."]);
}
