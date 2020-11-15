import { API } from '../plugins/api'

const api = new API()

export const state = () => ({
  entries: '__LOADING__',
  filter: null,
})

export const mutations = {
  setEntries(state, entries) {
    state.entries = entries
  },
  removeEntry(state, entryId) {
    state.entries = state.entries.filter((entry) => entry.id !== entryId)
  },
}

export const getters = {
  entries: (state) => {
    return state.entries
  },
}

export const actions = {
  async fetchEntries({ commit }, data) {
    commit('setEntries', '__LOADING__')
    const entries = await api.fetchFeed(data.handle, data.readLater)
    commit('setEntries', entries)
  },
  async setReadLater({ commit }, data) {
      await api.addToReadLater(data.handle, data.entryId)
      commit('removeEntry', entryId)
  }
}
