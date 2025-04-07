class ReviewsController < ApplicationController
  def new
    if params[:course_code]
      @review = Review.new
    else
      redirect_to :root
    end
  end

  def create
    @review = Review.new(
      course_code: params[:course_code],
      author: session[:username],
      review: params[:review][:review]
    )

    puts params[:course_code]
    mod_path(Mod.find(params[:course_code]))

    if @review.save
      redirect_to mod_path(Mod.find(params[:course_code]))
    else
      render :new, status: :unprocessable_entity
    end
  end

  def edit
    @review = Review.find(params[:id])
  end

  def update
    @review = Review.find(params[:id])

    if @review.update(
      course_code: params[:course_code],
      author: session[:username],
      review: params[:review][:review]
    )
      redirect_to mod_path(params[:course_code])
    else
      render :edit, status: :unprocessable_entity
    end
  end

  def destroy
    @review = Review.find(params[:id])
    @review.destroy
    
    redirect_to mod_path(params[:id])
  end
end
