SIG: Semantic Convention SIG
Date: 2026-07-27
Duration: 21 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:36 Hello.
**Liudmila Molkova** 00:38 Oh.
Hi, Christoph. Hi, John.
**Joe Josue** 00:44 Good evening.
Oh, for me.
**Liudmila Molkova** 01:31 Quiet today.
Okay, then, while the people are joining… Do a triage… Okay, nothing ready to be merged. A couple of blocked things… Let's see if anything has changed… We've been waiting on the prototype, and no updates here.
Where's this one blocked?
Job blocked it.
Not sure, but maybe it's worth another look?
From Zhao or Patrice… Okay, we have a few entriage things… Let's see… this is in… Draft… This is a NOS… For system semantic conventions, this is awaiting code owner approval.
And we are also awaiting co-donor approval here.
Okay, C… If we have anything that can be moved along… Non… non-approvals, no approvals… Okay, job approved.
But I think we are waiting for Patrice to take a look, and he didn't yet.
This is still awaiting, I think there were some updates recently.
Yeah, okay, this is on me to take another look.
Not sure if there is anybody who is interested in databases, but… Oracle, has now a formal way to propagate trace context from application to the database.
Which is pretty exciting, and we are discussing if the… An existing hockey approach can be retired.
Okay, there is a discussion.
But yeah, if you are interested in databases… This is an awesome change.
**Christophe Kamphaus** 05:01 I checked the Oracle documentation, and I didn't see it documented on their site which key to use.
I guess they want to document it here.
**Liudmila Molkova** 05:13 Okay, we can ask, sundar the document, just because he drives it from the Oracle side.
Would you be interested in… Check in with.
**Christophe Kamphaus** 05:26 American.
**Liudmila Molkova** 05:29 Nice, thank you.
Okay… Let's take a look at… A couple more to see if… They are in the right spot, yes, it's in the right spot, not provo so far.
And… no approvals here yet.
Okay, we don't have much on the agenda. I want to talk VTU migration.
But do people have any other topics they want to discuss first?
Oh, okay.
I'm not stuck with migration.
And maybe even before that, I see Ruediger, you're here. There is something that you might be interested?
You're misshoc?
So we… now we have merged, the… common templates.
For, that can be used across different conventions repos.
So, they live here.
There are some docs.
They are configurable, you can pick what you want to have.
The previous Hawks… was, like.
I don't remember which were they, but they… we don't need them anymore.
There are, like, these configuration options of whether you want the registry, or if you want, the markdown snippets, And you can pick one or another, or both.
There are some toggles, like excluding deprecated stuff, rendering stable things only.
And there is a configuration for… upstream docks. So, like, you would have a weaver tunnel, and in this weaver tunnel, you would have the section, and it would tell the mapping.
For each of your, schema URLs of which documents you want to include.
So this, this is used in, in the markdown tables, and… Like, when you reference an attribute from upstream, this is how you get the right link to… the upstream docs.
There is an example, like… In the PR… It was introduced then.
**Ruediger Schulze (IBM)** 08:46 Yeah, this is great, actually, that that merged already, comes right in time. I have more time this week to focus on this, so… let me try it out, and I will let you know.
**Liudmila Molkova** 08:58 Awesome, yeah!
That, that's great, yeah, so, like, if you have any questions, or… Boom.
for any of swords, so you can see, an example here.
It's slightly different.
than Semantic conventions. So, like, instead of breaking up by signals, we break up by namespaces.
And you would have, like, ZOS, and under it you would have wait.
Oh, I broke it, I think.
Give me a sec.
We'll get to the proper… Amit.
I don't know.
Purchased, yeah.
Yeah, so… Each namespace has a page, read me?
And there are definition… like, it's the pointers to definitions of metrics, bands, entities, if they were defined here.
And then instead of having a page for attributes, like AttributesMD, we have them dumped here.
Just to deprioritize attributes a little bit.
And then the… this is the… everything is auto-generated here. It's the detailed information about each signal.
Try it out if you have any problems, if you would like to tweak something in the templates.
Go ahead, let me know.
**Ruediger Schulze (IBM)** 11:06 We do. Yeah, no, this looks good, Actually, yeah, like I said, this comes the right time. I would try it.
**Liudmila Molkova** 11:16 Awesome Okay.
And then… We don't use them in Semantic Conventions Repo yet, but they have a PR switching.
GenAI semantic conventions to this.
Sorry, not V3, V2.
Let me leave a link in case somebody… We'll read the notes… Okay, and then another thing I want to share that's also might be interesting for you, Ruediger, is… V2 migration. We didn't… I didn't do anything about, this friend yet, but it's unblocked.
I… if you're… I don't know, should we… we probably should migrate it into V2 in this repo, and then deprecate.
Would you be interested in trying it out? Would you rather somebody else do it?
**Ruediger Schulze (IBM)** 12:45 So this was the… This was the, the refinement… yeah, right, I remember this. We refined the additional attributes there, right?
From the… well, the examples of the attributes, right?
Yeah, I can try that as well. Let me look at that.
**Liudmila Molkova** 13:06 Yeah, that would be awesome, because, it would also… be a chance to get familiar with V2 and maybe find any problems with this.
Where… Somebody who… Doesn't have bias.
Yeah.
Yeah, so we are effectively unblocked. There are… it was all the items here.
I have a pure… Demonstrating what we can do for, attributes groups. So, this France, like, okay, so this list is a list of attribute groups we render somewhere.
in the… Semantic conventions.
All other attributed groups are internal. They are just the way to avoid copy-paste.
But those have documentation.
And I'm thinking, we need to… If we keep them as internal attribute groups, we won't be able to render them.
So they are becoming a new thing called public attribute groups.
And… You can see it here, so… the… we had these groups, with ID, there is… there was a group ID, there was a secret contract that it must be called registry, something.
And then attributes were defined in this group. It had… A brief, a display name.
So with V2, it's no longer how it works, we have just the all-attributes section.
And it's not grouped, like, you can break them down into multiple files, or you can, merge multiple files, and then all the attributes become a big List of independent things.
But since server address and server port are related, they come together, you probably don't want one without another.
We are introducing, server group?
With visibility public.
And it gets the brief that we used to have on the server attributes.
When it's rendered, It's… No longer rendered in the registry.
Here.
So, the registry of attributes loses this group description because there is no group from Attribute Registry.
But we have a dock.
That describes… Like, the semantics of the… this.
And this is where this description comes back.
The rest, like the list of attributes, remains unchanged.
And… SBR… I'll also flood some, Additional stuff to make it all work, properly, just a little bit of templating.
And… It covers the server client source destination.
And I still have a few… Of them remaining.
And I wanted to check if we actually need to… Migrate all of them.
So, for example, we have open tracing.
group.
And open tracing migration pass is being deprecated, or is already deprecated in the spec.
So I'm thinking the corresponding group, we can just deprecate and stop rendering.
They will still remain in the attribute registry in case somebody needs them.
And… I'm thinking… About… Let me find it.
About this friend, I lost it.
Again.
Would anybody worry?
if we… stop rendering it. I don't know, if it's… it should be a group.
I don't… I'm not aware of any conventions that actually use it, and we can always add a public group when Some conventions would need it.
A.
Okay.
I don't hear any… thoughts?
So I assume it's okay.
Yeah, that's essentially all I had.
If people don't have any other topics, we can call it.
**Ruediger Schulze (IBM)** 19:32 Good, thank you.
**Christophe Kamphaus** 19:37 See ya!
**Liudmila Molkova** 19:37 Okay, nice. Good to see you all.
**Ruediger Schulze (IBM)** 19:40 Sorry.
**Armin (Dynatrace)** 19:41 Thank you. Bye-bye.
