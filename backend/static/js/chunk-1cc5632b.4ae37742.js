(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1cc5632b"],{"0cb2":function(e,t,n){var r=n("7b0b"),o=Math.floor,i="".replace,c=/\$([$&'`]|\d{1,2}|<[^>]*>)/g,a=/\$([$&'`]|\d{1,2})/g;e.exports=function(e,t,n,s,u,l){var d=n+e.length,f=s.length,p=a;return void 0!==u&&(u=r(u),p=c),i.call(l,p,(function(r,i){var c;switch(i.charAt(0)){case"$":return"$";case"&":return e;case"`":return t.slice(0,n);case"'":return t.slice(d);case"<":c=u[i.slice(1,-1)];break;default:var a=+i;if(0===a)return r;if(a>f){var l=o(a/10);return 0===l?r:l<=f?void 0===s[l-1]?i.charAt(1):s[l-1]+i.charAt(1):r}c=s[a-1]}return void 0===c?"":c}))}},1276:function(e,t,n){"use strict";var r=n("d784"),o=n("44e7"),i=n("825a"),c=n("1d80"),a=n("4840"),s=n("8aa5"),u=n("50c4"),l=n("14c3"),d=n("9263"),f=n("9f7f"),p=f.UNSUPPORTED_Y,h=[].push,m=Math.min,b=4294967295;r("split",2,(function(e,t,n){var r;return r="c"=="abbc".split(/(b)*/)[1]||4!="test".split(/(?:)/,-1).length||2!="ab".split(/(?:ab)*/).length||4!=".".split(/(.?)(.?)/).length||".".split(/()()/).length>1||"".split(/.?/).length?function(e,n){var r=String(c(this)),i=void 0===n?b:n>>>0;if(0===i)return[];if(void 0===e)return[r];if(!o(e))return t.call(r,e,i);var a,s,u,l=[],f=(e.ignoreCase?"i":"")+(e.multiline?"m":"")+(e.unicode?"u":"")+(e.sticky?"y":""),p=0,m=new RegExp(e.source,f+"g");while(a=d.call(m,r)){if(s=m.lastIndex,s>p&&(l.push(r.slice(p,a.index)),a.length>1&&a.index<r.length&&h.apply(l,a.slice(1)),u=a[0].length,p=s,l.length>=i))break;m.lastIndex===a.index&&m.lastIndex++}return p===r.length?!u&&m.test("")||l.push(""):l.push(r.slice(p)),l.length>i?l.slice(0,i):l}:"0".split(void 0,0).length?function(e,n){return void 0===e&&0===n?[]:t.call(this,e,n)}:t,[function(t,n){var o=c(this),i=void 0==t?void 0:t[e];return void 0!==i?i.call(t,o,n):r.call(String(o),t,n)},function(e,o){var c=n(r,e,this,o,r!==t);if(c.done)return c.value;var d=i(e),f=String(this),h=a(d,RegExp),v=d.unicode,g=(d.ignoreCase?"i":"")+(d.multiline?"m":"")+(d.unicode?"u":"")+(p?"g":"y"),x=new h(p?"^(?:"+d.source+")":d,g),O=void 0===o?b:o>>>0;if(0===O)return[];if(0===f.length)return null===l(x,f)?[f]:[];var j=0,y=0,_=[];while(y<f.length){x.lastIndex=p?0:y;var k,w=l(x,p?f.slice(y):f);if(null===w||(k=m(u(x.lastIndex+(p?y:0)),f.length))===j)y=s(f,y,v);else{if(_.push(f.slice(j,y)),_.length===O)return _;for(var S=1;S<=w.length-1;S++)if(_.push(w[S]),_.length===O)return _;y=j=k}}return _.push(f.slice(j)),_}]}),p)},"14c3":function(e,t,n){var r=n("c6b6"),o=n("9263");e.exports=function(e,t){var n=e.exec;if("function"===typeof n){var i=n.call(e,t);if("object"!==typeof i)throw TypeError("RegExp exec method returned something other than an Object or null");return i}if("RegExp"!==r(e))throw TypeError("RegExp#exec called on incompatible receiver");return o.call(e,t)}},2532:function(e,t,n){"use strict";var r=n("23e7"),o=n("5a34"),i=n("1d80"),c=n("ab13");r({target:"String",proto:!0,forced:!c("includes")},{includes:function(e){return!!~String(i(this)).indexOf(o(e),arguments.length>1?arguments[1]:void 0)}})},"44e7":function(e,t,n){var r=n("861d"),o=n("c6b6"),i=n("b622"),c=i("match");e.exports=function(e){var t;return r(e)&&(void 0!==(t=e[c])?!!t:"RegExp"==o(e))}},"498a":function(e,t,n){"use strict";var r=n("23e7"),o=n("58a8").trim,i=n("c8d2");r({target:"String",proto:!0,forced:i("trim")},{trim:function(){return o(this)}})},5319:function(e,t,n){"use strict";var r=n("d784"),o=n("825a"),i=n("50c4"),c=n("a691"),a=n("1d80"),s=n("8aa5"),u=n("0cb2"),l=n("14c3"),d=Math.max,f=Math.min,p=function(e){return void 0===e?e:String(e)};r("replace",2,(function(e,t,n,r){var h=r.REGEXP_REPLACE_SUBSTITUTES_UNDEFINED_CAPTURE,m=r.REPLACE_KEEPS_$0,b=h?"$":"$0";return[function(n,r){var o=a(this),i=void 0==n?void 0:n[e];return void 0!==i?i.call(n,o,r):t.call(String(o),n,r)},function(e,r){if(!h&&m||"string"===typeof r&&-1===r.indexOf(b)){var a=n(t,e,this,r);if(a.done)return a.value}var v=o(e),g=String(this),x="function"===typeof r;x||(r=String(r));var O=v.global;if(O){var j=v.unicode;v.lastIndex=0}var y=[];while(1){var _=l(v,g);if(null===_)break;if(y.push(_),!O)break;var k=String(_[0]);""===k&&(v.lastIndex=s(g,i(v.lastIndex),j))}for(var w="",S=0,E=0;E<y.length;E++){_=y[E];for(var N=String(_[0]),I=d(f(c(_.index),g.length),0),R=[],B=1;B<_.length;B++)R.push(p(_[B]));var q=_.groups;if(x){var T=[N].concat(R,I,g);void 0!==q&&T.push(q);var V=String(r.apply(void 0,T))}else V=u(N,g,I,R,q,r);I>=S&&(w+=g.slice(S,I)+V,S=I+N.length)}return w+g.slice(S)}]}))},"5a34":function(e,t,n){var r=n("44e7");e.exports=function(e){if(r(e))throw TypeError("The method doesn't accept regular expressions");return e}},"69d9":function(e,t,n){"use strict";n.d(t,"b",(function(){return o})),n.d(t,"e",(function(){return i})),n.d(t,"c",(function(){return c})),n.d(t,"d",(function(){return a})),n.d(t,"a",(function(){return l}));n("a4d3"),n("e01a"),n("d3b7"),n("d28b"),n("3ca3"),n("ddb0");function r(e){return r="function"===typeof Symbol&&"symbol"===typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"===typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},r(e)}n("ac1f"),n("1276"),n("498a"),n("caad"),n("2532"),n("a434"),n("5319");function o(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),r=0;r<n.length;r++){var o=n[r].trim();if(o.substring(0,e.length+1)===e+"="){t=decodeURIComponent(o.substring(e.length+1));break}}return t}function i(e){"object"!==r(e)&&(e=new Date(e));var t,n=Math.floor((new Date-e)/1e3),o=Math.floor(n/31536e3);return o>=1?t="ano":(o=Math.floor(n/2592e3),o>=1?t="mês":(o=Math.floor(n/86400),o>=1?t="dia":(o=Math.floor(n/3600),o>=1?t="hora":(o=Math.floor(n/60),o>=1?t="minuto":(o=n,t="segundo"))))),(o>1||0===o)&&("mês"==t?t="meses":t+="s"),o+" "+t}function c(e){for(var t=0;t<e.form.sections.length;t++)for(var n=0;n<e.form.sections[t].questions.length;)e.form.sections[t].questions[n].properties.field_type.includes("_exposition")?e.form.sections[t].questions.splice(n,1):n++;return e}function a(e,t){return-1!=e.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").indexOf(t.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,""))}function s(e,t,n,r){for(var o=0;o<e.answer.length;o++){var i=e.answer[o];i===parseInt(i,10)?e.answer[o]=t.form.sections[n].questions[r].properties.options[i]:e.answer[o]='Outro: "'+e.answer+'"'}}function u(e,t,n,r){e.answer===parseInt(e.answer,10)?e.answer=t.form.sections[n].questions[r].properties.options[e.answer]:e.answer='Outro: "'+e.answer+'"'}function l(e,t){for(var n=0;n<e.length;n++)for(var r=e[n],o=0;o<r.content.sections.length;o++)for(var i=r.content.sections[o],c=0;c<i.length;c++){var a=i[c];void 0!==a.answer&&("selectboxes"==a.field_type?s(a,t,o,c):"multiplechoice"==a.field_type?u(a,t,o,c):"date"==a.field_type?a.answer=new Date(a.answer).toLocaleDateString():"datetime"==a.field_type&&(a.answer=new Date(a.answer).toLocaleString()))}return e}},"8aa5":function(e,t,n){"use strict";var r=n("6547").charAt;e.exports=function(e,t,n){return t+(n?r(e,t).length:1)}},"91ba":function(e,t,n){"use strict";n.r(t);n("b0c0");var r=n("7a23"),o=Object(r["withScopeId"])("data-v-0d9e649c");Object(r["pushScopeId"])("data-v-0d9e649c");var i={key:0,class:"box"},c={ref:"formtitle",class:"title"},a=Object(r["createVNode"])("hr",null,null,-1),s={class:"steps has-content-centered mb-0"},u={class:"steps-marker"},l={class:"steps-content"},d={class:"steps-marker"},f=Object(r["createVNode"])("div",{class:"steps-content"},[Object(r["createVNode"])("p",null," Concluída ")],-1),p={key:0,class:"box"},h={key:0},m={key:0,class:"mt-4 mb-4",style:{width:"100%",height:"1px","background-color":"#ddd"}};Object(r["popScopeId"])();var b=o((function(e,t,n,o,b,v){var g=Object(r["resolveComponent"])("Submit");return b.api_data&&b.event&&b.form?(Object(r["openBlock"])(),Object(r["createBlock"])("div",i,[Object(r["createVNode"])("h1",c,[Object(r["createTextVNode"])(Object(r["toDisplayString"])(b.api_data.title),1),b.event?(Object(r["openBlock"])(),Object(r["createBlock"])(r["Fragment"],{key:0},[Object(r["createTextVNode"])(" ("+Object(r["toDisplayString"])(b.event.name)+") ",1)],64)):Object(r["createCommentVNode"])("",!0)],512),a,Object(r["createVNode"])("form",{id:"form-area",class:"flex column",method:"post",onSubmit:t[3]||(t[3]=Object(r["withModifiers"])((function(){return v.submit&&v.submit.apply(v,arguments)}),["prevent"]))},[Object(r["createVNode"])("ul",s,[(Object(r["openBlock"])(!0),Object(r["createBlock"])(r["Fragment"],null,Object(r["renderList"])(b.api_data.form.sections,(function(e,t){return Object(r["openBlock"])(),Object(r["createBlock"])("li",{key:e.id,class:["steps-segment is-primary",{"is-active":b.section==t,"has-gaps":b.section<=t}]},[Object(r["createVNode"])("span",u,[b.api_data.form.hide_section_numbers?Object(r["createCommentVNode"])("",!0):(Object(r["openBlock"])(),Object(r["createBlock"])(r["Fragment"],{key:0},[Object(r["createTextVNode"])(Object(r["toDisplayString"])(t+1),1)],64))]),Object(r["createVNode"])("div",l,[Object(r["createVNode"])("p",{class:{"has-text-weight-bold":b.section==t}},Object(r["toDisplayString"])(e.section_name),3)])],2)})),128)),Object(r["createVNode"])("li",{class:["steps-segment is-primary",{"is-active":b.section==b.api_data.form.sections.length}]},[Object(r["createVNode"])("span",d,[b.api_data.form.hide_section_numbers?Object(r["createCommentVNode"])("",!0):(Object(r["openBlock"])(),Object(r["createBlock"])(r["Fragment"],{key:0},[Object(r["createTextVNode"])(Object(r["toDisplayString"])(b.api_data.form.sections.length+1),1)],64))]),f],2)]),b.section<b.api_data.form.sections.length?(Object(r["openBlock"])(),Object(r["createBlock"])("div",p,[(Object(r["openBlock"])(!0),Object(r["createBlock"])(r["Fragment"],null,Object(r["renderList"])(b.api_data.form.sections[b.section].questions,(function(t,n){return Object(r["openBlock"])(),Object(r["createBlock"])("div",{key:t.id,set:e.qid="s"+b.section+"_q"+n},[Object(r["createVNode"])("label",{class:["label",{required:t.required}],for:e.qid},[b.api_data.form.hide_question_numbers||b.api_data.form.sections[b.section].hide_question_numbers?Object(r["createCommentVNode"])("",!0):(Object(r["openBlock"])(),Object(r["createBlock"])("span",h,Object(r["toDisplayString"])(n+1)+". ",1)),Object(r["createTextVNode"])(Object(r["toDisplayString"])(t.question),1)],10,["for"]),(Object(r["openBlock"])(),Object(r["createBlock"])(Object(r["resolveDynamicComponent"])(t.properties.field_type),{question:t,"question-index":n,"section-index":b.section,value:b.form.content.sections[b.section][n].answer,qid:e.qid,onUpdate:v.updateAnswer},null,8,["question","question-index","section-index","value","qid","onUpdate"])),n<b.api_data.form.sections[b.section].questions.length-1?(Object(r["openBlock"])(),Object(r["createBlock"])("hr",m)):Object(r["createCommentVNode"])("",!0)],8,["set"])})),128))])):(Object(r["openBlock"])(),Object(r["createBlock"])("div",{key:1,innerHTML:b.api_data.submit_message},null,8,["innerHTML"])),Object(r["createVNode"])(g,{error:b.response&&void 0===b.response.id,"error-message":"Houve um erro na submissão do formulário.","success-duration":"3000","success-message":b.success,loading:b.loading,"submit-text":b.section<b.api_data.form.sections.length-1?"Seguinte":"Submeter","cancel-text":b.section>0?"Anterior":"Sair","cancel-confirmation":0==b.section?"Deseja sair? <b>A sua resposta não será guardada.</br>":void 0,"cancel-conf-button":"Sair",hide:b.section==b.api_data.form.sections.length,onLeave:t[1]||(t[1]=function(e){return v.leave()}),onDismissed:t[2]||(t[2]=function(e){b.response=void 0,b.success=void 0})},null,8,["error","success-message","loading","submit-text","cancel-text","cancel-confirmation","hide"]),Object(r["createCommentVNode"])("",!0)],32)])):Object(r["createCommentVNode"])("",!0)})),v=n("1da1"),g=(n("96cf"),n("d3b7"),n("3ca3"),n("ddb0"),n("99af"),n("3f6f")),x=n("c427"),O=n("69d9"),j=n("1995"),y={name:"CreateResponse",components:Object.assign({},{Submit:j["a"]},g),data:function(){return{api_data:void 0,form:void 0,response:void 0,event:void 0,section:0,success:void 0,loading:!1}},created:function(){var e=this;return Object(v["a"])(regeneratorRuntime.mark((function t(){var n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Promise.all([x["a"].get("form/".concat(e.$route.params.id)).then((function(t){return e.api_data=t.data})),x["a"].get("event/".concat(e.$route.query.event)).then((function(t){return e.event=t.data}))]);case 2:if(null===(n=e.$route.query)||void 0===n||!n.edit){t.next=7;break}return t.next=5,x["a"].get("formAnswer/".concat(e.$route.query.edit)).then((function(t){return e.form=t.data}));case 5:t.next=8;break;case 7:e.form={content:{sections:[]},form:e.api_data.id,event:e.event.id};case 8:e.initializeData();case 9:case"end":return t.stop()}}),t)})))()},methods:{leave:function(){var e=this;this.section>0?(this.section--,this.$nextTick((function(){return e.$refs["formtitle"].scrollIntoView({behavior:"smooth"})}))):location.href="/forms"},submit:function(){var e=this;if(this.section<this.api_data.form.sections.length-1)this.section++,this.$nextTick((function(){return e.$refs["formtitle"].scrollIntoView({behavior:"smooth"})}));else{var t,n,r;this.loading=!0,void 0===this.form.id?(t="post",n="/formAnswer/",r="A resposta foi enviada com sucesso."):(t="put",n="/formAnswer/".concat(this.form.id).concat("/"),r="A resposta foi editada com sucesso.");var o={method:t,url:n,headers:{"X-CSRFToken":Object(O["b"])("csrftoken")},data:this.form,transformResponse:[function(){var t=Object(v["a"])(regeneratorRuntime.mark((function t(n){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:e.loading=void 0;try{e.response=JSON.parse(n),e.form=e.response,e.success=r,e.section++}catch(o){e.response=n}return t.abrupt("return",e.response);case 3:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}()]};Object(x["a"])(o)}},updateAnswer:function(e){this.form.content.sections[e.sectionIndex][e.questionIndex]["answer"]=e["answer"]},initializeData:function(){for(var e in this.api_data.form.sections)for(var t in this.form.content.sections[e]=[],this.api_data.form.sections[e].questions)this.form.content.sections[e][t]={field_type:this.api_data.form.sections[e].questions[t].properties["field_type"]}}}};n("a3cf");y.render=b,y.__scopeId="data-v-0d9e649c";t["default"]=y},9263:function(e,t,n){"use strict";var r=n("ad6d"),o=n("9f7f"),i=n("5692"),c=RegExp.prototype.exec,a=i("native-string-replace",String.prototype.replace),s=c,u=function(){var e=/a/,t=/b*/g;return c.call(e,"a"),c.call(t,"a"),0!==e.lastIndex||0!==t.lastIndex}(),l=o.UNSUPPORTED_Y||o.BROKEN_CARET,d=void 0!==/()??/.exec("")[1],f=u||d||l;f&&(s=function(e){var t,n,o,i,s=this,f=l&&s.sticky,p=r.call(s),h=s.source,m=0,b=e;return f&&(p=p.replace("y",""),-1===p.indexOf("g")&&(p+="g"),b=String(e).slice(s.lastIndex),s.lastIndex>0&&(!s.multiline||s.multiline&&"\n"!==e[s.lastIndex-1])&&(h="(?: "+h+")",b=" "+b,m++),n=new RegExp("^(?:"+h+")",p)),d&&(n=new RegExp("^"+h+"$(?!\\s)",p)),u&&(t=s.lastIndex),o=c.call(f?n:s,b),f?o?(o.input=o.input.slice(m),o[0]=o[0].slice(m),o.index=s.lastIndex,s.lastIndex+=o[0].length):s.lastIndex=0:u&&o&&(s.lastIndex=s.global?o.index+o[0].length:t),d&&o&&o.length>1&&a.call(o[0],n,(function(){for(i=1;i<arguments.length-2;i++)void 0===arguments[i]&&(o[i]=void 0)})),o}),e.exports=s},9342:function(e,t,n){},"9f7f":function(e,t,n){"use strict";var r=n("d039");function o(e,t){return RegExp(e,t)}t.UNSUPPORTED_Y=r((function(){var e=o("a","y");return e.lastIndex=2,null!=e.exec("abcd")})),t.BROKEN_CARET=r((function(){var e=o("^r","gy");return e.lastIndex=2,null!=e.exec("str")}))},a3cf:function(e,t,n){"use strict";n("9342")},ab13:function(e,t,n){var r=n("b622"),o=r("match");e.exports=function(e){var t=/./;try{"/./"[e](t)}catch(n){try{return t[o]=!1,"/./"[e](t)}catch(r){}}return!1}},ac1f:function(e,t,n){"use strict";var r=n("23e7"),o=n("9263");r({target:"RegExp",proto:!0,forced:/./.exec!==o},{exec:o})},b0c0:function(e,t,n){var r=n("83ab"),o=n("9bf2").f,i=Function.prototype,c=i.toString,a=/^\s*function ([^ (]*)/,s="name";r&&!(s in i)&&o(i,s,{configurable:!0,get:function(){try{return c.call(this).match(a)[1]}catch(e){return""}}})},c8d2:function(e,t,n){var r=n("d039"),o=n("5899"),i="​᠎";e.exports=function(e){return r((function(){return!!o[e]()||i[e]()!=i||o[e].name!==e}))}},d784:function(e,t,n){"use strict";n("ac1f");var r=n("6eeb"),o=n("9263"),i=n("d039"),c=n("b622"),a=n("9112"),s=c("species"),u=RegExp.prototype,l=!i((function(){var e=/./;return e.exec=function(){var e=[];return e.groups={a:"7"},e},"7"!=="".replace(e,"$<a>")})),d=function(){return"$0"==="a".replace(/./,"$0")}(),f=c("replace"),p=function(){return!!/./[f]&&""===/./[f]("a","$0")}(),h=!i((function(){var e=/(?:)/,t=e.exec;e.exec=function(){return t.apply(this,arguments)};var n="ab".split(e);return 2!==n.length||"a"!==n[0]||"b"!==n[1]}));e.exports=function(e,t,n,f){var m=c(e),b=!i((function(){var t={};return t[m]=function(){return 7},7!=""[e](t)})),v=b&&!i((function(){var t=!1,n=/a/;return"split"===e&&(n={},n.constructor={},n.constructor[s]=function(){return n},n.flags="",n[m]=/./[m]),n.exec=function(){return t=!0,null},n[m](""),!t}));if(!b||!v||"replace"===e&&(!l||!d||p)||"split"===e&&!h){var g=/./[m],x=n(m,""[e],(function(e,t,n,r,i){var c=t.exec;return c===o||c===u.exec?b&&!i?{done:!0,value:g.call(t,n,r)}:{done:!0,value:e.call(n,t,r)}:{done:!1}}),{REPLACE_KEEPS_$0:d,REGEXP_REPLACE_SUBSTITUTES_UNDEFINED_CAPTURE:p}),O=x[0],j=x[1];r(String.prototype,e,O),r(u,m,2==t?function(e,t){return j.call(e,this,t)}:function(e){return j.call(e,this)})}f&&a(u[m],"sham",!0)}}}]);
//# sourceMappingURL=chunk-1cc5632b.4ae37742.js.map