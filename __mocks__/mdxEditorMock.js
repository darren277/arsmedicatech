import React from 'react';

// Mock MDXEditor component
export const MDXEditor = React.forwardRef(
  (
    {
      markdown,
      onChange,
      readOnly,
      className,
      contentEditableClassName,
      plugins,
      ...props
    },
    ref
  ) => {
    return React.createElement(
      'div',
      {
        ref,
        className,
        'data-testid': 'mdx-editor',
        contentEditable: !readOnly,
        onInput: e => {
          if (onChange && !readOnly) {
            onChange(e.target.textContent || '');
          }
        },
        ...props,
      },
      markdown
    );
  }
);

// Mock all the plugins as empty objects
export const BoldItalicUnderlineToggles = () => null;
export const CreateLink = () => null;
export const InsertImage = () => null;
export const InsertTable = () => null;
export const ListsToggle = () => null;
export const UndoRedo = () => null;
export const toolbarPlugin = () => ({ toolbarContents: () => null });
export const headingsPlugin = () => ({});
export const listsPlugin = () => ({});
export const quotePlugin = () => ({});
export const thematicBreakPlugin = () => ({});
export const markdownShortcutPlugin = () => ({});
export const linkPlugin = () => ({});
export const linkDialogPlugin = () => ({});
export const imagePlugin = () => ({});
export const tablePlugin = () => ({});
export const codeBlockPlugin = () => ({});
export const codeMirrorPlugin = () => ({});
export const sandpackPlugin = () => ({});
export const frontmatterPlugin = () => ({});
export const AdmonitionDirectiveDescriptor = {};
export const diffSourcePlugin = () => ({});
