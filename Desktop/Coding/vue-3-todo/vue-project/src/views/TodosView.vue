<script setup>
const name = "Varoon";
</script>

<template>
  <div class="welcome-msg">
    <h1>Welcome back, {{ name }}</h1>
  </div>
</template>

<style lang="scss" scoped>
.welcome-msg {
  margin: 2% 2%;
}
</style>

<!-- <script setup>
import { ref } from "vue";
import { uid } from 'uid';
import TodoCreator from '../components/TodoCreator.vue';
const todoList = ref([]);

const createTodo = (todo) => {
  todoList.value.push({
    id: uid(),
    todo,
    isCompleted: null,
    isEditing: null,
  })
}
</script>

<template>
  <main>
    <h1>Create Todo</h1>
    <TodoCreator @create-todo="createTodo" />
  </main>
</template>

<style lang="scss" scoped>
    * {
      text-align: center;
      margin-top: 10px;
    }
</style> -->