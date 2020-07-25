# Develop: vmgabriel

"""Test Cases"""

# Libraries
from django.test import TestCase
from django.utils import timezone

# Models
from .models import Repeter, Priority, Category, TypeConsume, \
    Consume, TypeBill, Bill, Transaction


def get_data_basic():
    """Return Basic data Dict"""
    return {
        'name': 'test',
        'description': 'test description',
        'is_delete': False
    }


def create_priority():
    """Create a Priority Test and Save"""
    data_priority = get_data_basic()
    # Creating Priority Data
    return Priority.objects.create(**data_priority)


def create_category():
    """Create a Category Test and Save"""
    data_category = get_data_basic()
    data_category['priority'] = create_priority()

    return Category.objects.create(**data_category)


def create_type_consume():
    """Create a Type Consume Test and Save"""
    data_type_consume = get_data_basic()
    return TypeConsume.objects.create(**data_type_consume)


def create_repeter():
    """Create a Repeter Test and Save"""
    data = {
        'name': 'test',
        'description': 'test description',
        'hourly': 1,
        'each_day': 0,
        'weekly': 1,
        'each_month': 0,
        'each_year': 0,
        'is_delete': False
    }
    return Repeter.objects.create(**data)


def create_type_bill():
    """Create Type Bill"""
    data = get_data_basic()
    return TypeBill.objects.create(**data)


def create_consume():
    """Create Consume Test and Save"""
    data = get_data_basic()
    data['category'] = create_category()
    data['type_consume'] = create_type_consume()
    return Consume.objects.create(**data)


def create_bill():
    """Create a Bill Test and Save"""
    data = {
        'name': 'test',
        'description': 'test description',
        'date': timezone.now(),
        'is_delete': False,
        'is_repeter': True,
        'repeter': create_repeter(),
        'type_bill': create_type_bill()
    }
    return Bill.objects.create(**data)


class RepeterModelTests(TestCase):
    """
    Implementing data of reporter Test Model
    """

    def test_repeter_was_created(self):
        """Repeter was Created"""
        data = {
            'name': 'test',
            'description': 'test description',
            'hourly': 1,
            'each_day': 0,
            'weekly': 1,
            'each_month': 0,
            'each_year': 0,
            'is_delete': False
        }

        test_data = 'name: {}, hourly: {}, each day: {}, '
        test_data += 'weekly: {}, each month: {}'
        test_data = test_data.format(
            data['name'],
            data['hourly'],
            data['each_day'],
            data['weekly'],
            data['each_month']
        )

        obje = Repeter(**data)
        self.assertEqual(str(obje), test_data)

    def test_repeter_was_saved(self):
        """Repeter Was Saved into Persistence"""
        data = create_repeter()
        self.assertEqual(1, data.id)


class PriorityModelTests(TestCase):
    """
    Implementing test of Prority Model
    """

    def test_priority_was_created(self):
        """Priority was Created"""
        data = get_data_basic()

        test_data = 'name: {}, is deleted: {}'
        test_data = test_data.format(data['name'], data['is_delete'])

        obje = Priority(**data)
        self.assertEqual(str(obje), test_data)

    def test_priority_was_saved(self):
        """Verify if this is saved into database"""
        data = create_priority()
        self.assertEqual(1, data.id)


class CategoryModelTests(TestCase):
    """
    Implementing test of Category Model
    """

    def test_category_was_created(self):
        """Category was Created"""
        data = get_data_basic()
        data['priority'] = create_priority()

        test_data = 'name: {}, is deleted: {}'
        test_data = test_data.format(data['name'], data['is_delete'])

        obje = Category(**data)
        self.assertEqual(str(obje), test_data)

    def test_category_was_saved(self):
        """Category was Created and Save"""
        data = create_category()
        self.assertEqual(1, data.id)


class TypeConsumeModelTests(TestCase):
    """
    Implementing test of Type Consume Model
    """

    def test_type_consume_was_created(self):
        """Category was Created"""
        data = get_data_basic()

        test_data = 'name: {}, is deleted: {}'
        test_data = test_data.format(data['name'], data['is_delete'])

        obje = TypeConsume(**data)
        self.assertEqual(str(obje), test_data)

    def test_consume_type_was_saved(self):
        """Category was Saved"""
        data = create_type_consume()
        self.assertEqual(1, data.id)


class ConsumeModelTests(TestCase):
    """
    Implementing test of Consume Model
    """

    def test_consume_was_created(self):
        """Consume was Created"""
        data = get_data_basic()
        data['category'] = create_category()
        data['type_consume'] = create_type_consume()

        test_data = 'name: {}, is deleted: {}'
        test_data = test_data.format(data['name'], data['is_delete'])

        obje = Consume(**data)
        self.assertEqual(str(obje), test_data)

    def test_consume_was_saved(self):
        """Consume was Saved into Persistence"""
        data = create_consume()
        self.assertEqual(1, data.id)


class TypeBillModelTests(TestCase):
    """
    Implementing test of Type Bill Model
    """

    def test_type_bill_was_created(self):
        """Type Bill was Created"""
        data = get_data_basic()

        test_data = 'name: {}, is deleted: {}'
        test_data = test_data.format(data['name'], data['is_delete'])

        obje = TypeBill(**data)
        self.assertEqual(str(obje), test_data)

    def test_type_bill_was_saved(self):
        """Type Bill was Save into persistence"""
        data = create_type_bill()
        self.assertEqual(1, data.id)


class BillModelTests(TestCase):
    """
    Implementing test of Bill Model
    """

    def test_bill_was_created(self):
        """Test Bill Model Test was Created"""
        data = {
            'name': 'test',
            'description': 'test description',
            'date': timezone.now(),
            'is_delete': False,
            'is_repeter': True,
            'repeter': create_repeter(),
            'type_bill': create_type_bill()
        }

        test_data = 'name: {}, date: {}, is_repeter: {}'
        test_data = test_data.format(
            data['name'],
            data['date'],
            data['is_repeter']
        )

        obje = Bill(**data)
        self.assertEqual(str(obje), test_data)

    def test_bill_was_saved(self):
        """Test Bill Model Test Was Saved"""
        data = create_bill()
        self.assertEqual(1, data.id)


class TransactionModelTests(TestCase):
    """
    Implementing test of Transaction Model
    """
    def test_transaction_was_created(self):
        """Test Transaction Model Test was Created"""
        data = {
            'description': 'test description',
            'date_payed': timezone.now(),
            'is_delete': False,
            'consume': create_consume(),
            'bill': create_bill()
        }

        test_data = 'date payed: {}, is deleted: {}'
        test_data = test_data.format(data['date_payed'], data['is_delete'])

        obje = Transaction(**data)
        self.assertEqual(str(obje), test_data)
