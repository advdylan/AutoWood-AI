import { useI18n } from 'vue-i18n';

export function useColumns() {
  const { t } = useI18n();

  const columns = [
    { 
      field: 'name', 
      label: t('name'), 
      searchable: true
    },
    { 
      field: 'category', 
      label: t('category'), 
      searchable: true 
    },
    { 
      field: 'collection', 
      label: t('collection'),
      searchable: true
    },
    { 
      field: 'wood', 
      label: t('wood_type'), 
      searchable: true 
    },
    { 
      field: 'paints',
      label: t('painting'), 
      searchable: true 
    },
    {
      field: 'nawigacja',
      label: t('Nav') 
    }
  ];

  return { columns };
}
