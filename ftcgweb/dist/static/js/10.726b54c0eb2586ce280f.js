webpackJsonp([10],{"8C4o":function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var l={name:"basetable",data:function(){return{tableData:[],cur_page:1,multipleSelection:[],select_cate:"",select_word:"",del_list:[],is_search:!1,editVisible:!1,addVisible:!1,resetVisible:!1,form:{name:"",role:"",phone:""},idx:-1,uid:"",pagenum:0,totalnum:0}},created:function(){this.getData()},computed:{},methods:{handleCurrentChange:function(e){var t=this;this.pagenum=e-1,this.otableData="",setTimeout(function(){t.getData(t.jid)},300)},getData:function(){var e=this;this.url="/testftcg/user/getAllUserList?token="+localStorage.token+"&page="+this.pagenum+"&pageSize=10",this.$axios.get(this.url).then(function(t){if(t.data.code=1){e.totalnum=t.allPage,e.tableData=t.data.data;e.tableData;e.tableData.some(function(t){var a={0:"管理员",1:"分拣员",2:"物业",3:"用户"};e.tableData.map(function(e){var t=e.role;return e.role=a[t]?a[t]:t,e})})}else console.log("不知出啥问题了")})},search:function(){this.is_search=!0},add:function(){this.addVisible=!0},addtable:function(){var e=this;console.log(this.form.addname),null!=this.form.addname&&null!=this.form.addpassword&&null!=this.form.addrole?(this.url="/testftcg/user/register?token="+localStorage.token+"&name="+this.form.addname+"&password="+this.$md5(this.$md5(this.form.addpassword))+"&role="+this.form.addrole+"&phone="+this.form.addphone+"&villageId="+this.form.villageId,this.$axios.get(this.url).then(function(t){1!=t.data.code?e.$message.error(t.data.msg):(t.data.code=1)&&(e.$message.success("用户创建成功"),e.addVisible=!1,e.form.villageId="",e.form.addpassword="",e.form.addname="",e.form.addphone="",e.form.addrole="",e.getData())})):this.$message.error("请输入数据后再提交")},filterTag:function(e,t){return t.tag===e},handleEdit:function(e,t){this.$message.error("创建后暂不支持修改用户信息，如需操作，请联系运维管理")},handlereset:function(e){var t=this;this.uid=this.tableData[e].id,this.$confirm("此操作将重置账号的密码为手机号, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){t.url="/testftcg/user/adminResetPassword?token="+localStorage.token+"&userId="+t.tableData[e].id,t.$axios.get(t.url).then(function(e){console.log(e),(e.data.code=200)?t.$message.success("重置成功！新密码为用户的手机号"):t.$message.error(e.data.msg),t.getData()})}).catch(function(){})},handleDelete:function(e,t){this.uid=this.tableData[e].id,this.$message.error("本数据不能删除，请谨慎操作，如需操作，请联系运维管理")},handleSelectionChange:function(e){this.multipleSelection=e},saveEdit:function(){this.$message.success("等待修改接口api")}}},o={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"table"},[a("div",{staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-lx-cascades"}),e._v(" 用户管理")])],1)],1),e._v(" "),a("div",{staticClass:"container"},[a("div",{staticClass:"handle-box"},[a("el-button",{staticClass:"add",attrs:{type:"primary",icon:"search"},on:{click:e.add}},[e._v("新增用户")])],1),e._v(" "),a("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:e.tableData,border:""},on:{"selection-change":e.handleSelectionChange}},[a("el-table-column",{attrs:{type:"selection",width:"55",align:"center"}}),e._v(" "),a("el-table-column",{attrs:{prop:"name",label:"账号",width:"150"}}),e._v(" "),a("el-table-column",{attrs:{prop:"phone",label:"手机号",width:"150"}}),e._v(" "),a("el-table-column",{attrs:{prop:"role",label:"状态",width:"150"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"260",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(a){e.handleEdit(t.$index,t.row)}}},[e._v("编辑")]),e._v(" "),a("el-button",{staticClass:"red",attrs:{type:"text",icon:"el-icon-delete"},on:{click:function(a){e.handleDelete(t.$index,t.row)}}},[e._v("删除")]),e._v(" "),a("el-button",{staticClass:"blue",attrs:{type:"text",icon:"el-icon-refresh"},on:{click:function(a){e.handlereset(t.$index,t.row)}}},[e._v("重置密码")])]}}])})],1),e._v(" "),a("div",{staticClass:"pagination"},[a("el-pagination",{attrs:{background:"",layout:"prev, pager, next",total:e.totalnum},on:{"current-change":e.handleCurrentChange}})],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"编辑",visible:e.editVisible,width:"30%"},on:{"update:visible":function(t){e.editVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"70px"}},[a("el-form-item",{attrs:{label:"账号"}},[a("el-input",{model:{value:e.form.name,callback:function(t){e.$set(e.form,"name",t)},expression:"form.name"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"手机号111"}},[a("el-input",{model:{value:e.form.phone,callback:function(t){e.$set(e.form,"phone",t)},expression:"form.phone"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"状态"}},[a("el-input",{model:{value:e.form.role,callback:function(t){e.$set(e.form,"role",t)},expression:"form.role"}})],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.editVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.saveEdit}},[e._v("确 定")])],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"新增用户",visible:e.addVisible,width:"30%"},on:{"update:visible":function(t){e.addVisible=t}}},[a("el-form",{ref:"form",attrs:{model:e.form,"label-width":"80px"}},[a("el-form-item",{attrs:{label:"账号"}},[a("el-input",{attrs:{placeholder:"输入用户名"},model:{value:e.form.addname,callback:function(t){e.$set(e.form,"addname",t)},expression:"form.addname"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"密码"}},[a("el-input",{attrs:{placeholder:"输入密码"},model:{value:e.form.addpassword,callback:function(t){e.$set(e.form,"addpassword",t)},expression:"form.addpassword"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"手机号"}},[a("el-input",{attrs:{placeholder:"手机号"},model:{value:e.form.addphone,callback:function(t){e.$set(e.form,"addphone",t)},expression:"form.addphone"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"状态"}},[a("el-select",{attrs:{placeholder:"请选择用户"},model:{value:e.form.addrole,callback:function(t){e.$set(e.form,"addrole",t)},expression:"form.addrole"}},[a("el-option",{key:"0",attrs:{label:"管理员",value:"0"}}),e._v(" "),a("el-option",{key:"1",attrs:{label:"分拣员",value:"1"}}),e._v(" "),a("el-option",{key:"2",attrs:{label:"物业",value:"2"}}),e._v(" "),a("el-option",{key:"3",attrs:{label:"用户",value:"3"}})],1)],1),e._v(" "),a("el-form-item",{attrs:{label:"所属小区id"}},[a("el-input",{attrs:{placeholder:"所属小区id（当用户是物业或用户时必填）"},model:{value:e.form.villageId,callback:function(t){e.$set(e.form,"villageId",t)},expression:"form.villageId"}})],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.addVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:e.addtable}},[e._v("确 定")])],1)],1)],1)},staticRenderFns:[]};var i=a("VU/8")(l,o,!1,function(e){a("kykb")},"data-v-a9ed55c8",null);t.default=i.exports},kykb:function(e,t){}});