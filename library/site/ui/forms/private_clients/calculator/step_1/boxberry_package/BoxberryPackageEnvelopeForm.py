import allure

from .BasePackageForm import BasePackageForm


class PackageEnvelopeForm(BasePackageForm):
    def get_packages(self):
        with allure.step('Считать данные об упаковках'):
            packages = []
            cnt = self.count(self.css_package_item)
            for i in range(cnt):
                package = {}
                locator = f'{self.css_package_item}:nth-child({i + 1})'
                package['Название'] = self.inner_text(f'{locator} .calc-radio-btn__name').strip()
                package['Описание'] = self.inner_text(f'{locator} .calc-radio-btn__desc').strip()
                state = self.get_attribute(locator, 'class')
                if 'active' in state:
                    package['Статус'] = 'Выбран'
                else:
                    package['Статус'] = 'Не выбран'

                packages.append(package)
                allure.attach(str(packages), f'Упаковки: {packages}', allure.attachment_type.JSON)

        return packages
