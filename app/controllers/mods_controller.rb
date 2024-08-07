class ModsController < ApplicationController
  def index
    @mods = Mod.where('course_code LIKE ? OR title LIKE ?', "%#{request.query_parameters[:search]}%", "%#{request.query_parameters[:search]}%")
  end

  def show
    @mod = Mod.find(params[:id])
    @reviews = Review.where(course_code: params[:id]).order(created_at: :desc)
  end
end
