webpackJsonp([22],{uQ1P:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r={name:"futiantable",data:function(){return{tableData:[],xtableData:[],cur_page:1,jid:"",sid:"",multipleSelection:[],select_cate:"",select_word:"",del_list:[],is_search:!1,addVisible:!1,editVisible:!1,xaddVisible:!1,xeditVisible:!1,showtable:!0,form:{name:"",date:"",phone:""},idx:-1}},created:function(){this.getData()},computed:{},methods:{formatisnull1:function(e,t){return null==e.address?"":"null"==e.address?"":"undefined"==e.address?"":e.address},formatisnull2:function(e,t){return null==e.personCharge?"":"null"==e.personCharge?"":"undefined"==e.personCharge?"":e.personCharge},formatisnull3:function(e,t){return null==e.phone?"":"null"==e.phone?"":"undefined"==e.phone?"":e.phone},formatisnull4:function(e,t){return null==e.remarks?"":"null"==e.remarks?"":"undefined"==e.remarks?"":e.remarks},getData:function(){var e=this;this.url="/testftcg/config/getStreets?token="+localStorage.token,this.$axios.get(this.url).then(function(t){if(console.log(t),1!=t.data.code)e.$message.error(t.data.msg);else if(t.data.code=1){e.tableData=t.data.data,e.tableData.sort((a="number",function(e,t){return e[a]-t[a]})),console.log(e.tableData)}else console.log("不知出啥问题了");var a})},refresh:function(e){this.tableData=[],this.getData()},xgetData:function(e){var t=this;console.log("接受的id是"+e),this.url="/testftcg/config/getCommunitys?token="+localStorage.token+"&streetId="+e,this.$axios.get(this.url).then(function(e){if(console.log(e),1!=e.data.code)t.$message.error(e.data.msg);else if(e.data.code=1){t.xtableData=e.data.data,console.log(t.xtableData);t.xtableData}else console.log("不知出啥问题了")})},handlecheck:function(e,t){this.showtable=!this.showtable,this.xgetData(t.id),localStorage.setItem("xid",t.id),this.jid=t.id,console.log(this.jid)},xhandlecheck:function(e,t){console.log(t.id)},back:function(){this.showtable=!this.showtable},add:function(){this.addVisible=!0},addtable:function(){var e=this;null==this.form.addname?this.$message.error("请输入数据后再提交"):(this.url="/testftcg/config/baseConfigStreet?token="+localStorage.token+"&name="+this.form.addname+"&number="+this.form.addnumber+"&address="+this.form.addaddress+"&personCharge="+this.form.addpersonCharge+"&phone="+this.form.addphone+"&remarks="+this.form.addremarks,this.$axios.get(this.url).then(function(t){console.log(t),(t.status=200)?(e.addVisible=!1,e.$message.success("街道数据新增成功"),e.form.addname="",e.form.addnumber="",e.form.addaddress="",e.form.addpersonCharge="",e.form.addphone="",e.form.addremarks="",e.getData()):e.$message.error(t.data.msg)}))},xadd:function(e,t){this.xaddVisible=!0},xaddtable:function(){var e=this;null==this.form.xaddname?this.$message.error("请输入数据后再提交"):(this.url="/testftcg/config/baseConfigCommunity?token="+localStorage.token+"&name="+this.form.xaddname+"&number="+this.form.xaddnumber+"&address="+this.form.xaddaddress+"&personCharge="+this.form.xaddpersonCharge+"&phone="+this.form.xaddphone+"&remarks="+this.form.xaddremarks+"&streetId="+this.jid,this.$axios.get(this.url).then(function(t){console.log(t),(t.data.code=1)?(e.xaddVisible=!1,e.$message.success("街道数据新增成功"),e.form.xaddname="",e.form.xaddnumber="",e.form.xaddaddress="",e.form.xaddpersonCharge="",e.form.xaddphone="",e.form.xaddremarks="",e.xgetData(e.jid)):e.$message.error(t.data.msg)}))},filterTag:function(e,t){return t.tag===e},handleEdit:function(e,t){this.jid=t.id,this.editVisible=!0,this.form.name=this.tableData[e].name,this.form.number=this.tableData[e].number,this.form.address=this.tableData[e].address,this.form.personCharge=this.tableData[e].personCharge,this.form.phone=this.tableData[e].phone,this.form.remarks=this.tableData[e].remarks},saveEdit:function(e,t){var a=this;this.url="/testftcg/config/editBaseConfigStreet?token="+localStorage.token+"&name="+this.form.name+"&number="+this.form.number+"&address="+this.form.address+"&personCharge="+this.form.personCharge+"&phone="+this.form.phone+"&remarks="+this.form.remarks+"&streetId="+this.jid,this.$axios.get(this.url).then(function(e){console.log(e),(e.data.code=1)?(a.editVisible=!1,a.$message.success("街道数据编辑成功"),a.form.name="",a.form.number="",a.form.address="",a.form.personCharge="",a.form.phone="",a.form.remarks="",a.getData()):a.$message.error(e.data.msg)})},xhandleEdit:function(e,t){this.sid=t.id,this.xeditVisible=!0,this.form.name=this.xtableData[e].name,this.form.number=this.xtableData[e].number,this.form.address=this.xtableData[e].address,this.form.personCharge=this.xtableData[e].personCharge,this.form.phone=this.xtableData[e].phone,this.form.remarks=this.xtableData[e].remarks},xsaveEdit:function(e,t){var a=this;this.url="/testftcg/config/editBaseConfigCommunity?token="+localStorage.token+"&name="+this.form.name+"&number="+this.form.number+"&address="+this.form.address+"&personCharge="+this.form.personCharge+"&phone="+this.form.phone+"&remarks="+this.form.remarks+"&communityId="+this.sid,this.$axios.get(this.url).then(function(e){console.log(e),(e.data.code=1)?(a.xeditVisible=!1,a.$message.success("社区数据编辑成功"),a.form.name="",a.form.number="",a.form.address="",a.form.personCharge="",a.form.phone="",a.form.remarks="",a.xgetData(a.jid)):a.$message.error(e.data.msg)})},handleSelectionChange:function(e){this.multipleSelection=e},handleDelete:function(e,t){this.idx=e,this.$message.error("本数据不能删除，请谨慎操作，如需操作，请联系运维管理")},xhandleDelete:function(e,t){this.$message.error("本数据不能删除，请谨慎操作，如需操作，请联系运维管理")}}},o={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"table"},[a("div",{directives:[{name:"show",rawName:"v-show",value:e.showtable,expression:"showtable"}],staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-lx-cascades"}),e._v(" 街道基础数据")])],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:!e.showtable,expression:"!showtable"}],staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-lx-cascades"}),e._v(" 街道基础数据--社区基础数据")])],1)],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:e.showtable,expression:"showtable"}],staticClass:"container"},[a("div",{staticClass:"handle-box"},[a("el-button",{attrs:{type:"primary",icon:"search"},on:{click:e.refresh}},[e._v("刷新")]),e._v(" "),a("el-button",{staticClass:"add",attrs:{type:"primary",icon:"search"},on:{click:e.add}},[e._v("新增街道")])],1),e._v(" "),a("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:e.tableData,border:""},on:{"selection-change":e.handleSelectionChange}},[a("el-table-column",{attrs:{prop:"id",label:"id",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{prop:"name",label:"街道名",width:"150"}}),e._v(" "),a("el-table-column",{attrs:{prop:"number",label:"编号",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{prop:"address",label:"地址",formatter:e.formatisnull1,width:"180"}}),e._v(" "),a("el-table-column",{attrs:{prop:"personCharge",label:"负责人",formatter:e.formatisnull2,width:"70"}}),e._v(" "),a("el-table-column",{attrs:{prop:"phone",label:"号码",formatter:e.formatisnull3,width:"120"}}),e._v(" "),a("el-table-column",{attrs:{prop:"remarks",label:"备注",formatter:e.formatisnull4,width:"180"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"260",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(a){e.handleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),a("el-button",{staticClass:"red",attrs:{type:"text",icon:"el-icon-delete"},on:{click:function(a){e.handleDelete(t.$index,t.row)}}},[e._v("删除")]),e._v(" "),a("el-button",{staticClass:"blue",attrs:{type:"text",icon:"el-icon-info"},on:{click:function(a){e.handlecheck(t.$index,t.row)}}},[e._v("查看街道内社区")])]}}])})],1),e._v(" "),a("div",{staticClass:"pagination"})],1),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:!e.showtable,expression:"!showtable"}],staticClass:"container"},[a("div",{staticClass:"handle-box"},[a("el-button",{attrs:{type:"primary",icon:"search"},on:{click:e.back}},[e._v("返回")]),e._v(" "),a("el-button",{staticClass:"add",attrs:{type:"primary",icon:"search"},on:{click:e.xadd}},[e._v("新增社区")])],1),e._v(" "),a("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:e.xtableData,border:""},on:{"selection-change":e.handleSelectionChange}},[a("el-table-column",{attrs:{prop:"id",label:"id",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{prop:"name",label:"社区名",width:"150"}}),e._v(" "),a("el-table-column",{attrs:{prop:"number",label:"编号",width:"50"}}),e._v(" "),a("el-table-column",{attrs:{prop:"address",label:"地址",width:"180"}}),e._v(" "),a("el-table-column",{attrs:{prop:"personCharge",label:"负责人",width:"70"}}),e._v(" "),a("el-table-column",{attrs:{prop:"phone",label:"号码",width:"120"}}),e._v(" "),a("el-table-column",{attrs:{prop:"remarks",label:"备注",width:"180"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"260",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(a){e.xhandleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),a("el-button",{staticClass:"red",attrs:{type:"text",icon:"el-icon-delete"},on:{click:function(a){e.xhandleDelete(t.$index,t.row)}}},[e._v("删除")]),e._v(" "),a("el-button",{staticClass:"blue",attrs:{type:"text",icon:"el-icon-info"},on:{click:function(a){e.xhandlecheck(t.$index,t.row)}}},[e._v("查看社区内住户")])]}}])})],1),e._v(" "),a("div",{staticClass:"pagination"})],1),e._v(" "),a("el-dialog",{attrs:{title:"新增街道",visible:e.addVisible,width:"30%"},on:{"update:visible":function(t){e.addVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"70px"}},[a("el-form-item",{attrs:{label:"名称"}},[a("el-input",{attrs:{placeholder:"输入街道名"},model:{value:e.form.addname,callback:function(t){e.$set(e.form,"addname",t)},expression:"form.addname"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"编号"}},[a("el-input",{attrs:{placeholder:"输入编号"},model:{value:e.form.addnumber,callback:function(t){e.$set(e.form,"addnumber",t)},expression:"form.addnumber"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"地址"}},[a("el-input",{attrs:{placeholder:"输入地址"},model:{value:e.form.addaddress,callback:function(t){e.$set(e.form,"addaddress",t)},expression:"form.addaddress"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"负责人"}},[a("el-input",{attrs:{placeholder:"输入负责人"},model:{value:e.form.addpersonCharge,callback:function(t){e.$set(e.form,"addpersonCharge",t)},expression:"form.addpersonCharge"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"联系电话"}},[a("el-input",{attrs:{placeholder:"输入联系电话"},model:{value:e.form.addphone,callback:function(t){e.$set(e.form,"addphone",t)},expression:"form.addphone"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"备注"}},[a("el-input",{attrs:{placeholder:"输入备注"},model:{value:e.form.addremarks,callback:function(t){e.$set(e.form,"addremarks",t)},expression:"form.addremarks"}})],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.addVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.addtable}},[e._v("确 定")])],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"编辑街道数据",visible:e.editVisible,width:"30%"},on:{"update:visible":function(t){e.editVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"70px"}},[a("el-form-item",{attrs:{label:"名称"}},[a("el-input",{attrs:{placeholder:"输入街道名"},model:{value:e.form.name,callback:function(t){e.$set(e.form,"name",t)},expression:"form.name"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"编号"}},[a("el-input",{attrs:{placeholder:"输入编号"},model:{value:e.form.number,callback:function(t){e.$set(e.form,"number",t)},expression:"form.number"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"地址"}},[a("el-input",{attrs:{placeholder:"输入地址"},model:{value:e.form.address,callback:function(t){e.$set(e.form,"address",t)},expression:"form.address"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"负责人"}},[a("el-input",{attrs:{placeholder:"输入负责人"},model:{value:e.form.personCharge,callback:function(t){e.$set(e.form,"personCharge",t)},expression:"form.personCharge"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"联系电话"}},[a("el-input",{attrs:{placeholder:"输入联系电话"},model:{value:e.form.phone,callback:function(t){e.$set(e.form,"phone",t)},expression:"form.phone"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"备注"}},[a("el-input",{attrs:{placeholder:"输入备注"},model:{value:e.form.remarks,callback:function(t){e.$set(e.form,"remarks",t)},expression:"form.remarks"}})],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.editVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.saveEdit}},[e._v("确 定")])],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"新增社区",visible:e.xaddVisible,width:"30%"},on:{"update:visible":function(t){e.xaddVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"70px"}},[a("el-form-item",{attrs:{label:"名称"}},[a("el-input",{attrs:{placeholder:"输入社区名"},model:{value:e.form.xaddname,callback:function(t){e.$set(e.form,"xaddname",t)},expression:"form.xaddname"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"编号"}},[a("el-input",{attrs:{placeholder:"输入编号"},model:{value:e.form.xaddnumber,callback:function(t){e.$set(e.form,"xaddnumber",t)},expression:"form.xaddnumber"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"地址"}},[a("el-input",{attrs:{placeholder:"输入地址"},model:{value:e.form.xaddaddress,callback:function(t){e.$set(e.form,"xaddaddress",t)},expression:"form.xaddaddress"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"负责人"}},[a("el-input",{attrs:{placeholder:"输入负责人"},model:{value:e.form.xaddpersonCharge,callback:function(t){e.$set(e.form,"xaddpersonCharge",t)},expression:"form.xaddpersonCharge"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"联系电话"}},[a("el-input",{attrs:{placeholder:"输入联系电话"},model:{value:e.form.xaddphone,callback:function(t){e.$set(e.form,"xaddphone",t)},expression:"form.xaddphone"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"备注"}},[a("el-input",{attrs:{placeholder:"输入备注"},model:{value:e.form.xaddremarks,callback:function(t){e.$set(e.form,"xaddremarks",t)},expression:"form.xaddremarks"}})],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.xaddVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.xaddtable}},[e._v("确 定")])],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"编辑社区数据",visible:e.xeditVisible,width:"30%"},on:{"update:visible":function(t){e.xeditVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"70px"}},[a("el-form-item",{attrs:{label:"名称"}},[a("el-input",{attrs:{placeholder:"输入社区名"},model:{value:e.form.name,callback:function(t){e.$set(e.form,"name",t)},expression:"form.name"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"编号"}},[a("el-input",{attrs:{placeholder:"输入编号"},model:{value:e.form.number,callback:function(t){e.$set(e.form,"number",t)},expression:"form.number"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"地址"}},[a("el-input",{attrs:{placeholder:"输入地址"},model:{value:e.form.address,callback:function(t){e.$set(e.form,"address",t)},expression:"form.address"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"负责人"}},[a("el-input",{attrs:{placeholder:"输入负责人"},model:{value:e.form.personCharge,callback:function(t){e.$set(e.form,"personCharge",t)},expression:"form.personCharge"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"联系电话"}},[a("el-input",{attrs:{placeholder:"输入联系电话"},model:{value:e.form.phone,callback:function(t){e.$set(e.form,"phone",t)},expression:"form.phone"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"备注"}},[a("el-input",{attrs:{placeholder:"输入备注"},model:{value:e.form.remarks,callback:function(t){e.$set(e.form,"remarks",t)},expression:"form.remarks"}})],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.xeditVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.xsaveEdit}},[e._v("确 定")])],1)],1)],1)},staticRenderFns:[]};var s=a("VU/8")(r,o,!1,function(e){a("yeqp")},"data-v-2b12505c",null);t.default=s.exports},yeqp:function(e,t){}});