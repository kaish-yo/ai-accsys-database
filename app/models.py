# Models(classes) used as schemas for tables in the database
from .database import Base
from sqlalchemy.schema import Column
from sqlalchemy.types import BigInteger, Boolean, Date, DateTime, Float, Integer, String

# table names
GL_TABLE = 'general_ledger'
USER_TABLE = 'users'
ACC_TABLE = 'account_master'
VAT_TABLE = 'vat_master' # almost static


class GeneralLedger(Base):
    __tablename__ = GL_TABLE
    record_id = Column(Integer, primary_key=True)
    journal_id = Column(Integer, nullable=False)
    account_id = Column(BigInteger, nullable=False)
    account_name = Column(String(50), nullable=True)
    subaccount_id = Column(BigInteger, nullable=False)
    vat_id = Column(Integer, nullable=False)
    debter_creditor = Column(String, nullable=False)
    amount = Column(Float(), nullable=False)
    creator_id = Column(Integer(), nullable=False)
    approver_id = Column(Integer(), nullable=False)
    create_date = Column(DateTime(), nullable=False)
    approve_date = Column(DateTime(), nullable=False)
    
    def to_dict(self):
        return {
            'record_id': self.record_id,
            'journal_id': self.journal_id,
            'account_id': self.account_id,
            'account_name': self.account_name,
            'subaccount_id': self.subaccount_id,
            'vat_id': self.vat_id,
            'debter_creditor': self.debter_creditor,
            'amount': self.amount,
            'creator': self.creater,
            'approver': self.approver,
            'create_date': self.create_date,
            'approve_date': self.approve_date
        }


class User(Base):
    __tablename__ = USER_TABLE
    user_id = Column(BigInteger, primary_key=True)
    user_name = Column(String(50), nullable=False)
    title = Column(String(50), nullable=False)
    last_title = Column(String(50), nullable=True)
    join_date = Column(Date, nullable=False)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'title': self.title,
            'last_title': self.last_title,
            'join_date': self.join_date
        }


class Account(Base):
    __tablename__ = ACC_TABLE
    account_id = Column(BigInteger, primary_key=True)
    account_name = Column(String(50), nullable=False)    
    
    def to_dict(self):
        return {
            'account_id': self.account_id,
            'account_name': self.account_name
        }


class Vat(Base):
    __tablename__ = VAT_TABLE
    vat_id = Column(Integer, primary_key=True)
    vat_category = Column(String(50))
    
    def to_dict(self):
        return {
            'vat_id': self.vat_id,
            'vat_category': self.vat_category
        }