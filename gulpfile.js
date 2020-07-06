var gulp = require('gulp'), 
		sass = require('gulp-sass'); 

gulp.task('sass', function() { 
	return gulp.src(['venv/src/static/sass/**/*.sass', 'venv/src/static/sass/**/*.scss']) 
		.pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError)) 
		.pipe(gulp.dest('venv/src/static/css')) 
	});

gulp.task('watch', function() {
	gulp.watch(['venv/src/static/sass**/*.sass', 'venv/src/static/sass/**/*.scss'], gulp.parallel('sass')); 
});

gulp.task('default', gulp.parallel('watch'));
