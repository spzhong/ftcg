<template>
  <div class="table">
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item><i class="el-icon-lx-cascades"></i> 用户管理</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="container">
      <div class="handle-box">
        <el-button type="primary"
                   class="add"
                   icon="search"
                   @click="add">新增用户</el-button>
      </div>
      <el-table :data="tableData"
                border
                class="table"
                ref="multipleTable"
                @selection-change="handleSelectionChange">
        <el-table-column type="selection"
                         width="55"
                         align="center"></el-table-column>

        <el-table-column prop="name"
                         label="账号"
                         width="150">
        </el-table-column>
        <el-table-column prop="phone"
                         label="手机号"
                         width="150">
        </el-table-column>
        <el-table-column prop="role"
                         label="状态"
                         width="150">
        </el-table-column>
        <el-table-column label="操作"
                         width="260"
                         align="center">
          <template slot-scope="scope">
            <el-button type="text"
                       icon="el-icon-edit"
                       @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button type="text"
                       icon="el-icon-delete"
                       class="red"
                       @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            <el-button type="text"
                       icon="el-icon-refresh"
                       class="blue"
                       @click="handlereset(scope.$index, scope.row)">重置密码</el-button>

          </template>
        </el-table-column>
      </el-table>
      <!-- <div class="pagination">
        <el-pagination background
                       @current-change="handleCurrentChange"
                       layout="prev, pager, next"
                       :total="1000">
        </el-pagination>
      </div> -->
    </div>

    <!-- 编辑弹出框 -->
    <el-dialog title="编辑"
               :visible.sync="editVisible"
               width="30%">
      <el-form ref="form"
               :model="form"
               label-width="70px">
        <el-form-item label="账号">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="手机号">
          <el-input v-model="form.phone"></el-input>
        </el-form-item>
        <el-form-item label="状态">
          <el-input v-model="form.role"></el-input>
        </el-form-item>

      </el-form>
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="editVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="saveEdit">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 新增弹出框 -->
    <el-dialog title="新增用户"
               :visible.sync="addVisible"
               width="30%">
      <el-form ref="form"
               :model="form"
               label-width="80px">
        <el-form-item label="账号">
          <el-input v-model="form.addname"
                    placeholder="输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="form.addpassword"
                    placeholder="输入密码"></el-input>
        </el-form-item>
        <el-form-item label="手机号">
          <el-input v-model="form.addphone"
                    placeholder="手机号"></el-input>
        </el-form-item>
        <el-form-item label="状态">
          <!-- <el-input v-model="form.addrole"
                    placeholder="管理员0，分拣员1，物业2，用户3"></el-input> -->
          <el-select v-model="form.addrole"
                     placeholder="请选择用户">
            <el-option key="0"
                       label="管理员"
                       value="0"></el-option>
            <el-option key="1"
                       label="分拣员"
                       value="1"></el-option>
            <el-option key="2"
                       label="物业"
                       value="2"></el-option>
            <el-option key="3"
                       label="用户"
                       value="3"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="所属小区id">
          <el-input v-model="form.villageId"
                    placeholder="所属小区id（当用户是物业或用户时必填）"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addtable">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 重置密码提示框 -->
    <el-dialog title="重置密码"
               :visible.sync="resetVisible"
               width="30%">
      <div class="del-dialog-cnt">重置后将修改用户密码，请谨慎操作</div>
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="resetVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="onhandlereset">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
export default {
  name: 'basetable',
  data () {
    return {
      tableData: [],
      cur_page: 1,
      multipleSelection: [],
      select_cate: '',
      select_word: '',
      del_list: [],
      is_search: false,
      editVisible: false,
      addVisible: false,
      resetVisible: false,
      form: {
        name: '',
        role: '',
        phone: ''
      },
      idx: -1,
      uid: '',
    }
  },
  created () {
    this.getData();
  },
  computed: {
    // newdata () {

    // }
  },
  methods: {
    // 分页导航
    // handleCurrentChange (val) {
    //   this.cur_page = val;
    //   this.getData();
    // },
    // 获取用户数据
    getData () {
      this.url = '/chenjie/testftcg/user/getAllUserList?token=' + localStorage.token;
      this.$axios.get(this.url, ).then((res) => {

        if (res.data.code = 1) {
          this.tableData = res.data.msg
          var newtable = this.tableData
          this.tableData.some((item) => { // item为数组中的元素，index为下标，arr为目标数组
            var toStr = {
              0: '管理员',
              1: '分拣员',
              2: '物业',
              3: '用户'
            };
            this.tableData.map(function (value) {
              var role = value.role;
              value.role = toStr[role] ? toStr[role] : role;
              return value;
            });
          })
        } else {
          console.log("不知出啥问题了")
        }
        //[this.tableData[1], this.tableData[3]] = [this.tableData[3], this.tableData[1]];
      })
    },
    search () {
      this.is_search = true;
    },
    add () {
      this.addVisible = true
    },
    addtable () {
      console.log(this.form.addname)
      if (this.form.addname == null || this.form.addpassword == null || this.form.addrole == null) {
        this.$message.error('请输入数据后再提交');
        return
      }
      else if (process.env.NODE_ENV === 'development') {
        this.url = '/chenjie/testftcg/user/register?token=' + localStorage.token + '&name=' + this.form.addname + '&password=' + this.$md5(this.$md5(this.form.addpassword)) + '&role=' + this.form.addrole + '&phone=' + this.form.addphone + '&villageId=' + this.form.villageId;
      }
      this.$axios.get(this.url, ).then((res) => {
        if (res.data.code != 1) {
          this.$message.error(res.data.msg);
        } else if (res.data.code = 1) {
          this.$message.success('用户创建成功');
          this.addVisible = false;
          this.form.villageId = '';
          this.form.addpassword = '';
          this.form.addname = '';
          this.form.addphone = '';
          this.form.addrole = '';
          this.getData()
        }
      })
    },
    filterTag (value, row) {
      return row.tag === value;
    },
    handleEdit (index, row) {
      this.$message.error('创建后暂不支持修改用户信息，如需操作，请联系运维管理');
      // this.idx = index;
      // const item = this.tableData[index];
      // this.form = {
      //   name: item.name,
      //   role: item.role,
      //   phone: item.phone
      // }
      // this.editVisible = true;
    },
    handlereset (res) {
      this.resetVisible = true;
      this.uid = this.tableData[res].id
    },
    onhandlereset () {
      this.url = '/chenjie/testftcg/user/adminResetPassword?token=' + localStorage.token + '&userId=' + this.uid;
      this.$axios.get(this.url, ).then((res) => {
        if (res.data.code != 1) {
          this.$message.error(res.data.msg);
          this.resetVisible = false;
        } else
          if (res.data.code = 1) {
            this.resetVisible = false;
            this.$message.error('重置成功！新密码为用户的手机号');
          } else {
            console.log("不知出啥问题了")
          }
      })
    },
    handleDelete (index, row) {
      // this.idx = index;
      // this.delVisible = true;
      this.$message.error('用户信息不能删除，请谨慎操作，如需操作，请联系运维管理');
    },
    handleSelectionChange (val) {
      this.multipleSelection = val;
    },
    // 保存编辑
    saveEdit () {
      // this.$set(this.tableData, this.idx, this.form);
      // this.editVisible = false;
      // this.$message.success(`修改第 ${this.idx + 1} 行成功`);
      this.$message.success(`等待修改接口api`);
    },
    // 确定删除

  }
}

</script>

<style scoped>
.handle-box {
  margin-bottom: 20px;
  text-align: right;
}

.handle-select {
  width: 120px;
}

.handle-input {
  width: 300px;
  display: inline-block;
}
.del-dialog-cnt {
  font-size: 16px;
  text-align: center;
}
.table {
  width: 100%;
  font-size: 14px;
}
.red {
  color: #ff0000;
}
.add {
  margin-right: 30%;
}
.login-tips {
  font-size: 12px;
  line-height: 30px;
  color: red;
}
</style>
