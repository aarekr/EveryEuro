class SessionsController < ApplicationController
  def new
    # renders sign in page
  end

  def create
    user = User.find_by username: params[:username]
    if user
      if user.authenticate(params[:password])
        session[:user_id] = user.id
        redirect_to user_path(user), notice: "Welcome back!"
      end
    else
      redirect_to signin_path, notice: "Username and/or password mismatch"
    end
  end

  def destroy
    session[:user_id] = nil
    redirect_to :root
  end
end
