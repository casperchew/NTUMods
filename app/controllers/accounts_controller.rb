class AccountsController < ApplicationController
  def show
    @reviews = Review.where(author: session[:username]).order(created_at: :desc)
  end

  def new
    @account = Account.new
  end

  def create
    @account = Account.new(account_params)

    if @account.save
      session[:username] = @account.username
      redirect_to :root
    else
      render :new, status: :unprocessable_entity
    end
  end

  def login_post
    puts params
    @account = Account.find_by(username: params[:username], password: params[:password])

    if @account
      session[:username] = @account.username
      redirect_to :root
    else
      puts 'Account not found'
      redirect_to '/login'
    end
  end

  def signout
    session.delete(:username)
    redirect_to :root
  end

  private
    def account_params
      params.require(:account).permit(:username, :password)
    end
end