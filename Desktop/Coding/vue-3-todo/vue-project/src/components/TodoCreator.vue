<script setup>
import { reactive, defineEmits } from "vue";
import TodoButton from "./TodoButton.vue";

const emit = defineEmits(['create-todo']) // define emits method allows us to define an array of items that we want to emit from our component
const todoState = reactive({
    todo: "",
    invalid: null,
    errMsg: "",
});

const createTodo = () => {
    todoState.invalid = null;
    if (todoState.todo != "") {
        emit("create-todo", todoState.todo);
        todoState.todo = "";
        return;
    }
    todoState.invalid = true;
    todoState.errMsg = "Todo value cannot be empty"
};
</script>

<template>
    <div class="input-wrap">
        <input type="text" v-model="todoState.todo" :class="{ 'input-err' : todoState.invalid }" />
        <TodoButton @click="createTodo()"/>
    </div>
    <p v-show="todoState.invalid" class="err-msg">{{ todoState.errMsg }}</p>
</template>

<style lang="scss" scoped>
    * {
        text-align: center;
        margin-top: 10px;
    }
    .input-wrap {
        display: flex;
        gap: 0px;
        justify-content: center;
        input {
            font-size: 15px;
            width: 30%;
            padding: 0.5% 1%;
            text-align: left;
        }
    }
    .input-err {
        border-color: red;
    }
    .err-msg {
        margin-top: 6px;
        font-size: 12px;
        text-align: center;
        color: red;
    }
</style>