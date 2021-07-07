(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-b98719fa"],{1995:function(e,t,o){"use strict";var n=o("7a23"),c={class:"field is-grouped is-grouped-centered"},i={class:"control"},a={key:0,class:"control"},r={key:1,class:"control"},s={key:2,class:"control"};function l(e,t,o,l,u,d){var m=this,b=Object(n["resolveComponent"])("Notification");return Object(n["openBlock"])(),Object(n["createBlock"])("div",null,[o.error?(Object(n["openBlock"])(),Object(n["createBlock"])("div",{key:0,class:["flex row ca snackbar ontop",o.floatBottom?"bottom":"top"]},[Object(n["createVNode"])(b,{message:o.errorMessage,duration:o.errorDuration,bottom:o.floatBottom,class:"is-danger subtitle",onDeleted:t[1]||(t[1]=function(t){return e.$emit("dismissed")})},null,8,["message","duration","bottom"])],2)):o.successMessage?(Object(n["openBlock"])(),Object(n["createBlock"])("div",{key:1,class:["flex row ca snackbar ontop",o.floatBottom?"bottom":"top"]},[Object(n["createVNode"])(b,{message:o.successMessage,bottom:o.floatBottom,duration:o.successDuration,class:"is-success is-light",onDeleted:t[2]||(t[2]=function(t){return e.$emit("dismissed")})},null,8,["message","bottom","duration"])],2)):Object(n["createCommentVNode"])("",!0),Object(n["createVNode"])(n["Transition"],{name:"slide-fade-bottom",mode:"out-in"},{default:Object(n["withCtx"])((function(){return[o.hide?Object(n["createCommentVNode"])("",!0):(Object(n["openBlock"])(),Object(n["createBlock"])("div",{key:0,class:["flex row ca",{"snackbar bottom":o.floatBottom}]},[Object(n["createVNode"])("div",{class:{"box has-background-link-dark":o.floatBottom}},[u.confirmingCancel?(Object(n["openBlock"])(),Object(n["createBlock"])("span",{key:0,class:["level",{"has-text-light":o.floatBottom}],innerHTML:o.cancelConfirmation},null,10,["innerHTML"])):Object(n["createCommentVNode"])("",!0),u.confirmingSubmit?(Object(n["openBlock"])(),Object(n["createBlock"])("span",{key:1,class:["level",{"has-text-light":o.floatBottom}],innerHTML:o.submitConfirmation},null,10,["innerHTML"])):Object(n["createCommentVNode"])("",!0),Object(n["createVNode"])("div",c,[Object(n["createVNode"])("div",i,[Object(n["createVNode"])("button",{type:"button",class:["button",{"is-loading":!0===o.loading,"is-link is-light":!o.redGreen,"is-danger is-light":o.redGreen}],onClick:t[3]||(t[3]=function(e){return d.cancel()})},Object(n["toDisplayString"])(void 0===o.cancelText||u.confirmingCancel?"Cancelar":o.cancelText),3)]),u.confirmingCancel?(Object(n["openBlock"])(),Object(n["createBlock"])("div",a,[Object(n["createVNode"])("button",{type:"button",class:["button is-danger",{"is-loading":!0===o.loading}],onClick:t[4]||(t[4]=function(e){u.confirmingCancel=!1,m.$emit("leave")})},Object(n["toDisplayString"])(void 0!==o.cancelConfButton?o.cancelConfButton:"Confirmar"),3)])):u.confirmingSubmit?(Object(n["openBlock"])(),Object(n["createBlock"])("div",r,[Object(n["createVNode"])("button",{type:"submit",class:["button is-success",{"is-loading":!0===o.loading}]},Object(n["toDisplayString"])(void 0!==o.submitConfButton?o.submitConfButton:"Confirmar"),3)])):(Object(n["openBlock"])(),Object(n["createBlock"])("div",s,[Object(n["createVNode"])("button",{type:o.submitConfirmation?"button":"submit",class:["button",{"is-loading":!0===o.loading,"is-link":!o.redGreen,"is-success is-light":o.redGreen}],onClick:t[5]||(t[5]=function(e){return d.submit()})},Object(n["toDisplayString"])(void 0!==o.submitText?o.submitText:"Submeter"),11,["type"])]))])],2)],2))]})),_:1})])}var u=o("2b9d"),d={components:{Notification:u["a"]},name:"Submit",data:function(){return{confirmingCancel:!1,confirmingSubmit:!1}},props:["error","errorMessage","errorDuration","loading","successMessage","successDuration","submitText","cancelText","redGreen","hide","floatBottom","cancelConfirmation","submitConfirmation","cancelConfButton","submitConfButton"],methods:{cancel:function(){this.cancelConfirmation?this.confirmingCancel?this.confirmingCancel=!1:this.confirmingSubmit?this.confirmingSubmit=!1:this.confirmingCancel=!0:this.$emit("leave")},submit:function(){this.submitConfirmation&&(this.confirmingSubmit=!0)}},watch:{error:{immediate:!0,handler:function(){this.confirmingCancel=!1,this.confirmingSubmit=!1}},successMessage:{immediate:!0,handler:function(){this.confirmingCancel=!1,this.confirmingSubmit=!1}}}};d.render=l;t["a"]=d},"2b9d":function(e,t,o){"use strict";var n=o("7a23");function c(e,t,o,c,i,a){return Object(n["openBlock"])(),Object(n["createBlock"])(n["Transition"],{name:o.bottom?"slide-fade-bottom":"slide-fade",class:"box notification",mode:"out-in"},{default:Object(n["withCtx"])((function(){return[Object(n["withDirectives"])(Object(n["createVNode"])("span",null,[Object(n["createVNode"])("button",{type:"button",class:"delete",onClick:t[1]||(t[1]=function(e){return a.deactivate()})}),Object(n["createTextVNode"])(" "+Object(n["toDisplayString"])(o.message),1)],512),[[n["vShow"],i.active]])]})),_:1},8,["name"])}var i=o("1da1"),a=(o("96cf"),o("d3b7"),{name:"Notification",props:["message","duration","bottom"],emits:["deleted"],data:function(){return{active:!1}},mounted:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(e.active=!0,!e.duration){t.next=5;break}return t.next=4,new Promise((function(t){return setTimeout(t,e.duration)}));case 4:e.deactivate();case 5:case"end":return t.stop()}}),t)})))()},methods:{deactivate:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e.active=!1,t.next=3,new Promise((function(e){return setTimeout(e,500)}));case 3:e.$emit("deleted");case 4:case"end":return t.stop()}}),t)})))()}}});a.render=c;t["a"]=a},"3f58":function(e,t,o){"use strict";o("f333")},"91ba":function(e,t,o){"use strict";o.r(t);o("b0c0");var n=o("7a23"),c=Object(n["withScopeId"])("data-v-0d3a01f0");Object(n["pushScopeId"])("data-v-0d3a01f0");var i={key:0,class:"box"},a={ref:"formtitle",class:"title"},r=Object(n["createVNode"])("hr",null,null,-1),s={key:0,class:"flex column"},l=Object(n["createVNode"])("span",{class:"flex row ca subtitle mt-3 mb-6"},"Não consegue editar este formulário de momento.",-1),u={class:"steps has-content-centered mb-0"},d={class:"steps-marker"},m={class:"steps-content"},b={class:"steps-marker"},f=Object(n["createVNode"])("div",{class:"steps-content"},[Object(n["createVNode"])("p",null," Concluída ")],-1),p={key:0,class:"box"},j={key:0},O={key:0,class:"mt-4 mb-4",style:{width:"100%",height:"1px","background-color":"#ddd"}},h={key:1,class:"flex column box ca vca",style:{height:"50vh"}},v=Object(n["createVNode"])("span",{class:"title mb-4"},"A carregar formulário",-1),g=Object(n["createVNode"])("span",{class:"loader mt-4",style:{width:"100px",height:"100px"}},null,-1);Object(n["popScopeId"])();var k=c((function(e,t,o,c,k,B){var y=Object(n["resolveComponent"])("Submit");return k.api_data&&k.event&&k.form&&k.available?(Object(n["openBlock"])(),Object(n["createBlock"])("div",i,[Object(n["createVNode"])("h1",a,[Object(n["createTextVNode"])(Object(n["toDisplayString"])(k.api_data.title),1),k.event?(Object(n["openBlock"])(),Object(n["createBlock"])(n["Fragment"],{key:0},[Object(n["createTextVNode"])(" ("+Object(n["toDisplayString"])(k.event.name)+") ",1)],64)):Object(n["createCommentVNode"])("",!0)],512),r,k.cannotEdit?(Object(n["openBlock"])(),Object(n["createBlock"])("div",s,[l,Object(n["createVNode"])("button",{type:"button",class:"button is-primary",onClick:t[1]||(t[1]=function(e){return B.back()})}," Voltar ")])):(Object(n["openBlock"])(),Object(n["createBlock"])("form",{key:1,id:"form-area",class:"flex column",method:"post",onSubmit:t[4]||(t[4]=Object(n["withModifiers"])((function(){return B.submit&&B.submit.apply(B,arguments)}),["prevent"]))},[Object(n["createVNode"])("ul",u,[(Object(n["openBlock"])(!0),Object(n["createBlock"])(n["Fragment"],null,Object(n["renderList"])(k.api_data.form.sections,(function(e,t){return Object(n["openBlock"])(),Object(n["createBlock"])("li",{key:e.id,class:["steps-segment is-primary",{"is-active":k.section==t,"has-gaps":k.section<=t}]},[Object(n["createVNode"])("span",d,[k.api_data.form.hide_section_numbers?Object(n["createCommentVNode"])("",!0):(Object(n["openBlock"])(),Object(n["createBlock"])(n["Fragment"],{key:0},[Object(n["createTextVNode"])(Object(n["toDisplayString"])(t+1),1)],64))]),Object(n["createVNode"])("div",m,[Object(n["createVNode"])("p",{class:{"has-text-weight-bold":k.section==t}},Object(n["toDisplayString"])(e.section_name),3)])],2)})),128)),Object(n["createVNode"])("li",{class:["steps-segment is-primary",{"is-active":k.section==k.api_data.form.sections.length}]},[Object(n["createVNode"])("span",b,[k.api_data.form.hide_section_numbers?Object(n["createCommentVNode"])("",!0):(Object(n["openBlock"])(),Object(n["createBlock"])(n["Fragment"],{key:0},[Object(n["createTextVNode"])(Object(n["toDisplayString"])(k.api_data.form.sections.length+1),1)],64))]),f],2)]),k.section<k.api_data.form.sections.length?(Object(n["openBlock"])(),Object(n["createBlock"])("div",p,[(Object(n["openBlock"])(!0),Object(n["createBlock"])(n["Fragment"],null,Object(n["renderList"])(k.api_data.form.sections[k.section].questions,(function(t,o){return Object(n["openBlock"])(),Object(n["createBlock"])("div",{key:t.id,set:e.qid="s"+k.section+"_q"+o},[Object(n["createVNode"])("label",{class:["label",{required:t.required}],for:e.qid},[k.api_data.form.hide_question_numbers||k.api_data.form.sections[k.section].hide_question_numbers?Object(n["createCommentVNode"])("",!0):(Object(n["openBlock"])(),Object(n["createBlock"])("span",j,Object(n["toDisplayString"])(o+1)+". ",1)),Object(n["createTextVNode"])(Object(n["toDisplayString"])(t.question),1)],10,["for"]),(Object(n["openBlock"])(),Object(n["createBlock"])(Object(n["resolveDynamicComponent"])(t.properties.field_type),{question:t,"question-index":o,"section-index":k.section,value:k.form.content.sections[k.section][o].answer,qid:e.qid,onUpdate:B.updateAnswer},null,8,["question","question-index","section-index","value","qid","onUpdate"])),o<k.api_data.form.sections[k.section].questions.length-1?(Object(n["openBlock"])(),Object(n["createBlock"])("hr",O)):Object(n["createCommentVNode"])("",!0)],8,["set"])})),128))])):(Object(n["openBlock"])(),Object(n["createBlock"])("div",{key:1,innerHTML:k.api_data.submit_message},null,8,["innerHTML"])),Object(n["createVNode"])(y,{error:k.response&&void 0===k.response.id,"error-message":"Houve um erro na submissão do formulário.","success-duration":"3000","success-message":k.success,loading:k.loading,"submit-text":k.section<k.api_data.form.sections.length-1?"Seguinte":"Submeter","cancel-text":k.section>0?"Anterior":"Sair","cancel-confirmation":0==k.section?"Deseja sair? <b>A sua resposta não será guardada.</br>":void 0,"cancel-conf-button":"Sair",hide:k.section==k.api_data.form.sections.length,onLeave:t[2]||(t[2]=function(e){return B.leave()}),onDismissed:t[3]||(t[3]=function(e){k.response=void 0,k.success=void 0})},null,8,["error","success-message","loading","submit-text","cancel-text","cancel-confirmation","hide"]),Object(n["createCommentVNode"])("",!0)],32))])):(Object(n["openBlock"])(),Object(n["createBlock"])("div",h,[v,g]))})),B=o("1da1"),y=(o("96cf"),o("d3b7"),o("3ca3"),o("ddb0"),o("99af"),o("3f6f")),w=o("c427"),x=o("69d9"),C=o("1995"),N={name:"CreateResponse",components:Object.assign({},{Submit:C["a"]},y),data:function(){return{api_data:void 0,form:void 0,response:void 0,event:void 0,section:0,success:void 0,loading:!1,cannotEdit:!1,available:!0}},created:function(){var e=this;return Object(B["a"])(regeneratorRuntime.mark((function t(){var o,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return document.title="Resposta de Formulário",e.$route.query.event||(window.location.href="/forms/notfound"),t.next=4,Promise.all([w["a"].get("form/".concat(e.$route.params.id)).then((function(t){return e.api_data=t.data})).catch((function(){return window.location.href="/forms/badrequest"})),w["a"].get("event/".concat(e.$route.query.event)).then((function(t){e.event=t.data})).catch((function(){return window.location.href="/forms/badrequest"}))]);case 4:return 2!=e.api_data.type&&(null===(o=e.event)||void 0===o?void 0:o.formsignupid)!=e.$route.params.id&&(null===(n=e.event)||void 0===n?void 0:n.formfeedbackid)!=e.$route.params.id&&(window.location.href="/forms/badrequest"),t.next=7,w["a"].get("myFormAnswer/?form=".concat(e.$route.params.id).concat("&event=").concat(e.$route.query.event)).then((function(t){t.data[0]?(e.form=t.data[0],3!=e.form.status&&(e.cannotEdit=!0)):(console.log("new form"),e.available=!1,e.form={content:{sections:[]},form:e.api_data.id,event:e.event.id},e.initializeData(),e.available=!0)}));case 7:case"end":return t.stop()}}),t)})))()},methods:{back:function(){0==window.length?window.location.href="/":this.$router.back()},leave:function(){var e=this;this.section>0?(this.section--,this.$nextTick((function(){return e.$refs["formtitle"].scrollIntoView({behavior:"smooth"})}))):location.href="/forms"},submit:function(){var e=this;if(this.section<this.api_data.form.sections.length-1)this.section++,this.$nextTick((function(){return e.$refs["formtitle"].scrollIntoView({behavior:"smooth"})}));else{var t,o,n;this.loading=!0,void 0===this.form.id?(t="post",o="/myFormAnswer/",n="A resposta foi enviada com sucesso."):(t="put",o="/myFormAnswer/".concat(this.form.id).concat("/"),n="A resposta foi editada com sucesso.");var c={method:t,url:o,headers:{"X-CSRFToken":Object(x["b"])("csrftoken")},data:this.form,transformResponse:[function(){var t=Object(B["a"])(regeneratorRuntime.mark((function t(o){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e.loading=void 0,t.prev=1,e.response=JSON.parse(o),e.form=e.response,e.success=n,e.section++,t.next=8,new Promise((function(t){return setTimeout(t,1e3*e.api_data.redirect_delay)}));case 8:location.href=e.api_data.redirect,t.next=14;break;case 11:t.prev=11,t.t0=t["catch"](1),e.response=o;case 14:return t.abrupt("return",e.response);case 15:case"end":return t.stop()}}),t,null,[[1,11]])})));return function(e){return t.apply(this,arguments)}}()]};Object(w["a"])(c)}},updateAnswer:function(e){this.form.content.sections[e.sectionIndex][e.questionIndex]["answer"]=e["answer"]},initializeData:function(){for(var e in this.api_data.form.sections)for(var t in this.form.content.sections[e]=[],this.api_data.form.sections[e].questions)this.form.content.sections[e][t]={field_type:this.api_data.form.sections[e].questions[t].properties["field_type"]}}}};o("3f58"),o("b7c2");N.render=k,N.__scopeId="data-v-0d3a01f0";t["default"]=N},b7c2:function(e,t,o){"use strict";o("fe2a")},f333:function(e,t,o){},fe2a:function(e,t,o){}}]);
//# sourceMappingURL=chunk-b98719fa.a7371f85.js.map