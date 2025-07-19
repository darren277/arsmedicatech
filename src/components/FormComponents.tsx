import * as React from 'react';

/**
 * Minimal clsx/cn helper so we don't introduce an extra dependency.
 */
const cn = (...classes: (string | false | null | undefined)[]) =>
  classes.filter(Boolean).join(' ');

/* -------------------------------------------------------------------------------------------------
 * Button
 * -------------------------------------------------------------------------------------------------*/
export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** Visual style */
  variant?: 'primary' | 'secondary' | 'ghost' | 'destructive';
  /** Size */
  size?: 'sm' | 'md' | 'lg';
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'primary', size = 'md', ...props }, ref) => {
    const variantClasses: Record<string, string> = {
      primary: 'bg-primary text-white hover:bg-primary/90',
      secondary: 'bg-muted text-foreground hover:bg-muted/80',
      ghost: 'bg-transparent hover:bg-accent',
      destructive:
        'bg-destructive text-destructive-foreground hover:bg-destructive/90',
    };

    const sizeClasses: Record<string, string> = {
      sm: 'h-8 px-3 text-sm',
      md: 'h-10 px-4 text-base',
      lg: 'h-12 px-6 text-lg',
    };

    return (
      <button
        ref={ref}
        className={cn(
          'inline-flex items-center justify-center font-medium focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none rounded-2xl transition-colors',
          variantClasses[variant],
          sizeClasses[size],
          className
        )}
        {...props}
      />
    );
  }
);
Button.displayName = 'Button';

/* -------------------------------------------------------------------------------------------------
 * Card & CardContent
 * -------------------------------------------------------------------------------------------------*/
export interface CardProps extends React.HTMLAttributes<HTMLDivElement> {}
export const Card = React.forwardRef<HTMLDivElement, CardProps>(
  ({ className, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        'bg-card text-card-foreground rounded-2xl shadow-md',
        className
      )}
      {...props}
    />
  )
);
Card.displayName = 'Card';

export const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn('p-6', className)} {...props} />
));
CardContent.displayName = 'CardContent';

/* -------------------------------------------------------------------------------------------------
 * Input
 * -------------------------------------------------------------------------------------------------*/
export interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {}
export const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, ...props }, ref) => (
    <input
      ref={ref}
      className={cn(
        'flex h-10 w-full rounded-2xl border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
        className
      )}
      {...props}
    />
  )
);
Input.displayName = 'Input';

/* -------------------------------------------------------------------------------------------------
 * Checkbox
 * -------------------------------------------------------------------------------------------------*/
export interface CheckboxProps
  extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: React.ReactNode;
}
export const Checkbox = React.forwardRef<HTMLInputElement, CheckboxProps>(
  ({ className, label, ...props }, ref) => (
    <label className="inline-flex items-center gap-2 cursor-pointer select-none">
      <input
        ref={ref}
        type="checkbox"
        className={cn(
          'peer h-5 w-5 shrink-0 appearance-none rounded-md border border-input bg-background flex items-center justify-center focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 checked:bg-primary checked:border-primary',
          className
        )}
        {...props}
      />
      <span className="peer-disabled:opacity-50">{label}</span>
    </label>
  )
);
Checkbox.displayName = 'Checkbox';

export const IconButton = React.forwardRef<
  HTMLButtonElement,
  React.ButtonHTMLAttributes<HTMLButtonElement> & { icon: React.ReactNode }
>(({ icon, className, ...props }, ref) => (
  <button
    ref={ref}
    className={cn(
      'inline-flex items-center justify-center rounded-full p-2 transition-colors focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none disabled:bg-gray-100 disabled:text-gray-400',
      className
    )}
    {...props}
  >
    {icon}
  </button>
));
IconButton.displayName = 'IconButton';

export const RequiredAsterisk = () => (
  <span className="text-red-500 ml-0.5" title="Required">
    *
  </span>
);

export const Label = React.forwardRef<
  HTMLLabelElement,
  React.LabelHTMLAttributes<HTMLLabelElement>
>(({ className, ...props }, ref) => (
  <label
    ref={ref}
    className={cn('text-sm font-medium', className)}
    {...props}
  />
));
Label.displayName = 'Label';
