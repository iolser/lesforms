(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4bec4152"],{1276:function(e,t,n){"use strict";var r=n("d784"),c=n("44e7"),o=n("825a"),a=n("1d80"),i=n("4840"),l=n("8aa5"),s=n("50c4"),d=n("14c3"),u=n("9263"),f=n("9f7f"),p=f.UNSUPPORTED_Y,b=[].push,g=Math.min,h=4294967295;r("split",2,(function(e,t,n){var r;return r="c"=="abbc".split(/(b)*/)[1]||4!="test".split(/(?:)/,-1).length||2!="ab".split(/(?:ab)*/).length||4!=".".split(/(.?)(.?)/).length||".".split(/()()/).length>1||"".split(/.?/).length?function(e,n){var r=String(a(this)),o=void 0===n?h:n>>>0;if(0===o)return[];if(void 0===e)return[r];if(!c(e))return t.call(r,e,o);var i,l,s,d=[],f=(e.ignoreCase?"i":"")+(e.multiline?"m":"")+(e.unicode?"u":"")+(e.sticky?"y":""),p=0,g=new RegExp(e.source,f+"g");while(i=u.call(g,r)){if(l=g.lastIndex,l>p&&(d.push(r.slice(p,i.index)),i.length>1&&i.index<r.length&&b.apply(d,i.slice(1)),s=i[0].length,p=l,d.length>=o))break;g.lastIndex===i.index&&g.lastIndex++}return p===r.length?!s&&g.test("")||d.push(""):d.push(r.slice(p)),d.length>o?d.slice(0,o):d}:"0".split(void 0,0).length?function(e,n){return void 0===e&&0===n?[]:t.call(this,e,n)}:t,[function(t,n){var c=a(this),o=void 0==t?void 0:t[e];return void 0!==o?o.call(t,c,n):r.call(String(c),t,n)},function(e,c){var a=n(r,e,this,c,r!==t);if(a.done)return a.value;var u=o(e),f=String(this),b=i(u,RegExp),v=u.unicode,m=(u.ignoreCase?"i":"")+(u.multiline?"m":"")+(u.unicode?"u":"")+(p?"g":"y"),O=new b(p?"^(?:"+u.source+")":u,m),j=void 0===c?h:c>>>0;if(0===j)return[];if(0===f.length)return null===d(O,f)?[f]:[];var y=0,k=0,x=[];while(k<f.length){O.lastIndex=p?0:k;var V,N=d(O,p?f.slice(k):f);if(null===N||(V=g(s(O.lastIndex+(p?k:0)),f.length))===y)k=l(f,k,v);else{if(x.push(f.slice(y,k)),x.length===j)return x;for(var B=1;B<=N.length-1;B++)if(x.push(N[B]),x.length===j)return x;k=y=V}}return x.push(f.slice(y)),x}]}),p)},"14c3":function(e,t,n){var r=n("c6b6"),c=n("9263");e.exports=function(e,t){var n=e.exec;if("function"===typeof n){var o=n.call(e,t);if("object"!==typeof o)throw TypeError("RegExp exec method returned something other than an Object or null");return o}if("RegExp"!==r(e))throw TypeError("RegExp#exec called on incompatible receiver");return c.call(e,t)}},"305a":function(e,t,n){"use strict";n("4ad1")},"44e7":function(e,t,n){var r=n("861d"),c=n("c6b6"),o=n("b622"),a=o("match");e.exports=function(e){var t;return r(e)&&(void 0!==(t=e[a])?!!t:"RegExp"==c(e))}},"498a":function(e,t,n){"use strict";var r=n("23e7"),c=n("58a8").trim,o=n("c8d2");r({target:"String",proto:!0,forced:o("trim")},{trim:function(){return c(this)}})},"4ad1":function(e,t,n){},"4b04":function(e,t,n){"use strict";n.r(t);n("b0c0");var r=n("7a23"),c=Object(r["withScopeId"])("data-v-1e37b5a7");Object(r["pushScopeId"])("data-v-1e37b5a7");var o={key:0,id:"responses",class:"box",style:{"overflow-x":"auto"}},a={class:"table is-striped is-hoverable is-fullwidth"},i=Object(r["createVNode"])("caption",{class:"title is-scrollable"}," Formulários da Plataforma ",-1),l=Object(r["createVNode"])("thead",null,[Object(r["createVNode"])("tr",null,[Object(r["createVNode"])("th",null," Formulário "),Object(r["createVNode"])("th",{align:"center",colspan:"2"}," Respostas "),Object(r["createVNode"])("th",{align:"center"}," Tipo "),Object(r["createVNode"])("th",{align:"center"}," Categoria "),Object(r["createVNode"])("th",{align:"center"}," Ativo "),Object(r["createVNode"])("th"),Object(r["createVNode"])("th"),Object(r["createVNode"])("th")])],-1),s={align:"right",class:"subtitle"},d={key:1},u={align:"left"},f=Object(r["createVNode"])("span",{class:"icon flex row vca",style:{"font-size":"1.2em"}},[Object(r["createVNode"])("i",{class:"fas fa-eye"})],-1),p={align:"right"},b={class:"select is-rounded is-fullwidth"},g={align:"right"},h={key:0,class:"select is-rounded is-fullwidth"},v=Object(r["createVNode"])("option",{disabled:""},null,-1),m={align:"center"},O={align:"center"},j=Object(r["createVNode"])("i",{class:"far fa-clone"},null,-1),y={align:"center"},k=Object(r["createVNode"])("i",{class:"fas fa-edit"},null,-1),x={align:"center"},V=Object(r["createVNode"])("i",{class:"fas fa-trash-alt"},null,-1),N=Object(r["createVNode"])("tr",null,[Object(r["createVNode"])("td",{colspan:"9",align:"center",class:"has-background-info-light"},[Object(r["createVNode"])("a",{class:"flex row ca width-100",href:"createForm"},"Criar novo formulário")])],-1);Object(r["popScopeId"])();var B=c((function(e,t,n,c,B,C){var E=Object(r["resolveComponent"])("Switch");return void 0!==B.forms&&void 0!==B.categories?(Object(r["openBlock"])(),Object(r["createBlock"])("div",o,[Object(r["createVNode"])("table",a,[i,l,Object(r["createVNode"])("tbody",null,[(Object(r["openBlock"])(!0),Object(r["createBlock"])(r["Fragment"],null,Object(r["renderList"])(B.forms,(function(e){return Object(r["openBlock"])(),Object(r["createBlock"])("tr",{key:e.id},[Object(r["createVNode"])("td",null,Object(r["toDisplayString"])(e.title),1),Object(r["createVNode"])("td",s,[e.responses>0?(Object(r["openBlock"])(),Object(r["createBlock"])("a",{key:0,class:" flex row vca ra\r\n              ",href:"responses/"+e.id},Object(r["toDisplayString"])(e.responses),9,["href"])):(Object(r["openBlock"])(),Object(r["createBlock"])("span",d,Object(r["toDisplayString"])(e.responses),1))]),Object(r["createVNode"])("td",u,[e.responses>0?(Object(r["openBlock"])(),Object(r["createBlock"])("a",{key:0,href:"responses/"+e.id},[f],8,["href"])):Object(r["createCommentVNode"])("",!0)]),Object(r["createVNode"])("td",p,[Object(r["createVNode"])("div",b,[Object(r["withDirectives"])(Object(r["createVNode"])("select",{"onUpdate:modelValue":function(t){return e.type=t},style:{color:"black"},disabled:e.signup_uses>0||e.feedback_uses>0||e.responses>0||e.category&&B.categories[e.category].formproposalid==e.id,onChange:function(t){return C.changeType(e.id,""==e.type?null:e.type)}},[(Object(r["openBlock"])(!0),Object(r["createBlock"])(r["Fragment"],null,Object(r["renderList"])(B.types,(function(e,t){return Object(r["openBlock"])(),Object(r["createBlock"])("option",{key:t,value:t,style:{"background-color":"white",color:"black"}},Object(r["toDisplayString"])(e.name),9,["value"])})),128))],40,["onUpdate:modelValue","disabled","onChange"]),[[r["vModelSelect"],e.type,void 0,{number:!0}]])])]),Object(r["createVNode"])("td",g,[2==e.type?(Object(r["openBlock"])(),Object(r["createBlock"])("div",h,[Object(r["withDirectives"])(Object(r["createVNode"])("select",{"onUpdate:modelValue":function(t){return e.category=t},style:{color:"black"},disabled:e.responses>0||e.category&&B.categories[e.category].formproposalid==e.id,onChange:function(t){return C.changeCategory(e.id,""==e.category?null:e.category)}},[v,(Object(r["openBlock"])(!0),Object(r["createBlock"])(r["Fragment"],null,Object(r["renderList"])(B.categories,(function(e,t){return Object(r["openBlock"])(),Object(r["createBlock"])("option",{key:t,value:t,style:{"background-color":"white",color:"black"}},Object(r["toDisplayString"])(e.name),9,["value"])})),128))],40,["onUpdate:modelValue","disabled","onChange"]),[[r["vModelSelect"],e.category,void 0,{number:!0}]])])):Object(r["createCommentVNode"])("",!0)]),Object(r["createVNode"])("td",m,[e.category&&2==e.type?(Object(r["openBlock"])(),Object(r["createBlock"])(E,{key:0,"model-value":e.category&&B.categories[e.category].formproposalid==e.id,disabled:e.category&&B.categories[e.category].formproposalid==e.id,loading:e.loading,"onUpdate:modelValue":function(t){e.loading=!0,C.changeActive(e.category,e.id,e.type,e)}},null,8,["model-value","disabled","loading","onUpdate:modelValue"])):Object(r["createCommentVNode"])("",!0)]),Object(r["createVNode"])("td",O,[Object(r["createVNode"])("a",{href:"duplicateForm/"+e.id},[j],8,["href"])]),Object(r["createVNode"])("td",y,[Object(r["createVNode"])("a",{href:"createForm/"+e.id},[k],8,["href"])]),Object(r["createVNode"])("td",x,[0!=e.responses||e.category&&B.categories[e.category].formproposalid==e.id?Object(r["createCommentVNode"])("",!0):(Object(r["openBlock"])(),Object(r["createBlock"])("a",{key:0,href:"#delete",onClick:function(t){return C.remove(e.id)}},[V],8,["onClick"]))])])})),128)),N])])])):Object(r["createCommentVNode"])("",!0)})),C=(n("d3b7"),n("3ca3"),n("ddb0"),n("4de4"),n("99af"),n("ac1f"),n("1276"),n("498a"),n("75c6")),E=n("c427"),R={name:"CreateResponse",components:{Switch:C["a"]},data:function(){return{forms:void 0,categories:void 0,types:void 0}},created:function(){var e=this;Promise.all([E["a"].get("formType/").then((function(t){return e.types=t.data})),E["a"].get("form/").then((function(t){return e.forms=t.data})),E["a"].get("eventType/").then((function(t){return e.categories=t.data}))]).then((function(){e.loading=!1}))},methods:{remove:function(e){if(confirm("De certeza que quer eliminar este formulário?")){this.forms=this.forms.filter((function(t){return t.id!=e}));var t={method:"delete",url:"/form/"+e+"/",headers:{"X-CSRFToken":this.getCookie("csrftoken")}};Object(E["a"])(t)}},changeCategory:function(e,t){var n=this,r={method:"patch",url:"/form/"+e+"/",headers:{"X-CSRFToken":this.getCookie("csrftoken")},data:{category:t},transformResponse:[function(e){return n.response=e,e}]};Object(E["a"])(r)},changeType:function(e,t){var n=this,r={method:"patch",url:"/form/"+e+"/",headers:{"X-CSRFToken":this.getCookie("csrftoken")},data:{type:t},transformResponse:[function(e){return n.response=e,e}]};Object(E["a"])(r)},changeActive:function(e,t,n,r){var c=this,o="Deseja ativar este formulário?";if(this.categories[e].formproposalid&&(o=o.concat(" Já existe um formulário ativo para esta categoria.")),confirm(o)){var a;1==n?a={formsignupid:t}:2==n?a={formproposalid:t}:3==n&&(a={formfeedbackid:t});var i={method:"patch",url:"/eventType/"+e+"/",headers:{"X-CSRFToken":this.getCookie("csrftoken")},data:a,transformResponse:[function(e){return c.response=e,r.loading=void 0,e}]};Object(E["a"])(i).then((function(){E["a"].get("eventType/").then((function(e){return c.categories=e.data}))}))}else r.loading=void 0},getCookie:function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),r=0;r<n.length;r++){var c=n[r].trim();if(c.substring(0,e.length+1)===e+"="){t=decodeURIComponent(c.substring(e.length+1));break}}return t}}};n("305a");R.render=B,R.__scopeId="data-v-1e37b5a7";t["default"]=R},"4de4":function(e,t,n){"use strict";var r=n("23e7"),c=n("b727").filter,o=n("1dde"),a=o("filter");r({target:"Array",proto:!0,forced:!a},{filter:function(e){return c(this,e,arguments.length>1?arguments[1]:void 0)}})},5899:function(e,t){e.exports="\t\n\v\f\r                　\u2028\u2029\ufeff"},"58a8":function(e,t,n){var r=n("1d80"),c=n("5899"),o="["+c+"]",a=RegExp("^"+o+o+"*"),i=RegExp(o+o+"*$"),l=function(e){return function(t){var n=String(r(t));return 1&e&&(n=n.replace(a,"")),2&e&&(n=n.replace(i,"")),n}};e.exports={start:l(1),end:l(2),trim:l(3)}},"6f91":function(e,t,n){"use strict";n("c72f")},"75c6":function(e,t,n){"use strict";var r=n("7a23"),c={class:"level la is-mobile"},o={class:"level-left ca"},a={key:0,class:"loader",style:{width:"30px",height:"30px"}},i={key:1,class:"switch"},l=Object(r["createVNode"])("span",{class:"slider round"},null,-1);function s(e,t,n,s,d,u){var f=this;return Object(r["openBlock"])(),Object(r["createBlock"])("div",c,[Object(r["createVNode"])("div",o,[n.loading?(Object(r["openBlock"])(),Object(r["createBlock"])("span",a)):(Object(r["openBlock"])(),Object(r["createBlock"])("label",i,[Object(r["createVNode"])("input",{id:"switch_component_"+d.id,value:n.modelValue,class:{checked:n.modelValue,disabled:n.disabled},disabled:n.disabled,type:"checkbox",onChange:t[1]||(t[1]=function(e){f.$emit("update:modelValue",!f.modelValue)})},null,42,["id","value","disabled"]),l])),n.text&&!n.loading?(Object(r["openBlock"])(),Object(r["createBlock"])("label",{key:2,class:"ml-3 is-unselectable is-clickable",for:"switch_component_"+d.id},Object(r["toDisplayString"])(n.text),9,["for"])):Object(r["createCommentVNode"])("",!0)])])}var d={name:"Switch",props:["modelValue","text","disabled","loading"],data:function(){return{id:this.$store.getters.getUidSeq}}};n("6f91");d.render=s;t["a"]=d},"8aa5":function(e,t,n){"use strict";var r=n("6547").charAt;e.exports=function(e,t,n){return t+(n?r(e,t).length:1)}},9263:function(e,t,n){"use strict";var r=n("ad6d"),c=n("9f7f"),o=n("5692"),a=RegExp.prototype.exec,i=o("native-string-replace",String.prototype.replace),l=a,s=function(){var e=/a/,t=/b*/g;return a.call(e,"a"),a.call(t,"a"),0!==e.lastIndex||0!==t.lastIndex}(),d=c.UNSUPPORTED_Y||c.BROKEN_CARET,u=void 0!==/()??/.exec("")[1],f=s||u||d;f&&(l=function(e){var t,n,c,o,l=this,f=d&&l.sticky,p=r.call(l),b=l.source,g=0,h=e;return f&&(p=p.replace("y",""),-1===p.indexOf("g")&&(p+="g"),h=String(e).slice(l.lastIndex),l.lastIndex>0&&(!l.multiline||l.multiline&&"\n"!==e[l.lastIndex-1])&&(b="(?: "+b+")",h=" "+h,g++),n=new RegExp("^(?:"+b+")",p)),u&&(n=new RegExp("^"+b+"$(?!\\s)",p)),s&&(t=l.lastIndex),c=a.call(f?n:l,h),f?c?(c.input=c.input.slice(g),c[0]=c[0].slice(g),c.index=l.lastIndex,l.lastIndex+=c[0].length):l.lastIndex=0:s&&c&&(l.lastIndex=l.global?c.index+c[0].length:t),u&&c&&c.length>1&&i.call(c[0],n,(function(){for(o=1;o<arguments.length-2;o++)void 0===arguments[o]&&(c[o]=void 0)})),c}),e.exports=l},"9f7f":function(e,t,n){"use strict";var r=n("d039");function c(e,t){return RegExp(e,t)}t.UNSUPPORTED_Y=r((function(){var e=c("a","y");return e.lastIndex=2,null!=e.exec("abcd")})),t.BROKEN_CARET=r((function(){var e=c("^r","gy");return e.lastIndex=2,null!=e.exec("str")}))},ac1f:function(e,t,n){"use strict";var r=n("23e7"),c=n("9263");r({target:"RegExp",proto:!0,forced:/./.exec!==c},{exec:c})},ad6d:function(e,t,n){"use strict";var r=n("825a");e.exports=function(){var e=r(this),t="";return e.global&&(t+="g"),e.ignoreCase&&(t+="i"),e.multiline&&(t+="m"),e.dotAll&&(t+="s"),e.unicode&&(t+="u"),e.sticky&&(t+="y"),t}},b0c0:function(e,t,n){var r=n("83ab"),c=n("9bf2").f,o=Function.prototype,a=o.toString,i=/^\s*function ([^ (]*)/,l="name";r&&!(l in o)&&c(o,l,{configurable:!0,get:function(){try{return a.call(this).match(i)[1]}catch(e){return""}}})},c72f:function(e,t,n){},c8d2:function(e,t,n){var r=n("d039"),c=n("5899"),o="​᠎";e.exports=function(e){return r((function(){return!!c[e]()||o[e]()!=o||c[e].name!==e}))}},d784:function(e,t,n){"use strict";n("ac1f");var r=n("6eeb"),c=n("9263"),o=n("d039"),a=n("b622"),i=n("9112"),l=a("species"),s=RegExp.prototype,d=!o((function(){var e=/./;return e.exec=function(){var e=[];return e.groups={a:"7"},e},"7"!=="".replace(e,"$<a>")})),u=function(){return"$0"==="a".replace(/./,"$0")}(),f=a("replace"),p=function(){return!!/./[f]&&""===/./[f]("a","$0")}(),b=!o((function(){var e=/(?:)/,t=e.exec;e.exec=function(){return t.apply(this,arguments)};var n="ab".split(e);return 2!==n.length||"a"!==n[0]||"b"!==n[1]}));e.exports=function(e,t,n,f){var g=a(e),h=!o((function(){var t={};return t[g]=function(){return 7},7!=""[e](t)})),v=h&&!o((function(){var t=!1,n=/a/;return"split"===e&&(n={},n.constructor={},n.constructor[l]=function(){return n},n.flags="",n[g]=/./[g]),n.exec=function(){return t=!0,null},n[g](""),!t}));if(!h||!v||"replace"===e&&(!d||!u||p)||"split"===e&&!b){var m=/./[g],O=n(g,""[e],(function(e,t,n,r,o){var a=t.exec;return a===c||a===s.exec?h&&!o?{done:!0,value:m.call(t,n,r)}:{done:!0,value:e.call(n,t,r)}:{done:!1}}),{REPLACE_KEEPS_$0:u,REGEXP_REPLACE_SUBSTITUTES_UNDEFINED_CAPTURE:p}),j=O[0],y=O[1];r(String.prototype,e,j),r(s,g,2==t?function(e,t){return y.call(e,this,t)}:function(e){return y.call(e,this)})}f&&i(s[g],"sham",!0)}}}]);
//# sourceMappingURL=chunk-4bec4152.57e9d438.js.map