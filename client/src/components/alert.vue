<template>
  <div :class="`alert alert-${type} fade show py-3 px-5 m-2`" role="alert">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'Alert',
  props: {
    type: {
      type: String,
      required: true,
    },
  },
}
</script>
