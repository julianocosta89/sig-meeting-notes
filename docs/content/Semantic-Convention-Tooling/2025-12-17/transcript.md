SIG: Semantic Convention Tooling
Date: 2025-12-17
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:37 Aww, I ran up.
ariannavespri 00:00:40 Hello, hello, Dunmila.
Don't time no here. How are you?
Liudmila Molkova 00:00:45 I'm fine, thanks, how are you?
ariannavespri 00:00:47 I'm fine, I just, I recently started working for, for Oli Garden with Jurassic.
So now I'm very invested in OpenTelemetry, so… Yeah.
Arthur Silva Sens 00:00:58 Hello, Ariana.
ariannavespri 00:01:00 Hello, Arthur.
Told you we would have seen each other more often.
Arthur Silva Sens 00:01:05 Yeah, I can see that.
Liudmila Molkova 00:01:07 That's cool.
Let's give folks a few minutes to join, we should have… Josh and Jeremy here today.
ariannavespri 00:01:22 Maybe also Nicholas, I think?
Arthur Silva Sens 00:01:26 Yeah, I have the impression that Nicholas will join today as well.
Liudmila Molkova 00:01:30 Nice. Do you or folks want to add anything to the agenda?
Arthur Silva Sens 00:01:39 I… I intend to be a fly on the wall for a few meetings.
And while I learn Rust, and once I'm comfortable, then I'm starting.
Discussing more.
ariannavespri 00:01:52 Yeah, same here.
Liudmila Molkova 00:01:56 Jeremy is the Rust expert. I've been on these calls for a while, and still I don't know Rust.
ariannavespri 00:02:03 Okay.
Jeremy Blythe 00:02:05 I'm not.
ariannavespri 00:02:06 So, everybody…
Jeremy Blythe 00:02:07 I'm gonna say I'm somewhere.
I'm okay at rest.
Liudmila Molkova 00:02:18 Let's see, Josh?
Wanted to be curious.
Jeremy Blythe 00:02:27 For sure.
Liudmila Molkova 00:02:37 Maybe it will start… Slowly was the… Project board… So what do we do here, usually? We go through the consider for the next release.
And… I think we just did a release, and it's a bunch of… Nice to have, so we wanted to… Fix.
So I don't know if there is any point in going through them.
Schema…
Josh Suereth 00:03:26 Hey.
Liudmila Molkova 00:03:27 Hey, Josh. No worries.
Josh Suereth 00:03:30 Yeah, apologies if I don't have the camera on, I'm, flying across time zones, and I'm trying to do the time shift thing where you avoid light, so my room is, like, dark, and I'm wearing sunglasses. It's pretty fun. Anyway, so… I did a bunch of, triage across Weaver, so I actually, created 3 new labels, in our issue tracker, one for the template engine.
One for the policy engine, one for the filter engine, which is JQ. Sorry, I made 4 labels. I made another one for model. And what I… and I went through all of the issues and annotated them, and… Just to see, like, where we stand across the 100 issues or so. So, the unsurprising thing is almost all the, like, 30% of the issues are about the model.
And we're actually doing pretty good on the rest of it. If you look at 2Consider for next release, there's only one thing I want to throw in there that I would like to get merged this year, if possible, which is the Weaver update markdown. And I think that's either in there or in V2 schema.
I don't remember where I put it.
Oh, it's in V2 schema.
This is… this is, in my opinion, this is ready. It has no… it has some reviews, but no approvals, but I think this is, a decent path forward. It seems way more flexible. So I'd like to try to get that merged, because this is one of the things for V2 that didn't make the release.
Liudmila Molkova 00:05:02 Yeah, I've tried it, it works, it's good enough for me, so I'm going to approve it. Well, I had some comments on… actually, no, let me take a look, I had some comments on some minor stuff.
Okay.
Josh Suereth 00:05:17 I think there's an ergonomic… pass at this that we'll have to make, but I want people to try to use it. So, I want it as, like, a preview thing, right?
Liudmila Molkova 00:05:26 Yeah, the reason I didn't approve it is that because, well, we can go through it later.
Josh Suereth 00:05:33 Okay.
Laurent Querel 00:05:34 And I think a little bit of documentation will be, will be nice, if we want people also using it.
Josh Suereth 00:05:40 I did add some documentation. I don't know if it's enough, but I added, basically a…
Laurent Querel 00:05:46 Because I was reviewing, and I didn't see the Swinme.mdfi now, so I missed it, sorry.
Josh Suereth 00:05:52 Okay.
Liudmila Molkova 00:05:55 Yeah.
This is not registered.
Am I passing in the registry and not the whole…
Josh Suereth 00:06:04 Schema? Is that what I did?
Liudmila Molkova 00:06:07 So, you're passing the inner part of the registry, not the outer.
Josh Suereth 00:06:14 Huh, I thought I was passing the whole thing. If I'm not, I can fix that. That's a bug.
Liudmila Molkova 00:06:20 Okay.
Josh Suereth 00:06:25 Okay.
Liudmila Molkova 00:06:26 Cool! Thanks! Do you want to present, by the way, or do you… I can keep going.
Josh Suereth 00:06:33 You can keep going. Yeah, maybe I'll take over when we get to the notes instead of the triage.
Liudmila Molkova 00:06:41 I actually have no idea what to do with this triage, and it seems you already triaged everything, so we can get to the… Cool.
Josh Suereth 00:06:50 Yeah, I can just briefly mention some themes I saw. So, I think the… the general themes that I had were, we have a lot of easy-use stuff to… that a lot of it's kind of docs, or just minor cleanups and tidbits. There's a ton of modeling questions, and I think the modeling questions… there's duplicates that I'd like to get rid of. I'm actually thinking of making a duplicate finding thing that says, hey, this may be a duplicate of this other one to automatically close that, like an agent that does this.
To help us out, but because it turns out, over the past 3 years, we have opened the same issue 3 times by 3 different people, saying almost exactly the same thing 3 times for, like, V2 schema-related problems, so… That was one thing. The, to consider for next release, I think the main… the main thing to think about here in making progress is, I think we need to talk a little bit about registry loading.
and do a refactor of registry loading. This is handling, like, SSH capabilities, and if we're gonna start publishing resolve schema, I think we need to take that code and, do a little bit of refactoring to make it more flexible, because I would… that would go a long way.
there's a few other things in there that I don't think are… Worth mentioning now.
Outside of just a general need to debug.
So, I'd rather defer to what Jeremy has with the UI discussion.
Because I think that will actually resolve a lot of the… a lot of the underlying problems without actually doing what the issue says, if that makes sense, so… Alright. Yeah, should we move on?
Liudmila Molkova 00:08:38 Yeah, let's move on.
So, the Weaver Update Markdown is the first… do you want to take over?
Josh Suereth 00:08:46 You can… you can keep pushing. What, why don't you go through… I'll take notes, and you can tell me what your issues are.
Liudmila Molkova 00:08:53 Yeah, so, I'm trying to use it, and it works like a charm.
Josh Suereth 00:08:59 Better.
Liudmila Molkova 00:08:59 It doesn't, unfortunately, solve the problems in Semantic conventions. So let's take a look at the cloud events.
followed.
There we go.
So what… what do we have here for this group?
Right? If I want to replace it with, let's say, namespace filter, then…
Josh Suereth 00:09:32 Let's actually do this.
Liudmila Molkova 00:09:35 You see, this is… this is not just a set of attributes, there is a requirement level.
And… If… We can probably remove it, we can render an attribute namespace here, that's fine.
But it means that… Like, we cannot get to pretty much zero diff with schema V2.
At least, yet.
Josh Suereth 00:10:03 Should… should that be a public attribute group?
Liudmila Molkova 00:10:07 It should be a public attribute group, this one.
Josh Suereth 00:10:09 If we move it to be a public attribute group with requirement level, would that fix the problem? Because I actually think… The lack of attribute group inference, where, like, what needs to be public and not in V2. I think… I almost fixed that prior to today, I just didn't have time.
But that was my thinking of, like, a next step, was actually to figure out how to get public attribute groups in V1, so you can annotate this as a public attribute group in some fashion, and then we can, Get access to it in the way that you need it here.
Liudmila Molkova 00:10:48 I see. Okay, so it's just not in this release, because I think we removed public groups, and we won't be able to use them, but yeah, it makes sense.
Josh Suereth 00:10:56 They're still there. I never… I was too lazy to actually remove them.
Liudmila Molkova 00:10:59 Oh, okay.
Josh Suereth 00:11:01 Yeah, so public attribute groups are there. Whether or not they do what you want, I don't know. But there's… there is no possible way for you to take a V1 schema and create a public attribute group. You have to use the V2, like, definition to get a public attribute group.
Liudmila Molkova 00:11:17 Yeah, cool. I'll try that. So then there is nothing else that I wanted to bring up, except that it's, what I see, it's not the registry, but the attributes, metrics, and so on.
Josh Suereth 00:11:30 Yeah, that we'll have to fix. I don't… I've run into some wonkiness. Lauren, I don't know if you're familiar with this, but, like, when you send stuff to Jinja, Mini Jinja.
in Rust.
it flattens the crap out of it into an object. And so if you send a string.
It tries to make key-value pairs of the individual characters of the string.
for some reason, if I send it a string.
Laurent Querel 00:11:58 And… Yeah, I think that there is a way in Mini, Ginja to… to expose… I mean, you have a set of traits to expose, object.
Josh Suereth 00:12:12 So you should be able to…
Laurent Querel 00:12:16 To get rid of this behavior, if you want.
I need to refresh my memory on that, but I don't remember having some… a similar issue before.
Josh Suereth 00:12:30 Yeah, you have a thing that wraps some context in a thing, like, in an object, that just, like, you turn everything into a JSON object that has a value in it.
Laurent Querel 00:12:41 And if not.
Josh Suereth 00:12:41 context.
Even with that, I was running into issues where it was still, like, turning a string into an object. I'm not sure why. But I… I… I'll leave that as a, yeah.
Laurent Querel 00:12:57 Exploration.
Josh Suereth 00:12:58 Yeah, okay. Figure out why JQ filters that return primitives, like… Hello.
Are being auto-converted into objects.
Like… The worst part is, it's, like, H0… And it should be alphabetical order. So, this is what it turned into, and it was… it was awful. H0… L.
Laurent Querel 00:13:29 Hmm.
Josh Suereth 00:13:32 And I… it might have been false, not zero, but anyway.
H0L0… And I think that's it in Hello, right?
There's only 3 letters?
Laurent Querel 00:13:45 You should remove the double L, yes.
Josh Suereth 00:13:50 It, yeah, it would. Like, like, that's… that's… that's the problem. Like, it would take a string and turn it into this, and I was like, what the heck? So my tests were failing. So, instead of… what I, what I ended up doing is every JQ test that I have returns an object instead of raw values. This would also be true if you returned an array. It would try to flatten the array into an object, and you'd get nothing.
And I don't know why it's doing that, but if you return an object, it's fine, so it could be we just document it for now, but it's a… that's a… Anyway, that's a huge usability problem that I'm not… I wasn't sure how to deal with.
But I kind of think people are only… only advanced people will be interacting with JQ, possibly.
So…
Laurent Querel 00:14:41 Okay, I will, I won't promise anything, but I will, during the review that I started this morning, I will try to… to look at the mini-Ginja interface and try to figure out if there is a way to pass… basically, you want to pass a string, and you want to get this string from From the template, right?
Josh Suereth 00:15:01 Yeah, in the template, I want, the context value to just be that string.
Laurent Querel 00:15:06 Yeah.
Josh Suereth 00:15:09 Okay.
With that, I think that's all I really needed, besides, you know, please take a look and let me know what you think. I think it's, like I said, I think it's a big improvement over what we had before, even if we plan to, you know, eventually deprecate Update Markdown or not use it for general purpose things. Making it very flexible but hard to use actually leans into that… don't take huge dependencies on this.
But, alright. Anyway, Lyudmila, you want to talk about V2 stuff?
Liudmila Molkova 00:15:42 Yeah, so I want to talk about V2 stuff from a different angle. I want to talk about using it to publish a V2 schema, and what do we want the end result to look like.
So…
Josh Suereth 00:15:56 So what do we have today?
Liudmila Molkova 00:15:58 We have this beautiful, thing. Let's take a look here. So we publish this as a schema.
And this is a diff, it's a partial diff, and But that's what we have. Instead of this, what we discussed in the past and what they tried to model.
Is that we should have a registry, manifest?
It would live next to our YAML models.
And it will be used for all the things Weaver, and I think we need to define and change the format of this registry.
Manifest.
So this is what… I think Weaver wants today.
But I think we need file format, following our schema definition format, right?
I like the OpenTelemetry… sorry, the name, the description, which are just the metadata.
The version… I don't know if we want to prefix it with SEMconf, this is all semconconf prefixed, then?
And then the main part…
Josh Suereth 00:17:17 is…
Liudmila Molkova 00:17:18 the actual definitions, right? So this file is tiny.
Josh Suereth 00:17:24 By the way, Here is the list of our schema files, and you see they're growing over time.
Liudmila Molkova 00:17:33 It probably would never go too, too high, but that… that was the problem in the past. But anyway, this file is tiny.
when people hit the schema URL, They would hit this file.
For those of them who want to download full schema, they would go and download the archive.
It could be, I don't know. At the beginning, it could be GitHub, artifacts that we release.
This… Archive.
But… of… Two files.
This is the content of the archive. Sorry, three files. This manifest, for convenience, the actual schema V2.
And it contains everything, all the definitions, Also, the refinements, and then the diff.
Here.
Actually, This is a good question, what we do here.
Because… I… I think this is not the final state of this file.
But I also think we're nowhere close to knowing what the final stage should be.
And for the time being, I would rather just keep the DF as it is.
Maybe remove unnecessary stuff from it.
Or just stay, okay, it's that file format.
Josh Suereth 00:19:11 I think… Yeah, I'll say, I'll say a few things. So, first off, the registry manifest, I think we need, from the implementation, we need two things for registry manifest. We need a definition registry manifest, which is what you write… what you have in SEMCOM there.
And then we need a release registry manifest.
Where, like, the… here is the resolve schema and stuff would be in the released version.
So, the idea would be, when I'm defining my local schema, I define a manifest for it.
And… I don't get diff.
and I don't get a resolved model, Weaver has to actually go look in that directory and search for YAML files in Resolve, as it does today. That is how remote repositories work. However, if I read this manifest and I see that it tells me I have a pre-resolved schema.
then I can go grab the pre-resolved schema instead.
of doing the resol… like, instead of looking at the local directory, if you will. So, it kind of lets us reuse manifest for both purposes. There's, like, the… what manifest looks like when I'm doing local definition, and there's what it looks like when I'm doing remote resolution.
So, that was, like, part… like, thing number one I wanted to talk about, because, that was code I was looking through recently.
to try to make, To try to improve the ability for us to actually resolve against resolved repositories instead of doing resolution for every single thing in the dependency chain.
Okay. Second thing, regarding diff.
I think we could do one of two things. One is, we can leave the diff exactly as is today.
And call it File Format 1.1, and just don't make any changes, and just generate this thing.
Option number two is, we make a 2.0 that, basically looks more like Weaver Diff.
And we would have additional files that are optimized for transformations. So, like, we would publish both the Weaver diff output And we would publish the telemetry schema output with file format and all that stuff at, like, at the same time.
Liudmila Molkova 00:21:41 Oh, so what you're saying, that we can publish this one.
And also the 2O, which is Viva D.
Josh Suereth 00:21:50 Right, I would actually call that, like, the… the schema URL schema or something, you know, like, I would say, like, we're gonna publish a… The idea would be, we always publish a diff, but the diff is the Weaver diff. We publish the schema, which is the Weaver schema. We publish the manifest, which is Weaver Manifest. We always publish those three documents.
Then we have an extension mechanism that would say, cool, I want to take the diff and turn it into the… what schema URL expects.
I want to take the diff and turn it into something for Prometheus, right? And so, I would have possibly an optimized diff.
for Prometheus. I would have an optimized diff for the OpenTelemetry Collector that does this. Like, this… this is… this file structure is kind kind of targeted at the OpenTelemetry Collector a little bit for doing transformations. I think when we were talking to Bartek earlier, and Ariana, that the… file format for Prometheus might not be the most optimal.
And so, we had talked about having, like, a plugin capability, right? Or the ability to, like, optimize that diff for various use cases. So that's why my thinking is, I would actually rather deviate significantly in the diff, to keep it close to the Weaver V2 model.
And then, kind of generate you know, the specific things we need for components that exist today. So, we can keep… Keep the telemetry schema almost exactly as is, where people can ingest that whole stupid thing, but that's like an extension.
and then whatever Prometheus wants to do and build, we can have that as an extension. As long as those can be inferred from our diff, great. Everything's gravy.
Liudmila Molkova 00:23:46 Yeah, nice, I like it. Let's… Alright, I think the diff… the Weaver Diff… I don't have an example here, but… I'll review it. If there is anything that we don't want there, we can… we can massage it.
Cool, so then, there were some interesting questions.
on the backward compatibility. So we never declared this… this thing stable.
We document that if the file format is higher, then just don't attempt.
And I don't believe there is a lot of things that rely on the schema format. The schema processor was never finished.
So, I would rather… do a breaking change, and just start publishing to O.
We could… imagined, backward compatibility, backward compatible change, where we, I don't know, keep publishing 110, but I don't think there is a point.
Josh Suereth 00:25:05 I… yeah, I… I… I'm personally with you here. We probably do need to walk that through the collector, SIG, and the, the maintainers meeting… the spec maintainer's meeting, just to make people aware that we're doing that.
I… I think that what we're proposing should probably be an OTEP.
like, like, the detailed design OTEP, we wanted to get out the door, what, in April? So…
Liudmila Molkova 00:25:36 Yeah.
Josh Suereth 00:25:53 But yeah, let's… let's… in this case, just given low… Sorry, people do use it.
But the accuracy of it and the way they use it is not necessarily by, you know, directly consuming that file, or if we give them the same file somewhere else, I think it's fine. So… I think we should push for this breaking change, because the new model will be significantly better, and will work When we start doing, federated semantic conventions, so…
Liudmila Molkova 00:26:30 Cool.
That's… that gives me a lot of things to try and, figure out, and thank you.
Josh Suereth 00:26:42 Yeah, one thing I want to ask is, right now, Weaver Diff.
is a different, like, command than Weaver Resolve, right?
And we have this GitHub action.
What I would like to get to… is where, we can give you a GitHub action.
that will generate the… or… or, sorry, a GitHub action, or at least just a workflow.
that will let you generate this repository layout in your GitHub repository, where you can basically say, cool, in my release workflow, here's the Weaver section, it generates these artifacts, it publishes them to your release.
So, they're, like, attached as, like, you know, files or something? Like, something that makes this dead simple on GitHub for open source projects to publish what they need when they make a tag. You know, so if someone's using a, I create a tag, and then a bunch of stuff happens, we can have a Weaver component of that, where Weaver will take the tag.
do the diffs.
generate the Resolve schema, and then publish this whole repository to a, you know, a file, or a set of files on your GitHub release. So, something there. Even if people don't use GitHub release, I don't care. I want, like, a… For people that do.
I want to make this dead simple and really easy, and then we can show the whole ecosystem in OpenTelemetry how to do that. Does that make sense?
Laurent Querel 00:28:17 Yeah, like a package and publish a command. Package will do the… the, the… Orchestration of what you described, the generation of the values element.
And once we have a package, we publish it.
Josh Suereth 00:28:35 Yeah, in fact.
Laurent Querel 00:28:35 to see that.
Josh Suereth 00:28:36 Weaver might only need the package command, because we can just use, you know, GitHub has a publish artifacts you know, target. We can just show an example where it's, okay.
use the… use the Weaver action to set up Weaver.
Laurent Querel 00:28:52 Oh, man.
Josh Suereth 00:28:52 package, and make sure you specify these, you know, things here. Here's an example that works on 99% of GitHub repos, and then, you know.
Add the output of the package command to your release with upload artifacts, you're done.
Laurent Querel 00:29:09 Yeah, makes sense for me. I think there is somewhere in some documentation a description of the Weaver registry package, come on.
That doesn't exist in the con, but, please describe it a bit.
Somewhere.
Liudmila Molkova 00:29:36 Cool!
Anything else on this one? I think I'm good.
Really appreciate all the feedback.
Okay, moving on to the UI next steps. Jeremy, do you want to take over? Do you want me to present?
Jeremy Blythe 00:29:58 Shall I show you what I've got?
Liudmila Molkova 00:30:00 Yeah, please do.
Josh Suereth 00:30:03 I'm really excited to see what it looks like now.
Laurent Querel 00:30:05 Me too.
Jeremy Blythe 00:30:07 -Oh.
That's wrong.
Okay, alright.
So, I simplified it a lot. There was, There was a bit too much in the API, I thought, and the searching and the browsing were very similar, so anyway, now you've got You go to search… Now, let me get this out of the way. We got… Okay, so if you just hit enter, you're kind of browsing everything.
in, you know, alphabetical order, deprecated things get grayed out.
Each one of these cards… If it's an attribute, like, this… you get a little bit of something about the fact that this, like, this is the type, but… if it's a metric or whatever, you'll see different things. You can then filter by the types, so I can just say… Metrics only, or… spans… Obviously, you're searching within that, so, like, HTTP client.
If you… the fact that this is a span means the extra information I've got is, like.
It's kind here. If I click on it, this view hasn't changed much.
It's rendering the mark down as best as it can. I think that needs a bit of… bit more effort.
Then you get all the information about the attributes.
Laurent Querel 00:31:39 Do we see the… could we see the provenance and the lineage?
Jeremy Blythe 00:31:46 So I'm doing this from the Forge Resolve… So I'm not sure you get that in there.
Josh Suereth 00:31:52 Oh, so, Lauren, I haven't… I haven't wired Lineage through, that's a to-do. We're in preview.
Laurent Querel 00:31:58 Okay.
Josh Suereth 00:31:59 Yeah, so we have some lineage because of the way the model works, but we don't have the full lineage yet, so that… that is something I'm adding, yeah.
Okay.
Absolutely necessary, I think, when we do, like, layers, yeah.
Jeremy Blythe 00:32:12 Yeah, absolutely.
Laurent Querel 00:32:13 to help semantic conventional reviewers, for example, try to understand where… I mean, there is two concepts. There is provenance and lineage. Provenance is where this thing was defined, in terms of file.
So that will help people to fill out, we could even have, for example, a link to append the file, or something like that, at some point.
And the lineage is all the transformation step.
That have been applied from the original, element.
That has been inerated and overridden, and so on.
With the value steps.
Jeremy Blythe 00:32:57 Yeah, you need… you need that for sure. So when you've got… So, my company use case, where we've got the multiple registries that depend on each other, I want to know that this… which…
Laurent Querel 00:33:08 Yeah.
Jeremy Blythe 00:33:09 Registry is defined in.
As a minimum.
And then you'd want to be able to filter on that, I think, as well.
So that's search.
Now, now you can see the schemas now, so I've got… this… the Forge Resolved one, which I think I've fixed all the bugs in, so you… it's actually displaying things correctly. You can click on these things, and it takes you through.
Click the thing, takes you back to the root.
So, I… I haven't found… I think, you know, I've just been debugging it by hand, but I haven't really found anywhere where it's not… Doing this properly.
I added in the SEMConf, which is… Routine much the same, except you get imports.
Pretty much the rest of it's very, very similar, so… It seems to be, but I don't know, just… you can click around and see.
Explore the spec.
And now I just added… OpenAPI.
And this is a… What's it called?
Rappy Dog, I think it's called Rapidoc, which is kind of… So, in the code, you… it's using a… crates called, Misspelling of Utopia, Uto EPA, or something.
So you can annotate the code, and then it will create the, OpenAPI spec document.
And then you can use standard OpenAPI, UI things, like this one.
And then you could even go… you know, you can do the things where you try it out, so I can… I can get the HTTP client span, and… Run it?
Get it? Yeah? So it's like a real developer.
You know, something…
Laurent Querel 00:35:13 That's great.
Jeremy Blythe 00:35:13 used to doing if you use OpenAPI, right?
Laurent Querel 00:35:19 It's exactly what?
Jeremy Blythe 00:35:20 And that's where I've got to. The… the… Sorry, I think I've lost you now.
Since we're in.
I'm so used to using two screens that when I go to one screen, I just, like, can't find anything anymore.
It's crazy. Anyway, yeah, I'm not sure I've got much else to show you.
Josh Suereth 00:35:47 What's the dashboard link have?
Jeremy Blythe 00:35:50 Well, at the moment, it just has, like, counts of things as, like, stats of what you've got. I think we could have all sorts of things on that page, but it's… it's fairly minimal at the moment.
You've got a light and darkening thing going on as well.
Which I managed to make… go through to this sort of plug-in thing.
So, yeah.
Josh Suereth 00:36:15 This is awesome. I'm really looking forward to when we can test Rego policies and JQ filters in here.
Jeremy Blythe 00:36:23 Yeah, so that's what I'm thinking. This left-hand menu will grow and grow. Like, I want to have, like, a live check thing where I can put in a sample and see, and then play around with Rego and JQ and… You know, you have playgrounds in here, so it's a real, sort of, developer tool.
Laurent Querel 00:36:38 So how do you start the… so you start Weaver with a Weaver.gistry serve, or something like that, to… In order to display the… that to get access to the… the REST API?
And is the TFI that are served.
Jeremy Blythe 00:36:54 Yeah, you just go WeaverServe, and then you give it the registry that you want. That's the way it works at the moment.
I'd like it if you could, like, hot load the registry once you're serving, that would be really cool. But for the moment, it's like, we've a serve with the registry You know, the normal registry parameters on the command line.
Laurent Querel 00:37:16 And why, why not registry, sir, and the following, the same pattern that we have, From the beginning?
Jeremy Blythe 00:37:25 Because I think I want it to actually be the other way around, where, I guess I'm not too bothered, I just… it feels like we're serving Weaver stuff more generally than just registry things.
You see what I mean? So, like, I've got the schemas and so on. So, like.
Showing a schema is not about a registry.
You see what I mean? Okay.
I mean, it's…
Laurent Querel 00:37:55 I can understand, yeah, I was just psyched into that, because if the… The parameter describing the registry is mandatory.
Then looks like the serve is… Oriented around the registry.
Jeremy Blythe 00:38:14 Yeah.
Laurent Querel 00:38:16 That's why the river registry itself, for me, was also making sense.
But, yeah, we have this API documentation.
Yeah. Okay.
I'm, I'm, I'm fine with those, I mean, it's, the, the, the… this UI is so nice and so cool to have, but I don't think that the… The way to run it is necessarily the most important.
Jeremy Blythe 00:38:48 Yes, I was thinking you could do WeaverServe, and then you don't have a registry, but you can still get at the schemas.
Laurent Querel 00:38:54 Yeah.
Jeremy Blythe 00:38:56 But maybe you could then go to a load or something up here.
which, if you then click on it, you could, I don't know, give it… Give it the path to where the registry is, or something?
Then it would load it in, and then that means that you'd be able to load in different registries while it's running.
Or if you're develop… if you're developing… You'll be using the tool to help you to create a registry, so maybe on… maybe somewhere else you're making a registry, and then you want to go, like, okay, reload.
And then you can browse around in it.
Laurent Querel 00:39:27 Yeah, I'm convinced.
Jeremy Blythe 00:39:28 Kind of what I was thinking.
Josh Suereth 00:39:32 Go ahead, Arthur.
Arthur Silva Sens 00:39:33 I'm thinking about connecting this UI with the inference work.
If I understand correctly, you were… when you were guiding me with the infer command, you were guiding me towards, similar to life check, where the CLI runs for a couple of seconds, and then it dies.
terminates, whatever.
like, could this be some kind of surf as well? Like, Weaver is always online, always surfing, and is always accepting.
LTLP messages and doing live checks or inference.
Or would you prefer that this goes more in, like, short-lived, executions.
Josh Suereth 00:40:28 Right.
So… I'll jump in quick. I think the idea that you can fire OTLP at it and infer a repository, I love… I love that, and I think we… we want that. That would be… I can totally see that in this UI, as a thing that we might allow or do, but the question is, do you… do we open an OTLP port, which would be a different port, or do we have, like, a UI checkbox that you'd say, okay, open an OTLP port now, or what I think Jeremy's done so far is this idea of copy-pasting stuff in.
Like, I can, I could, like, copy-paste in an example.
OTLP JSON, and then just parse it right there. I don't know. What do you think? I like that direction. I think that that makes sense as, like, a development thing, where I could actually start firing some OTLP at it, and this would tell me what it's inferred, and I can use it to debug.
Arthur Silva Sens 00:41:19 Yeah. Yeah. I was thinking, like, as a… also as a TBT thing, because some, I bet… People will do… will do this with, like, legacy systems, and then they want to switch to something new. Then the… what is being inferred is gonna look ugly.
And they will use the UI to change what was inferred a little bit before committing to writing to the disk, hey, this is the new schema that we are gonna commit.
Nicholas?
Nicolas Takashi 00:41:55 Yeah, I was, like, mostly pretty aligned with you, like, I think the months ago, when we discussed it, one of the ideas was to, like, be able to live ingest the OTLP and parse the schema, and eventually even exposing an API where people can define which kind of… rules that you want to apply on ingestion, like, for example, imagine you have two different telemetries, you have the same telemetry with two different schemes.
And you can make one schema as the, oh, the official one, or this table, or the approval, or whatever, and you can get those information from the, like, this Weaver hash history in runtime, and decide if you want to drop or not the telemetry that's not… Expo… like, matching the schema that you, you, you agree that it's a valid schema, you know?
So I think that this live ingestion would be, like, maybe there's an option, like, someone that, like, explicitly say, oh, I want this feature, you know, but would be very valuable.
Liudmila Molkova 00:43:04 So it seems that the weaver surf is a bit ambiguous, right? You would expect both. Like, you would expect all the serving functions from the surf.
And in some… in the future, it would be cool to have ability to listen and do UX, but they are also two independent features.
Right, you don't necessarily want to listen to OTLP while you're showing this beautiful UX.
Nicolas Takashi 00:43:32 Yep, yep.
Laurent Querel 00:43:33 And also, I think the… having a pure CLI without HTML UI to infer schema It was also interesting, independently.
We could imagine that we… We have to do that for many, many components of an infrastructure.
And we just configured the different microservices, for example, to a single during a, let's say, a… some testing into the CI infrastructure, and we just configure Weaver to get that, collect the inferred schema, and then people will work on that, In a single stage.
Not sure that, in the CI we… we want to get access to a UI, So I, I, in my opinion, I see that this, this pattern, these two patterns, coexisting.
Arthur Silva Sens 00:44:34 Got it.
I feel like we deviated a little bit.
from the main topic, but yeah, the UI overall… Great work, I would love to see that life.
Laurent Querel 00:44:51 You too.
Jeremy Blythe 00:44:53 Yeah, I think I just feel like I want to do a little bit more tidying now.
On the code, it does build. There's a custom build RS that does the NPM build.
I think I've persuaded cargo discs.
To do it.
Without having to change CargoDisk's output?
And… yeah, I just want to tidy up a little bit more, and then I'll change that PR into a, out of being a draft and a proof of concept type thing, and then you can pile on.
Tell me it's rubbish, but… It's pretty good. It's pretty good, I think.
I'm just not a… I'm… I'm not a UI… Guy, really, so it's, like, it's fun to get it to the.
Nicolas Takashi 00:45:51 Yeah, I would be more than available to help with this UI part, like, as I proposed in the past, like, unfortunately, pre-order has shifted a bit since then, but, like, I'm available again.
Jeremy Blythe 00:46:07 Yeah, that would be really great, yeah. So, I think if we can get this in with, like, the features that I've got now… Now that I've tidied it up a bit… Daniel could collaborate on it.
Make it look a little better than I can.
Josh Suereth 00:46:21 So, my main thought here, Jeremy, is if you… if you figure out what the command line argument to run it is.
And we're confident that we have the right boundary for… sorry, and we're confident that generating the package for the UI is appropriate in our release process.
And then the third thing would be the OpenAPI stuff you did, which I think… I think looks awesome, and hopefully that boundary's right.
Where we can add new API endpoints, and we, like, we can have a clear interface there. If you have those three, I'd commit, even if the features don't necessarily work yet, I'm more worried about the ability for us to work on the UI.
And so, I think you, like, that the… it looks like you have the core ready, so I'd like to get this in quickly.
Yeah.
Jeremy Blythe 00:47:07 Okay.
Alright, I'll… I'll aim to get that in the next, next couple of days, hopefully.
Laurent Querel 00:47:16 That's the word.
Nicolas Takashi 00:47:20 Let me know when you push it, and we can collaborate.
Jeremy Blythe 00:47:24 Awesome. Thank you.
Liudmila Molkova 00:47:27 Awesome. So we have just one more topic on the agenda. Josh, it's yours, creating agents. Do you want to talk about it?
Josh Suereth 00:47:35 Yeah, yeah, do you mind opening that up?
literally just got, the agent done here, so I'm gonna show you, a link. So basically, the idea here is we get a lot of, Sorry, I'm seeing a lot of AI-generated code.
In general. And my… my… one of my overall goals here is to figure out how we can share using an AI instead of one person figure out how to prompt an agent and build an AI, and then, like, none of the rest of us benefit from it.
So, what I wanted to do was start thinking about what agents we would like to have to support us, and build those out in a way that we can all make improvements and fix them. So this is an agent that's supposed to just go through and look for document problems.
make a plan, fix the documentation, and then execute on that plan and give it to us. So the idea is it makes a set of things it's gonna try to do, it goes and tries to do those improvements, it validates it, and then it pushes it. This is using, currently, the agents feature of GitHub, which You would have to have it on your personal account to make this thing run today, because that's just how it works, but we could all benefit from the same set of improvements to that agent, and we could all share at least the, like.
reference of what it is. If you want an example of its output, I actually ran this through, now, I ran it through Gemini.
Because, you know, I work at Google.
But if you want an example of what it does, I can show you, you can look at… here is a branch.
If you'd like, I can turn it into a PR.
Of what the agent has generated.
using this set of documentation. So, if you look, it's supposed to create individual commits in the branch.
Each commit is supposed to explain clearly what it's trying to do.
And I… I did make some tweaks to prompts while it was working, but you can see what it did. And it's, you know, some of it's reasonable, some of it we might want to improve over time or change, but it's, I think it's doing a decent enough job to kind of help us with documentation. So, I wanted to get folks' thoughts on both the high-level objective of, like, when we do agent-based coding, trying to find a way to share.
that… those prompts, that syntax via agent's markdown file. And then secondarily, what do we think of this specific documentation agent idea, where we would have an agent that we could at times, like, let's say when serve comes out, Jeremy, you could basically get the PR through, then you could prompt the agent and say, hey, can you go update docs for serve, and see how it does? Right?
Yeah, I don't know if you want to look at other things it did. If you look at the full diff, it did a lot. In fact, and if you look in my PR description, you can see the plan that it was executing on, where I just gave it a improved docs. Like, I was super generic.
Liudmila Molkova 00:50:54 It's… it's cool. It's… it's awesome. I… I think it… it… I don't believe AI can write a great doc, but it can definitely do, like.
60% job of getting there, and it could highlight the gaps that we have.
Josh Suereth 00:51:13 Yeah, yeah, I agree. The… just the plan itself, I think, is somewhat useful for us to understand where we have gaps.
Liudmila Molkova 00:51:20 Well, yeah, the plan is in the PR description you mentioned, right?
Josh Suereth 00:51:25 Yeah, I asked it not to include the plan in any of the… the, the PRs. When it… when it… if I let it make a PR, which I didn't want to do, I didn't give it access to my GitHub yet, but… like, theoretically, with the notes, when it's done with the plan, this will actually be the PR description of what it did.
So you'll get that as the PR description, and then individual PRs for each item in the plan that it tackled with what it did. What's funny is it found a spelling error, and then when it went to fix the spelling error.
it couldn't find it a second time, which I find this hilarious.
The spelling error's still there, I went and verified. So… I don't know what's going on there, but… yeah. I think because it made two changes first, and it says it's on line 54, it didn't realize line 54 had moved, based on its first two changes.
So, yeah, you know, what do you call it, Lamila? Like, we have to teach baby how to find line number changes, but… I think it did a decent job overall. The SELinux one is one… that's actually a bug that we have, describing how to use SELinux. So, the only thing I don't like about the documentation it did here.
was it doesn't have a security mindset, so it's basically saying, if you're using SELinux, you have to use this old… the old mount commands instead of the new mount commands, and so it has this "-Z.
It also failed to switch from… We have to actually block that particular commit.
I was looking at this later, because that, that is actually wrong. Like, the command that it says to run.
won't work.
You can't use the dash dash mount, you have to switch to "-" with the colon z. I don't know how it figured out the colon z, but not the dash V part, but whatever. Like, there's some… there's some tweaks here.
But what's interesting is it caught that this was a bug, it caught that it needed to add it, and this was, like, a long-standing thing in, Weaver, where we have a bug about supporting SELinux.
We couldn't figure out how to support SELinux with the new mount capabilities of Docker.
You have to use the old school ones, and this is actually the workaround that the C++ team is using to run Weaver with SELinux.
So, it's interesting, like, how close it is, you know what I mean? But this kind of a thing, we'll have to go in and actually make changes to the PR and fix that actual Docker run command to match what was in the thing, or reprompt the agent to go fix that commit, right?
Liudmila Molkova 00:54:16 Yeah, and I think this would be our flow with any of the PRs, that we would create using it, right? So, some of them will be crap, others will be awesome, and there will be the majority, which is somewhere in between, and we would need to decide for each of them what we do.
If they, actually, if they come from the bot, right?
It gives us the right signal that, okay, we should take it with a grain of salt and verify everything, or ask it to verify everything.
Josh Suereth 00:54:47 Yeah.
Yeah. Now, locally, I did have the option to… Reprompt it to fix this?
But I didn't have time before the meeting to let it do that, because I would not have had anything to show you if I did.
because I wasn't planning to necessarily keep this output, this is just, like, an example run, I wanted… and we're debugging the set of instructions, I let some things through that I otherwise wouldn't have, right? But that's… we… I need to look at how it works with GitHub, but we should be able to… We should be able to get it to the point where when it runs into something like that, it either asks us, or we can, like, prompt it directly to, like, correct things in the middle.
Liudmila Molkova 00:55:28 Yeah, here we would… we would have to have a CU Linux tested.
And this… this would be fun. We would need to manually test it.
As you've done, probably.
Josh Suereth 00:55:39 I don't have an SELinux machine to test it on. The reason I know that it doesn't work is because of the bug that describes a working solution.
Which is not this.
Liudmila Molkova 00:55:54 Yeah, that's fine.
So, how do you think about the flow? Like, we would, like, the current flow, I think we have is with Copilot and GitHub, that you create a bug and you just assign it to Copilot, and here it would be the human that initiates the documentation process, right?
Josh Suereth 00:56:12 Yes, and I feel like what we can do is… what I'm hoping to have is, with this prompt.
The… the agent prompt is we give it, like, an objective for how it… how it… goes about making improvements. So, the focus here is you give it some identity of its role, you tell it what it can't do, which is really important. I don't want it touching Rust code, ever.
I have had a lot of… I've been trying to use agents with Rust, and it's really hit or miss, but when they go wrong, they go wrong hard.
Even trying to tell an agent not to touch production code and only touch test code, it will violate that so much because they're in the same file.
So, I don't think there's a safe… in my opinion, there's not a safe way to let it go with Rust right now, and just get… they run into too much problems.
Even if sometimes they do amazing things.
So, this is… this flow is what I like, and then the idea would be, like, I added, you know, a new feature to V2, and I didn't have time to document it. I can go prompt the agent to go read the code and write the docs.
And it should go through this flow and this process, so that we have, like.
an understanding of what it did and why it did it, and we have these individual commits for, I'm making small changes so the thing doesn't spew on too much context.
Yeah, so at the bottom, the boundaries are also important, right? What I don't have is how to validate, so if you look at the validation instructions, it's really limited. That's why I didn't run the Docker command.
Because there's no way for it to validate whether it's accurate or ground it in any way.
I think that's fine, because I don't, you know, I think that's where our code review comes in.
Liudmila Molkova 00:58:04 Yeah, and if we would ask it to validate, we would run Winters, which I don't think we have today, and we would tell it how to run Linters, because it only allows to change docs.
Josh Suereth 00:58:13 Yep.
Liudmila Molkova 00:58:14 Yeah.
It's cool! I mean, we probably need to iterate on this, but let… I would be… It would be cool to get it in and start using it, and then iterate.
Josh Suereth 00:58:26 Cool. Like, I guess that's the question, is do we want to iterate on it together, or do we want to… do you want me to take more cracks at running it and give an example where we're happy with the output first?
Liudmila Molkova 00:58:39 I think it makes the most sense when we do something, like, that we need to do.
And if we… I will write a bunch of docs for V2, and I will try to use it to write docs for V2. And when I see it failing, I could tweak it.
Josh Suereth 00:58:56 Cool.
Yeah, and then we can all review how you tweaked it and make suggestions, that kind of thing. Cool. If you want, I can remove this from draft if we're comfortable with that as a way forward.
Liudmila Molkova 00:59:10 I am. I'm curious if Loren and Jeremy have any thoughts, or anybody else?
Laurent Querel 00:59:16 I totally agree with you, I think it's, interesting to… test iterate, On a specific, goal, purpose?
I really like the approach.
Josh Suereth 00:59:28 Okay. Yep.
Jeremy Blythe 00:59:29 That's good to me.
Josh Suereth 00:59:31 Cool. The other thing I want to call out is there's a… you're proving it before it's even out of draft, nice.
you know, I was looking through, like, what other folks are doing on GitHub with agents and this agents.md thing. It's possible we could actually create, like.
a couple of these that are dedicated for certain tasks that we don't have time to get to, and I think that could be pretty powerful if we figure out what those are.
like I said, I've been trying to experiment with testing, and this is on a different project, but, like, Rust just released… You no longer need the, async trait crate?
Because it's stabilized in core?
And Gemini cannot figure that out, and keeps destroying my cargo to a mil.
Repeatedly, by adding and removing that trait over and over and over again, until it, like, gives up. So… Yay. Like, I think we… there's, like, things that we can't do yet.
But if you think of, like.
stuff that could work out here. The other thing I was thinking about is triaging. Categorizing bugs by default automatically into various areas, give it an idea what the architecture of the codebase is, and just ask it to tag bugs.
that's the other thing I was thinking about, like, those kinds of things. So, anyway, if you have ideas of, like, really trivial tasks that you think an agent could help us out with, I'd love to start trying that out to see if it can help accelerate us.
If not… yeah, if this ends up making us take more time, then it's not worth it, right?
Awesome, thank you, we have to go.
Yep.
Liudmila Molkova 01:01:20 Yeah.
Josh Suereth 01:01:20 Thanks, everybody.
Liudmila Molkova 01:01:22 Happy New Year, by the way, it's the last meeting of the year.
You know, totally.
Laurent Querel 01:01:26 Yes, I've been around.
Jeremy Blythe 01:01:27 Happy New Year.
Laurent Querel 01:01:28 But…
Liudmila Molkova 01:01:29 Bye.
