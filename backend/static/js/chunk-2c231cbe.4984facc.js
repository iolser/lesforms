(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2c231cbe"],{2532:function(e,t,o){"use strict";var n=o("23e7"),c=o("5a34"),s=o("1d80"),r=o("ab13");n({target:"String",proto:!0,forced:!r("includes")},{includes:function(e){return!!~String(s(this)).indexOf(c(e),arguments.length>1?arguments[1]:void 0)}})},"44e7":function(e,t,o){var n=o("861d"),c=o("c6b6"),s=o("b622"),r=s("match");e.exports=function(e){var t;return n(e)&&(void 0!==(t=e[r])?!!t:"RegExp"==c(e))}},"5a34":function(e,t,o){var n=o("44e7");e.exports=function(e){if(n(e))throw TypeError("The method doesn't accept regular expressions");return e}},ab13:function(e,t,o){var n=o("b622"),c=n("match");e.exports=function(e){var t=/./;try{"/./"[e](t)}catch(o){try{return t[c]=!1,"/./"[e](t)}catch(n){}}return!1}},f7c9:function(e,t,o){"use strict";o.r(t);var n=o("7a23"),c={class:"flex column ca"},s=Object(n["createVNode"])("hr",null,null,-1),r={key:0},a={key:0},i={key:1,class:"requiredticker"},l={key:0},p={key:0,class:"noanswer"},b={key:1},d={key:0},O={key:1},j={key:0,class:"noanswer"},u={key:1},f={key:2},k={key:0},m={key:2},h={key:3},B={key:4};function _(e,t,o,_,y,g){return Object(n["openBlock"])(),Object(n["createBlock"])("div",null,[Object(n["createVNode"])("h1",null,Object(n["toDisplayString"])(y.api_data.title),1),Object(n["createVNode"])("div",c,[(Object(n["openBlock"])(!0),Object(n["createBlock"])(n["Fragment"],null,Object(n["renderList"])(y.api_data.form.sections,(function(t,o){return Object(n["openBlock"])(),Object(n["createBlock"])("div",{key:o},[s,Object(n["createVNode"])("h2",null,[y.api_data.form.hide_section_numbers?Object(n["createCommentVNode"])("",!0):(Object(n["openBlock"])(),Object(n["createBlock"])("span",r,Object(n["toDisplayString"])(o+1)+". ",1)),Object(n["createTextVNode"])(Object(n["toDisplayString"])(t.section_name),1)]),(Object(n["openBlock"])(!0),Object(n["createBlock"])(n["Fragment"],null,Object(n["renderList"])(t.questions,(function(c,s){return Object(n["openBlock"])(),Object(n["createBlock"])("div",{key:s,set:e.qid="s"+o+"_q"+s,class:"flex column ca vla no-bottom question"},[Object(n["createVNode"])("label",{class:"question-field",for:e.qid},[Object(n["createVNode"])("h3",null,[y.api_data.form.hide_question_numbers||t.hide_question_numbers?Object(n["createCommentVNode"])("",!0):(Object(n["openBlock"])(),Object(n["createBlock"])("span",a,Object(n["toDisplayString"])(s+1)+". ",1)),Object(n["createTextVNode"])(Object(n["toDisplayString"])(c.question)+" ",1),c.required?(Object(n["openBlock"])(),Object(n["createBlock"])("span",i,"*")):Object(n["createCommentVNode"])("",!0)])],8,["for"]),"selectboxes"==c.properties.field_type?(Object(n["openBlock"])(),Object(n["createBlock"])("div",l,[void 0===y.form_response.content.sections[o][s].answer||""==y.form_response.content.sections[o][s].answer||y.form_response.content.sections[o][s].answer==[]?(Object(n["openBlock"])(),Object(n["createBlock"])("span",p," Sem resposta ")):(Object(n["openBlock"])(),Object(n["createBlock"])("ul",b,[(Object(n["openBlock"])(!0),Object(n["createBlock"])(n["Fragment"],null,Object(n["renderList"])(y.form_response.content.sections[o][s].answer,(function(e){return Object(n["openBlock"])(),Object(n["createBlock"])("li",{key:e},[e===parseInt(e,10)?(Object(n["openBlock"])(),Object(n["createBlock"])("span",d,Object(n["toDisplayString"])(c.properties.options[e]),1)):(Object(n["openBlock"])(),Object(n["createBlock"])("span",O," Outro: "+Object(n["toDisplayString"])(e),1))])})),128))]))])):"multiplechoice"==c.properties.field_type?(Object(n["openBlock"])(),Object(n["createBlock"])("div",{key:1,set:e.answer=y.form_response.content.sections[o][s].answer},[void 0===e.answer?(Object(n["openBlock"])(),Object(n["createBlock"])("span",j," Sem resposta ")):e.answer===parseInt(e.answer,10)?(Object(n["openBlock"])(),Object(n["createBlock"])("span",u,Object(n["toDisplayString"])(c.properties.options[e.answer]),1)):(Object(n["openBlock"])(),Object(n["createBlock"])("span",f,[Object(n["createTextVNode"])(Object(n["toDisplayString"])(c.properties.other_string),1),e.answer?(Object(n["openBlock"])(),Object(n["createBlock"])("span",k,' "'+Object(n["toDisplayString"])(e.answer)+'"',1)):Object(n["createCommentVNode"])("",!0)]))],8,["set"])):"date"==c.properties.field_type?(Object(n["openBlock"])(),Object(n["createBlock"])("div",m,Object(n["toDisplayString"])(new Date(y.form_response.content.sections[o][s].answer).toLocaleDateString()),1)):"datetime"==c.properties.field_type?(Object(n["openBlock"])(),Object(n["createBlock"])("div",h,Object(n["toDisplayString"])(new Date(y.form_response.content.sections[o][s].answer).toLocaleString()),1)):(Object(n["openBlock"])(),Object(n["createBlock"])("div",B,Object(n["toDisplayString"])(y.form_response.content.sections[o][s].answer),1))],8,["set"])})),128))])})),128))])])}o("caad"),o("2532"),o("a434");var y=o("3f6f"),g=o("c427"),w={name:"ViewResponse",components:y,data:function(){return{api_data:{},form_response:{}}},created:function(){var e=this;g["a"].get("formAnswer/".concat(this.$route.params.id)).then((function(t){e.initializeResponseData(t),g["a"].get("form/".concat(t.data.form)).then((function(t){return e.initializeData(t)})).catch((function(e){return console.log(e.response)}))}))},methods:{initializeData:function(e){this.api_data=e.data;for(var t=0;t<this.api_data.form.sections.length;){for(var o=0;o<this.api_data.form.sections[t].questions.length;)this.api_data.form.sections[t].questions[o].properties.field_type.includes("_exposition")?this.api_data.form.sections[t].questions.splice(o,1):o++;this.api_data.form.sections[t].questions.length>0?t++:this.api_data.form.sections.splice(t,1)}},initializeResponseData:function(e){this.form_response=e.data;for(var t=0;t<this.form_response.content.sections.length;){for(var o=0;o<this.form_response.content.sections[t].length;)this.form_response.content.sections[t][o].field_type.includes("_exposition")?this.form_response.content.sections[t].splice(o,1):o++;this.form_response.content.sections[t].length>0?t++:this.form_response.content.sections.splice(t,1)}}}};w.render=_;t["default"]=w}}]);
//# sourceMappingURL=chunk-2c231cbe.4984facc.js.map