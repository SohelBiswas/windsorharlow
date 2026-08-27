"""Windsor Harlow — shared page shell."""

SITE = "https://www.windsorharlow.com"
import os

MAIL = "business@windsorharlow.com"

NAV = [
    ("Services", "/services.html"),
    ("Engagement", "/#engagement"),
    ("Delivery", "/#delivery"),
    ("Work", "/#work"),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}{path}">
<meta property="og:site_name" content="Windsor Harlow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{site}{path}">
<meta property="og:image" content="{site}{ogimg}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Windsor Harlow — backends that hold under load, AI that survives production">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}{ogimg}">
<link rel="icon" href="/assets/brand/favicon.svg" type="image/svg+xml">
__FONTS__
<link rel="stylesheet" href="/assets/css/wh.css">
__FAILSAFE__
{extra_head}</head>
<body>
<a class="skip" href="#top">Skip to content</a>
__NOSCRIPT__
<svg class="wh-defs" width="0" height="0" aria-hidden="true" focusable="false">
  <defs>
    <linearGradient id="wmG" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#0079CA"/><stop offset="1" stop-color="#1FA6B8"/>
    </linearGradient>
    <g id="wmDots" fill="#16536B"><path d="M355 0h3v3h-3zM364 0h3v3h-3zM373 0h3v3h-3zM382 0h3v3h-3zM391 0h3v3h-3zM399 0h3v3h-3zM408 0h3v3h-3zM417 0h3v3h-3zM426 0h3v3h-3zM435 0h3v3h-3zM444 0h3v3h-3zM346 10h3v3h-3zM355 10h3v3h-3zM364 10h3v3h-3zM373 10h3v3h-3zM382 10h3v3h-3zM391 10h3v3h-3zM399 10h3v3h-3zM408 10h3v3h-3zM417 10h3v3h-3zM426 10h3v3h-3zM435 10h3v3h-3zM444 10h3v3h-3zM719 10h3v3h-3zM728 10h3v3h-3zM737 10h3v3h-3zM746 10h3v3h-3zM755 10h3v3h-3zM764 10h3v3h-3zM773 10h3v3h-3zM782 10h3v3h-3zM791 10h3v3h-3zM799 10h3v3h-3zM808 10h3v3h-3zM817 10h3v3h-3zM231 21h3v3h-3zM239 21h3v3h-3zM248 21h3v3h-3zM257 21h3v3h-3zM266 21h3v3h-3zM275 21h3v3h-3zM284 21h3v3h-3zM293 21h3v3h-3zM302 21h3v3h-3zM346 21h3v3h-3zM355 21h3v3h-3zM364 21h3v3h-3zM373 21h3v3h-3zM382 21h3v3h-3zM391 21h3v3h-3zM399 21h3v3h-3zM408 21h3v3h-3zM417 21h3v3h-3zM426 21h3v3h-3zM435 21h3v3h-3zM684 21h3v3h-3zM693 21h3v3h-3zM702 21h3v3h-3zM711 21h3v3h-3zM719 21h3v3h-3zM728 21h3v3h-3zM737 21h3v3h-3zM746 21h3v3h-3zM755 21h3v3h-3zM764 21h3v3h-3zM773 21h3v3h-3zM782 21h3v3h-3zM791 21h3v3h-3zM799 21h3v3h-3zM808 21h3v3h-3zM817 21h3v3h-3zM826 21h3v3h-3zM835 21h3v3h-3zM844 21h3v3h-3zM853 21h3v3h-3zM862 21h3v3h-3zM871 21h3v3h-3zM879 21h3v3h-3zM888 21h3v3h-3zM44 32h3v3h-3zM53 32h3v3h-3zM62 32h3v3h-3zM71 32h3v3h-3zM79 32h3v3h-3zM88 32h3v3h-3zM97 32h3v3h-3zM115 32h3v3h-3zM124 32h3v3h-3zM133 32h3v3h-3zM142 32h3v3h-3zM151 32h3v3h-3zM159 32h3v3h-3zM168 32h3v3h-3zM177 32h3v3h-3zM186 32h3v3h-3zM195 32h3v3h-3zM204 32h3v3h-3zM213 32h3v3h-3zM222 32h3v3h-3zM231 32h3v3h-3zM239 32h3v3h-3zM248 32h3v3h-3zM257 32h3v3h-3zM266 32h3v3h-3zM275 32h3v3h-3zM284 32h3v3h-3zM293 32h3v3h-3zM302 32h3v3h-3zM311 32h3v3h-3zM355 32h3v3h-3zM364 32h3v3h-3zM373 32h3v3h-3zM382 32h3v3h-3zM391 32h3v3h-3zM399 32h3v3h-3zM408 32h3v3h-3zM417 32h3v3h-3zM426 32h3v3h-3zM568 32h3v3h-3zM577 32h3v3h-3zM666 32h3v3h-3zM675 32h3v3h-3zM684 32h3v3h-3zM693 32h3v3h-3zM702 32h3v3h-3zM711 32h3v3h-3zM719 32h3v3h-3zM728 32h3v3h-3zM737 32h3v3h-3zM746 32h3v3h-3zM755 32h3v3h-3zM764 32h3v3h-3zM773 32h3v3h-3zM782 32h3v3h-3zM791 32h3v3h-3zM799 32h3v3h-3zM808 32h3v3h-3zM817 32h3v3h-3zM826 32h3v3h-3zM835 32h3v3h-3zM844 32h3v3h-3zM853 32h3v3h-3zM862 32h3v3h-3zM871 32h3v3h-3zM879 32h3v3h-3zM888 32h3v3h-3zM897 32h3v3h-3zM906 32h3v3h-3zM915 32h3v3h-3zM924 32h3v3h-3zM933 32h3v3h-3zM942 32h3v3h-3zM951 32h3v3h-3zM44 43h3v3h-3zM53 43h3v3h-3zM62 43h3v3h-3zM71 43h3v3h-3zM79 43h3v3h-3zM88 43h3v3h-3zM97 43h3v3h-3zM106 43h3v3h-3zM115 43h3v3h-3zM124 43h3v3h-3zM133 43h3v3h-3zM142 43h3v3h-3zM151 43h3v3h-3zM159 43h3v3h-3zM168 43h3v3h-3zM177 43h3v3h-3zM186 43h3v3h-3zM195 43h3v3h-3zM204 43h3v3h-3zM213 43h3v3h-3zM222 43h3v3h-3zM231 43h3v3h-3zM239 43h3v3h-3zM248 43h3v3h-3zM257 43h3v3h-3zM266 43h3v3h-3zM275 43h3v3h-3zM284 43h3v3h-3zM293 43h3v3h-3zM302 43h3v3h-3zM311 43h3v3h-3zM364 43h3v3h-3zM373 43h3v3h-3zM382 43h3v3h-3zM391 43h3v3h-3zM399 43h3v3h-3zM408 43h3v3h-3zM417 43h3v3h-3zM444 43h3v3h-3zM453 43h3v3h-3zM559 43h3v3h-3zM568 43h3v3h-3zM577 43h3v3h-3zM595 43h3v3h-3zM604 43h3v3h-3zM613 43h3v3h-3zM622 43h3v3h-3zM631 43h3v3h-3zM639 43h3v3h-3zM648 43h3v3h-3zM657 43h3v3h-3zM666 43h3v3h-3zM675 43h3v3h-3zM684 43h3v3h-3zM693 43h3v3h-3zM702 43h3v3h-3zM711 43h3v3h-3zM719 43h3v3h-3zM728 43h3v3h-3zM737 43h3v3h-3zM746 43h3v3h-3zM755 43h3v3h-3zM764 43h3v3h-3zM773 43h3v3h-3zM782 43h3v3h-3zM791 43h3v3h-3zM799 43h3v3h-3zM808 43h3v3h-3zM817 43h3v3h-3zM826 43h3v3h-3zM835 43h3v3h-3zM844 43h3v3h-3zM853 43h3v3h-3zM862 43h3v3h-3zM871 43h3v3h-3zM879 43h3v3h-3zM888 43h3v3h-3zM897 43h3v3h-3zM906 43h3v3h-3zM915 43h3v3h-3zM924 43h3v3h-3zM933 43h3v3h-3zM942 43h3v3h-3zM951 43h3v3h-3zM959 43h3v3h-3zM968 43h3v3h-3zM977 43h3v3h-3zM986 43h3v3h-3zM62 54h3v3h-3zM71 54h3v3h-3zM79 54h3v3h-3zM88 54h3v3h-3zM97 54h3v3h-3zM106 54h3v3h-3zM115 54h3v3h-3zM124 54h3v3h-3zM133 54h3v3h-3zM142 54h3v3h-3zM151 54h3v3h-3zM159 54h3v3h-3zM168 54h3v3h-3zM177 54h3v3h-3zM186 54h3v3h-3zM195 54h3v3h-3zM204 54h3v3h-3zM213 54h3v3h-3zM222 54h3v3h-3zM231 54h3v3h-3zM239 54h3v3h-3zM248 54h3v3h-3zM257 54h3v3h-3zM266 54h3v3h-3zM275 54h3v3h-3zM284 54h3v3h-3zM293 54h3v3h-3zM302 54h3v3h-3zM311 54h3v3h-3zM319 54h3v3h-3zM373 54h3v3h-3zM382 54h3v3h-3zM391 54h3v3h-3zM551 54h3v3h-3zM559 54h3v3h-3zM568 54h3v3h-3zM577 54h3v3h-3zM595 54h3v3h-3zM604 54h3v3h-3zM613 54h3v3h-3zM622 54h3v3h-3zM631 54h3v3h-3zM639 54h3v3h-3zM648 54h3v3h-3zM657 54h3v3h-3zM666 54h3v3h-3zM675 54h3v3h-3zM684 54h3v3h-3zM693 54h3v3h-3zM702 54h3v3h-3zM711 54h3v3h-3zM719 54h3v3h-3zM728 54h3v3h-3zM737 54h3v3h-3zM746 54h3v3h-3zM755 54h3v3h-3zM764 54h3v3h-3zM773 54h3v3h-3zM782 54h3v3h-3zM791 54h3v3h-3zM799 54h3v3h-3zM808 54h3v3h-3zM817 54h3v3h-3zM826 54h3v3h-3zM835 54h3v3h-3zM844 54h3v3h-3zM853 54h3v3h-3zM862 54h3v3h-3zM871 54h3v3h-3zM879 54h3v3h-3zM888 54h3v3h-3zM897 54h3v3h-3zM906 54h3v3h-3zM915 54h3v3h-3zM924 54h3v3h-3zM933 54h3v3h-3zM942 54h3v3h-3zM951 54h3v3h-3zM959 54h3v3h-3zM968 54h3v3h-3zM977 54h3v3h-3zM124 65h3v3h-3zM133 65h3v3h-3zM142 65h3v3h-3zM151 65h3v3h-3zM159 65h3v3h-3zM168 65h3v3h-3zM177 65h3v3h-3zM186 65h3v3h-3zM195 65h3v3h-3zM204 65h3v3h-3zM213 65h3v3h-3zM222 65h3v3h-3zM231 65h3v3h-3zM239 65h3v3h-3zM248 65h3v3h-3zM257 65h3v3h-3zM266 65h3v3h-3zM275 65h3v3h-3zM284 65h3v3h-3zM293 65h3v3h-3zM302 65h3v3h-3zM311 65h3v3h-3zM319 65h3v3h-3zM328 65h3v3h-3zM533 65h3v3h-3zM542 65h3v3h-3zM551 65h3v3h-3zM559 65h3v3h-3zM568 65h3v3h-3zM577 65h3v3h-3zM586 65h3v3h-3zM595 65h3v3h-3zM604 65h3v3h-3zM613 65h3v3h-3zM622 65h3v3h-3zM631 65h3v3h-3zM639 65h3v3h-3zM648 65h3v3h-3zM657 65h3v3h-3zM666 65h3v3h-3zM675 65h3v3h-3zM684 65h3v3h-3zM693 65h3v3h-3zM702 65h3v3h-3zM711 65h3v3h-3zM719 65h3v3h-3zM728 65h3v3h-3zM737 65h3v3h-3zM746 65h3v3h-3zM755 65h3v3h-3zM764 65h3v3h-3zM773 65h3v3h-3zM782 65h3v3h-3zM791 65h3v3h-3zM799 65h3v3h-3zM808 65h3v3h-3zM817 65h3v3h-3zM826 65h3v3h-3zM835 65h3v3h-3zM844 65h3v3h-3zM853 65h3v3h-3zM862 65h3v3h-3zM871 65h3v3h-3zM879 65h3v3h-3zM888 65h3v3h-3zM897 65h3v3h-3zM906 65h3v3h-3zM915 65h3v3h-3zM924 65h3v3h-3zM933 65h3v3h-3zM942 65h3v3h-3zM951 65h3v3h-3zM142 76h3v3h-3zM151 76h3v3h-3zM159 76h3v3h-3zM168 76h3v3h-3zM177 76h3v3h-3zM186 76h3v3h-3zM195 76h3v3h-3zM204 76h3v3h-3zM213 76h3v3h-3zM222 76h3v3h-3zM231 76h3v3h-3zM239 76h3v3h-3zM248 76h3v3h-3zM257 76h3v3h-3zM266 76h3v3h-3zM275 76h3v3h-3zM284 76h3v3h-3zM293 76h3v3h-3zM302 76h3v3h-3zM311 76h3v3h-3zM319 76h3v3h-3zM328 76h3v3h-3zM337 76h3v3h-3zM488 76h3v3h-3zM497 76h3v3h-3zM524 76h3v3h-3zM533 76h3v3h-3zM542 76h3v3h-3zM551 76h3v3h-3zM559 76h3v3h-3zM568 76h3v3h-3zM577 76h3v3h-3zM586 76h3v3h-3zM595 76h3v3h-3zM604 76h3v3h-3zM613 76h3v3h-3zM622 76h3v3h-3zM631 76h3v3h-3zM639 76h3v3h-3zM648 76h3v3h-3zM657 76h3v3h-3zM666 76h3v3h-3zM675 76h3v3h-3zM684 76h3v3h-3zM693 76h3v3h-3zM702 76h3v3h-3zM711 76h3v3h-3zM719 76h3v3h-3zM728 76h3v3h-3zM737 76h3v3h-3zM746 76h3v3h-3zM755 76h3v3h-3zM764 76h3v3h-3zM773 76h3v3h-3zM782 76h3v3h-3zM791 76h3v3h-3zM799 76h3v3h-3zM808 76h3v3h-3zM817 76h3v3h-3zM826 76h3v3h-3zM835 76h3v3h-3zM844 76h3v3h-3zM853 76h3v3h-3zM862 76h3v3h-3zM871 76h3v3h-3zM879 76h3v3h-3zM888 76h3v3h-3zM897 76h3v3h-3zM151 87h3v3h-3zM159 87h3v3h-3zM168 87h3v3h-3zM177 87h3v3h-3zM186 87h3v3h-3zM195 87h3v3h-3zM204 87h3v3h-3zM213 87h3v3h-3zM222 87h3v3h-3zM231 87h3v3h-3zM239 87h3v3h-3zM248 87h3v3h-3zM257 87h3v3h-3zM266 87h3v3h-3zM275 87h3v3h-3zM284 87h3v3h-3zM293 87h3v3h-3zM302 87h3v3h-3zM311 87h3v3h-3zM319 87h3v3h-3zM328 87h3v3h-3zM337 87h3v3h-3zM479 87h3v3h-3zM488 87h3v3h-3zM497 87h3v3h-3zM524 87h3v3h-3zM533 87h3v3h-3zM542 87h3v3h-3zM551 87h3v3h-3zM559 87h3v3h-3zM568 87h3v3h-3zM577 87h3v3h-3zM586 87h3v3h-3zM595 87h3v3h-3zM604 87h3v3h-3zM613 87h3v3h-3zM622 87h3v3h-3zM631 87h3v3h-3zM639 87h3v3h-3zM648 87h3v3h-3zM657 87h3v3h-3zM666 87h3v3h-3zM675 87h3v3h-3zM684 87h3v3h-3zM693 87h3v3h-3zM702 87h3v3h-3zM711 87h3v3h-3zM719 87h3v3h-3zM728 87h3v3h-3zM737 87h3v3h-3zM746 87h3v3h-3zM755 87h3v3h-3zM764 87h3v3h-3zM773 87h3v3h-3zM782 87h3v3h-3zM791 87h3v3h-3zM799 87h3v3h-3zM808 87h3v3h-3zM817 87h3v3h-3zM826 87h3v3h-3zM835 87h3v3h-3zM844 87h3v3h-3zM853 87h3v3h-3zM862 87h3v3h-3zM871 87h3v3h-3zM879 87h3v3h-3zM888 87h3v3h-3zM159 98h3v3h-3zM168 98h3v3h-3zM177 98h3v3h-3zM186 98h3v3h-3zM195 98h3v3h-3zM204 98h3v3h-3zM213 98h3v3h-3zM222 98h3v3h-3zM231 98h3v3h-3zM239 98h3v3h-3zM248 98h3v3h-3zM257 98h3v3h-3zM266 98h3v3h-3zM275 98h3v3h-3zM284 98h3v3h-3zM293 98h3v3h-3zM302 98h3v3h-3zM311 98h3v3h-3zM319 98h3v3h-3zM328 98h3v3h-3zM337 98h3v3h-3zM497 98h3v3h-3zM506 98h3v3h-3zM515 98h3v3h-3zM524 98h3v3h-3zM533 98h3v3h-3zM542 98h3v3h-3zM551 98h3v3h-3zM559 98h3v3h-3zM568 98h3v3h-3zM577 98h3v3h-3zM586 98h3v3h-3zM595 98h3v3h-3zM604 98h3v3h-3zM613 98h3v3h-3zM622 98h3v3h-3zM631 98h3v3h-3zM639 98h3v3h-3zM666 98h3v3h-3zM675 98h3v3h-3zM684 98h3v3h-3zM693 98h3v3h-3zM702 98h3v3h-3zM711 98h3v3h-3zM719 98h3v3h-3zM728 98h3v3h-3zM737 98h3v3h-3zM746 98h3v3h-3zM755 98h3v3h-3zM764 98h3v3h-3zM773 98h3v3h-3zM782 98h3v3h-3zM791 98h3v3h-3zM799 98h3v3h-3zM808 98h3v3h-3zM817 98h3v3h-3zM826 98h3v3h-3zM835 98h3v3h-3zM844 98h3v3h-3zM853 98h3v3h-3zM862 98h3v3h-3zM871 98h3v3h-3zM159 109h3v3h-3zM168 109h3v3h-3zM177 109h3v3h-3zM186 109h3v3h-3zM195 109h3v3h-3zM204 109h3v3h-3zM213 109h3v3h-3zM222 109h3v3h-3zM231 109h3v3h-3zM239 109h3v3h-3zM248 109h3v3h-3zM257 109h3v3h-3zM275 109h3v3h-3zM284 109h3v3h-3zM319 109h3v3h-3zM497 109h3v3h-3zM506 109h3v3h-3zM515 109h3v3h-3zM524 109h3v3h-3zM533 109h3v3h-3zM568 109h3v3h-3zM577 109h3v3h-3zM586 109h3v3h-3zM595 109h3v3h-3zM604 109h3v3h-3zM613 109h3v3h-3zM622 109h3v3h-3zM675 109h3v3h-3zM684 109h3v3h-3zM693 109h3v3h-3zM702 109h3v3h-3zM711 109h3v3h-3zM719 109h3v3h-3zM728 109h3v3h-3zM737 109h3v3h-3zM746 109h3v3h-3zM755 109h3v3h-3zM764 109h3v3h-3zM773 109h3v3h-3zM782 109h3v3h-3zM791 109h3v3h-3zM799 109h3v3h-3zM808 109h3v3h-3zM817 109h3v3h-3zM826 109h3v3h-3zM835 109h3v3h-3zM844 109h3v3h-3zM853 109h3v3h-3zM862 109h3v3h-3zM159 120h3v3h-3zM168 120h3v3h-3zM177 120h3v3h-3zM186 120h3v3h-3zM195 120h3v3h-3zM204 120h3v3h-3zM213 120h3v3h-3zM222 120h3v3h-3zM231 120h3v3h-3zM239 120h3v3h-3zM248 120h3v3h-3zM257 120h3v3h-3zM266 120h3v3h-3zM275 120h3v3h-3zM284 120h3v3h-3zM293 120h3v3h-3zM302 120h3v3h-3zM479 120h3v3h-3zM488 120h3v3h-3zM497 120h3v3h-3zM639 120h3v3h-3zM648 120h3v3h-3zM657 120h3v3h-3zM666 120h3v3h-3zM675 120h3v3h-3zM684 120h3v3h-3zM693 120h3v3h-3zM702 120h3v3h-3zM711 120h3v3h-3zM719 120h3v3h-3zM728 120h3v3h-3zM737 120h3v3h-3zM746 120h3v3h-3zM755 120h3v3h-3zM764 120h3v3h-3zM773 120h3v3h-3zM782 120h3v3h-3zM791 120h3v3h-3zM799 120h3v3h-3zM808 120h3v3h-3zM817 120h3v3h-3zM826 120h3v3h-3zM835 120h3v3h-3zM844 120h3v3h-3zM853 120h3v3h-3zM159 131h3v3h-3zM168 131h3v3h-3zM177 131h3v3h-3zM186 131h3v3h-3zM195 131h3v3h-3zM204 131h3v3h-3zM213 131h3v3h-3zM222 131h3v3h-3zM231 131h3v3h-3zM239 131h3v3h-3zM248 131h3v3h-3zM257 131h3v3h-3zM266 131h3v3h-3zM275 131h3v3h-3zM284 131h3v3h-3zM293 131h3v3h-3zM479 131h3v3h-3zM622 131h3v3h-3zM657 131h3v3h-3zM666 131h3v3h-3zM675 131h3v3h-3zM684 131h3v3h-3zM693 131h3v3h-3zM702 131h3v3h-3zM711 131h3v3h-3zM719 131h3v3h-3zM728 131h3v3h-3zM737 131h3v3h-3zM746 131h3v3h-3zM755 131h3v3h-3zM764 131h3v3h-3zM773 131h3v3h-3zM782 131h3v3h-3zM791 131h3v3h-3zM799 131h3v3h-3zM808 131h3v3h-3zM817 131h3v3h-3zM826 131h3v3h-3zM835 131h3v3h-3zM168 142h3v3h-3zM177 142h3v3h-3zM186 142h3v3h-3zM195 142h3v3h-3zM204 142h3v3h-3zM213 142h3v3h-3zM222 142h3v3h-3zM231 142h3v3h-3zM239 142h3v3h-3zM248 142h3v3h-3zM257 142h3v3h-3zM266 142h3v3h-3zM275 142h3v3h-3zM284 142h3v3h-3zM524 142h3v3h-3zM613 142h3v3h-3zM622 142h3v3h-3zM631 142h3v3h-3zM639 142h3v3h-3zM648 142h3v3h-3zM657 142h3v3h-3zM719 142h3v3h-3zM728 142h3v3h-3zM737 142h3v3h-3zM746 142h3v3h-3zM755 142h3v3h-3zM764 142h3v3h-3zM773 142h3v3h-3zM782 142h3v3h-3zM791 142h3v3h-3zM799 142h3v3h-3zM808 142h3v3h-3zM817 142h3v3h-3zM826 142h3v3h-3zM835 142h3v3h-3zM853 142h3v3h-3zM888 142h3v3h-3zM177 153h3v3h-3zM186 153h3v3h-3zM195 153h3v3h-3zM204 153h3v3h-3zM213 153h3v3h-3zM222 153h3v3h-3zM231 153h3v3h-3zM239 153h3v3h-3zM248 153h3v3h-3zM257 153h3v3h-3zM266 153h3v3h-3zM275 153h3v3h-3zM488 153h3v3h-3zM497 153h3v3h-3zM506 153h3v3h-3zM515 153h3v3h-3zM524 153h3v3h-3zM533 153h3v3h-3zM542 153h3v3h-3zM551 153h3v3h-3zM604 153h3v3h-3zM613 153h3v3h-3zM622 153h3v3h-3zM631 153h3v3h-3zM639 153h3v3h-3zM648 153h3v3h-3zM657 153h3v3h-3zM666 153h3v3h-3zM702 153h3v3h-3zM711 153h3v3h-3zM728 153h3v3h-3zM737 153h3v3h-3zM746 153h3v3h-3zM755 153h3v3h-3zM764 153h3v3h-3zM773 153h3v3h-3zM782 153h3v3h-3zM791 153h3v3h-3zM799 153h3v3h-3zM808 153h3v3h-3zM817 153h3v3h-3zM826 153h3v3h-3zM835 153h3v3h-3zM871 153h3v3h-3zM186 164h3v3h-3zM195 164h3v3h-3zM204 164h3v3h-3zM213 164h3v3h-3zM222 164h3v3h-3zM231 164h3v3h-3zM239 164h3v3h-3zM248 164h3v3h-3zM257 164h3v3h-3zM266 164h3v3h-3zM275 164h3v3h-3zM471 164h3v3h-3zM479 164h3v3h-3zM488 164h3v3h-3zM497 164h3v3h-3zM506 164h3v3h-3zM515 164h3v3h-3zM524 164h3v3h-3zM533 164h3v3h-3zM542 164h3v3h-3zM551 164h3v3h-3zM559 164h3v3h-3zM568 164h3v3h-3zM577 164h3v3h-3zM586 164h3v3h-3zM595 164h3v3h-3zM604 164h3v3h-3zM613 164h3v3h-3zM622 164h3v3h-3zM631 164h3v3h-3zM639 164h3v3h-3zM648 164h3v3h-3zM657 164h3v3h-3zM666 164h3v3h-3zM693 164h3v3h-3zM702 164h3v3h-3zM711 164h3v3h-3zM719 164h3v3h-3zM746 164h3v3h-3zM755 164h3v3h-3zM764 164h3v3h-3zM773 164h3v3h-3zM782 164h3v3h-3zM791 164h3v3h-3zM799 164h3v3h-3zM808 164h3v3h-3zM817 164h3v3h-3zM826 164h3v3h-3zM195 175h3v3h-3zM204 175h3v3h-3zM213 175h3v3h-3zM222 175h3v3h-3zM231 175h3v3h-3zM266 175h3v3h-3zM462 175h3v3h-3zM471 175h3v3h-3zM479 175h3v3h-3zM488 175h3v3h-3zM497 175h3v3h-3zM506 175h3v3h-3zM515 175h3v3h-3zM524 175h3v3h-3zM533 175h3v3h-3zM542 175h3v3h-3zM551 175h3v3h-3zM559 175h3v3h-3zM568 175h3v3h-3zM577 175h3v3h-3zM586 175h3v3h-3zM595 175h3v3h-3zM604 175h3v3h-3zM613 175h3v3h-3zM639 175h3v3h-3zM648 175h3v3h-3zM657 175h3v3h-3zM666 175h3v3h-3zM693 175h3v3h-3zM702 175h3v3h-3zM711 175h3v3h-3zM719 175h3v3h-3zM728 175h3v3h-3zM755 175h3v3h-3zM764 175h3v3h-3zM782 175h3v3h-3zM791 175h3v3h-3zM799 175h3v3h-3zM808 175h3v3h-3zM817 175h3v3h-3zM826 175h3v3h-3zM204 186h3v3h-3zM213 186h3v3h-3zM222 186h3v3h-3zM231 186h3v3h-3zM462 186h3v3h-3zM471 186h3v3h-3zM479 186h3v3h-3zM488 186h3v3h-3zM497 186h3v3h-3zM506 186h3v3h-3zM515 186h3v3h-3zM524 186h3v3h-3zM533 186h3v3h-3zM542 186h3v3h-3zM551 186h3v3h-3zM559 186h3v3h-3zM568 186h3v3h-3zM577 186h3v3h-3zM586 186h3v3h-3zM595 186h3v3h-3zM604 186h3v3h-3zM613 186h3v3h-3zM693 186h3v3h-3zM702 186h3v3h-3zM711 186h3v3h-3zM719 186h3v3h-3zM728 186h3v3h-3zM737 186h3v3h-3zM746 186h3v3h-3zM755 186h3v3h-3zM791 186h3v3h-3zM799 186h3v3h-3zM808 186h3v3h-3zM817 186h3v3h-3zM213 197h3v3h-3zM222 197h3v3h-3zM231 197h3v3h-3zM239 197h3v3h-3zM462 197h3v3h-3zM471 197h3v3h-3zM479 197h3v3h-3zM488 197h3v3h-3zM497 197h3v3h-3zM506 197h3v3h-3zM515 197h3v3h-3zM524 197h3v3h-3zM533 197h3v3h-3zM542 197h3v3h-3zM551 197h3v3h-3zM559 197h3v3h-3zM568 197h3v3h-3zM577 197h3v3h-3zM586 197h3v3h-3zM595 197h3v3h-3zM604 197h3v3h-3zM613 197h3v3h-3zM702 197h3v3h-3zM711 197h3v3h-3zM719 197h3v3h-3zM728 197h3v3h-3zM222 208h3v3h-3zM231 208h3v3h-3zM239 208h3v3h-3zM248 208h3v3h-3zM462 208h3v3h-3zM471 208h3v3h-3zM479 208h3v3h-3zM488 208h3v3h-3zM497 208h3v3h-3zM506 208h3v3h-3zM515 208h3v3h-3zM524 208h3v3h-3zM533 208h3v3h-3zM542 208h3v3h-3zM551 208h3v3h-3zM559 208h3v3h-3zM568 208h3v3h-3zM577 208h3v3h-3zM586 208h3v3h-3zM595 208h3v3h-3zM604 208h3v3h-3zM613 208h3v3h-3zM711 208h3v3h-3zM719 208h3v3h-3zM728 208h3v3h-3zM773 208h3v3h-3zM835 208h3v3h-3zM257 219h3v3h-3zM266 219h3v3h-3zM462 219h3v3h-3zM471 219h3v3h-3zM479 219h3v3h-3zM488 219h3v3h-3zM497 219h3v3h-3zM506 219h3v3h-3zM515 219h3v3h-3zM524 219h3v3h-3zM533 219h3v3h-3zM542 219h3v3h-3zM551 219h3v3h-3zM559 219h3v3h-3zM568 219h3v3h-3zM577 219h3v3h-3zM586 219h3v3h-3zM595 219h3v3h-3zM604 219h3v3h-3zM613 219h3v3h-3zM711 219h3v3h-3zM719 219h3v3h-3zM773 219h3v3h-3zM782 219h3v3h-3zM835 219h3v3h-3zM266 230h3v3h-3zM275 230h3v3h-3zM302 230h3v3h-3zM311 230h3v3h-3zM319 230h3v3h-3zM479 230h3v3h-3zM488 230h3v3h-3zM497 230h3v3h-3zM506 230h3v3h-3zM515 230h3v3h-3zM524 230h3v3h-3zM533 230h3v3h-3zM542 230h3v3h-3zM551 230h3v3h-3zM559 230h3v3h-3zM568 230h3v3h-3zM577 230h3v3h-3zM586 230h3v3h-3zM595 230h3v3h-3zM604 230h3v3h-3zM613 230h3v3h-3zM622 230h3v3h-3zM631 230h3v3h-3zM639 230h3v3h-3zM711 230h3v3h-3zM719 230h3v3h-3zM773 230h3v3h-3zM782 230h3v3h-3zM791 230h3v3h-3zM835 230h3v3h-3zM844 230h3v3h-3zM284 241h3v3h-3zM293 241h3v3h-3zM302 241h3v3h-3zM311 241h3v3h-3zM319 241h3v3h-3zM328 241h3v3h-3zM471 241h3v3h-3zM479 241h3v3h-3zM488 241h3v3h-3zM497 241h3v3h-3zM506 241h3v3h-3zM515 241h3v3h-3zM524 241h3v3h-3zM533 241h3v3h-3zM542 241h3v3h-3zM551 241h3v3h-3zM559 241h3v3h-3zM568 241h3v3h-3zM577 241h3v3h-3zM586 241h3v3h-3zM595 241h3v3h-3zM604 241h3v3h-3zM613 241h3v3h-3zM622 241h3v3h-3zM631 241h3v3h-3zM782 241h3v3h-3zM844 241h3v3h-3zM284 252h3v3h-3zM293 252h3v3h-3zM302 252h3v3h-3zM311 252h3v3h-3zM319 252h3v3h-3zM328 252h3v3h-3zM337 252h3v3h-3zM346 252h3v3h-3zM355 252h3v3h-3zM524 252h3v3h-3zM533 252h3v3h-3zM542 252h3v3h-3zM551 252h3v3h-3zM559 252h3v3h-3zM568 252h3v3h-3zM577 252h3v3h-3zM586 252h3v3h-3zM595 252h3v3h-3zM604 252h3v3h-3zM613 252h3v3h-3zM622 252h3v3h-3zM631 252h3v3h-3zM782 252h3v3h-3zM284 263h3v3h-3zM293 263h3v3h-3zM302 263h3v3h-3zM311 263h3v3h-3zM319 263h3v3h-3zM328 263h3v3h-3zM337 263h3v3h-3zM346 263h3v3h-3zM355 263h3v3h-3zM524 263h3v3h-3zM533 263h3v3h-3zM542 263h3v3h-3zM551 263h3v3h-3zM559 263h3v3h-3zM568 263h3v3h-3zM577 263h3v3h-3zM586 263h3v3h-3zM595 263h3v3h-3zM604 263h3v3h-3zM613 263h3v3h-3zM622 263h3v3h-3zM782 263h3v3h-3zM791 263h3v3h-3zM799 263h3v3h-3zM808 263h3v3h-3zM817 263h3v3h-3zM826 263h3v3h-3zM835 263h3v3h-3zM844 263h3v3h-3zM284 274h3v3h-3zM293 274h3v3h-3zM302 274h3v3h-3zM311 274h3v3h-3zM319 274h3v3h-3zM328 274h3v3h-3zM337 274h3v3h-3zM346 274h3v3h-3zM355 274h3v3h-3zM364 274h3v3h-3zM373 274h3v3h-3zM533 274h3v3h-3zM542 274h3v3h-3zM551 274h3v3h-3zM559 274h3v3h-3zM568 274h3v3h-3zM577 274h3v3h-3zM586 274h3v3h-3zM595 274h3v3h-3zM604 274h3v3h-3zM613 274h3v3h-3zM791 274h3v3h-3zM799 274h3v3h-3zM808 274h3v3h-3zM817 274h3v3h-3zM826 274h3v3h-3zM835 274h3v3h-3zM844 274h3v3h-3zM853 274h3v3h-3zM862 274h3v3h-3zM871 274h3v3h-3zM879 274h3v3h-3zM888 274h3v3h-3zM897 274h3v3h-3zM906 274h3v3h-3zM284 285h3v3h-3zM293 285h3v3h-3zM302 285h3v3h-3zM311 285h3v3h-3zM319 285h3v3h-3zM328 285h3v3h-3zM337 285h3v3h-3zM346 285h3v3h-3zM355 285h3v3h-3zM364 285h3v3h-3zM373 285h3v3h-3zM382 285h3v3h-3zM391 285h3v3h-3zM533 285h3v3h-3zM542 285h3v3h-3zM551 285h3v3h-3zM559 285h3v3h-3zM568 285h3v3h-3zM577 285h3v3h-3zM586 285h3v3h-3zM595 285h3v3h-3zM604 285h3v3h-3zM791 285h3v3h-3zM799 285h3v3h-3zM808 285h3v3h-3zM817 285h3v3h-3zM826 285h3v3h-3zM835 285h3v3h-3zM844 285h3v3h-3zM853 285h3v3h-3zM906 285h3v3h-3zM915 285h3v3h-3zM293 296h3v3h-3zM302 296h3v3h-3zM311 296h3v3h-3zM319 296h3v3h-3zM328 296h3v3h-3zM337 296h3v3h-3zM346 296h3v3h-3zM355 296h3v3h-3zM364 296h3v3h-3zM373 296h3v3h-3zM382 296h3v3h-3zM391 296h3v3h-3zM399 296h3v3h-3zM533 296h3v3h-3zM542 296h3v3h-3zM551 296h3v3h-3zM559 296h3v3h-3zM568 296h3v3h-3zM577 296h3v3h-3zM586 296h3v3h-3zM595 296h3v3h-3zM604 296h3v3h-3zM826 296h3v3h-3zM835 296h3v3h-3zM844 296h3v3h-3zM293 307h3v3h-3zM302 307h3v3h-3zM311 307h3v3h-3zM319 307h3v3h-3zM328 307h3v3h-3zM337 307h3v3h-3zM346 307h3v3h-3zM355 307h3v3h-3zM364 307h3v3h-3zM373 307h3v3h-3zM382 307h3v3h-3zM391 307h3v3h-3zM533 307h3v3h-3zM542 307h3v3h-3zM551 307h3v3h-3zM559 307h3v3h-3zM568 307h3v3h-3zM577 307h3v3h-3zM586 307h3v3h-3zM595 307h3v3h-3zM604 307h3v3h-3zM293 318h3v3h-3zM302 318h3v3h-3zM311 318h3v3h-3zM319 318h3v3h-3zM328 318h3v3h-3zM337 318h3v3h-3zM346 318h3v3h-3zM355 318h3v3h-3zM364 318h3v3h-3zM373 318h3v3h-3zM382 318h3v3h-3zM391 318h3v3h-3zM533 318h3v3h-3zM542 318h3v3h-3zM551 318h3v3h-3zM559 318h3v3h-3zM568 318h3v3h-3zM577 318h3v3h-3zM586 318h3v3h-3zM595 318h3v3h-3zM604 318h3v3h-3zM622 318h3v3h-3zM631 318h3v3h-3zM853 318h3v3h-3zM862 318h3v3h-3zM871 318h3v3h-3zM879 318h3v3h-3zM888 318h3v3h-3zM897 318h3v3h-3zM302 329h3v3h-3zM311 329h3v3h-3zM319 329h3v3h-3zM328 329h3v3h-3zM337 329h3v3h-3zM346 329h3v3h-3zM355 329h3v3h-3zM364 329h3v3h-3zM373 329h3v3h-3zM382 329h3v3h-3zM542 329h3v3h-3zM551 329h3v3h-3zM559 329h3v3h-3zM568 329h3v3h-3zM577 329h3v3h-3zM586 329h3v3h-3zM595 329h3v3h-3zM622 329h3v3h-3zM631 329h3v3h-3zM835 329h3v3h-3zM844 329h3v3h-3zM853 329h3v3h-3zM862 329h3v3h-3zM871 329h3v3h-3zM879 329h3v3h-3zM888 329h3v3h-3zM897 329h3v3h-3zM906 329h3v3h-3zM311 340h3v3h-3zM319 340h3v3h-3zM328 340h3v3h-3zM337 340h3v3h-3zM346 340h3v3h-3zM355 340h3v3h-3zM364 340h3v3h-3zM373 340h3v3h-3zM382 340h3v3h-3zM542 340h3v3h-3zM551 340h3v3h-3zM559 340h3v3h-3zM568 340h3v3h-3zM577 340h3v3h-3zM586 340h3v3h-3zM595 340h3v3h-3zM622 340h3v3h-3zM631 340h3v3h-3zM826 340h3v3h-3zM835 340h3v3h-3zM844 340h3v3h-3zM853 340h3v3h-3zM862 340h3v3h-3zM871 340h3v3h-3zM879 340h3v3h-3zM888 340h3v3h-3zM897 340h3v3h-3zM906 340h3v3h-3zM311 351h3v3h-3zM319 351h3v3h-3zM328 351h3v3h-3zM337 351h3v3h-3zM346 351h3v3h-3zM355 351h3v3h-3zM364 351h3v3h-3zM542 351h3v3h-3zM551 351h3v3h-3zM559 351h3v3h-3zM568 351h3v3h-3zM577 351h3v3h-3zM586 351h3v3h-3zM631 351h3v3h-3zM817 351h3v3h-3zM826 351h3v3h-3zM835 351h3v3h-3zM844 351h3v3h-3zM853 351h3v3h-3zM862 351h3v3h-3zM871 351h3v3h-3zM879 351h3v3h-3zM888 351h3v3h-3zM897 351h3v3h-3zM906 351h3v3h-3zM915 351h3v3h-3zM311 362h3v3h-3zM319 362h3v3h-3zM328 362h3v3h-3zM337 362h3v3h-3zM346 362h3v3h-3zM355 362h3v3h-3zM542 362h3v3h-3zM551 362h3v3h-3zM559 362h3v3h-3zM568 362h3v3h-3zM577 362h3v3h-3zM586 362h3v3h-3zM826 362h3v3h-3zM835 362h3v3h-3zM844 362h3v3h-3zM853 362h3v3h-3zM862 362h3v3h-3zM871 362h3v3h-3zM879 362h3v3h-3zM888 362h3v3h-3zM897 362h3v3h-3zM906 362h3v3h-3zM915 362h3v3h-3zM924 362h3v3h-3zM311 373h3v3h-3zM319 373h3v3h-3zM328 373h3v3h-3zM337 373h3v3h-3zM346 373h3v3h-3zM355 373h3v3h-3zM551 373h3v3h-3zM559 373h3v3h-3zM568 373h3v3h-3zM577 373h3v3h-3zM826 373h3v3h-3zM835 373h3v3h-3zM844 373h3v3h-3zM853 373h3v3h-3zM862 373h3v3h-3zM871 373h3v3h-3zM879 373h3v3h-3zM888 373h3v3h-3zM897 373h3v3h-3zM906 373h3v3h-3zM915 373h3v3h-3zM302 384h3v3h-3zM311 384h3v3h-3zM319 384h3v3h-3zM328 384h3v3h-3zM337 384h3v3h-3zM346 384h3v3h-3zM551 384h3v3h-3zM559 384h3v3h-3zM568 384h3v3h-3zM879 384h3v3h-3zM888 384h3v3h-3zM897 384h3v3h-3zM906 384h3v3h-3zM915 384h3v3h-3zM302 395h3v3h-3zM311 395h3v3h-3zM319 395h3v3h-3zM328 395h3v3h-3zM337 395h3v3h-3zM888 395h3v3h-3zM897 395h3v3h-3zM906 395h3v3h-3zM302 406h3v3h-3zM311 406h3v3h-3zM319 406h3v3h-3zM977 406h3v3h-3zM986 406h3v3h-3zM302 417h3v3h-3zM311 417h3v3h-3zM319 417h3v3h-3zM968 417h3v3h-3zM293 428h3v3h-3zM302 428h3v3h-3zM311 428h3v3h-3zM302 439h3v3h-3zM311 439h3v3h-3zM494 84h3v3h-3zM499 84h3v3h-3zM494 89h3v3h-3zM528 91h3v3h-3zM533 91h3v3h-3zM528 96h3v3h-3zM544 58h3v3h-3zM549 58h3v3h-3zM544 63h3v3h-3zM597 159h3v3h-3zM602 159h3v3h-3zM597 164h3v3h-3zM651 185h3v3h-3zM656 185h3v3h-3zM651 190h3v3h-3z"/></g>
  </defs>
</svg>
<div class="progress" id="prog"></div>

<header class="mast" id="mast">
  <div class="wrap mast-in">
    <a class="mark" href="/" aria-label="Windsor Harlow, home">
      <img class="mark-img mark-img--dark" src="/assets/brand/logo-primary.svg" alt="Windsor Harlow" width="480" height="128">
      <img class="mark-img mark-img--light" src="/assets/brand/logo-reverse.svg" alt="" aria-hidden="true" width="480" height="128">
    </a>
    <nav class="nav" id="nav">
{navlinks}
    </nav>
    <a class="btn" href="/contact.html">Start a conversation <span class="arrow">&#8594;</span></a>
    <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false"><span></span></button>
  </div>
</header>

<div class="scrim" id="scrim"></div>
<aside class="drawer" id="drawer" aria-hidden="true">
  <button class="drawer-x" id="drawerX">Close &#10005;</button>
  <img class="mark-img mark-img--light drawer-mark" src="/assets/brand/logo-reverse.svg" alt="Windsor Harlow" width="480" height="128">
  <nav>
{drawerlinks}
    <a href="/contact.html">Contact</a>
  </nav>
  <a class="btn" href="/contact.html">Start a conversation <span class="arrow">&#8594;</span></a>
</aside>

<main id="top" tabindex="-1">
"""

FOOT = """</main>

<footer class="foot">
  <div class="wrap">
    <div class="foot-top">
      <div>
        <a class="mark" href="/" aria-label="Windsor Harlow, home"><img class="mark-img mark-img--light" src="/assets/brand/logo-reverse.svg" alt="Windsor Harlow" width="480" height="128"></a>
        <p class="foot-note">A technology consultancy for systems that have to keep running after we leave. Engineered in India, delivering globally.</p>
      </div>
      <div>
        <h2 class="foot-h">Services</h2>
        <ul>
          <li><a href="/practices/ai-ml.html">AI, ML &amp; MLOps</a></li>
          <li><a href="/practices/salesforce.html">Salesforce</a></li>
          <li><a href="/practices/cloud.html">Cloud &amp; Infrastructure</a></li>
          <li><a href="/practices/web.html">Web &amp; Distributed Systems</a></li>
          <li><a href="/practices/mobile.html">Mobile</a></li>
          <li><a href="/practices/commerce.html">Commerce &amp; Design</a></li>
          <li><a href="/services.html">All services</a></li>
        </ul>
      </div>
      <div>
        <h2 class="foot-h">Firm</h2>
        <ul>
          <li><a href="/#engagement">Engagement models</a></li>
          <li><a href="/#delivery">How we deliver</a></li>
          <li><a href="/#index">Capability index</a></li>
          <li><a href="/#work">Work</a></li>
          <li><a href="/brand.html">Brand guidelines</a></li>
          <li><a href="/privacy.html">Privacy &amp; data handling</a></li>
        </ul>
      </div>
      <div>
        <h2 class="foot-h">Contact</h2>
        <ul>
          <li><a href="mailto:__MAIL__">__MAIL__</a></li>
          <li>Registered office &mdash; India</li>
          <li>Serving clients worldwide</li>
        </ul>
      </div>
    </div>
    <div class="foot-btm">
      <span>&copy; <span id="yr"></span> Windsor Harlow &middot; India</span>
      <span>Senior engineers only &middot; Documented handoff</span>
    </div>
  </div>
</footer>

<script src="/assets/js/data.js"></script>
<script src="/assets/js/live.js"></script>
<script src="/assets/js/wh.js"></script>
</body>
</html>
""".replace("__MAIL__", MAIL)


FAILSAFE = """<script>
window.WH_BASE="__BASE__";
window.WH_MAIL="__MAIL__";

/* ----------------------------------------------------------------
   Backend endpoint. Null means there is no backend yet, and the site
   behaves accordingly: no portfolio fetch, no status pill, and the
   enquiry form hands the message straight to the visitor's mail
   client instead of pretending to post it somewhere.
   After deploying the enquiry Lambda, set this to its base URL —
   e.g. "https://api.windsorharlow.com" — and everything wakes up.
   ---------------------------------------------------------------- */
window.WH_API = null;
/* If scripting dies before the overture closes, remove it after 6s so the page
   is never held behind a curtain that will not lift. */
setTimeout(function(){var o=document.getElementById("overture");
  if(o&&!o.classList.contains("done")){o.remove();document.body.classList.remove("ov-locked");}},9000);
</script>"""

NOSCRIPT = ('<noscript><style>.overture{display:none!important}'
            'body{overflow:auto!important}</style></noscript>')


def relativise(html, depth):
    """Make every internal link work over file:// as well as over HTTP."""
    prefix = "../" * depth
    html = html.replace('href="/"', f'href="{prefix}index.html"')
    html = html.replace('href="/practices/"', f'href="{prefix}services.html"')
    html = html.replace('="/assets/', f'="{prefix}assets/')
    html = html.replace('="/practices/', f'="{prefix}practices/')
    for f in ("index.html", "contact.html", "admin.html", "brand.html",
              "privacy.html", "404.html", "services.html"):
        html = html.replace(f'="/{f}', f'="{prefix}{f}')
    html = html.replace('href="/#', f'href="{prefix}index.html#')
    return html.replace("__BASE__", prefix)


# ---------------------------------------------------------------- fonts
# Google's stylesheet is a render-blocking request to a third party that sees
# every visitor's IP. Once tools/fetch-fonts.py has pulled the files locally,
# the build serves them itself and drops the CDN entirely. Until then it falls
# back to the CDN, so the pages always have their typefaces.
_FONT_DIR = os.path.join(os.path.dirname(__file__), "..", "public", "assets", "fonts")
SELF_HOSTED_FONTS = os.path.isdir(_FONT_DIR) and any(
    f.endswith(".woff2") for f in os.listdir(_FONT_DIR))

if SELF_HOSTED_FONTS:
    _first = sorted(f for f in os.listdir(_FONT_DIR) if f.endswith(".woff2"))[:3]
    FONTS = "\n".join(
        [f'<link rel="preload" href="/assets/fonts/{f}" as="font" type="font/woff2" crossorigin>'
         for f in _first]
        + ['<link rel="stylesheet" href="/assets/css/fonts.css">'])
else:
    FONTS = (
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,'
        'wght@0,6..72,200..500;1,6..72,300&family=Archivo:wght@400;500;600'
        '&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')


# Per-page share cards, if tools/make-og.py has produced them. A page with
# no card of its own falls back to the shared one rather than shipping a
# broken image URL.
_OG_DIR = os.path.join(os.path.dirname(__file__), "..", "public",
                       "assets", "brand", "og")


def og_image(path):
    rel = path.lstrip("/") or "index.html"
    name = rel.replace("/", "-").replace(".html", "") + ".jpg"
    if os.path.isfile(os.path.join(_OG_DIR, name)):
        return "/assets/brand/og/" + name
    return "/assets/brand/og.jpg"


def page(path, title, desc, body, extra_head="", depth=0):
    navlinks = "\n".join(
        f'      <a href="{h}">{n}</a>' for n, h in NAV)
    drawerlinks = "\n".join(
        f'    <a href="{h}">{n}</a>' for n, h in NAV)
    head = HEAD.format(title=title, desc=desc, site=SITE, path=path,
                       ogimg=og_image(path),
                       navlinks=navlinks, drawerlinks=drawerlinks,
                       extra_head=extra_head)
    head = head.replace("__FONTS__", FONTS)
    head = head.replace("__FAILSAFE__", FAILSAFE.replace("__MAIL__", MAIL)).replace("__NOSCRIPT__", NOSCRIPT)
    return relativise(head + body + FOOT, depth)


def cta(heading, sub, label="Scope an engagement"):
    return f"""
<section class="dark band-tight">
  <div class="wrap">
    <div class="split">
      <h2>{heading}</h2>
      <div>
        <p class="lede">{sub}</p>
        <p style="margin-top:26px"><a class="btn" href="/contact.html">{label} <span class="arrow">&#8594;</span></a></p>
      </div>
    </div>
  </div>
</section>
"""


TERMINAL = """
      <div class="term" id="term">
        <div class="term-bar">
          <div class="term-dots"><i></i><i></i><i></i></div>
          <span class="term-file" id="termFile">&nbsp;</span>
          <span class="term-tag" id="termTag">&nbsp;</span>
        </div>
        <div class="term-body" id="termBody"></div>
        <div class="term-foot">
          <span class="term-status" id="termStatus"><i></i><span>Running</span></span>
          <span class="term-elapsed" id="termElapsed">0.0s</span>
        </div>
      </div>
"""

PIPELINE = """
      <div class="pipe" style="margin-top:24px">
        <div class="pipe-head">
          <b id="pipeName">pipeline</b>
          <span id="pipeBranch">main</span>
          <span class="run">&#9679; live run</span>
        </div>
        <div class="pipe-stages" id="pipeStages"></div>
      </div>
"""

ORBIT = """
      <div class="orbit-wrap" id="orbit" aria-hidden="true">
        <div class="orbit-ring"></div>
        <div class="orbit-ring r-mid"></div>
        <div class="orbit-ring r-in"></div>
        <div class="orbit-spin"></div>
        <div class="orbit-spin mid"></div>
        <div class="orbit-spin inner"></div>
        <div class="orbit-core">
            <img src="/assets/brand/badge-reverse.svg" alt="" width="118" height="88">
          </div>
      </div>
"""


def live_section(dark=True):
    """The terminal + pipeline block, with tabs."""
    cls = "dark band" if dark else "band lift"
    return f"""
<section class="{cls}" id="live">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <p class="eyebrow">In the work</p>
        <h2>This is what an engagement <em>actually looks like</em>.</h2>
      </div>
    </div>
    <div class="live">
      <div>
        <div class="live-tabs" id="liveTabs"></div>
        {TERMINAL}
        {PIPELINE}
      </div>
      <div class="live-copy">
        <h3>Tests, CI and infrastructure-as-code from the first commit.</h3>
        <p>A pipeline that fails a build rather than a customer conversation.</p>
        <p style="margin-top:14px">Written so the engineer who inherits it can read it without a call.</p>
        <p style="margin-top:24px"><a class="btn btn-ghost" href="/services.html">See all services <span class="arrow">&#8594;</span></a></p>
      </div>
    </div>
  </div>
</section>
"""


def orbit_section():
    return f"""
<section class="band" id="platform">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <p class="eyebrow">One firm, one stack</p>
        <h2>The layers most consultancies split across <em>three vendors</em>.</h2>
      </div>
    </div>
    <div class="live">
      {ORBIT}
      <div class="live-copy">
        <h3>The handoffs are where projects die.</h3>
        <p>Split a feature across an AI shop, a cloud partner and a front-end agency, and the failure lands in the gaps.</p>
        <p style="margin-top:14px"></p>
        <p style="margin-top:24px"><a class="btn btn-ghost" href="/contact.html">Scope an engagement <span class="arrow">&#8594;</span></a></p>
      </div>
    </div>
  </div>
</section>
"""


INTRO = """
<section class="intro" id="intro">
  <div class="intro-visual">
    <p class="intro-tag"><b></b>Windsor Harlow &middot; the whole stack</p>
    <div class="platform-wrap">
      <svg class="platform" viewBox="0 0 640 620" xmlns="http://www.w3.org/2000/svg"
         role="img" aria-label="The four layers Windsor Harlow builds: infrastructure, data, services and interface"
         preserveAspectRatio="xMidYMid meet">
      <line class="pf-spine" x1="300" y1="590" x2="300" y2="36"/>
      <line class="pf-pulse" x1="300" y1="590" x2="300" y2="36"/>
      <g class="pf-layer" style="--d:0.0s">
        <polygon class="pf-plane" points="300 36 508 118 300 200 92 118"/>
        <polygon class="pf-cell lit alt" points="92.0,118.0 144.0,97.5 196.0,118.0 144.0,138.5" style="--d:0.25s"/>
        <polygon class="pf-cell" points="144.0,138.5 196.0,118.0 248.0,138.5 196.0,159.0" style="--d:0.34s"/>
        <polygon class="pf-cell lit alt" points="196.0,159.0 248.0,138.5 300.0,159.0 248.0,179.5" style="--d:0.43s"/>
        <polygon class="pf-cell" points="248.0,179.5 300.0,159.0 352.0,179.5 300.0,200.0" style="--d:0.52s"/>
        <polygon class="pf-cell" points="144.0,97.5 196.0,77.0 248.0,97.5 196.0,118.0" style="--d:0.34s"/>
        <polygon class="pf-cell" points="196.0,118.0 248.0,97.5 300.0,118.0 248.0,138.5" style="--d:0.43s"/>
        <polygon class="pf-cell lit alt" points="248.0,138.5 300.0,118.0 352.0,138.5 300.0,159.0" style="--d:0.52s"/>
        <polygon class="pf-cell" points="300.0,159.0 352.0,138.5 404.0,159.0 352.0,179.5" style="--d:0.61s"/>
        <polygon class="pf-cell" points="196.0,77.0 248.0,56.5 300.0,77.0 248.0,97.5" style="--d:0.43s"/>
        <polygon class="pf-cell" points="248.0,97.5 300.0,77.0 352.0,97.5 300.0,118.0" style="--d:0.52s"/>
        <polygon class="pf-cell lit alt" points="300.0,118.0 352.0,97.5 404.0,118.0 352.0,138.5" style="--d:0.61s"/>
        <polygon class="pf-cell" points="352.0,138.5 404.0,118.0 456.0,138.5 404.0,159.0" style="--d:0.7s"/>
        <polygon class="pf-cell" points="248.0,56.5 300.0,36.0 352.0,56.5 300.0,77.0" style="--d:0.52s"/>
        <polygon class="pf-cell" points="300.0,77.0 352.0,56.5 404.0,77.0 352.0,97.5" style="--d:0.61s"/>
        <polygon class="pf-cell" points="352.0,97.5 404.0,77.0 456.0,97.5 404.0,118.0" style="--d:0.7s"/>
        <polygon class="pf-cell lit" points="404.0,118.0 456.0,97.5 508.0,118.0 456.0,138.5" style="--d:0.79s"/>
        <path class="pf-edge" d="M92 118 L300 36 L508 118"/>
        <text class="pf-name" x="530" y="116">INTERFACE</text>
        <line class="pf-tick" x1="512" y1="112" x2="524" y2="112"/>
      </g>
      <g class="pf-layer" style="--d:0.34s">
        <polygon class="pf-plane" points="300 166 508 248 300 330 92 248"/>
        <polygon class="pf-cell" points="92.0,248.0 144.0,227.5 196.0,248.0 144.0,268.5" style="--d:0.59s"/>
        <polygon class="pf-cell lit" points="144.0,268.5 196.0,248.0 248.0,268.5 196.0,289.0" style="--d:0.68s"/>
        <polygon class="pf-cell lit alt" points="196.0,289.0 248.0,268.5 300.0,289.0 248.0,309.5" style="--d:0.77s"/>
        <polygon class="pf-cell" points="248.0,309.5 300.0,289.0 352.0,309.5 300.0,330.0" style="--d:0.86s"/>
        <polygon class="pf-cell" points="144.0,227.5 196.0,207.0 248.0,227.5 196.0,248.0" style="--d:0.68s"/>
        <polygon class="pf-cell lit" points="196.0,248.0 248.0,227.5 300.0,248.0 248.0,268.5" style="--d:0.77s"/>
        <polygon class="pf-cell" points="248.0,268.5 300.0,248.0 352.0,268.5 300.0,289.0" style="--d:0.86s"/>
        <polygon class="pf-cell" points="300.0,289.0 352.0,268.5 404.0,289.0 352.0,309.5" style="--d:0.95s"/>
        <polygon class="pf-cell lit alt" points="196.0,207.0 248.0,186.5 300.0,207.0 248.0,227.5" style="--d:0.77s"/>
        <polygon class="pf-cell" points="248.0,227.5 300.0,207.0 352.0,227.5 300.0,248.0" style="--d:0.86s"/>
        <polygon class="pf-cell" points="300.0,248.0 352.0,227.5 404.0,248.0 352.0,268.5" style="--d:0.95s"/>
        <polygon class="pf-cell" points="352.0,268.5 404.0,248.0 456.0,268.5 404.0,289.0" style="--d:1.04s"/>
        <polygon class="pf-cell" points="248.0,186.5 300.0,166.0 352.0,186.5 300.0,207.0" style="--d:0.86s"/>
        <polygon class="pf-cell lit" points="300.0,207.0 352.0,186.5 404.0,207.0 352.0,227.5" style="--d:0.95s"/>
        <polygon class="pf-cell" points="352.0,227.5 404.0,207.0 456.0,227.5 404.0,248.0" style="--d:1.04s"/>
        <polygon class="pf-cell" points="404.0,248.0 456.0,227.5 508.0,248.0 456.0,268.5" style="--d:1.13s"/>
        <path class="pf-edge" d="M92 248 L300 166 L508 248"/>
        <text class="pf-name" x="530" y="246">SERVICES</text>
        <line class="pf-tick" x1="512" y1="242" x2="524" y2="242"/>
      </g>
      <g class="pf-layer" style="--d:0.68s">
        <polygon class="pf-plane" points="300 296 508 378 300 460 92 378"/>
        <polygon class="pf-cell lit alt" points="92.0,378.0 144.0,357.5 196.0,378.0 144.0,398.5" style="--d:0.93s"/>
        <polygon class="pf-cell lit" points="144.0,398.5 196.0,378.0 248.0,398.5 196.0,419.0" style="--d:1.02s"/>
        <polygon class="pf-cell" points="196.0,419.0 248.0,398.5 300.0,419.0 248.0,439.5" style="--d:1.11s"/>
        <polygon class="pf-cell lit" points="248.0,439.5 300.0,419.0 352.0,439.5 300.0,460.0" style="--d:1.2s"/>
        <polygon class="pf-cell" points="144.0,357.5 196.0,337.0 248.0,357.5 196.0,378.0" style="--d:1.02s"/>
        <polygon class="pf-cell" points="196.0,378.0 248.0,357.5 300.0,378.0 248.0,398.5" style="--d:1.11s"/>
        <polygon class="pf-cell" points="248.0,398.5 300.0,378.0 352.0,398.5 300.0,419.0" style="--d:1.2s"/>
        <polygon class="pf-cell" points="300.0,419.0 352.0,398.5 404.0,419.0 352.0,439.5" style="--d:1.29s"/>
        <polygon class="pf-cell lit alt" points="196.0,337.0 248.0,316.5 300.0,337.0 248.0,357.5" style="--d:1.11s"/>
        <polygon class="pf-cell" points="248.0,357.5 300.0,337.0 352.0,357.5 300.0,378.0" style="--d:1.2s"/>
        <polygon class="pf-cell" points="300.0,378.0 352.0,357.5 404.0,378.0 352.0,398.5" style="--d:1.29s"/>
        <polygon class="pf-cell" points="352.0,398.5 404.0,378.0 456.0,398.5 404.0,419.0" style="--d:1.38s"/>
        <polygon class="pf-cell" points="248.0,316.5 300.0,296.0 352.0,316.5 300.0,337.0" style="--d:1.2s"/>
        <polygon class="pf-cell" points="300.0,337.0 352.0,316.5 404.0,337.0 352.0,357.5" style="--d:1.29s"/>
        <polygon class="pf-cell lit alt" points="352.0,357.5 404.0,337.0 456.0,357.5 404.0,378.0" style="--d:1.38s"/>
        <polygon class="pf-cell" points="404.0,378.0 456.0,357.5 508.0,378.0 456.0,398.5" style="--d:1.47s"/>
        <path class="pf-edge" d="M92 378 L300 296 L508 378"/>
        <text class="pf-name" x="530" y="376">DATA</text>
        <line class="pf-tick" x1="512" y1="372" x2="524" y2="372"/>
      </g>
      <g class="pf-layer" style="--d:1.02s">
        <polygon class="pf-plane" points="300 426 508 508 300 590 92 508"/>
        <polygon class="pf-cell" points="92.0,508.0 144.0,487.5 196.0,508.0 144.0,528.5" style="--d:1.27s"/>
        <polygon class="pf-cell lit" points="144.0,528.5 196.0,508.0 248.0,528.5 196.0,549.0" style="--d:1.36s"/>
        <polygon class="pf-cell lit alt" points="196.0,549.0 248.0,528.5 300.0,549.0 248.0,569.5" style="--d:1.45s"/>
        <polygon class="pf-cell lit" points="248.0,569.5 300.0,549.0 352.0,569.5 300.0,590.0" style="--d:1.54s"/>
        <polygon class="pf-cell" points="144.0,487.5 196.0,467.0 248.0,487.5 196.0,508.0" style="--d:1.36s"/>
        <polygon class="pf-cell" points="196.0,508.0 248.0,487.5 300.0,508.0 248.0,528.5" style="--d:1.45s"/>
        <polygon class="pf-cell lit alt" points="248.0,528.5 300.0,508.0 352.0,528.5 300.0,549.0" style="--d:1.54s"/>
        <polygon class="pf-cell" points="300.0,549.0 352.0,528.5 404.0,549.0 352.0,569.5" style="--d:1.63s"/>
        <polygon class="pf-cell" points="196.0,467.0 248.0,446.5 300.0,467.0 248.0,487.5" style="--d:1.45s"/>
        <polygon class="pf-cell" points="248.0,487.5 300.0,467.0 352.0,487.5 300.0,508.0" style="--d:1.54s"/>
        <polygon class="pf-cell" points="300.0,508.0 352.0,487.5 404.0,508.0 352.0,528.5" style="--d:1.63s"/>
        <polygon class="pf-cell" points="352.0,528.5 404.0,508.0 456.0,528.5 404.0,549.0" style="--d:1.72s"/>
        <polygon class="pf-cell" points="248.0,446.5 300.0,426.0 352.0,446.5 300.0,467.0" style="--d:1.54s"/>
        <polygon class="pf-cell" points="300.0,467.0 352.0,446.5 404.0,467.0 352.0,487.5" style="--d:1.63s"/>
        <polygon class="pf-cell lit alt" points="352.0,487.5 404.0,467.0 456.0,487.5 404.0,508.0" style="--d:1.72s"/>
        <polygon class="pf-cell" points="404.0,508.0 456.0,487.5 508.0,508.0 456.0,528.5" style="--d:1.81s"/>
        <path class="pf-edge" d="M92 508 L300 426 L508 508"/>
        <text class="pf-name" x="530" y="506">INFRASTRUCTURE</text>
        <line class="pf-tick" x1="512" y1="502" x2="524" y2="502"/>
      </g>
    </svg>
    </div>
    <dl class="intro-readout">
      <div><dt>Layers</dt><dd>Four &mdash; one team</dd></div>
      <div><dt>Vendor handoffs</dt><dd>None</dd></div>
      <div><dt>Overlap</dt><dd id="introClock">&mdash;</dd></div>
    </dl>
  </div>

  <div class="intro-copy">
    <p class="eyebrow">Introducing</p>
    <h2>A consultancy built by the people who <em>stay for the hard part</em>.</h2>
    <p class="intro-cta">
      <a class="btn" href="/services.html">See what we build <span class="arrow">&#8594;</span></a>
    </p>
  </div>
</section>
"""


OVERTURE = """
<div class="overture" id="overture" role="presentation">
  <div class="ov-map" aria-hidden="true">
    <svg class="worldmap ov-worldmap" viewBox="0 0 1000 460" xmlns="http://www.w3.org/2000/svg"
         role="img" aria-label="Windsor Harlow delivery map: engineering in India, clients worldwide"
         preserveAspectRatio="xMidYMid meet">
      <use href="#wmDots"/>
      <g class="wm-net">
        <path class="wm-arc" d="M722 199 Q487 57 224 133" style="animation-delay:0.0s"/>
        <path class="wm-arc" d="M722 199 Q508 32 242 78" style="animation-delay:0.28s"/>
        <path class="wm-arc" d="M722 199 Q513 155 366 309" style="animation-delay:0.56s"/>
        <path class="wm-arc" d="M722 199 Q641 79 496 86" style="animation-delay:0.84s"/>
        <path class="wm-arc" d="M722 199 Q632 77 482 89" style="animation-delay:1.12s"/>
        <path class="wm-arc" d="M722 199 Q656 93 530 94" style="animation-delay:1.4s"/>
        <path class="wm-arc" d="M722 199 Q673 80 546 60" style="animation-delay:1.68s"/>
        <path class="wm-arc" d="M722 199 Q668 97 553 89" style="animation-delay:1.96s"/>
        <path class="wm-arc" d="M722 199 Q691 174 653 187" style="animation-delay:2.24s"/>
        <path class="wm-arc" d="M722 199 Q776 212 793 265" style="animation-delay:2.52s"/>
        <path class="wm-arc" d="M722 199 Q791 124 890 144" style="animation-delay:2.8s"/>
        <path class="wm-arc" d="M722 199 Q773 134 855 144" style="animation-delay:3.08s"/>
        <path class="wm-arc" d="M722 199 Q749 155 802 155" style="animation-delay:3.36s"/>
        <path class="wm-arc" d="M722 199 Q840 234 873 353" style="animation-delay:3.64s"/>
        <path class="wm-arc" d="M722 199 Q909 231 979 408" style="animation-delay:3.92s"/>
        <path class="wm-arc" d="M722 199 Q600 239 570 364" style="animation-delay:4.2s"/>
        <g class="wm-mark" style="animation-delay:0.0s"><circle class="wm-pt-ring" cx="223.7" cy="133.3" r="3.2"/><circle class="wm-pt" cx="223.7" cy="133.3" r="3.2"/><text class="wm-label" x="223.7" y="119" text-anchor="mid">USA</text></g>
        <g class="wm-mark" style="animation-delay:0.28s"><circle class="wm-pt-ring" cx="241.5" cy="78.4" r="3.2"/><circle class="wm-pt" cx="241.5" cy="78.4" r="3.2"/><text class="wm-label" x="241.5" y="64" text-anchor="mid">CANADA</text></g>
        <g class="wm-mark" style="animation-delay:0.56s"><circle class="wm-pt-ring" cx="365.9" cy="309.1" r="3.2"/><circle class="wm-pt" cx="365.9" cy="309.1" r="3.2"/><text class="wm-label" x="365.9" y="329" text-anchor="mid">BRAZIL</text></g>
        <g class="wm-mark" style="animation-delay:0.84s"><circle class="wm-pt-ring" cx="495.9" cy="85.6" r="3.2"/><circle class="wm-pt" cx="495.9" cy="85.6" r="3.2"/><text class="wm-label" x="495.9" y="74" text-anchor="end">UK</text></g>
        <g class="wm-mark" style="animation-delay:1.12s"><circle class="wm-pt-ring" cx="481.5" cy="89.4" r="3.2"/><circle class="wm-pt" cx="481.5" cy="89.4" r="3.2"/><text class="wm-label" x="481.5" y="105" text-anchor="end">IRELAND</text></g>
        <g class="wm-mark" style="animation-delay:1.4s"><circle class="wm-pt-ring" cx="530.4" cy="93.5" r="3.2"/><circle class="wm-pt" cx="530.4" cy="93.5" r="3.2"/><text class="wm-label" x="530.4" y="92" text-anchor="start">GERMANY</text></g>
        <g class="wm-mark" style="animation-delay:1.68s"><circle class="wm-pt-ring" cx="545.9" cy="59.9" r="3.2"/><circle class="wm-pt" cx="545.9" cy="59.9" r="3.2"/><text class="wm-label" x="545.9" y="48" text-anchor="start">SWEDEN</text></g>
        <g class="wm-mark" style="animation-delay:1.96s"><circle class="wm-pt-ring" cx="552.6" cy="89.4" r="3.2"/><circle class="wm-pt" cx="552.6" cy="89.4" r="3.2"/><text class="wm-label" x="552.6" y="112" text-anchor="start">POLAND</text></g>
        <g class="wm-mark" style="animation-delay:2.24s"><circle class="wm-pt-ring" cx="652.9" cy="186.9" r="3.2"/><circle class="wm-pt" cx="652.9" cy="186.9" r="3.2"/><text class="wm-label" x="652.9" y="203" text-anchor="start">UAE</text></g>
        <g class="wm-mark" style="animation-delay:2.52s"><circle class="wm-pt-ring" cx="792.6" cy="265.1" r="3.2"/><circle class="wm-pt" cx="792.6" cy="265.1" r="3.2"/><text class="wm-label" x="792.6" y="281" text-anchor="start">SINGAPORE</text></g>
        <g class="wm-mark" style="animation-delay:2.8s"><circle class="wm-pt-ring" cx="890.4" cy="144.3" r="3.2"/><circle class="wm-pt" cx="890.4" cy="144.3" r="3.2"/><text class="wm-label" x="890.4" y="136" text-anchor="start">JAPAN</text></g>
        <g class="wm-mark" style="animation-delay:3.08s"><circle class="wm-pt-ring" cx="854.8" cy="144.3" r="3.2"/><circle class="wm-pt" cx="854.8" cy="144.3" r="3.2"/><text class="wm-label" x="854.8" y="162" text-anchor="end">SOUTH KOREA</text></g>
        <g class="wm-mark" style="animation-delay:3.36s"><circle class="wm-pt-ring" cx="801.5" cy="155.3" r="3.2"/><circle class="wm-pt" cx="801.5" cy="155.3" r="3.2"/><text class="wm-label" x="801.5" y="141" text-anchor="mid">CHINA</text></g>
        <g class="wm-mark" style="animation-delay:3.64s"><circle class="wm-pt-ring" cx="872.6" cy="353.0" r="3.2"/><circle class="wm-pt" cx="872.6" cy="353.0" r="3.2"/><text class="wm-label" x="872.6" y="375" text-anchor="mid">AUSTRALIA</text></g>
        <g class="wm-mark" style="animation-delay:3.92s"><circle class="wm-pt-ring" cx="979.3" cy="407.9" r="3.2"/><circle class="wm-pt" cx="979.3" cy="407.9" r="3.2"/><text class="wm-label" x="979.3" y="426" text-anchor="end">NEW ZEALAND</text></g>
        <g class="wm-mark" style="animation-delay:4.2s"><circle class="wm-pt-ring" cx="570.4" cy="364.0" r="3.2"/><circle class="wm-pt" cx="570.4" cy="364.0" r="3.2"/><text class="wm-label" x="570.4" y="386" text-anchor="mid">SOUTH AFRICA</text></g>
        <g class="wm-home">
          <circle class="wm-home-ring" cx="721.5" cy="199.2" r="6"/>
          <circle class="wm-home-ring d2" cx="721.5" cy="199.2" r="6"/>
          <circle class="wm-home-dot" cx="721.5" cy="199.2" r="5.2"/>
          <text class="wm-label wm-label-home" x="721.5" y="181" text-anchor="mid">INDIA</text>
        </g>
      </g>
    </svg>
  </div>

  <div class="ov-center">
    <div class="ov-lockup">
      <img class="ov-badge" src="/assets/brand/badge-reverse.svg" alt="" aria-hidden="true" width="118" height="88">
      <p class="ov-word"><span class="ov-logo"><img src="/assets/brand/wordmark-reverse.svg" alt="Windsor Harlow" width="350" height="128"></span></p>
    </div>
    <p class="ov-sub"><span>Engineered in India</span><i></i><span>Delivering globally</span></p>
  </div>

  <div class="ov-meta">
    <span class="ov-count"><b id="ovNum">Connecting</b></span>
    <span class="ov-skip" id="ovSkip">Skip &#8594;</span>
  </div>
  <div class="ov-bar"><i></i></div>
</div>
"""
