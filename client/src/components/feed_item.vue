<template>
  <div class="pb-3">
    <div
      class="card-body feed-html-container"
      v-html="entry.content['#text']"
    />
    <div class="p-3">
      <button type="button" class="btn btn-primary float-right">
        Read Later
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeedItem',
  props: {
    entry: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>
.feed-html-container {
  padding-bottom: 0 !important;
}
</style>
