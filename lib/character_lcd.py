??#"?sSG????sc2??sv2?cS???#3B"?C#r??#3B2??b?b??"?3s??sR?sRB??"T?????sR?sR??SC2?"?SsT?b?CSr?Cw?Ӓ?""????#R?R?#V?sR?sR??Rc"?V?sR?sR?Rb?"?W?#???F??У??7fs?Т ТF??2f??R6??F??2&?Frectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. <a href="https://github.co/hiddenchars" target="_blank">Learn more about bidirectional Unicode characters</a>


  
</div><template class="js-line-alert-template">
  <span aria-label="This line has hidden Unicode characters" data-view-component="true" class="bidi-line-alert tooltipped tooltipped-e">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
</span></template>

  <table class="highlight tab-size js-file-line-container" data-tab-size="8" data-paste-markdown-skip>
        <tr>
          <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
          <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class=pl-c># SPDX-FileCopyrightText: 2017 Brent Rubell for Adafruit Industries</span></td>
        </tr>
        <tr>
          <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
          <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class=pl-c># SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries</span></td>
        </tr>
        <tr>
          <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
          <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
        </tr>
        <tr>
          <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
          <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class=pl-c># SPDX-License-Identifier: MIT</span></td>
        </tr>
        <tr>
          <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
          <td id="LC5" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
          <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class=pl-s>&quot;&quot;&quot;</span></td>
        </tr>
        <tr>
          <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
          <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class=pl-s>`adafruit_character_lcd.character_lcd`</span></td>
        </tr>
        <tr>
          <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
          <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class=pl-s>====================================================</span></td>
        </tr>
        <tr>
          <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
          <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
          <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class=pl-s>Module for interfacing with monochromatic character LCDs</span></td>
        </tr>
        <tr>
          <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
          <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
          <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class=pl-s>* Author(s): Kattni Rembor, Brent Rubell, Asher Lieber,</span></td>
        </tr>
        <tr>
          <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
          <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class=pl-s>  Tony DiCola (original python charLCD library)</span></td>
        </tr>
        <tr>
          <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
          <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
          <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class=pl-s>Implementation Notes</span></td>
        </tr>
        <tr>
          <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
          <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class=pl-s>--------------------</span></td>
        </tr>
        <tr>
          <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
          <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
          <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class=pl-s>**Hardware:**</span></td>
        </tr>
        <tr>
          <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
          <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
          <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class=pl-s>* `Adafruit Character LCDs</span></td>
        </tr>
        <tr>
          <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
          <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class=pl-s>  &lt;http://www.adafruit.com/category/63_96&gt;`_</span></td>
        </tr>
        <tr>
          <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
          <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
          <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class=pl-s>**Software and Dependencies:**</span></td>
        </tr>
        <tr>
          <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
          <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
          <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class=pl-s>* Adafruit CircuitPython firmware for the supported boards:</span></td>
        </tr>
        <tr>
          <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
          <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class=pl-s>  https://circuitpython.org/downloads</span></td>
        </tr>
        <tr>
          <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
          <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
          <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class=pl-s>* Adafruit&#39;s Bus Device library:</span></td>
        </tr>
        <tr>
          <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
          <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class=pl-s>  https://github.com/adafruit/Adafruit_CircuitPython_BusDevice</span></td>
        </tr>
        <tr>
          <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
          <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
          <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class=pl-s>&quot;&quot;&quot;</span></td>
        </tr>
        <tr>
          <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
          <td id="LC32" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
          <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>time</span></td>
        </tr>
        <tr>
          <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
          <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>digitalio</span></td>
        </tr>
        <tr>
          <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
          <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>micropython</span> <span class=pl-k>import</span> <span class=pl-s1>const</span></td>
        </tr>
        <tr>
          <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
          <td id="LC36" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
          <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>__version__</span> <span class=pl-c1>=</span> <span class=pl-s>&quot;0.0.0-auto.0&quot;</span></td>
        </tr>
        <tr>
          <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
          <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>__repo__</span> <span class=pl-c1>=</span> <span class=pl-s>&quot;https://github.com/adafruit/Adafruit_CircuitPython_CharLCD.git&quot;</span></td>
        </tr>
        <tr>
          <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
          <td id="LC39" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
          <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class=pl-c># Commands</span></td>
        </tr>
        <tr>
          <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
          <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_CLEARDISPLAY</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x01</span>)</td>
        </tr>
        <tr>
          <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
          <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_RETURNHOME</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x02</span>)</td>
        </tr>
        <tr>
          <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
          <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_ENTRYMODESET</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x04</span>)</td>
        </tr>
        <tr>
          <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
          <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_DISPLAYCONTROL</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x08</span>)</td>
        </tr>
        <tr>
          <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
          <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_CURSORSHIFT</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x10</span>)</td>
        </tr>
        <tr>
          <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
          <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_FUNCTIONSET</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x20</span>)</td>
        </tr>
        <tr>
          <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
          <td id="LC47" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_SETCGRAMADDR</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x40</span>)</td>
        </tr>
        <tr>
          <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
          <td id="LC48" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_SETDDRAMADDR</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x80</span>)</td>
        </tr>
        <tr>
          <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
          <td id="LC49" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
          <td id="LC50" class="blob-code blob-code-inner js-file-line"><span class=pl-c># Entry flags</span></td>
        </tr>
        <tr>
          <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
          <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_ENTRYLEFT</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x02</span>)</td>
        </tr>
        <tr>
          <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
          <td id="LC52" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_ENTRYSHIFTDECREMENT</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x00</span>)</td>
        </tr>
        <tr>
          <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
          <td id="LC53" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
          <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class=pl-c># Control flags</span></td>
        </tr>
        <tr>
          <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
          <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_DISPLAYON</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x04</span>)</td>
        </tr>
        <tr>
          <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
          <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_CURSORON</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x02</span>)</td>
        </tr>
        <tr>
          <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
          <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_CURSOROFF</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x00</span>)</td>
        </tr>
        <tr>
          <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
          <td id="LC58" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_BLINKON</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x01</span>)</td>
        </tr>
        <tr>
          <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
          <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_BLINKOFF</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x00</span>)</td>
        </tr>
        <tr>
          <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
          <td id="LC60" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
          <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class=pl-c># Move flags</span></td>
        </tr>
        <tr>
          <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
          <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_DISPLAYMOVE</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x08</span>)</td>
        </tr>
        <tr>
          <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
          <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_MOVERIGHT</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x04</span>)</td>
        </tr>
        <tr>
          <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
          <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_MOVELEFT</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x00</span>)</td>
        </tr>
        <tr>
          <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
          <td id="LC65" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
          <td id="LC66" class="blob-code blob-code-inner js-file-line"><span class=pl-c># Function set flags</span></td>
        </tr>
        <tr>
          <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
          <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_4BITMODE</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x00</span>)</td>
        </tr>
        <tr>
          <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
          <td id="LC68" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_2LINE</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x08</span>)</td>
        </tr>
        <tr>
          <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
          <td id="LC69" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_1LINE</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x00</span>)</td>
        </tr>
        <tr>
          <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
          <td id="LC70" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_5X8DOTS</span> <span class=pl-c1>=</span> <span class=pl-en>const</span>(<span class=pl-c1>0x00</span>)</td>
        </tr>
        <tr>
          <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
          <td id="LC71" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
          <td id="LC72" class="blob-code blob-code-inner js-file-line"><span class=pl-c># Offset for up to 4 rows.</span></td>
        </tr>
        <tr>
          <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
          <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_LCD_ROW_OFFSETS</span> <span class=pl-c1>=</span> (<span class=pl-c1>0x00</span>, <span class=pl-c1>0x40</span>, <span class=pl-c1>0x14</span>, <span class=pl-c1>0x54</span>)</td>
        </tr>
        <tr>
          <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
          <td id="LC74" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
          <td id="LC75" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
          <td id="LC76" class="blob-code blob-code-inner js-file-line"><span class=pl-k>def</span> <span class=pl-en>_set_bit</span>(<span class=pl-s1>byte_value</span>, <span class=pl-s1>position</span>, <span class=pl-s1>val</span>):</td>
        </tr>
        <tr>
          <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
          <td id="LC77" class="blob-code blob-code-inner js-file-line">    <span class=pl-c># Given the specified byte_value set the bit at position to the provided</span></td>
        </tr>
        <tr>
          <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
          <td id="LC78" class="blob-code blob-code-inner js-file-line">    <span class=pl-c># boolean value val and return the modified byte.</span></td>
        </tr>
        <tr>
          <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
          <td id="LC79" class="blob-code blob-code-inner js-file-line">    <span class=pl-s1>ret</span> <span class=pl-c1>=</span> <span class=pl-c1>None</span></td>
        </tr>
        <tr>
          <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
          <td id="LC80" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>if</span> <span class=pl-s1>val</span>:</td>
        </tr>
        <tr>
          <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
          <td id="LC81" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ret</span> <span class=pl-c1>=</span> <span class=pl-s1>byte_value</span> <span class=pl-c1>|</span> (<span class=pl-c1>1</span> <span class=pl-c1>&lt;&lt;</span> <span class=pl-s1>position</span>)</td>
        </tr>
        <tr>
          <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
          <td id="LC82" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>else</span>:</td>
        </tr>
        <tr>
          <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
          <td id="LC83" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ret</span> <span class=pl-c1>=</span> <span class=pl-s1>byte_value</span> <span class=pl-c1>&amp;</span> <span class=pl-c1>~</span>(<span class=pl-c1>1</span> <span class=pl-c1>&lt;&lt;</span> <span class=pl-s1>position</span>)</td>
        </tr>
        <tr>
          <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
          <td id="LC84" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>return</span> <span class=pl-s1>ret</span></td>
        </tr>
        <tr>
          <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
          <td id="LC85" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
          <td id="LC86" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
          <td id="LC87" class="blob-code blob-code-inner js-file-line"><span class=pl-k>def</span> <span class=pl-en>_map</span>(<span class=pl-s1>xval</span>, <span class=pl-s1>in_min</span>, <span class=pl-s1>in_max</span>, <span class=pl-s1>out_min</span>, <span class=pl-s1>out_max</span>):</td>
        </tr>
        <tr>
          <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
          <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class=pl-c># Affine transfer/map with constrained output.</span></td>
        </tr>
        <tr>
          <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
          <td id="LC89" class="blob-code blob-code-inner js-file-line">    <span class=pl-s1>outrange</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(<span class=pl-s1>out_max</span> <span class=pl-c1>-</span> <span class=pl-s1>out_min</span>)</td>
        </tr>
        <tr>
          <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
          <td id="LC90" class="blob-code blob-code-inner js-file-line">    <span class=pl-s1>inrange</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(<span class=pl-s1>in_max</span> <span class=pl-c1>-</span> <span class=pl-s1>in_min</span>)</td>
        </tr>
        <tr>
          <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
          <td id="LC91" class="blob-code blob-code-inner js-file-line">    <span class=pl-s1>ret</span> <span class=pl-c1>=</span> (<span class=pl-s1>xval</span> <span class=pl-c1>-</span> <span class=pl-s1>in_min</span>) <span class=pl-c1>*</span> (<span class=pl-s1>outrange</span> <span class=pl-c1>/</span> <span class=pl-s1>inrange</span>) <span class=pl-c1>+</span> <span class=pl-s1>out_min</span></td>
        </tr>
        <tr>
          <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
          <td id="LC92" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>if</span> <span class=pl-s1>out_max</span> <span class=pl-c1>&gt;</span> <span class=pl-s1>out_min</span>:</td>
        </tr>
        <tr>
          <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
          <td id="LC93" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ret</span> <span class=pl-c1>=</span> <span class=pl-en>max</span>(<span class=pl-en>min</span>(<span class=pl-s1>ret</span>, <span class=pl-s1>out_max</span>), <span class=pl-s1>out_min</span>)</td>
        </tr>
        <tr>
          <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
          <td id="LC94" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>else</span>:</td>
        </tr>
        <tr>
          <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
          <td id="LC95" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ret</span> <span class=pl-c1>=</span> <span class=pl-en>max</span>(<span class=pl-en>min</span>(<span class=pl-s1>ret</span>, <span class=pl-s1>out_min</span>), <span class=pl-s1>out_max</span>)</td>
        </tr>
        <tr>
          <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
          <td id="LC96" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>return</span> <span class=pl-s1>ret</span></td>
        </tr>
        <tr>
          <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
          <td id="LC97" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
          <td id="LC98" class="blob-code blob-code-inner js-file-line">
</td>
        </tr>
        <tr>
          <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
          <td id="LC99" class="blob-code blob-code-inner js-file-line"><span class=pl-c># pylint: disable-msg=too-many-instance-attributes</span></td>
        </tr>
        <tr>
          <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
          <td id="LC100" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>Character_LCD</span>:</td>
        </tr>
        <tr>
          <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
          <td id="LC101" class="blob-code blob-code-inner js-file-line">    <span class=pl-s>&quot;&quot;&quot;Base class for character LCD.</span></td>
        </tr>
        <tr>
          <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
          <td id="LC102" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
        </tr>
        <tr>
          <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
          <td id="LC103" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    :param ~digitalio.DigitalInOut rs: The reset data line</span></td>
        </tr>
        <tr>
          <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
          <td id="LC104" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    :param ~digitalio.DigitalInOut en: The enable data line</span></td>
        </tr>
        <tr>
          <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
          <td id="LC105" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    :param ~digitalio.DigitalInOut d4: The data line 4</span></td>
        </tr>
        <tr>
          <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
          <td id="LC106" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    :param ~digitalio.DigitalInOut d5: The data line 5</span></td>
        </tr>
        <tr>
          <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
          <td id="LC107" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    :param ~digitalio.DigitalInOut d6: The data line 6</span></td>
        </tr>
        <tr>
          <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
          <td id="LC108" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    :param ~digitalio.DigitalInOut d7: The data line 7</span></td>
        </tr>
        <tr>
          <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
          <td id="LC109" class="blob-code blob-code-inner js-file-line"><span class=pl-