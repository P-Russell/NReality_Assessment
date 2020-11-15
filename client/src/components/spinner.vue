<template>
  <div
    class="spinner-grow text-secondary"
    :style="`width: ${size}rem; height: ${size}rem;`"
    role="status"
  >
    <span class="sr-only">Loading...</span>
  </div>
</template>

<script>
export default {
  name: 'Spinner',
  props: {
    size: {
      type: Number,
      default: 1,
    },
  },
}
</script>

<style></style>
