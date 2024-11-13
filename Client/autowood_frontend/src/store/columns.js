import { useI18n } from 'vue-i18n';

export function useColumns() {
  const { t } = useI18n();

  const columns = [
    { 
      field: 'name', 
      label: t('name'), // Use i18n translation
      searchable: true
    },
    { 
      field: 'category', 
      label: t('category'), // Use i18n translation
      searchable: true 
    },
    { 
      field: 'collection', 
      label: t('collection'), // Use i18n translation
      searchable: true
    },
    { 
      field: 'wood', 
      label: t('wood_type'), // Use i18n translation
      searchable: true 
    },
    { 
      field: 'paints',
      label: t('painting'), // Use i18n translation
      searchable: true 
    },
    {
      field: 'nawigacja',
      label: t('Nav') // Use i18n translation
    }
  ];

  return { columns };
}
