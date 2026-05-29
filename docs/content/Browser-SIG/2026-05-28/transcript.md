SIG: Browser SIG
Date: 2026-05-28
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Maxime Quentin** 00:58 True.
**Martin Kuba** 00:58 Hi, Maxine, how are you.
**Maxime Quentin** 01:00 Doing good, and you?
**Martin Kuba** 01:04 Hey, I was thinking, do you work with Benoit?
**Maxime Quentin** 01:07 Oh, yeah.
**Martin Kuba** 01:08 Yeah.
Like, he used to come, like, but he doesn't… he doesn't… Have you switched? Have you switched, or is he still…
**Maxime Quentin** 01:16 So, I think he has a wider scope than I, at Dalog, so he's… I think he moved to another topic, but it's still, like, here in the background.
**Martin Kuba** 01:29 Okay.
**Maxime Quentin** 01:30 But yeah… I will probably join soon.
**Martin Kuba** 01:34 Okay.
**Jared Freeze** 01:38 Is that?
**Maxime Quentin** 01:41 Bonoit.
**Jared Freeze** 01:42 I have been one.
So you guys work together, is that right?
**Maxime Quentin** 01:47 Yep, yeah. Okay.
**Martin Kuba** 03:01 I'm just waiting for one more minute, I guess.
Stop with Bristol joining.
Alright, let's get… let's get started.
We have one topic on the agenda.
Actually, maybe David has another one, but Maxime, if you want to… Started off…
**Maxime Quentin** 03:50 Yep, so, out of the entity description, and, yes, last week, Jared, suggestion, we were, like, wondering if, having… how we deal with mutating in the full URL.
Like, if some… like, a URL mutates, between the start of a signal and the end of it, what URL should we use, and everything, and so, it had me, thinking about what happens… If you have a lot of, different URLs across the, like, all your signals.
Because, for instance, you… you, instrument the query parameters.
Which means that your… every time a query parameter changes, you have a new, full URL.
And therefore, you have a lot of entities.
And so it wasn't very clear for us if… we would include the URL parameter in the browser document URL 4, or not.
And if we do, like I was saying, we would have Too many entities.
And if we don't, we are kind of… not aligned anymore with the definition of URL full in the specs?
So I was not super clear, about that, and if you would have any inputs, any suggestions about, about this?
**Joaquín Díaz** 05:20 I think I asked this from the PR, I thought… they all wouldn't include the query string, but I see the definition on, like, you're all the full that includes the query string.
Is that something that we want to change for browser, that URL for? Given that I think… Document that you're a fool, that's… not include the greatest finger, yes, but I'm checking.
But in any case, I think what the intention of having that attribute is So the user can, like, identify on that… on which page something is happening.
And I think the query string is not part of that, like, you don't need to know the query string to know when… where is something happening, and it also has a lot of… Like, changes and notations to it.
So I don't know, I guess my question is, like, do we want to… query string to URL for… or browser to URL for…
**Maxime Quentin** 06:26 Yeah, go ahead, Martin.
**Martin Kuba** 06:28 Yeah, so, I mean, I think, I would say that it's… if you don't include it, then it's… Like, we're kind of making a decision for users, like, whether that's useful or not useful.
I think, you know, sending the data as is, I think is… at least that's what we do, like, in… in our Grafana's FairWeb SDK, like, we sell the whole… we send the whole thing, and then, like, it can be, you know.
it can be processed in the backend, right? I mean, you're not losing any data that way. I think for entities, like, there's a concept of identifying attributes, and Like, descriptive for… attributes that can… that can mutate for the entity without changing the identity of the… of the entity. So I wonder, like, if… If maybe, like, the full URL is not the identity.
It would be, like, an attribute… Additional attribute, but we… then we would have to decide, like, what actually identifies the document.
Is it… is it just, like, the… Like, the domain and the path, and then maybe we send those as… Separate attributes, maybe we don't send the URL full, maybe we send, like, all the different parts as separate attributes, and, like, we define that the domain and the path are the identifying ones.
**Jared Freeze** 07:55 So, I… I got some… I got some pushback for canonical URL in the past.
Which is basically a combination of origin and template.
Sort of. But it's how we think of canonical, which is, like, you know, think of a blog post that has, you know, UTM params or something, like, that you would never include. But without needing to exclude those, you would just have you know, whatever you consider the canonical URL of that page to be. Now, that may include query string params to you, you know, if you're saying, hey, this is a view of my dashboard that's, like, a very specific page, that is included, but the other stuff is not. I do think that there's room For that, you know, maybe we could restart that discussion, but… Yeah, the cardinality… like, I guess if, like, the resource is sort of, like, a key, like, if there's a key for that resource, you know, some people may want to use template, but that's not really an individual page, right? That's still, like, kind of a folder, like a collection.
I don't know if that would be appropriate. I think, obviously, for some people it will be, but maybe not for others, so… I do think there's room for that middle ground where you're still including the domain, though.
Where it's not just a path.
You know, I don't know if domain's always kind of the same for every… you know, maybe that's a resource, too. I don't know if… would you have, like, maybe separate resources, like a domain resource, and then something like a template resource? Or is that overkill? Would you have, like, two keys within the same one?
**Martin Kuba** 09:25 Yeah, I was just looking at the, the link that Maxime shared, like, there's a bunch of different attributes, existing attributes, like, if you wanted to reuse the existing attributes.
we could… You know, you could… we could add or… add a few of them, I mean, the other option is, like what you're saying, like, maybe defining, like, a completely new attribute for browser only.
like a canonical URL or something like that, but…
**Joaquín Díaz** 09:53 Yeah, I… I… I had that good idea of… Thinking, what is the identifier of this entity that represents the page?
I'm using that, and then users cannot… can use, the 4-year-old, if you want, but I think… we should say what's, like, what limits a new entity from another entity when the world changes? What are the things that will create a new entity?
Like, changing the path, for example, or changing the domain, but not changing the query screen.
**Maxime Quentin** 10:27 I mean, to me, if the goal of the entity is to, like, pack signals together.
Yeah, maybe we could even, like, let customers, like, configure what they want to use.
As an entity.
If the goal is to reduce the size of the payload.
it means, like, either we are losing context by cutting the full URL, because we don't want to have, for each signal, a full URL in the payload.
So we could cut, like, using just the domain plus path, or just the path.
But I feel well losing that out, because… for me, you… I find it very useful to have the full context with parameters when you have an error on your page, because sometimes you never know, like, you have a weird parameter, then… you can use that to kind of replicate the issue on your local test or whatever. If you're missing this.
like, I find it difficult sometimes to, like, have… Contacts of a web page without queries.
**Jared Freeze** 11:38 This seems to mirror, like, kind of what we were talking about with User Agent.
which is, like, parts of the user agent are really important, but having, you know, kind of the whole raw strength, like, all of it, is really useful for the backend. So, like, not including URL original, or whatever it's called, you know, or whatever scrub with PII, I think.
You'd probably want that, and then to add other stuff, so… I'm not sure many people would opt out of seeing the exact URL that the user saw, generally, so I think reducing You know, network size or file size is probably not something most people would choose.
So I don't know that that's the biggest concern, because, like.
It'd be weird to have a log that you'd have to associate later, right? Because I think one of the tenets of Hotel is that, you know, everything is sort of discrete, right? That you don't have to go link stuff together later.
So… That's kind of my two cents.
**Joaquín Díaz** 12:35 I think we are talking about two different problems here, like, one is… You want to solve a specific issue, then you have, like, a… an example where you look at a single log, and you see the URL, and you see the full URL, and then you want to reproduce what… whatever is happening on that log to fix something, or to investigate something.
That's fine, if that's an attribute. But then there is the… like, the idea of the entity grouping things together, because they belong to the same context. So… and that is what I… when I look at the role, I think… that is what I say. I think the query string doesn't necessarily add more information to the context. I think it'll have enough context by looking at the URL without the query string.
And that is where I say, like, We… like, if we are, for example, trying to find issues on a specific page.
You probably are not going to filter by querystream, because the query stream is going to change a lot within the same page, and then you will have, like, more fragmented data to look into.
you will probably say, give me all the logs from this, like, slash home, slash whatever page, and then you look at things, and if you see something wrong, you may go to an example, in there, you may see, alright, so this user is on this page, and then it has this query string state, where I can see what's going on.
But I think those are the two use cases for you all, and I think we have to… figure out, like, which one was as an entity and which one was as an attribute, or as a description of the entity. I don't know how… what you said, Martina, descriptor, or what it's called?
**Martin Kuba** 14:12 Yeah, descriptive attributes.
**Maxime Quentin** 14:22 how do we feel about, maybe, measuring the impact of having the full browser URL as an entity?
Because maybe the… even including the query string.
Maybe it would still, like, not mutate that much.
Or maybe on some web apps where they use, like, the URL as a state for everything, but maybe it's not that bad, and maybe we could… like, I have kind of a middle ground where, for most web apps, the full URL as an entity would work.
And then if it doesn't, we can split it in two, like, have in the entity the actual, pass plus domain, and then… Introduce a new semantic for just the query part.
Yeah.
**Joaquín Díaz** 15:13 Yeah, in that case, I'm wondering if we just let the user pick what they want, and say.
they… we have some setting on the SDK, like, the style SDK function, where you can set up all… Your patient entity works.
And if you want to use gray screen, that's fine, and if you don't, you don't…
**Martin Kuba** 15:37 What we have in our SDK, what we have is, like, we, by default, we capture the full URL.
With everything, and… but you'll also provide an API for the user, like, to override the URL if they want to.
**Joaquín Díaz** 15:53 Yeah.
Yeah, we definitely need that also to, like, let them remove any PAI that may…
**Martin Kuba** 15:59 Yeah.
**Joaquín Díaz** 15:59 Stay on the grace ring.
I guess that works, like, we can have that and let the user pick. Like, they gave it for all, they can, like, strip out the entire question if you want.
**Martin Kuba** 16:12 But I think if you go in that direction, it sounds to me like we might need a new attribute, because it's not… it may not be the full URL anymore, like, it's something that's, like, browser-specific.
**Maxime Quentin** 16:28 Yeah, I mean, I enjoy…
**Joaquín Díaz** 16:32 I guess I'm talking about the entity identification.
Does that need to be, As semantic convention attribute, or can we define the patient entity at its own, and say this attribute may or may not have it for issuing, depending on whatever the user is doing?
Like, do we need… browser, that document that you are full.
too much, we… D… page entity identifier, or we can define our own identifier for that entity.
**Maxime Quentin** 17:09 I feel we could do, like, a bit like they're doing in the spec right now. It's like, we do have the full URL, but we also define all the sub parts.
And maybe we could use, even, like, a combination of different, fields out of this semantic to compute the entity.
And if we have something custom on the instrumentation, we could have something that is a combination of fields, could be, like, origin plus domain.
So the world would be, like, first in the semantic, on top of the browser document.url.fool, we have.
browser document.url plus all the exact same that we have in the semantic right now, and then, by default, we use the URL full as an entity, and have an optional, like.
combination picker or field picker for the page entity, something like that.
**Jared Freeze** 18:04 Yeah, I think that's already the intent of url.full. Maybe… not that we should redefine it, but it already is supposed to be, like, the scrubbed version of url.original.
So maybe we just need to… Tighten it for web.
You know, because I think it's already… I mean, it's basically what you're saying, right, which is path.
But it includes fragment and query string, so… I don't know.
**Martin Kuba** 18:41 Yeah, so I guess we have a few different ideas, so… so maybe, Are we, at least on a… do you have, like, an… are we agreeing that we want to have Or represent the document or the page as an entity.
Instead of… adding the URL on every signal. I think that's… we are in agreement on that, right?
**Maxime Quentin** 19:03 Yep.
**Martin Kuba** 19:04 So it's just a matter of, like, figuring out what the right attributes on that entity would be.
**Joaquín Díaz** 19:11 Yeah, what is… what identifies the patient entity, and what is a description of the entity?
**Martin Kuba** 19:18 Yeah.
Okay, would it be helpful to create an issue for this? We can discuss this some more.
**Maxime Quentin** 19:37 Yeah. Yeah.
**Martin Kuba** 19:40 I'll take that as an action item. I think it was… there's, like, a couple different threads going. I think there's a… there's a PR, and then there's a discussion thread.
But I think we just need to make a decision on this, and… I'm done.
**Maxime Quentin** 19:53 So you want to extract it from the main entity description?
As a main entity description in your existing description?
**Martin Kuba** 20:03 I got… yeah, maybe you're right. Maybe for now we can just continue the discussion there.
**Maxime Quentin** 20:09 Because I think there is a session ID, also, that is part of the same… Yeah. So…
**Martin Kuba** 20:15 I was just thinking, like, that discussion was more about, like.
do we want these things as entities? And I think that's, like, sounds like that's settled. So I think at this point, like, we're just, like, specifically need to define what those attributes are.
Awesome.
Yeah, that's what I was thinking. But that's why I was thinking, new issue, but… Anyway.
Okay.
**Maxime Quentin** 20:45 And yes, that's what is… that was it for me.
**Martin Kuba** 20:50 I've got 10 minutes left, David, do you want to take… we have the next item?
**David Luna Bistuer** 20:56 Yeah, maybe we just kind of skip. It's just, so the PR from somatic devices won't, remove.
kind of the exclusivity between usurization data and URL user isn't original. It's approved, so thank you for the people who reviewed it, but I got a comment at the end from From Thompson?
That, puzzled me a little bit, so he was, asking about why not removing interlock?
The comment says, should we remove these articles?
Let me share my screen.
Basically says this, should we remove this attribute?
From the entity, as currently the docs is saying that it's recommended to provide in all cases.
So I know… I don't know exactly what he… meant?
So, if somebody can give me a clue… .
**Jared Freeze** 21:54 I mean, the literal read is that they're equivalent, right?
And they're not, right? Like, it says Intel Mac right there in the thing, like, if I want to know it's an Intel versus Silicon.
Apple Silicon, like, I can't get that from… What is currently provided in the client hints.
So, I think they're… they're not equivalent, which is why we had that discussion about including, you know, both. You know, it's a good thing if you've got it, because parsing the brand name sucks. It's hard to do, but… you know, it's not everything that's included here, so you lose a lot in the newest browsers, which I think was a bad trade-off, so… I understand that's what it says, I don't think it should say that. I think we should modify this.
**David Luna Bistuer** 22:39 Okay.
**Jared Freeze** 22:40 Yeah, that's… I mean, I can comment here as well, but…
**David Luna Bistuer** 22:46 Okay, good.
Thanks, Sean.
That's it, we can move on to the next item.
**Jared Freeze** 22:53 Unless anybody disagrees.
**Christopher Arredondo** 22:55 Hi, everyone. Well, I have an issue related with the challenge to use compression in the browser side, so… Our principal clients in the app for frozen applications has a lot of requests from the front end for tracking traces, logs.
And I have found a challenge related with the modify the max attempt default, the retry to send this signal. Because without compression, we have a lot of requests started from the browser.
So, in some cases, we have, We have the max capability in the… collector, so… when we have rate limits, we receive a lot of error from the server, so the idea is to have the possibility to reduce the max attempt using a configuration to set, depending in every specific case.
But the definition in OpenTelemetry is a static value, so my approach is offer the possibility to… Passed by configurations this parameter to set the max attempt to retry a request from the browser to the collector.
maybe this can pass, because I think… I know that exists an approach to discussing, related to implement the compression, using the compression stream API, or using another external library, but right now, this is an issue blocking our client's internal the company.
**Joaquín Díaz** 24:49 I don't think I was here when this was defined, but I don't see a reason.
to not… via configuration.
Did you have any pushback from the PR?
Or anyone, they commented?
**Christopher Arredondo** 25:06 I already created the issue, I started to create the issue, and I need to… I have to create the PR with the changes to receive the feedback.
So, I create the issue, and I present to you guys to have some internal feedback before to present the PR to the open community.
**David Luna Bistuer** 25:29 Okay, I'll check with the JavaScript SIC, which, usually I have meetings on… on Wednesdays.
Because I think that the create, the return transport, it affects, all the protocols, not only HTTP, but also gRPC, so… Let me check with them if there is any… possible issue.
With that.
Okay. And then, I'll ping you, I'll ping you back. Maybe I'll drop a comment in the issue itself.
**Christopher Arredondo** 25:56 Okay, thank you.
**David Luna Bistuer** 25:57 call.
But I don't see any issue, so if there is any problem of complexity, I think that that's a good addition on the options.
**Christopher Arredondo** 26:10 Okay.
**Martin Kuba** 26:12 And it looks like it will also, affect Node, not just… not just browser, right? Like it would, yeah.
**David Luna Bistuer** 26:18 Exactly. That's what I meant. Yeah. Thank you.
**Martin Kuba** 26:30 Okay, is there any other topics?
That anyone wants to talk about?
**Joaquín Díaz** 26:38 David and I created a PR each for the migration of the special instrumentation?
If you want to take a look, like, they are both on the same, but in different ways, so I think it's a good way of… Trying to settle down on some conventions, and trying to understand, like, the… Code style that we want to have on the… on the code base.
Yeah, I think they both work fine, but yeah, just getting your feedback on that.
**Martin Kuba** 27:15 So, Joaquin, are you and David working on this together, or are you looking for feedback?
**Joaquín Díaz** 27:21 We happen to be, like, by coincidence, doing the same, without knowing.
So, I guess… Yeah, I think I don't want you to go through two PRs is more time, so I don't know. I think we have to settle down on…
**David Luna Bistuer** 27:40 Yeah.
It is not a competition. But basically, I think the main difference… I'll drop a comment… I'll put a comment here in the… in the doc later. The main difference between, the approaches are… that, about resource timings. My PR is doing nothing about resource timings, I'm just creating a spanse for For the fetch request, and then… I'm kind of putting something in the middle, some place to start a state, so the resource timing Interpretation is capable to, attach.
So, correlate the logs.
With the… with the spuns.
So it's… it's just a… let's think about it like a kind of a PLC. On Joaquin.
Correct me if I'm wrong, but it's handling everything, so it's also using the performance observer, and then getting the resources.
So, main difference, like, yeah, there are some pros and cons. I made a comment about that.
I think no solution is better than the other, it's just that they have different traits.
That's… that's the difference. So, I guess, for example, in my… in my situation, I would say it's something that is maybe tricky, it's about the configuration, because maybe you want to ignore some URLs in the fetch, but then you are getting the resource timings, because you didn't set the configuration properly, you didn't sync configurations in both.
So it's kind of the configuration's… Some configurations get split in two interpretations.
But one of the processes that maybe you don't get, you don't have the chance to… you're avoiding to have duplicated rock records for the same resource.
So, it's… you have to, you know, you have to… there are some trade-offs in each of them, so… but I'm fine… I'm fine with, So, I'll put a comment there, have a look, and… disrupt your thoughts, and you'll see what is preferred. So I'm fine with either with either instrumentation, so I think both are fine.
**Joaquín Díaz** 29:50 Yeah, my main idea was, so given that span events are getting deprecated, Having something that is as equivalent as possible to the old existing instrumentation.
So there's less pain on users migrating from… the current fetch instrumentation to the new fetch instrumentation.
I guess it was simpler for them to have one instrumentation instead of some two, I guess, for resources.
I agree that… The instrumentation should be as… reducing scope as possible, so this looks like a big instrumentation, given that it's doing, like.
Two things are estimating spans and logs.
And maybe in the future, I can see us breaking them apart, but also, I think we have to figure out the best way of migrating, like, from the old one to the new one.
**David Luna Bistuer** 30:43 That's a good point.
**Joaquín Díaz** 30:45 In any case, we are still breaking the, like, the current… way by moving away from spun events, so… I can see the case of the new one just not having anything to do with resource hanging and one, but I'm open to discussion on that.
**Martin Kuba** 31:05 If you… if you have some… if you want to provide some feedback on this, like, where should we, comment on… each of those PRs, or should we have, like, some… Or there's… I think there's, like, a migration… an issue to migrate these instrumentations.
Right.
**Joaquín Díaz** 31:21 Yeah, that's Let's unify the discussion, so I will… maybe we can have each a comment on the approach we took.
with the link to the PR, and we continue the discussion there.
like, again, call-wise, they are the same. I guess, as David was saying, like, the main difference will be, do we want to have Blocks for resource timing, or we want to have that on a separate instrumentation?
**Martin Kuba** 31:50 Okay.
Alright, yeah, let's move those comments there.
We're at time, so thanks, thanks, everyone.
**David Luna Bistuer** 31:59 Thank you.
**Christopher Arredondo** 32:01 Hi.
