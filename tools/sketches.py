# Original line drawings, one per module (viewBox 0 0 320 170). Strokes use currentColor-like classes.
S = {}
S['01'] = '''<path class="ink" d="M140 30 h40 M146 30 v38 L112 136 a10 10 0 0 0 9 14 h78 a10 10 0 0 0 9 -14 L174 68 v-38"/>
<path class="ink thin" d="M124 112 h72"/><circle class="ink thin" cx="150" cy="126" r="5"/><circle class="ink thin" cx="170" cy="118" r="3.5"/><circle class="ink thin" cx="160" cy="98" r="3"/><circle class="ink thin" cx="162" cy="78" r="2.5"/>
<path class="red" d="M246 150 v-40 M240 110 h12 v40 h-12 z"/><path class="red" d="M246 104 c-9 -10 -3 -22 0 -30 c4 10 10 18 0 30 z"/>
<path class="pencil" d="M60 60 q20 -14 40 0 M64 74 q18 -10 34 0"/>'''
S['02'] = '''<path class="ink" d="M120 70 h80 v76 a8 8 0 0 1 -8 8 h-64 a8 8 0 0 1 -8 -8 z"/><path class="ink" d="M114 64 h92 v8 h-92 z"/>
<path class="ink" d="M160 64 v-34"/><circle class="ink" cx="160" cy="24" r="7"/><path class="pencil" d="M124 112 h72 M124 112 q36 8 72 0"/>
<path class="red" d="M176 22 l14 -6 -6 12 16 -4 -10 12 14 2"/><path class="red" d="M146 18 l-12 -8 2 12 -14 -4 8 12"/>'''
S['03'] = '''<ellipse class="pencil dash" cx="170" cy="92" rx="130" ry="46"/><circle class="red" cx="50" cy="92" r="9"/>
<path class="red thin" d="M50 80 v-6 M50 104 v6 M38 92 h-6 M62 92 h6 M41 83 l-4 -4 M59 101 l4 4 M41 101 l-4 4 M59 83 l4 -4"/>
<circle class="ink" cx="258" cy="62" r="6"/><path class="ink thin" d="M262 58 L312 34 M264 64 L314 50 M262 68 L310 66"/>'''
S['04'] = '''<rect class="ink" x="70" y="22" width="86" height="126" rx="8" transform="rotate(-8 113 85)"/>
<rect class="ink" x="160" y="22" width="86" height="126" rx="8" transform="rotate(6 203 85)"/>
<path class="red fill" d="M203 66 c-14 14 -22 20 -22 30 a11 11 0 0 0 20 6 l-4 16 h12 l-4 -16 a11 11 0 0 0 20 -6 c0 -10 -8 -16 -22 -30 z" transform="rotate(6 203 85)"/>
<path class="ink fill" d="M113 70 c-12 12 -19 18 -19 26 a10 10 0 0 0 17 5 l-3 14 h10 l-3 -14 a10 10 0 0 0 17 -5 c0 -8 -7 -14 -19 -26 z" transform="rotate(-8 113 85)"/>
<path class="pencil" d="M262 40 q16 -8 24 6 q-12 2 -10 14"/><circle class="pencil fill" cx="276" cy="70" r="2.5"/>'''
S['05'] = '''<circle class="red fill" cx="48" cy="90" r="10"/><path class="pencil dash" d="M48 90 m-70 0 a70 60 0 1 0 140 0 a70 60 0 1 0 -140 0"/>
<path class="ink" d="M58 90 a150 110 0 0 1 220 -10"/><circle class="ink" cx="190" cy="30" r="9"/><path class="pencil dash" d="M190 30 l12 -12"/>
<circle class="red" cx="272" cy="86" r="12"/><path class="red" d="M266 80 q6 -8 12 0 q0 6 -6 8 v6"/><circle class="red fill" cx="272" cy="102" r="1.5"/>'''
S['06'] = '''<circle class="pencil" cx="160" cy="90" r="60"/><circle class="ink fill small" cx="160" cy="90" r="4"/>
<circle class="ink" cx="220" cy="90" r="20"/><path class="pencil" d="M160 90 L220 90"/>
<path class="red" d="M40 120 C90 110 110 70 150 66 C178 64 176 96 156 96 C136 96 140 64 172 60 C212 56 240 90 290 80"/>'''
S['07'] = '''<path class="ink" d="M60 40 C90 30 110 44 118 64 C126 86 116 104 104 124 C96 140 84 152 74 148 C70 128 56 112 54 92 C52 70 50 50 60 40 z"/>
<path class="ink" d="M200 34 C226 30 252 40 258 62 C264 88 250 108 236 128 C228 140 212 150 204 140 C200 120 190 110 186 92 C182 70 182 44 200 34 z"/>
<path class="red" d="M128 84 h52 M170 76 l10 8 -10 8 M138 76 l-10 8 10 8"/><path class="pencil dash" d="M150 20 v130"/>'''
S['08'] = '''<circle class="ink" cx="70" cy="86" r="34"/><path class="pencil" d="M40 76 q30 10 60 0 M38 92 q32 10 64 0"/>
<circle class="ink" cx="170" cy="86" r="16"/><circle class="ink" cx="232" cy="86" r="8"/><circle class="red" cx="280" cy="86" r="9"/>
<path class="red" d="M266 60 l28 52 M294 60 l-28 52"/><path class="pencil dash" d="M20 140 h290"/>'''
S['09'] = '''<circle class="red fill" cx="160" cy="86" r="8"/><ellipse class="ink" cx="160" cy="86" rx="90" ry="26"/>
<ellipse class="ink" cx="160" cy="86" rx="90" ry="26" transform="rotate(60 160 86)"/><ellipse class="ink" cx="160" cy="86" rx="90" ry="26" transform="rotate(-60 160 86)"/>
<circle class="ink fill small" cx="250" cy="86" r="5"/><circle class="ink fill small" cx="115" cy="51" r="5"/><circle class="ink fill small" cx="206" cy="48" r="5"/>'''
S['10'] = '''<path class="ink" d="M160 30 v116 M120 150 h80 M70 50 h180"/><path class="ink" d="M70 50 l-28 52 h56 z M250 50 l-28 52 h56 z"/>
<path class="pencil" d="M42 102 a28 12 0 0 0 56 0 M222 102 a28 12 0 0 0 56 0"/><circle class="ink" cx="160" cy="30" r="6"/>
<path class="red" d="M58 92 h24 M70 80 v24"/><path class="red" d="M236 92 h28"/>'''
S['11'] = '''<rect class="pencil" x="70" y="22" width="130" height="130" rx="4"/><path class="pencil" d="M86 50 h96 M86 68 h96 M86 86 h70 M86 104 h90 M86 122 h60"/>
<circle class="ink" cx="196" cy="94" r="38"/><path class="ink" d="M224 122 l46 40"/><path class="red" d="M178 86 h36"/>'''
S['12'] = '''<path class="ink" d="M100 20 v130 M30 85 h160"/><circle class="red fill" cx="70" cy="50" r="5"/><circle class="ink fill small" cx="140" cy="60" r="5"/>
<circle class="ink fill small" cx="128" cy="118" r="5"/><circle class="ink fill small" cx="62" cy="110" r="5"/>
<circle class="ink" cx="250" cy="85" r="44"/><path class="red fill" d="M250 47 l8 38 -8 38 -8 -38 z"/><path class="pencil" d="M206 85 h88 M250 41 v88"/>'''
