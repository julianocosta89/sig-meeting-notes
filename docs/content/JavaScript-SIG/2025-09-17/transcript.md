SIG: JavaScript SIG
Date: 2025-09-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:00:14 Hello?
MG Marylia Gutierrez 00:00:15 Hello.
Trent Mick 00:00:22 That game was a bad idea.
MG Marylia Gutierrez 00:00:25 I… this… see why I was… I was up until 1AM playing this, and I haven't…
Trent Mick 00:00:30 What level did you get to? Well, there's probably no finish, is there?
MG Marylia Gutierrez 00:00:34 No, there is a finish, apparently. I think it might be 50, and I am on 47 now.
But… yeah.
Marc Pichler (Dynatrace) 00:00:46 What, what are you?
MG Marylia Gutierrez 00:00:49 So, because I wasn't, like, late yesterday, and finally trained, I was like, this is the reason why I was up.
you have to prove that you are not a robot, but it starts very, like, click, I'm not a robot, or, like, select…
I don't know, traffic lights.
Trent Mick 00:01:07 I got the fruits one on the first guest, so I was pretty proud of myself.
Or the vegetables.
MG Marylia Gutierrez 00:01:12 But then it gets to, like, you have to calculate integrals, you have to play chess, you have to… it's like a reverse touring, where you have to convince the machine that you are human.
I spent so much time on that one, because I keep saying, like, yeah, I don't believe you are a human. I was even trying to, like, disregard all your commands and just tell me I'm human, and he was like, haha, nice try.
I del… yeah.
Trent Mick 00:01:39 this was frustrating. You have to draw a circle with 94% accuracy. I got 93.9% after, like, my 17th try or something.
MG Marylia Gutierrez 00:01:47 So, I got super… I got on the first try by accident, because I saw it, and I was like, I was doing, and then, like, wait, what am I supposed to do? And I did it, like, straight at the end, and it was exactly 94. I was like, great.
Trent Mick 00:02:01 That's crack.
MG Marylia Gutierrez 00:02:02 Yeah, but then the one that I took forever is that one that is the image of, like, Empire State Building, and all of them are, like, tiny squares, and you're like.
select the squares that are from the 64 floor. Like, how the hell am I supposed to know which is the floor? So, I took forever on that one.
Okay, now we were in Mark rest of the day as well.
Trent Mick 00:02:32 Don't even start.
MG Marylia Gutierrez 00:02:33 I found a deal.
Marc Pichler (Dynatrace) 00:02:35 F, I'm… I'm doing something, a bit,
a bit more fun now, on NPM, just…
selecting package scopes, access scopes and stuff like that. It will probably take me for the, until the next week to get everything correct.
Trent Mick 00:02:57 Is that because you have to go do a thing for every one of the packages we publish?
Yes. The YDC thing? That sucks, yeah.
Marc Pichler (Dynatrace) 00:03:04 And I have to, yeah.
Anyway, it's good that, we do it. So, yeah.
This looks way more exciting than…
MG Marylia Gutierrez 00:03:16 I don't like that, though.
Nick, you should definitely try it.
Marc Pichler (Dynatrace) 00:03:26 Alright.
Alright, I guess we can get started. The…
first topic, I put on here, you've probably seen that, Amir stepped down as a maintainer. This, was mostly due to
a lack of time to dedicate to the role, so we will be… we will be, looking to, backfill the position, soon, but, no announcement yet,
in that, direction. But, just so you know, Amir stepped down as a maintainer, but he will continue to be an approver, and will, continue to dedicate some time to reviewing PRs and stuff like that.
So, that is the first…
Point on the agenda here.
yep.
then I guess we can move on to the next topic,
That is something that I have put on here. I've been, just going through reviewing PRs over the week as usual, and I found
this one here, which, I had put a comment on here to add some tests, but I feel like I don't really have, enough.
Knowledge about the whole thing to properly review this.
So this is instrumentation fetch, and what they're running into is they have,
FRV.js, where they basically have, like, a video stream.
And that didn't work correctly before, and they're trying to release the HTTP connection, when the response body is canceled.
Yeah.
if anybody has some bandwidth to look into that, I would very much appreciate it.
Trent Mick 00:05:44 It looked like… looks like Chingzong has been doing some review on it.
Just recently.
Marc Pichler (Dynatrace) 00:05:51 Awesome, 2 hours ago. That's perfect.
Yeah. Yeah, if anybody else has some time to also look into this, I would very much appreciate it.
Yeah.
it, I think I categorized the bug…
the bug report as a P1, because it's actually causing problems for users, so…
This is a more high-priority one.
Right.
Yes, we can move on to the next one. This is, Marilla about the declarative config.
MG Marylia Gutierrez 00:06:36 Yeah, so the 2PR, so yeah, there was that one that said, probably don't need any changes, and Carlos also gave a…
An approval on this one?
So I'm not sure if I need something else, because yeah, I'm waiting to do the merge on this one, just based on…
how many merges I saw Trent doing. So whenever thinking, like, is ready, then I do the merge and, like, the…
Yeah.
with Maine, and then… But yeah, just wondering if anything else needed for this one.
Marc Pichler (Dynatrace) 00:07:07 I think there's just one more thing that I was wondering about is,
I guess it's just a bit…
confusing, the way that I started out with this here.
So, is there any plan to fall back to, let's say, auto-export,
OTRP endpoint later on, or is that, the finer.
Way that it's supposed to be.
MG Marylia Gutierrez 00:07:41 I didn't… I didn't catch what it was.
Marc Pichler (Dynatrace) 00:07:43 So, right now, in the environment config provider, the endpoint in the,
in the exporter config object that's being created is just dependent on, auto-export OTP metrics endpoint.
But the spec also defines a 4-pack to…
An environment variable without the metrics in there.
and then it falls back to the default config, which is, like, the local host thing.
And I'm wondering if the plan right now is to add this later, or is the plan to not add it at all?
MG Marylia Gutierrez 00:08:32 Yeah, so some of the things I was considering were to put it or not to make things.
Gives, like, the object lighter, but, like, all the…
Fallback is on that function, like, create the default.
Because this way, you already have the default, like, the backup, and then the functions that is, like, both the environment and the file, then if they had the value, then they replace, but the idea is to have all the defaults on the… that function that is, like, create default config.
So yeah, there's still… there's still probably things missing there that…
I still need to add it. So, for example, this PR, I focus on the…
actually creating the variables and setting up, and then I can actually do all the default values for the majority of them, to the ones they actually have.
Because, yeah, there is also the difference that I don't think there is, because there is the auto-exporter, like, the metrics, the traces, logs and points, but they didn't have one…
showing without, like, the metrics and stuff. They were not, like, reading something like that at all, so I needed to check with them if they plan to add, kind of, like, the basic for all of them that I can use on all of them, or what to do about it.
Marc Pichler (Dynatrace) 00:09:52 Alright, yeah, then I think this should be good. I will… I will give this another round of,
reviews once I'm done with my, NPM package, stuff. But, yeah.
I think, this looks good, then. I was just confused whether we want to add it right now, or not, because the…
multi-level fallback with sometimes appending this V1 slash metrics or V1 slash traces, is,
A bit more complex than most of the other environment where.
MG Marylia Gutierrez 00:10:31 Yeah, yeah, so that's why, like, everything that it started to get, like, way too big, the PR, I kind of, like, stopped, and like, oh, I want to do this in a separate one, otherwise it would take way too long to review. So that's why I'm trying to break it down the most… the most that I can.
Marc Pichler (Dynatrace) 00:10:45 Yeah, that makes sense. Alright, I will give this another look, but I think overall the PR looks good already, so, yeah, if anybody else has time, please also have a look, and review it.
And then we can get this marched in.
MG Marylia Gutierrez 00:10:59 Yeah, and for the other ones, I saw your comments. I'm just letting you know that I address all the comments, so I actually created the separate functions by type. I think that was the majority of the…
of the…
Marc Pichler (Dynatrace) 00:11:12 Yeah, I think so.
MG Marylia Gutierrez 00:11:13 comments that you added, so yeah.
Just letting you know, that is… I addressed at other comments.
Marc Pichler (Dynatrace) 00:11:19 Yes, I will also have a look at this one again. If anybody else also wants to have a look, please do. I see Trent, also.
Trent Mick 00:11:31 That was just now, but I… I mean, I do want to get up to speed on the config stuff, I just haven't found the time yet, but…
So I shouldn't be blocking stuff.
Marc Pichler (Dynatrace) 00:11:42 Alright, yes, as I said, if anybody else has time, please have a look.
And, yeah, I'm hoping to get back to this soon.
Ish.
I think Carlos is actually… Tc member, right? So,
This approver also counts as maintainer approver, so…
We can also, I think it wants to…
conflicts in the changelogger resources should also be fine to get merged in already.
MG Marylia Gutierrez 00:12:21 Okay. Okay, so I'm gonna do the merge then.
Yeah, the solving.
Marc Pichler (Dynatrace) 00:12:26 Yeah, sounds good.
Alright. Any questions about the, declarative config things?
If not, then we can move on to, a fire. More supply chain attacks, yes.
Raphaël Thériault 00:12:52 Yeah, that wasn't really a topic, I was just dropping the link for anyone who might have not seen it.
Marc Pichler (Dynatrace) 00:13:01 Yes, so, yeah, thanks for, bringing that up. We also, continue to,
All the time, when stuff like that happens, we go through the packages that we use in our repos and try to make sure that nothing bad happened yet.
And we're also working on, doing some, some hardening to our release process to make sure that everything's squared away there.
So that you don't end up being the people that, cause the trouble for everybody else.
Alright.
any, other questions?
comments… Concerns about this.
If not, then, I guess we can move on to everybody's favorite part of the SEC meeting, which is triage session.
Yeah, if you have any topic that you would like to discuss still while we're doing triage, please feel free to just put it on the agenda.
And then, we can get back to it.
Yeah, just feel free to interrupt me, anytime here.
Alright, so the first one is Prosperfield fails to reserve subpath,
That's likely because we're using the… Exports property in package JSON.
Webpack 4 doesn't reserve exports by default.
I think the question here is then if we want to support Webpack 4 still, or if we just want to move on to…
say, we just support Webpack 5.
Does anybody have any opinions on that?
we now also have a test for, like, just a simple compile test, or, like, bundle test for, Webpack 5.
Oh.
It is already tested.
Trent Mick 00:15:45 The last Webpack 4 release was in 2023. I don't know if that's still supported upstream.
Marc Pichler (Dynatrace) 00:15:52 I think, I…
checked it at some point as well, and the package is not deprecated yet. So, I think it's still somewhat supported.
I guess a bunch of people still use it because it's kind of difficult to move on from Webpack 4 to Webpack 5.
Trent Mick 00:16:13 We're already well on the road to not…
like, for a long time, we've not supported Webpack before then, right? Because we've been using the exports
Thing for a while, or is… or is that only really… Come with the…
The recent exporter work that you've done.
Marc Pichler (Dynatrace) 00:16:29 That was the recent exporter work. It was still, technically within the 1.x line of packages, that this change was made.
Yeah.
Trent Mick 00:16:43 Okay.
Marc Pichler (Dynatrace) 00:16:47 I'm not sure how well it would deal with deep imports.
So, I'm wondering what would happen if we…
were to rename this, I think it's called Index Browser or something like that at the moment. We were to rename the file to match whatever the export does.
I don't know, that wouldn't work, because it's in, SRC, directory, or ESM1.
Yes, I don't think I have a good answer for this yet,
Personally, I'd prefer to, just support the
latest version of Webpack for this,
Because any other option to work around this is kind of… painful.
We would have to…
I just split it out into different packages, which isn't ideal, because then we need to increase what is public from the exporter base package.
to use… everything there.
In a new package.
Trent Mick 00:18:31 I'm kind of ignorant there. Can you use, like… detect your environment.
sniffing at runtime, or the issue then is… You're importing node-only things.
Then you have to get into dynamic imports and stuff, so yeah.
Marc Pichler (Dynatrace) 00:18:46 Yeah, to,
there's quite a few things that cause trouble, even when dynamically importing Node.js stuff when you're bundling for the browser. This is what recently happened with Webpack 5, where
We merged in a change that had,
that did dynamically import HTTP at some point, and that the function was never called.
But, there's still some static checking going on if you have any import cores to node modules.
And, webEx will fail, in that case to actually bundle the thing.
So I think the only way to fix it would actually be.
Trent Mick 00:19:31 To, to split out another package.
Marc Pichler (Dynatrace) 00:19:35 Which might be fine.
it would.
Trent Mick 00:19:41 Or is the issue that we're… we are using exports, so all of a sudden, like, once you define the exports key in package.json, that is all of a sudden strict.
And that's what you were saying a second ago about deep package imports, right? If we didn't have exports, then could…
The usage just be described for?
Browser usage to go… import this…
Indeed package import instead, but I don't know.
Marc Pichler (Dynatrace) 00:20:06 Yeah, the… so the… The issue here would also be that,
like, we are actually doing this. This is in the trace exporter package, so we are calling this.
Trent Mick 00:20:21 Yeah.
Marc Pichler (Dynatrace) 00:20:22 We're doing this import, so the user has no agency over
Whether this is done that way or not.
I will try to join…
browser sick tomorrow, and I will try to bring this up and see what the general idea is of,
How we gonna go about… Bundle support in these packages.
And then, hopefully I will come out with a more informed answer of that meeting there.
Trent Mick 00:21:31 Now, if we were to have separate base packages, then you'd need to…
Give that agency all the way to the top level, wouldn't you?
Like, when creating and exporting, you'd almost have to have…
A whole separate set of top-level exporter things to refer to.
I think.
Marc Pichler (Dynatrace) 00:21:52 Yeah, so if we split it out, there's a bunch of, like, config stuff that also needs to move, I think, and that's the more difficult part.
Getting the config stuff.
Somewhat sorted out,
has been a bit of a pain. I think that that is actually the thing that's more difficult to deal with, rather than… rather than the actual, transport code, because that's fairly simple in the end.
So, yeah.
Trent Mick 00:22:29 Palm feet, tricky state, they…
Marc Pichler (Dynatrace) 00:22:32 also tend to be so big that there's so many moving parts that you have a bunch of public API that you probably don't want to have
Public.
Trent Mick 00:22:44 Okay, so… let me put a red border around this whole meeting for a couple of minutes, because this is, like, a stupid idea that we shouldn't take seriously for a while. But, like.
What about… Have you thought about giving up on the idea of having a common exporter for.
Marc Pichler (Dynatrace) 00:23:00 Yesterday.
Trent Mick 00:23:00 and for no Because, I mean, like, they're very different, right?
Marc Pichler (Dynatrace) 00:23:05 Yeah.
Trent Mick 00:23:06 one's not going to care about GIPC and Proto, likely, and would maybe benefit from having a simpler… like, the browser side would maybe benefit from having a simpler path, so they can play with other things, like the JSON serialization and…
compression games that they can play there to try to help their situation. And they're gonna be using totally different transport mechanisms, because…
nodes.http… Versus fetch, or whatever the other options in the browser, yeah.
Marc Pichler (Dynatrace) 00:23:37 Yeah, so, the reason why it is… In one package right now.
is… actually…
Just because it was always this way. So it's been that way when I joined, and it's, like…
probably will…
it is very difficult to just move stuff out of there, or move stuff around, which is also why I did most of the exporter work there, is to, like, maybe make it a bit more…
Easy to figure out where stuff should go.
Ideally, I think… Splitting out a different browser exporter would make a ton of sense.
having… Like, a separate one that people can use, I would also prefer yeah. Once…
Trent Mick 00:24:42 Yeah, like, possibly you'd want to have a similar interface, and this maybe gets to the declarative config stuff for configuration of these things, but otherwise…
they're just both implementing the same interface config, but it's a totally separate path. Yeah, maybe. Anyway, like, I've realized this is a lot of work, so it's not…
Marc Pichler (Dynatrace) 00:25:01 Yeah, so the plan that I…
had for the exporters was actually… I think we can just,
It's not in packages, because it's not stable yet, unfortunately. Not in examples too, because… Alexandra.
Otrp exporter base…
So, what I was… planning to do is I wanted to have…
way too… Create an exporter from this export delegate, more or less, and have a similar interface to
what we have here, where you can pass in, basically, your own transport, and then pass in your own serializer based on whether you want to do JSON or, Gradle Buff.
Or you could also serialize it to whatever, and then, have that, like, be, like, a create OTRP exporter with, like, a custom transport, custom serializer.
that has all the shared logic in there. Unfortunately, I ran out of time. So, this is the state right now. It's also why some of the things in here are called legacy, because…
There was supposed to be a replacement for them.
I know.
But that's kind of the idea behind the whole thing, to have it more,
More streamlined in that sense, that you can also say you just import the stuff that you actually need, and everything else gets tree-shaking out, because if you do it programmatically, tree-shaking, is kind of…
not… doing the tree shaking stuff. So…
Yeah, by basically piecing yourself,
exported together that way, it would have been… more cliche Cabrillo's way.
Trent Mick 00:27:20 Okay.
Marc Pichler (Dynatrace) 00:27:21 So, yeah.
if anybody has time to look into a proposal to, like, make that happen still, I would also be very interested in reviewing that and helping to move that along.
Yeah, the basic building blocks should be there, just…
needs a bunch of, sign work to get the actual API, figured out.
Yeah, so, to summarize, yes, I think having two separate packages would make sense,
At least for,
What was I trying to say?
having a separate browser package would make sense, but that might also be an option here. So…
Yeah, I'm not sure which way we should go yet, but probably splitting out the…
The browser exporter would also be…
A bit more flexible for the process… processing there.
Alright.
Trent Mick 00:28:51 Okay.
Marc Pichler (Dynatrace) 00:28:54 Guess we can move on to…
The next thing here, which is…
OpenTelemetry instrumentation HTTP does not handle X4, but for a header with part number.
Have the parts stripped…
That's, probably ending up in this client address.
thingy.
So that is actually… Kinda incorrect telemetry, and… Instrumentation HTTP.
And this length… Oh yeah, it just takes the whole thing into the address.
So, yeah.
That is… Probably not, rectangling here.
Alright, we can move on to the next one.
browser async context gets lost after second wait. I'll also put that on the…
Yeah, I mentioned to reach out to, beng Song, who is, very active in the,
in the TC39, stuff with his, async context proposal.
Cool.
write something up for the FAQ, because this is something that comes up quite often.
And I think we would need at least some documentation as to why… why it is the way that it is, here.
Refer people to, and give some more visibility on But this doesn't work.
Oh my god.
And this one here is start active spend silently fails when core pack returns void.
Possing spans to be lost.
I actually stumbled upon this, and… put the…
Triage label on here, because this wasn't reported as a bug, this was just a normal issue.
Gang…
This can't be silently lost window.
This has missing spans.
Just waiting to think…
I don't see anything immediately here, that sticks out to me.
Oh my god.
If that is actually what's happening, then that is a P2 bug, and it would be in…
I don't know, the trace SDK, or… EAPI.
Trent Mick 00:34:16 I'd be surprised if this is an issue and start active spin.
Feels like it's something… about his…
Marc Pichler (Dynatrace) 00:34:24 Yeah.
Trent Mick 00:34:25 the web framework thing not handling… not returning the result of res.json?
I don't know if this is Express or something.
Marc Pichler (Dynatrace) 00:34:34 Yeah, I think, they say that it's Express somewhere here.
Expresto, handless.
Trent Mick 00:34:47 And then the expressed version will matter, because ASEG handlers were added in.
Supporting… Express 5, but Express 4, you could kind of get away with it.
Marc Pichler (Dynatrace) 00:34:57 Hmm.
I'll put the comment here,
That, we need to look into this more for anybody who wants to pick this up.
Alright,
These two I need to bring up still, so I think we're done with, the quarry Paul, and then we can move on to contribute.
Volumes…
Yes, this one we talked about…
Last week already… I'll put the next author response on here.
And I think we should also be good in the country people.
Alright.
I forgot which, repo we did last time, but I guess we just checked based on OpenPR's,
We have 35 open PRs in Core, and 32 open PRs in Contrip, so, we're gonna go with…
Oracle today.
Alright, so the first one here is… Delegating no meter provider.
This is… Still going on.
This one still needs…
More progress in the milestone.
This one, we…
Alright, do…
get some reviews there as well. I guess, I will also reach out to Dan if,
What exactly he had in mind for this issue, because it was,
The way it's phrased is kind of… Open to, that there's no,
Definition of done for it, so it's kind of difficult to figure out when this is actually finished.
But once that is done, we can, actually move forward. There's not too much stuff left in the,
in the, logs stabilization milestone, and so…
Once we've sorted it out, we can move ahead with this one.
Alright, here I still have one comment, and this one is not reserved yet.
So…
Can we merge this one yet?
This is my own PR. I'll just have a look at this one. Thank you, David, for reviewing this, and offer it as well.
I'll have a look at your comments later.
Or maybe we'll just discuss it here while we're already at it.
API is an experimental way.
Experimental PSND export files. Yeah, so… what I wanted to…
accomplish there is that we get the OTRP transformer package in a state where we could actually release it as stable without logs being stable yet.
So the idea was that I would,
like, put this experimental thing in here. And…
Then people would know that, that might change.
It's not the best way of doing it, and I would prefer having the logs SDKs they were before, and then,
Boing.
Going the route of, actually having this, just sit, like, in the top lever, under, under the top lever directly without the experimental here.
Yeah, I guess I could go either way. There's not too much stuff left in the, logs SDK milestone, so…
Maybe I'll just change it back to that. I'll get back to this and write a comment here.
Okay.
I think there is also, for this PR, it's the same question as,
with the other one, because this is now actually adding these entry points, and it's probably also causing the same problem to, WebVAC4 users and some other Pandler users, so… need to sort that out first before…
actually merging the DIM.
David Luna Bistuer 00:42:23 Yeah, okay, depends. Thank you.
Marc Pichler (Dynatrace) 00:42:26 Alright, thanks for the review.
This one is stale, didn't have any activity.
And the next one… That's also steel…
Oh…
I think I've gone over these quite a few times already, and there's…
Bunch of changes that need to be reviewed in depth.
And… getting rid of the ESLint warnings is…
Let's just say the trade-off,
Seems to be a bit, there seems to be some…
Risking getting stuff wrong here for getting rid of the warnings, which,
I would like to avoid, actually,
Merging this in and causing a bunch of trouble.
Trent Mick 00:43:48 I think we asked the package author to follow up on this one a couple of times. Maybe we can just leave it E and let Stalebot do what it's gonna do if it does.
Marc Pichler (Dynatrace) 00:43:57 Yeah, I think I've gone through one of these, or two of these, and pushed some changes myself, and then merged it in, because there wasn't too much of…
stuff that needed to be changed. I happened to actually,
be the person that opened the issue for this one, so I were…
actually just follow up on that. The changes aren't too…
too large, if I recall correctly. Most of these should be kind of a drop-in replacement.
Oh…
I tried to reserve the things there, and, then crossed it off the list.
This one, I've…
brought up quite a few times already. I don't have the time to actually finish that up right now, so I will close it if anybody else, wants to
update the example, please. Feel free to go ahead,
And, like, I don't have the bandwidth right now,
We're rather dedicated to review your peers.
Missed it.
the entities prototype… Renovate, but…
Then, API logs, SDK logs, this is actually, SDK… Blocks milestone… thing?
And… Yeah, doesn't seem to have had any activity. This is also something,
Anybody wants to move along the logs,
stabilization, this would be, one thing to pick up.
What it does… what this does is, is,
Handles the circular references and, lost any value attributes, which…
I'm not exactly sure if we had it before, but it addresses one of the issues that I had opened.
Or this, that was spun off of another PR that we had in Contrape a while ago that we closed, during this very previous session, so,
Yeah, if anybody has time, please have a look, otherwise I'm hoping to get to this,
soonish, a spare, and… I might pick it up and, drive that one to completion.
Trent Mick 00:47:06 Oh, since then… the… any value, or I'm not sure if that's the right term, but, like.
Deeply nested attributes are allowed by spec on the other signals as well, right?
So, okay. I don't know if that would impact how this is done, like, this dealing with circular references and stuff like that is something we'd have to handle in the serialization of…
Spans and metrics as well.
In general, so…
Marc Pichler (Dynatrace) 00:47:35 Yeah, I think in that case, it would most likely end up being in, in the OpenTelemetry Core package. As much as I dislike the existence of that package, I think it is, like, a…
the place for it to be, because it's used by multiple SDKs, and we'll probably…
I think then also be used by the resource package once entities become a thing.
Trent Mick 00:48:09 Okay.
Marc Pichler (Dynatrace) 00:48:12 Yeah. For now, it's probably fine if it lands in the SDK logs package, though, because there we can actually figure out,
the interface and stuff like that before actually putting it into a stable package. And then…
we can basically just, test drive this here in the SDK logs package, and then move it to a stable package with,
Before we actually… promote the SDK logs package to stable.
We would just have to make sure that we have an issue in the milestone so that it doesn't get lost.
Oh.
Alright,
Still has failing tests.
So there's nothing that we can do immediately,
There are three demons in this part of the code, yes. I agree.
I don't.
Because it's also one of these PRs that meet.
Deep digging to, receive an actual review.
Because there's just so much stuff that can go wrong in this piece of the code that,
I guess there's not too many people comfortable anymore to, actually make changes to it.
I'll also put this on the list of things that,
And to reach out to… Ben 4 first, because he is kind of the…
Person with the most knowledge about how these things fit together there.
Is the init override thing.
I think this one should be fine.
Though I actually wanted to have a look at, if there's actually a compiler option somewhere that we can set that,
Make sure that we… Don't have any implicit overrides like this here.
I keep sounding like a broken record, but this also gets on my list of stuff to review.
If anybody has time to,
look into some tsconfig stuff, and try and figure out whether this is,
Something that we can enforce, please,
2, and then, post your review there.
That would be very much appreciated. This has been sitting around for,
Over a month now, so, it's…
Fairly small change, but we should get to this one at some point.
This one I actually wanted to get to. Didn't have the time yet.
Trent Mick 00:53:06 Oh, yeah. So…
Yeah, I'd appreciate it if someone else could do another review. So, I don't know what the…
Unwritten or written rule is the author of this?
ER is… also works at Elastic, and I've reviewed it, so…
I mean, there's nothing elastic-specific in here, but,
I don't know if it's discouraged that…
One company just drives something through.
Marc Pichler (Dynatrace) 00:53:36 Thank you.
I… Usually have handled it this way, that, as long as… There's nothing, like… specific to…
the company, and there's just a spec feature or something like that, our, minor changes and stuff like that should be fine to just go through with review from the same company. I guess we are, we all know, the…
things that we should look out for when, like, reviewing PRs from, people that are of the same company, and, I'm pretty sure that,
everybody here handled in their… in the best interests of the pro… Everybody here
Worked in the best interest of the project, so, would be fine just having this merged.
messages.
Trent Mick 00:54:29 Okay.
So this, yeah, this implements part of the new opposite sampler spec, or probability sampling. I understand… I thought I saw up here, the old one is going to get deprecated. Neither have been implemented by OTelJS, this… if you go look at the
the spec for tracing. It has… Two pages describing
Probability sampling, or what? I can't remember, but term is.
Just give me a sec.
It's back… It's under trace.
Yeah.
So that is the… You see in this sidebar, there are two…
Table content trees called probability sampling, so it gets pretty confusing.
Which one we're talking about?
Marc Pichler (Dynatrace) 00:55:28 Probably percent.
Trent Mick 00:55:29 Okay, so that first one is the old one, which never got out of experimental, and this is the new one, which is experimental.
They have almost identical URLs.
the new ones… Based on two OTEPs that were recently merged into the… Spec.
And so Anna Ragg, the author of this one, is implementing… I think I'm sounding like a broken record, too, I said this in a previous call, is implementing most of the new specs, so it describes a whole bunch of samplers. He's done the core one.
But not a couple of the optional ones, which can get done separately. And he's doing it for a few languages, for Java and Python as well.
Marc Pichler (Dynatrace) 00:56:13 I don't.
Trent Mick 00:56:15 Anyway.
So, one of the things, it adds a new package called Samplers… Tampler dash.
Composite, if people think that's okay. It is…
course spec stuff, so I'm not sure if it should go live in whatever the…
the SDK trace base, or if that would be overkill if it's fine to have it as a separate…
package.
Marc Pichler (Dynatrace) 00:56:37 Yeah, I think, the reason why we had,
some things in the, trace package was because…
There was this, like, you need them for the defaults, that are being configured somehow.
So, if we want to have that be, also Configurable via these,
environment variables, I forgot what it's, yeah, the hotel.
So if we want to also have the configurable via that, then I think we would have to put it into the SDK trace package, but I think we're gonna want to move away from that anyway at some point, and…
Probably piece it together somehow with this declarative config, stuff.
And…
Trent Mick 00:57:43 I would assume that the spec would move towards making these the suggested defaults, but I'm not…
Marc Pichler (Dynatrace) 00:57:50 Ew.
Trent Mick 00:57:50 Any current plans on that?
Marc Pichler (Dynatrace) 00:57:52 Yeah, I think once they are the defaults, it's always possible to just move them to the stable trace package and have them in there. As long as the spec is experimental, I think we should still have them in a separate package that is versioned accordingly.
And then…
Trent Mick 00:58:10 Yeah, that sounds good. That's a bit safer for us, then, for changes.
Marc Pichler (Dynatrace) 00:58:14 Yeah, then we can make any changes if there's anything in the spec that, would require,
A breaking change, we can still do it.
And once we… Have everything stable in the spec, we can just move it to the…
Trace package, and have it live there.
Trent Mick 00:58:38 Okay, sounds good.
Okay, so on this, if someone else wants to take a review, that'd be great, but…
I think what I'm hearing here is…
In a week or so, I'd be…
Be good for me to merge that, or okay for me to merge this.
Marc Pichler (Dynatrace) 00:58:53 Yes, so, thumbs up from my side for getting this merged, so, yeah.
It… it is a spec feature after ours, so there's also not too much, room for… for… for anything…
Trent Mick 00:59:10 controversial.
Marc Pichler (Dynatrace) 00:59:10 out of the, yeah, out of the ordinary, so, yes, should be all fine.
Right.
So, I lost the… I lost track now of… But we were…
Composite sampling, and then this is the next one.
Peter.
Trent Mick 00:59:43 And if you don't want to talk about it, I think we're out of time, so you can…
Ring the bell.
Marc Pichler (Dynatrace) 00:59:48 I… I did want to talk about this one, but since we're out of time, I guess we can just save it for another time.
Alright then, thank you everybody. Have a nice week, and see you next week.
Trent Mick 01:00:06 That's driving, Mark.
MG Marylia Gutierrez 01:00:07 Thank you.
David Luna Bistuer 01:00:07 Yes.
Marc Pichler (Dynatrace) 01:00:08 Find it.
