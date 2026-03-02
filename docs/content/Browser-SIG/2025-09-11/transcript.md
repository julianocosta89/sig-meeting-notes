SIG: Browser SIG
Date: 2025-09-11
Duration: 44 minutes
Zoom Recording URL: https://zoom.us/rec/share/GBpl3_h62GrwZKgi043_9rddYf4AF8pXNzwOUv_0IzyNFb67ulL5Vm74Y2uVMqmZ.ltdwm8EtT_6gN41a
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 01:58 How's it going?
**Benoît Zugmeyer** 02:04 Hey…
**Jared Freeze (embrace)** 02:10 Hey, Martin.
**Martin Kuba** 02:10 Hey, good morning.
Evening.
**Jared Freeze (embrace)** 02:18 Oh yeah, where are you?
**Martin Kuba** 02:22 I'm on the West Coast, so morning for me, but I'm not sure about others.
**Jared Freeze (embrace)** 02:26 Yeah, right.
Mmm.
Yeah, Dan said he's not coming.
Thanks for all the work you've been putting in, by the way.
I mean, to everybody, but… That's cool. Did we ever get in touch with Carly?
**Martin Kuba** 03:13 No.
**Jared Freeze (embrace)** 03:14 She never wrote back, but, there was the, the PR I wanted to go over, but…
**Ted Young** 03:20 Man…
**Martin Kuba** 03:21 She's…
**Ted Young** 03:22 Overlap between this and the entities, SIG is unfortunate. Sorry.
**Martin Kuba** 03:30 Yeah, Carly, Carly, I think she's at Microsoft, so maybe you should, reach out to Ram.
I'll ask him if she's still working on this.
**Ted Young** 03:40 Oh.
Yeah.
**Martin Kuba** 03:42 Yeah.
**Hector Hernandez** 03:43 Yeah, Carly is in my team. She should be working on that, if… I can talk to her later today.
**Martin Kuba** 03:51 Okay, great, thank you.
**Jared Freeze (embrace)** 03:54 It's so funny.
**Ted Young** 03:56 Would you mind asking her to say hi on, Slack?
Because I think we're ping… we're not sure if we're pinging the right Carly there.
Huh.
**Hector Hernandez** 04:07 Okay, yeah, yeah, sure.
**Ted Young** 04:17 Okay.
Deep, deep, dear…
And another FYI, I will, once again, I'll be out next week. I'm having surgery on my arm,
So I'll be recuperating for the rest of the week, so I probably won't be coming to…
meetings at 8.30am, but, I'll probably still be checking Slack, if you want to ping me.
**Jared Freeze (embrace)** 04:59 So we won't catch you on medication.
**Ted Young** 05:01 Yeah.
Yeah, it'll pretty much depend on the painkiller load that I'm on.
**Daniel Dyla (Dynatrace)** 05:09 Is that related to your freak filmmaking accident?
**Ted Young** 05:13 Freak filmmaking accident.
**Daniel Dyla (Dynatrace)** 05:16 I haven't had…
Didn't you try to grab a dolly and rip the muscles in your shoulder or something like that?
**Ted Young** 05:23 Oh, I did have a freak accident last year, but I was moving a table. It was, like, very boring.
**Daniel Dyla (Dynatrace)** 05:31 Oh, it was a table. I thought it was, I thought it was a piece of table making.
**Ted Young** 05:35 And, it swung, and I tried to catch it with my arms so it wouldn't bang into my knees.
And my bicep popped off of my elbow.
Which was very surprising.
And then, I got surgery for that, and they said, now, because your left arm is basically the same as your right arm, genetics and everything else.
**Daniel Dyla (Dynatrace)** 05:58 the chances are pretty high this will happen there, and seeing as you probably didn't learn anything from this experience, you'll probably just do it again.
**Ted Young** 06:14 So, yeah. It didn't actually pop off this time. Thankful.
Well, good luck to you Thanks.
**Jared Freeze (embrace)** 06:21 Yeah.
**Ted Young** 06:22 Anyways, browsers.
How do they work?
We've got a couple things on the agenda. We've got people on the case for,
Making us a repo and everything.
If you aren't a GitHub org member, and you don't have a membership request, please make one.
Just FYI.
And, we've got stuff on our agenda. Do you want to kick us off, Martin?
**Martin Kuba** 07:00 Yeah, so my topic is about the page view semantic conventions.
that I've… that we talked about last week,
So we made some progress on that, but…
I actually started a discussion in Slack about this, and my question here is…
Whether or not we want to include
The soft navigation as part of this event.
So originally, we wanted to, and we even have…
implementation that I think Abinad… Ebenad worked on.
But since… since, like, we talked about this, you know, there's been, like, a couple years.
There's been some work done, in…
In the space about self-negations, there's a… there's an experimental in, experimental…
Implementation of soft navigations in Chrome, that's behind a feature flag.
And essentially, it's, it's more than just… it's about more than just…
observing the change in the URL. There needs to be, like, they define soft navigations as a combination of user taking an action.
the URL changing, and some change happens in the DOM.
And there is… and soft navigation is reported using the Performance Observer API, so it just becomes another entry in,
You know, in performance.
Observer?
So, given that,
I was wondering if it still makes sense to include it in this for a few reasons. One is that the instrumentation will likely be,
more complex. It will not just be, you know, hit…
Patching History API. It will be…
looking for user actions, observing DOM changes.
So, and because…
this thing is evolving, and it's very much experimental, like, it's not standardized yet. I expect that it will take longer, for that instrumentation to also become stable, so I don't know if it makes sense to, like, have it, like, in this
basic, very basic, like, page view instrumentation.
The, the, the other thing that I, that,
I was just wondering, like, if… like, since, like, it's being called soft navigation… self-navigation, like, in the Performance Observer, and in these proposals that Chrome and other people are working on?
Like, do we want to just call it soft navigation event?
You know, instead of page view, with the type, so that was, like, my last reason. And so, my proposal, I guess, is to…
To have a separate instrumentation, and maybe even a separate event.
Semantic conventions for self-navigation specifically.
**Jared Freeze (embrace)** 10:12 Yeah, so as you're explaining it, I'm thinking… so they are completely different things, in my mind. So, how you navigate and what you consider a page view, I don't even think are the same thing, because you can definitely… I remember, like, in the old Google Analytics days, to talk about that again, which I always do, is…
you know, we would mark stuff as page views that had no URL change, right? Where there was a major change in the DOM only. So, doing auto-instrumentation for that is gonna be…
maybe impossible. I think people are just gonna have to say, like, this is a page view. Now, I'm not saying that you can't have that on, like, first paint, which I think is where I would probably start. I probably wouldn't wait for LCP, but, I think first paint is kind of like…
the user has intent, they've seen something. Like, this is a page view now, not technically navigation start, because you're like, I requested something, but I left because it took too long. Not a page view in my mind, right? But you also might want to mark something that's just somebody moving through
a modal.
Right? Like, this is the page view, and no URL has changed. So, I think we need to separate those two. I think you're right about the fact that navigation is not counting.
How people are interacting with your site.
**Martin Kuba** 11:31 Yeah, that's interesting, like, so it sounds like your definition of page view is, like, yet different.
So, like, soft navigation, like, here is…
So the page views event was supposed to…
So it was intended to, to capture page loads, like, when a page is actually, like, a document is loaded, and then, like, and then, like, I think many people consider SPA route changes as page views as well.
When, like, you… like, you navigate… instead of, like, reloading… reloading the whole page, You know, like, you just…
updates the whole DOM.
Without reloading the page.
And, like, so that sounds like… but the URL… in that case, the URL is… needs to change. That's, like, the definition, of, like, the spot… spot…
Page view or spot route change.
**Ted Young** 12:26 But…
But there's a logical concept, it sounds like that's what we're getting at here. There's the mechanisms of, like, how the browser works, there's different ways you could end up at the same state, and we need to know how you ended up there.
The reason why I think people would care about soft navigation, however we model it, is you want to know how the state refreshed is often when you're trying to debug something, the different ways you get to a resulting layout.
May involve different kinds of state getting refreshed, and that can lead to figuring out why something's a bug in this situation versus not that situation.
But what Jared's talking about is more like a logical concept for, like, business value.
Right? Where you're trying to… you have, like, more of a… a business concept of a page view.
**Martin Kuba** 13:21 Yeah.
**Ted Young** 13:22 And that… and maybe what we need to be doing is, like, keeping that…
that separate. Like, maybe the approach is, as much as possible, to try to stick to browser events and browser concepts when we're talking about reporting the mechanics of what the browser is doing.
And we try to avoid making kind of, like, synthesis… synthetic things that represent that. And then the synthetic things we generate.
Are more like these logical concepts, like page views and stuff.
**Jared Freeze (embrace)** 13:53 Yeah, like, do you agree? Like, every navigation has a page view, but not every page view has a navigation. That's all I was trying to cover, is that people are not always changing the URL, so that's… But I definitely think, like.
Yeah, that type of navigation belongs in every
like, load of a page, you know, whatever that might be, so…
**Joaquín Díaz** 14:18 I think, like, I agree of having different concepts for page view and navigation. I agree with
Navigation, meaning the mechanics on how you get to a page.
But I still, like, I was saying in the Slack said, I still think we have to define what a page is to us, and I still believe that a page is
like, conceptually.
how you use difference… like, difference between pages is, most of the time, the URL. So if you wanna, like, if you have users trying to do analytics on pages, they were… they will want to group those… those pages by URL, right? You have to know, I'm on the home page, I'm on the products page, whatever.
I understand that there are many ways of…
navigate 18 through the two different patients, I'm…
they may not include URL changes, that's true, but you can change the title by changing a state or whatever, like, a variable. But at the end of the day, if you're a user trying to understand, like, how users are using your page, you want to group by something, or, like, you want to slice that dimension by something, and that… to me, that something is the URL.
Right. So that's what I think, like.
We can have multiple instrumentations trying to understand each navigation mechanism, but then, at the end of the day, a page view, to me, is a…
page, like, an actual browser URL with something in there.
**Ted Young** 15:42 But it also feels like my takeaway from what Jared was saying is, like, we need an API
for end users to manually be able to take over control of this, which is a little bit different from a lot of the stuff that we report from the browser, right? A lot of it is just the browser did a thing, so we report it.
But now we're saying we might have a situation where the browser's doing things, and the user might be like.
maybe you have a default way of using these as triggers to mark page views, but for this app, for my situation, I actually have my own opinions about what does and does not count as a page view.
**Wolfgang Therrien** 16:23 Yeah.
Yeah, I think that could be really powerful if there's a supplemental way for users to emit
supplemental page views that take into the context of their app, whether that's modal, or maybe they're hooking it to some sort of bespoke routing, or something that they've got going on inside their single-page application, or their micro front-end architecture, right, that they're doing some… some wonderfully crazy stuff.
But if they're able to emit these similar types of events.
you know, based on some composite underlying instrumentation primitives, I think that could really
Help with a lot of the types of questions that we're seeing.
**Ted Young** 17:03 And they may want to suppress things, too, is the other things they may want to do, right? You may have your React app is… has some part of it cycle where you're like, that's not a frickin' page view, suppress that. That's just noise.
**Joaquín Díaz** 17:16 Stir.
Yeah, I think, like, I will…
I will have that, I will have, like, some way for getting to, like, each SPA's navigation or roading library. Right.
But also, I think, like.
having something really simple to start with, which will be listening to URL changes, I think is fine for most people. And then, if you don't like it, you can disable, and you can tell us, okay, this is a page, it's a new page, it's another page.
But I would start with having something that, you know, works for most people.
**Ted Young** 17:48 But it seems like the thing that would work with most people, and then, yeah, I want to let other people talk, but it seems like the thing that would work with most people is if we separated this out, and we're saying, like, we don't want to mix in this logical event with the browser mechanisms we're reporting. It's more like we want to create a separate synthetic event.
And then we want to have our instrumentation, like, by default, like, trigger it in all of these scenarios.
and then have an API for the user being able to…
to maybe manage that in some way. I don't know, I'm curious how, like, existing implementations deal with this.
**Abinet Debele** 18:29 I can talk about our… our experience, at AppDynamics related to this instrumentation.
So the page view instrumentation is…
The main idea is to just get a count of the pages that are being done in a minute or in an hour.
So the page view, it just counts whether it's… whether it's a base page, or we call it a base page, which, if it is a page load, or a virtual page if it is a subscription application. So we… we're just getting the count of those… those types of pages.
But for the detailed metrics of each of the page loads, or the virtual page, we have separated.
So we have documented loading instrumentation for the PS page, which provides the detailed matrix for the
For the page, and also, we have a separate instrumentation called Virtual Page Instrumentation.
Which is like, what Martin's talking about, the software navigation instrumentation.
So, we have that to give us detailed metrics about the virtual page, where… how long it took to load, what type of dome changes happened, what type of XHR or phase calls happened during that instrumentation.
So, I think we still probably need this event to get the count of these pages, but for the detailed metrics, we can still use the other instrumentations.
**Ted Young** 20:02 Cool.
So, I think circling back to your question, Martin, it seems like maybe the direction we're going is, like, let's… let's try to…
To maybe not make synthetic events…
Like, for your page view event right now, maybe we want…
To move more towards, like, an event that's more like the initial load and paint.
Kind of stuff.
**Martin Kuba** 20:28 Finish load.
**Ted Young** 20:29 And then for the other changes that are happening, try to maybe just model it mechanistically.
For now.
And then figure out how we want this, like, page load concept to… to sit on top of those things.
**Martin Kuba** 20:45 So basically, to take out the soft navigation from the page view right now.
Yeah.
**Joaquín Díaz** 20:54 I mean, I will take it out last night.
As you say, we can't wait until this…
this experimental feature from Chrome is there, so we don't have to do it ourselves.
But you still want to chuck… Page views.
That happened… that are happening in SBA. So it…
How do you do that, Agita? That's the question, I guess.
Because you… those are also important, you want to know how people navigate through all the pages, not only the first one.
**Ted Young** 21:25 Yeah.
But it's actually, like, the soft navigation is maybe… there's some of what other people have been calling virtual navigation, right? Either, like, React using the pound…
You know, changing the pound parameters, right? And you're navigating that way, and it's not technically a page load.
Or like what Jared was saying, maybe just something literally arbitrary happens, like a modal appears, and for that app, they want to be like, we want this to count as a different page. So it's almost like…
what Abinet was saying, it's like, maybe that we just have a concept of, like, a virtual
navigation change, or, like, a virtual page change. And then soft navigation is maybe something that gets actually just bundled into that stuff when it shows up.
**Joaquín Díaz** 22:16 Yep.
**Ted Young** 22:17 Or at any rate, it doesn't exist right now, but a lot of virtual navigation does exist right now, so maybe we should focus more on that stuff.
**Jared Freeze (embrace)** 22:23 Yeah, and if you guys think I'm… it's an edge case that, like, you have views change without URL changes, it's just, like, I've been at plenty of places where they just don't do routing properly, so if we just want to do the routing, that's fine. Maybe this is just added later, but, I don't want to hold anything up, you know?
**Ted Young** 22:40 It's worth writing that down, right? Like, to me, that sounds like a requirement we'd have to honor eventually.
**Jared Freeze (embrace)** 22:48 Yeah, I think, I think so.
**Wolfgang Therrien** 22:50 Yeah, even if we don'.
**Jared Freeze (embrace)** 22:51 Everyone's on Next.
**Wolfgang Therrien** 22:54 even if we're not building the mechanism to capture that automatically, right? If we're able to define the shape of the data that would be emitted there, and we can point folks to
some best practice, or a slack that's like, hey, this is the thing that you want to emit in the bowels of your application, because…
it's your application, and maybe you're doing something a little non-standard, or something that is not in the, you know, in the set of prevailing best practices that we're trying to encompass here, it's better than, not having it considered at all.
**Ted Young** 23:23 Yep.
**Martin Kuba** 23:25 This is so sarcastic.
**Abinet Debele** 23:26 Martin, you were arguing, like, the soft navigation part should be removed from, the page waven, right?
Similarly, like, we have the page load, we already have document load instrumentation that is already reporting on the page load.
If we… if we are saying… We have to…
Remove the virtual page event from this instrumentation.
We also may have to remove the base page, too, because there's already an instrumentation for document load, so…
So what I'm saying is, like, we need this just to counter…
That changes the pages, not to give us a detailed instrumentation, or detailed metrics.
So, what, what is… What's the problem if we just keep it as is, and then…
Create a separate instrumentation for the software navigation still.
**Martin Kuba** 24:22 Do you mean, keeping… so… so do you… do you mean using the page view instrumentation only for hard…
**Abinet Debele** 24:29 inf…
**Martin Kuba** 24:30 Oats.
**Abinet Debele** 24:31 No, keeping it as it is for post, hard navigation is soft navigation.
But it just keeps count of the changes? No, it doesn't… Give detailed instrumentation.
**Martin Kuba** 24:44 Yeah, so I don't… I don't agree with that, because… because, like, right now, the… the instrumentation only takes… only listens to URL changes that… that happen using the History API.
**Abinet Debele** 24:56 Nope.
**Martin Kuba** 24:57 And… That may or may not represent PageView, so… You know, like, it's… that, like…
like, the definition of, like, the self-navigation is, like, more than just URL change.
like, the URL change could change for different reasons, things, like, you could… you could add, like, a hash, you could add a query parameter.
So… and that may not represent an actual page view.
**Joaquín Díaz** 25:31 I agree with that, but I also think if you remove a query string,
and you listen to URL changes, I think you are correct in most of the cases anyways.
I agree, like.
Changing the gray string, yeah, it's definitely not a page change, but changing the URL is, in most cases, a page change.
So I… yeah. I don't know how much we want to offer out of the box, or…
You know, cover all these such cases.
**Ted Young** 26:00 What about when you change the page back to the same page that you were just on?
Right. Does this…
Do you need to record the rendering information that happened, but this doesn't count as a page view?
You know what I mean?
**Joaquín Díaz** 26:15 They can refresh. Around there.
**Ted Young** 26:20 No shorter.
**Joaquín Díaz** 26:21 If I forgot.
**Ted Young** 26:21 It programmatically makes a URL update that doesn't actually, like…
For a paint change, for example.
**Joaquín Díaz** 26:31 I mean, yeah, you…
**Ted Young** 26:32 There's probably a lot of edge cases here.
**Joaquín Díaz** 26:34 I mean, at the end, At the end of the day, you can do whatever.
On the browser.
and Europe can work. But, I think, like, conceptually.
If you want to separate those species, if they… if they have the same year old, it's hard to separate them.
**Benoît Zugmeyer** 26:51 If we want to be a bit more unopinionated, we could just have a… URL change event.
And so we will record any URL change.
**Martin Kuba** 27:09 Yeah, that's what I… that's what I was also proposing, not calling it page viewage, but the URL change.
**Ted Young** 27:16 That's what you mean?
**Benoît Zugmeyer** 27:17 Yep.
**Ted Young** 27:18 Yeah. We might want both, I guess, is kind of what I was suggesting. There's, like, I'm trying to debug this system from the perspective of, like, I want to know all the operations the browser was actually performing, because maybe something dumb is happening, so, like, don't…
don't hide that from me and give me some synthetic stuff, like, just tell me all the things that it did. And that would include, probably, some calls to, like, navigation APIs and, like, stuff like that.
And then you have this concept of, like, a logical page view, and the primary purpose of this is not so much, like, debugging the situation as it is, like, you know, just producing, like, business metrics.
Essentially?
**Joaquín Díaz** 27:59 Yeah, so I'm working on the concept of a page load event, which seems to be conflicting a lot with this.
I'm maybe… It's, like, pretty much the same.
we can maybe think about it. I like the idea of having a virtual page, maybe with, like, virtual page load, and…
our page, or whatever. And those could be the ones that are more used for analytics in a way of, okay, I want to know how many people went to my homepage, or how many people went to my products page.
And then you have all the, like, actual…
mechanism events that are, like, they all changed. There was a soft navigation, there was a hard navigation.
And also, we just report them as they are. No opinion or anything, we just say, okay, this happened, and that's it.
And then we have the other concept of the page being loaded, different… in different ways, like self-loaded, or hard-loaded, or post-start, or whatever we call it.
**Wolfgang Therrien** 28:59 Yeah, I mean, I think eventually we'll definitely want, sort of, something that handles, like, user impressions, so that we can look at trends and how that relates to maybe performance or something like that. But, like, right now, if we have to choose between
something that is maybe very ambiguous, and something that's very concrete. Like, I think getting these instrumentations that are omitting what is very, very close to what the browser's doing is probably the most, like, useful tactically. And then we can layer on some stuff that either composes the outputs of this sort of underlying instrumentation, or we can provide guidance to be like, hey, when you are interpreting these metrics, these are… you need to decide which of these things
is… You know, automatically going to be an impression here, and we can have user impression instrumentation that
can, you know, do that on the client, or do that in a, you know, a collector or something, right? Wherever that makes sense. But we can't do that without the sort of very, very close to what the browser's doing sort of picture, right? So I think if we have to choose between those two things, I would mirror as close as we can to what the browser's doing today.
**Joaquín Díaz** 30:04 Yeah, Galaxy.
**Ted Young** 30:06 I like that.
**Martin Kuba** 30:07 So just to quickly wrap up for what I have is, so for the semantic conventions.
I think I would… I would leave them…
the way they are. Whereas, like, we'll have the type, which is, the hard page load, and there's a virtual
Page view.
So we can leave the semantic conventions, but the question is still about the instrumentation. Like, it sounds like…
In the instrumentation, we haven't made a decision of if you want to, like, auto-capture virtual page views or not.
**Joaquín Díaz** 30:40 A thing that you were saying at the beginning is, like.
if we want to do it properly, it's complex, because we have to listen to the DOM changes, user actions and URL changes.
like…
if we can work on doing that, but then also we know that eventually that API will be available.
So I don't know if it's worth doing it, or we can't start simple by just…
Taking what we currently have, which is URL changes and, and all else.
But, I…
**Jared Freeze (embrace)** 31:13 I will say, I think going after, like, URL changes, like, technically is gonna be easier. Like, DOM… like, snapshotting the DOM is heavy.
we might not want to do that. I know it's a combination of things, but yeah, like, going after just URL change, I think, is probably the easiest thing, if we're gonna do it that way.
**Ted Young** 31:34 Yeah, so maybe the takeaway, Martin, is just to treat this event like… like a business metric?
So, keep it just totally sep-
Don't mix in any… any concepts.
about, like, you know, page rendering, or a virtual page, or, like, any of those things. Just, like, maybe keep it super clean and basic for now, and we'll learn what we want to do with it later. And then, per Wolfgang's suggestion, what we focus on instrumentation-wise in this first round is maybe…
Because there's… it's a little bit less…
debate that we have to think about is, like, getting stuff stood up that just reports directly what the browser's doing, and we can say.
We're gonna get that stood up, and then that'll give us a better platform for understanding.
how to deal… like, we could probably, like, do some more experimentation and poking to figure out about, like, business metrics and page loads and, like, these other things. Like, how…
How we want them to work, what kind of options we want to give people.
That kind of stuff.
**Martin Kuba** 32:37 Okay. So, like, just really quick, like, so we do… do you want to keep the… the type, the page you type in the semantic conventions, or no?
**Ted Young** 32:47 Page view is not a term that has overlap with browser events, right? So I think it's fine to keep it.
But just strip it down for now. And per what Joaquin was saying, is, like, we don't… we don't worry too much. We just, like, for now, we're only gonna fire it on the initial render, and that's just, like, that's just where we're starting, because we know for sure that counts.
And that's just, like, our starting point, and then we'll kind of progressively figure out.
these edge cases.
**Martin Kuba** 33:17 Okay.
**Joaquín Díaz** 33:19 Alright, so quick follow-up, because I'm… I am still working on something similar, which is spatial, but it's still…
it's not a concept that the browser has, it's more like reporting based on navigation performance API type, the list of resources that you get.
And it has some, maybe, opinions, so I don't know if we should… following this idea of
More, like, reporting instead of building metrics in the client yet.
They should… Should I move on to…
maybe taking a look into the… I think it's called Web Resources?
Pan that we have right now on the instrumentation.
And transforming into something, like.
an event, like, it's a resources load event that just reports what is on the performance API on the browser.
Instead of, having, like, a facial event.
**Ted Young** 34:14 Maybe even just writing down a proposal, because page load is, like, so complicated. It's, like, so important, and so much is going on there. Maybe we just need to have a bit of a model.
For, like, here's all the things the browser fires when this happens, here's how we want to bundle that up, would probably…
Help people give you feedback on how to model that area.
**Joaquín Díaz** 34:39 Okay. Yeah, I can work on a proposal, then we can think about it. It's like a bigger… sorry, a deeper dive on the documentation I wrote earlier.
**Ted Young** 34:50 Great.
**Joaquín Díaz** 34:50 And.
**Martin Kuba** 34:52 just… I was just gonna say really quick on this, and we can… we can continue the discussion in Slack, but there is a… there's an issue and proposal, like, to just basically capture a navigation timing event.
And… and then Web Vitals events.
Which, so, like, that, you know, navigation timing gives you all the timing that the browser gives you, and the Web Vitals captures the, like.
you know, the LCP and… So, that is…
**Joaquín Díaz** 35:18 Okay, that is not merged yet on the conventions.
**Martin Kuba** 35:22 It's not merged yet, no. Actually, Web Vitals semantic conventions is merged.
Navigation timing is not.
**Joaquín Díaz** 35:32 Yeah, okay, yeah, for sure, navigation timing is part of this, so I can take a look.
Like, do you know if someone, like, on this group is working on that, or…
the PR is just there, or it's an issue mode of PR.
**Martin Kuba** 35:46 Let's see, yeah, like, I actually, I entered the issue a while ago, so we can just continue the discussion in Slack through that.
**Joaquín Díaz** 35:53 Okay, yeah, sounds good.
**Ted Young** 35:58 Great.
Cool. Well, we're over time.
The other thing I wanted to consider that started on Slack, someone was asking about attributes like page full URL and stuff.
And I started to wonder whether there's some amount of this page view info or navigation info that's relevant to just everything going on, and maybe could be modeled as a resource. So that's the other thing.
I wanted to, like, stick in people's brains. Is there some stuff where we're just gonna get our users asking for, like, page full URL on, like, every single event that we, like, produce? Someone at some point is gonna show up and be like, I need to know what page this event happened on.
You know, and for things like that, where they are effectively a singleton in the browser, do we want to actually, like, lift some of that information up?
into the… Into the resources, since we can change them now.
Rather than… Sticking them on all the different events.
**Joaquín Díaz** 36:57 a lot of resources can't change now, because the URL will definitely change.
**Ted Young** 37:01 They, they, they will be… resources can change in the future, yes, with entities. That was a thing we needed to push through so that sessions could work.
Essentially, because your session ID changes.
**Joaquín Díaz** 37:15 Okay, yeah, in that case, that definitely makes sense, clavular resource.
**Ted Young** 37:19 Yeah. Zero.
I don't want to go too crazy, but that is, like, a place where it's, like, you could almost see the page… page view, page change almost be more like an entity.
Change.
than an event. But that's, like, getting us into, like, new APIs and new stuff in OTEL, so I'm, like, a little nervous about it.
For the stuff that seems like it's, like, relative to any event we would emit from the browser, it almost… that kind of feels like stuff that should be up there.
**Daniel Dyla (Dynatrace)** 37:51 I'm also not… entirely sure how long it will be before those, like, mutable APIs are available.
**Ted Young** 38:01 Right.
Exactly. We don't have APIs for these things yet, so we're certainly not.
**Daniel Dyla (Dynatrace)** 38:05 We're still pretty early in that process. We're in, like, the… somewhere between OTEP and SPEC part of the process.
**Ted Young** 38:13 Yeah.
I mean, we do need that stuff effectively before we…
you know, call this… our browser stuff stable, because we definitely need it for sessions, but… Yep.
I don't wanna… I don't wanna derail us with that concept, but I did… did think it was, like, pretty notable that…
We'll… there's a bunch of stuff that'll either… we'll find a way to put it on an entity, or just for the next several years, we're gonna have a whole bunch of, like, this constant drip of issues, just getting every single browser concept added to, like, every single event, kind of a thing.
And it'll be worse for us than your traditional vendor, right? Because people are taking our data and then looking at it in, like, 10 different tools.
**Jared Freeze (embrace)** 38:58 I had a quick question. Is this… so, somebody was talking about url.full being on a resource, and is like, is it the image that loaded, or is it the page that loaded the image?
Is that related to this at all? Like, where you're sort of… Yeah.
**Daniel Dyla (Dynatrace)** 39:14 If it's on the…
on the resource, I would expect that to be the page that loaded the image, and if it's on the request, like, as an attribute, I would expect it to be on the actual image load.
Yeah.
**Ted Young** 39:33 Yeah, there's, like, HTTP requests we're making in the browser, and those all get handled as spans. But we're saying for the browser itself, right, it's this funny thing where, yes, we're talking about some HTTP webby stuff, but we're really talking about the environment that the… everything is executing in in that tab, and, like.
When that changes, like, that, like, that it changes for everything.
Right? Now you're running this route, or this function, or whatever on this, like, new page, right, with this new navigation and new everything.
Etc, etc. But it might have been, like, a pound page load, so, like.
The session and everything else didn't change.
I don't know.
**Wolfgang Therrien** 40:17 Yep.
**Ted Young** 40:19 It's worth looking at.
**Wolfgang Therrien** 40:21 I could definitely see full URL and, like, URL, like, route, like, route pattern being really useful here.
**Ted Young** 40:29 Yeah, yeah, a lot of… there's a lot of, essentially, framework information that's just describing everything going on.
**Wolfgang Therrien** 40:36 Yeah.
**Ted Young** 40:37 Right there.
But there might be also edge cases where people are loading multiple things. I don't know how any of that works. I don't know how we deal with iframes.
It's probably a long tail of everything here.
**Wolfgang Therrien** 40:50 Yep.
**Benoît Zugmeyer** 40:51 Also, also in, in this… That kind of resource.
I think it could be interesting to have an ID, a unique ID, so we can kind of…
Query all the telemetry that happened on a single instance of the page.
**Ted Young** 41:12 Right.
So you certainly have, like, session ID,
Yeah, it would be interesting to know what other kind of IDs we want.
you know… Is there, like, a…
Do we have IDs other than the session that we really care about in Rome?
**Jared Freeze (embrace)** 41:34 we're actually building something for this already, where we're, like, chaining tabs together. Keep track of the tab, keep track of the URL, keep… you know, there's, like, a lot of stuff that we bring together, but the chaining is going out today, so maybe I'll send it over, because we do want to propose that for,
you know, again, I'm turning into the business guide, it's not what I intended, but like, you know, seeing the funnel, you know, seeing the URLs that go together, basically, so…
**Ted Young** 41:59 Great.
Great.
**Jared Freeze (embrace)** 42:02 So, anyways.
**Ted Young** 42:02 And I would like that to go into our doc as well, right? Like, this gets back to us needing to be describing what kind of… what kind of observability we want to be providing at this stage, you know?
And it definitely seems like people are super interested in sessions, and sessions that will span multiple pages and everything, and being able to, like, load all of that up in some way to… to…
apples-to-apples compare sessions with each other, but then also debug on, like, the session level. Kind of seems like that's our first… the most valuable thing we could go after first.
**Jared Freeze (embrace)** 42:40 Yeah, we're finding that with customers, right? Like, they'll look at a page, and then the next page is the error state, but really, it was the one before. And we… we just want to make sure that, like, the referrer is captured. But not only that, it might be the two pages before that as well. So, that was kind of the problem we were trying to solve, is that, you know, your problem's not always in the experience… like, in the page you're having.
That you land on, right? So…
**Ted Young** 43:02 And we're totally over time, but yeah, the philosophical thing I note, this difference between client debugging and server is, like, server-side transactions…
are usually very repetitive and fairly, like, short-lived before the state gets obliterated, right? Whereas on clients, you have this situation where the state is the most random combination of different petro…
perturbations of state you could possibly imagine, right? So it's far more common to have, like, weird state, out-of-order, logical, buggy, nonsense stuff
that slip through your unit testing and everything with client-side things, especially long-lived client-side things, or things where some kind of information is building up over that session. You just, like, don't encounter that nearly as much.
on server side, debugging.
In our industry, right? But on the client, there's very much trying to figure out this, like, long chain of, like, state changes, and when it gets into some invalid state, and everything is bad from that point onwards.
**Jared Freeze (embrace)** 44:13 The web is fun.
**Ted Young** 44:16 Good times.
This is, like, all clients. Yeah.
**Jared Freeze (embrace)** 44:21 Yeah.
**Ted Young** 44:23 Okay, I've gotta run. It's good talking to y'all.
**Jared Freeze (embrace)** 44:27 Oh, dear.
**Joaquín Díaz** 44:28 So…
