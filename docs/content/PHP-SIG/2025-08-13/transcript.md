SIG: PHP SIG
Date: 2025-08-13
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/Kzsha3zOx36SUO3lxZsO_erY5kMltOp3mxb12xkczcO32ISuCQQkWwMZ54hStFpq.TTN14cR-PYi0yLAE
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:13 Hello?
**Sergey** 00:15 Nice.
Where's the weather?
Did, the winds from the desert reach, …
Which part of England? Are you in England, or…?
**Chris Lightfoot-Wild** 00:30 Yeah, I'm in England, yeah, I'm in, West Yorkshire, so it's usually wet, but it's very hot.
**Sergey** 00:37 So it's reached you as well?
**Chris Lightfoot-Wild** 00:39 I guess, subjectively very hot, but ….
**Sergey** 00:43 What is hot for you? Like, what is, like, for England, it's, 25 degrees sun?
**Chris Lightfoot-Wild** 00:48 It's 28 today here, where I am.
**Sergey** 00:52 Alright.
**Chris Lightfoot-Wild** 00:53 I mean, anything over low 20s is pretty warm for… So, yeah.
I don't know whether it was in Freedom Units, Bob, sorry.
**Bob Strecansky** 01:03 I can't… I cannot commiserate with that. It is. I think it's 8 AM, and it's already, …
Funny one.
**Chris Lightfoot-Wild** 01:14 What's your indoor temperature? So, have you got nice aircon.
**Bob Strecansky** 01:18 Oh, yeah, yeah, we do have… I mean, my office is, like, I have to wear… I often have to wear a sweatshirt in my office in the summer, because it's cold.
**Chris Lightfoot-Wild** 01:28 The thing here on my desk is it's, currently 28….
**Bob Strecansky** 01:35 I think I'd rather have hot outside and air conditioning than just, like, medium all around, but that's probably just the USA in me.
**Chris Lightfoot-Wild** 01:44 Yeah, it's not that complex, yeah, I'd love to have it, but I think it's just, you know, it's quite expensive for us.
**Bob Strecansky** 01:52 Well, our power company… the power company that runs my city is very corrupt, and none of the politicians that run the company even live in the district where the prices have gone up, so it's been, it's been something over the last year or so.
My air conditioning bill for most of my adult life is somewhere between 100 and 150 bucks, and the last couple months has been, like, four or five hundred bucks.
It's not cause the… it's not cause anything's changing.
Except for… Corruption, but… you know.
**Sergey** 02:26 Do you have a single-family house? Can you install solar? Yeah.
**Bob Strecansky** 02:30 Yes.
**Sergey** 02:30 It's either way.
**Bob Strecansky** 02:32 It's funny… it's funny that you mention that, because a bunch of my friends and I have been discussing putting in solar panels here. The problem is, they're really expensive here, because… now because of tariffs, too, and because of, just, like, getting somebody to install solar is difficult.
In my part… like, in my part of the United States, because we're…
very… like, I am not, but my part of the world is very Republican, so, like, oh, there are a lot of people, like, no, no solar power, that's… use diesel, like…
Got it.
That's not me, but that's a lot of people that live near me. Anyway, we can get going with our discussion… meeting discussions for today.
I'll share my screen.
Is anybody going to KubeConn North America?
**Brett McBride** 03:28 For me….
**Bob Strecansky** 03:30 Okay, I guess I'll be the sole PHP person there, that's okay.
I'm excited because it's here. It's in Atlanta, so it's really nice for me.
Alright, let's look at some of these things.
**Sergey** 03:47 When is it?
**Bob Strecansky** 03:49 It's in November. There's a maintainer summit on the 9th, and then the rest of the conference is the 10th to the 13th.
Nope.
Open purpose… I'll go in.
I went to look at these, depend about actions yesterday, and I think that this one fundamentally breaks something, so I'll have to… I wanted to look deeper into it, I just haven't had a chance to yet.
Rest of these.
**Chris Lightfoot-Wild** 04:22 The top one has been, like, spamming, I've noticed. The code….
**Bob Strecansky** 04:25 Yeah, yeah, I think that they've been doing a lot of, like, it seems like they've been doing a lot of incremental upgrades.
But…
You know, whatever. I'm sure that there's a reason behind it, but we haven't yet figured it out.
**Brett McBride** 04:39 grades also depend a bot.
**Bob Strecansky** 04:43 You know, it very well could be, right?
**Brett McBride** 04:45 I see a lot of… I see a lot of minor releases of just random things that are just dependabot updating something.
**Bob Strecansky** 04:54 Yeah, it ends up being, like, what, like, not a circular dependency, but, like, a multi-stage dependency, where, like, Dependable updates something for one repo, which updates something for another repo, which updates something for another repo, and….
**Brett McBride** 05:04 Mmm.
**Bob Strecansky** 05:05 I always go into those upgrades with extreme trepidation, because it's like, you know, it's some robot somewhere just going, beep boop, beep-boop.
Anyhow, let's go to… sorry, let's go to the next one…
Contributor has a bunch of OPR, so again, some dependable hotlines.
Did anybody look at this Lambda wrapper code for manual instrumentation?
I didn't even see it.
**Brett McBride** 05:35 Good.
**Bob Strecansky** 05:36 Okay, I'll take a look at that later. Oh, lies, Brett!
**Brett McBride** 05:41 Okay, I did.
**Bob Strecansky** 05:43 Yeah, and some tests with an astag analysis would be nice. That's correct.
**Brett McBride** 05:49 Understated.
**Bob Strecansky** 05:51 Understood. Or you should have said it should be….
**Sergey** 05:53 Doesn't it run automatically, or…?
**Bob Strecansky** 05:57 They didn't… I mean, it should, but….
**Brett McBride** 06:01 You need to add the files and the configuration so that it will run.
**Sergey** 06:06 It's limited to certain subdirectories, and, that PR, it's, ….
**Brett McBride** 06:11 the… Yeah, yeah, so requires.
Yeah, a configuration file for each tool, which we don't run globally, because we… they can be configured differently per
This sort of package.
**Bob Strecansky** 06:31 Right?
Instrumentation, do I have any open ports?
Let's check out this project board…
Chris, is this one still pending review?
**Chris Lightfoot-Wild** 06:43 It got merged, so….
**Brett McBride** 06:46 We got merged, yeah.
**Chris Lightfoot-Wild** 06:49 Well, someone suggested giving it a go with something, but they had a
problem, but I wasn't sure, I have to test that scenario.
**Bob Strecansky** 06:58 Okay. Do you want me to change that ticket at all, or you just want me to leave it like it is?
**Chris Lightfoot-Wild** 07:04 I mean, I'm easy, whichever way, like….
**Bob Strecansky** 07:07 Okay, we'll leave it alone.
**Chris Lightfoot-Wild** 07:08 Yeah, just to make sure.
**Bob Strecansky** 07:11 Just to have a little footnote to note that we're still doing something with it.
**Chris Lightfoot-Wild** 07:15 Sure.
**Bob Strecansky** 07:16 I think that's been system suppression strategies.
So, it's another… okay.
Still working.
Nothing on the road to SDKv2, or SDKv2 is done, we can ship it now.
Just kidding.
Okay, that's all the… Saw the normie stuff, let's see how package installs are going.
Close to 20 million.
Looks like we'll get there in a month and a half.
**Brett McBride** 07:48 Who doesn't remember.
**Bob Strecansky** 07:50 Anybody have anything on the agenda for today?
Sergey, I know you had a question about Octane.
**Sergey** 07:57 Yeah, if I have some time, I was just wondering. I saw that there were a couple of issues where it was raised, I was just wondering if there's anything…
new since then, otherwise I will maybe…
I'll try to… to replicate and see if it's….
**Chris Lightfoot-Wild** 08:15 Don't forget.
**Sergey** 08:15 Because technically, like, the way… please go ahead.
**Chris Lightfoot-Wild** 08:18 No, as I say, I don't think anything had, changed, but obviously I'd seen something, left a note on that one you'd linked.
But again, I've not gone around and tested it.
So I can perhaps try and pick that up, but it depends on what you're about to say, I guess.
**Brett McBride** 08:32 Was that, was that right?
**Sergey** 08:34 I was just.
**Brett McBride** 08:34 Lynn?
Chris, I just… I saw something fly by.
When Bob was scrolling. Was this just a .env?
**Chris Lightfoot-Wild** 08:43 Nope, … No, that was where…
I think by default, Octane is starting a new process of passing explicit environment variables in, and it doesn't contain the OTEL-specific ones.
And I thought for that that…
We could potentially just hook into that method and inject them ourselves.
But I guess it depends what, …
You were about to say, Sylvia?
**Sergey** 09:10 Okay, yeah, no, that's a very important comment, thank you. I guess, so you're saying it's not about the inherent technical limitation of the… because I was thinking, like, so here we come into those frameworks that… unless… I don't know much about Roadrunner, but I assume, like, fully, I think,
No, I'm not sure. I know that React PHP, it doesn't use the classical PHP model, right? So, we cannot rely on request init, request shutdown, but I wonder, like, external things like Swoolly and Roadrunner, technically they can use the same model, right? The fact that they are doing… well, I guess maybe they cannot, because they want to run out, but now you said that
They do… they run multiple processes, not like they're trying to run multiple requests in the context of one process, which PHP itself will not support unless it's multi-threaded.
But, … so you're saying the technical issue most likely related to inheriting environment variables, so it's not… it's not a collateral problem per se, it's just a question of passing the environment variables to those child processes. Did I understand correctly?
**Chris Lightfoot-Wild** 10:13 I think that's what it was, yeah. I know we looked at, like, the surface level, but yeah, I need to test that theory out. That's what it looks like it was doing.
Laravel Framework had decided a very small subset of things could pass through.
And then everything else that was, you know, hotel-related didn't make the cut, so….
**Sergey** 10:33 Okay. Are you saying that the process, the child process spawned from PHP code, from Laravel itself, like this, Laravel, like.
**Chris Lightfoot-Wild** 10:43 Yeah, if you do the artisan octane work or something, it spawns another process, I think.
**Sergey** 10:49 And it filters what to inherit, so technically the master process had those environment variables, but it just didn't pass them along to the child, like, actively blocked it. Okay.
**Chris Lightfoot-Wild** 10:59 Yeah, but I think that was the case, but then I was aware recently, I think, right, you'd merged something in from a different contributor that was, …
Propagated environment variables in processes or something, aren't they?
I don't know if that was….
**Brett McBride** 11:12 It might be worth just retesting if this time.
**Chris Lightfoot-Wild** 11:14 this.
**Brett McBride** 11:14 I don't think that was the same thing that was doing, that was… propagation through the environment.
similar, but I don't think that's what it's for.
**Chris Lightfoot-Wild** 11:28 Okay.
**Brett McBride** 11:29 Yeah.
**Sergey** 11:30 That's maybe a good start. I will find, like, we will ask this from some customer that our support…
sales, or I don't know what is the status they're trying to do. So, … I will try to find out from them if they have concrete kind of, like, use case, and…
Maybe I will try to run it, and then I will report it back.
**Chris Lightfoot-Wild** 11:49 I think if you scroll up slightly on that issue, Bob, there's a link to… yeah, my previous comment there.
… So, yeah, it starts out a new process, and…
I was thinking that potentially hooking into this underlying symphony process.
Potentially being able to inject what we wanted, which major sounds… that might sound hacky or bad.
I don't know, but….
**Sergey** 12:17 Yeah, but that's very interesting. So you're saying it's all about passing the environment variable. It's not related to the Laravel proper, like, it wouldn't work with any framework.
Not related to the fact that it's a lot of implementation, it's just that
The way they spawn the process might be the only thing that is specific, maybe.
**Chris Lightfoot-Wild** 12:36 Yeah. Okay.
**Sergey** 12:39 Okay, interesting, so….
**Chris Lightfoot-Wild** 12:41 That's certainly my understanding, like I said in that, I could maybe try and test and see if I can get it to work, but that looked like the limitation.
**Sergey** 12:50 And frontend PHP, is that something that is also used in…
it's on top of Laravel Octane? Like, what is the relation between…
A lot of it will obtain and fun.
**Chris Lightfoot-Wild** 13:00 I've always done PHP, I've not used that before.
Is that new-ish, I think, is it?
**Bob Strecansky** 13:07 Yeah, I think Frankie PHP is… it's like a Go runtime with PHP embedded in it. I'm trying to remember all the very explicit details.
**Sergey** 13:14 When you say go, you mean, like, this Roadrunner?
**Bob Strecansky** 13:17 No, I mean… Oh, the programming language.
**Brett McBride** 13:20 Yes, but….
**Sergey** 13:21 I think Roadrunner is implemented in Go now?
Hmm.
**Bob Strecansky** 13:26 Yes, I think that's right.
**Brett McBride** 13:28 This one maybe has the benefit of being sponsored by the PHP Foundation.
And written by a symphony dev.
**Bob Strecansky** 13:36 It looks….
**Brett McBride** 13:36 dinged.
**Bob Strecansky** 13:38 Looks like they have examples for Symphony and Laravel and some other… and some other, skeletons, so…
I don't know that it's necessarily for….
**Sergey** 13:48 That might be some kind, if I understand correctly, that might be some kind of, like, sibling, so it's maybe not directly related to Laravel Octane, maybe same approach, but, like, in parallel to that?
**Bob Strecansky** 13:58 I think… I don't know that there… I think… I think Frank and PHP is more along the lines of, you have this PHP code, we want to serve it more efficiently for you, and I think Roadrunner is, like, we want to embed in the PHP, if I understand it correctly.
**Sergey** 14:14 I thought that Roadrunner is kind of like an external service, and then you run PHP inside of it, so it's kind of like, …
makes it, I guess… I don't know what… like, what advantages Roadrunner has over, like, HP FPM, I guess. Some?
**Bob Strecansky** 14:29 I think… I'm assuming that these have some sort of overlap, I don't exactly understand right now what they are.
**Brett McBride** 14:36 Yeah, there's a bit of overlap, but… but…
I think both of them we would consider modern PHP runtimes, where you
Fire your application up once, and then it accepts multiple, requests in that one process without restarting the process.
So….
**Sergey** 14:57 When you say it, you mean.
**Brett McBride** 14:58 link requests, and….
**Sergey** 15:02 But you can say the same about HPFPM, technically, right? Like, you have this master process, and then it spawns child processes.
Or do you mean, like, it's even not following, like, this classical PHP model where you keep memory between requests? So, essentially, you can keep data in memory between requests with those new runtimes?
in pitch… so PHP code will see the same memory between requests. Is that what you mean?
**Brett McBride** 15:26 Yeah, yeah, yeah, yeah. So if you had a Laravel application, for example, you've got a wait request sort of loop, and every time a Roadrunner hands a new request to your running process.
as a PSR7 request, or using Superglobals, or, … He then…
pass that request to your Laravel application, it processes it, you give the result back to Roadrunner.
So it acts as an intermediary.
with a number of workers, each of which is, you know, the same bit of PHP code running.
**Sergey** 16:06 I guess it requires investigation. So… but I guess the advantage over, like, HPFPM, because what you described, HPFPM more or less works the same way, right? You have, … it spawns a child process, it can reuse it, like, but…
But PHP code doesn't see any data, it cannot keep this… it follows classical model, right? PHP code cannot see any memory between requests, so it essentially can rely on the fact that, no, my memory leaks… it's essentially… the decision, I guess, back then was made to simplify application development model, right? You don't care, like, you just, …
do whatever, and then you assume that each new request will have a completely clean memory. But then, I guess the optimization here is that you can save yourself time loading the whole framework.
So that's why people try to reuse that.
I'm just wondering, like, how more complicated it makes the framework itself, because I assume…
Framework developers also assume that the memory is wiped between requests, right? So, the fact that you're trying to rerun it on different requests, I guess, you need to do something about the framework itself.
Reset it somehow.
**Brett McBride** 17:13 I don't know. I mean, I haven't run into that problem, and I've used it quite a bit. I think.
**Sergey** 17:18 Which part do you use?
**Brett McBride** 17:20 Roadrunner. We use it at my… at my day job.
….
**Sergey** 17:26 And which framework do you use on PHP side?
**Brett McBride** 17:28 Slim.
**Sergey** 17:30 So you use just a regular PHP framework that's not even aware, so you could have just run this same PHP application in PHP FPM.
**Brett McBride** 17:38 Yes.
**Sergey** 17:40 So Roadrunner by itself, without you changing application anyway, optimizes still. That's something that is better than HPFPM. There's some advantages.
**Brett McBride** 17:49 Yeah, yeah, I… Yeah.
Yes, so the application is the same. You need a little bit of glue to… …
which, you know, talks to Roadrunner, and it's, you know, it needs to implement a worker interface.
Accept a request, hand it to Slim.
and get the response and hand that response back to Roadrunner, and that's what a worker process does.
Which is….
**Sergey** 18:19 Then you reuse, so you keep the… you keep the…
the request going, so you're not relying on the speech fee model.
You keep the food going, waiting for the next, ….
**Brett McBride** 18:30 Yep, so that worker and that, say, slim application will serve hundreds, thousands of applica- requests without restarting.
**Sergey** 18:41 Okay, so… so you do need to change application a bit, and then you also need to make sure that you are…
compatible with that new model, right? The fact that you…
can serve… do you serve in parallel multiple requests, or are you not going that far? It's one.
**Brett McBride** 18:57 No, one worker runs… processes one request in
series. It'll just do one thing at a time, but Roadrunner can spawn
As many workers as you… as you want.
So it scales up that way.
**Sergey** 19:15 So it's not, like, fully, like, Node.js model, where you can even serve, like, if you're blocked on some I.O, then you can go and serve another request, so you can still be single-threaded, but you can, asynchronously serve multiple requests at the same time. That's even more advanced, but you're not doing that.
**Brett McBride** 19:32 That is more advanced. I think Swool is probably the way to do that, and possibly even React.
Now that it's….
**Sergey** 19:39 Then you will need these fibers, right? The block, like, the block, in a way, compatible with BHP itself.
**Brett McBride** 19:45 Yes.
**Sergey** 19:47 So it would be probably more modern than… More recent, the HP fibers.
Okay, got it. But you send Roadrunner, you can take it. So I guess the advantage, then, is this ability to reuse, like, instead of reload, you're just trying to reuse the same, context and just accept the next request.
**Brett McBride** 20:06 Yeah, yep.
**Ago Allikmaa** 20:09 Does this also work with, like, frameworks that, are hard-coded to use, global variables, like…
Server, and so on.
**Brett McBride** 20:22 No. No, so Roadrunner… is, built around PSR7.
**Ago Allikmaa** 20:29 Okay.
**Brett McBride** 20:30 HTTP messages, although frank and PHP, which we just saw before, does just use regular superglobals.
So, that's probably… more aligned to…
You know, some of those old frame… older frameworks that… You know, expect To get things out of…
the Superglobals.
**Sergey** 20:52 I mean, technically, if you have control over PHP Engine, I don't know about Frankie PHP, like, if they run some custom version of PHP Engine that has been embedded inside Go, I don't know what they did with PHP Engine itself, they can reset even the globals, right? It's in their hands.
And then on each request, they can set them to new request values.
The just application needs to be there, huh?
**Ago Allikmaa** 21:15 Yeah, I guess you could write, like, a PSL7 clue for any framework, so you just, in there, you update the superglobals yourself.
Or something.
If they're all writable.
**Sergey** 21:29 You can update those globals from PHP code, they're changeable?
**Ago Allikmaa** 21:33 I'm not sure if they are all changeable.
**Sergey** 21:39 Yeah, maybe.
**Ago Allikmaa** 21:41 If they are, it could be possible.
**Sergey** 21:45 And PSRP7, I'm not familiar, is it, like, completely, like, not dependent on those globals, just users' interfaces, when a request is just being passed as some kind of object, and you get your information from that object instead of relying on globals?
**Brett McBride** 22:00 Correct. It should be….
**Ago Allikmaa** 22:01 the case, yes.
**Brett McBride** 22:04 Yeah, and I mean, most frameworks these days do operate on PSR7, you know, which is an abstraction of
HTTP requests and responses.
**Sergey** 22:17 When you say that most frameworks, do you mean, like, they still will be compatible with regular PHP model, but they construct, like, as a bridge, they construct this PSR7 message, or incoming request from the globals? So this is what they do when they run, like, in classical PHP FPM context.
**Brett McBride** 22:33 missing.
Yes, they do.
**Sergey** 22:36 But technically, you can kind of, like, shortcut and provide those objects directly instead of them reading globals.
**Brett McBride** 22:43 Yes.
**Sergey** 22:46 Okay, but you're still kind of, like, not guaranteed, like, …
it's not clear, like, do they compatible with the fact that you will reuse… well, I guess they should be, right? If they allow you…
pass this as an object, are they compatible with the, you know, the use case where you will, after you send the response, you will pass as another object in the same context, and then they will act on that new object, I guess, like…
If that's the interface issue.
**Brett McBride** 23:11 I guess that depends on the framework, but … given that, you know, some of these runtimes have been around for a while.
You know, those issues have… have come up, and … you know, the frameworks have evolved to work… work with them by not storing state in strange ways, and not using static variables, and….
**Sergey** 23:34 Yeah, I mean… I mean, ideally… or they can reset them, right? So, if they can reset them…
Like, the hardest case is this one that you said fully maybe supports when you want to even have multiple set at the same time.
But if you don't need that, then you can still, like, even if you use globals, if you… if you account for them and you reset them when you accept this new request, then you can still get away with that, right?
**Brett McBride** 23:59 Yes.
**Sergey** 24:00 Yeah.
Okay.
**Ago Allikmaa** 24:04 No, coming back to Frank and PHP, I'm wondering if, like, extensions would even work there.
for doing any auto-instrumentation stuff. Because it says it uses the official PHP executor.
But I don't know if that also means that all the extensions made for PHP… work, also.
**Sergey** 24:34 You mean, like, does it support, like, for example, this observability API that we rely on?
So it's… so it… So it says that it uses official PHP Engine Executor.
**Ago Allikmaa** 24:47 Yeah.
But then….
**Sergey** 24:50 Why do you think that extensions will not work? Like, do they do something else that might
Make it not work?
**Ago Allikmaa** 25:00 There's, like, there's something about extensions later, I'm looking at their, like, main website, and they say that popular PHP extensions, such as Opcache and Xdebug, are natively supported, which makes it sound like they're doing something, like, special to make them work.
**Sergey** 25:23 depends, like, what is… what is it? Like, if they use a regular PHP engine, then what do they do special? Like, what….
**Ago Allikmaa** 25:29 Yeah, I, I mean….
**Sergey** 25:30 What is the use case for this frankly picture?
**Ago Allikmaa** 25:32 One possibility is that they used, like, the official engine, but they skipped some of the init shutdown stuff that is necessary for extensions.
So it will… from PHP, like, they might implement that part on their own, and just use the execute more, like, …
at a lower level, invoke it.
**Sergey** 25:55 So you're saying when they say that they use the official, like, regular, ZEND, or they have the name, Zend Executor, they use it as a base, but maybe they modified it, so it's not.
**Ago Allikmaa** 26:06 Yeah, it looks like it's not clear what the… how they use it exactly, at what level of abstraction.
If they enroll….
**Sergey** 26:18 Yes, there are multiple… but there are multiple use cases that might be not related directly to each other, right? So we have this franking PHP, and Laravel Octane.
just because we will find out, like, what Chrissy mentioned, how to solve it for Laravel Octane. With environment variables, not necessarily we'll solve it with Frank and Pichu, it might be different approaches here, right?
the way it works. Like, it doesn't look like it's, it all comes from the same thing. Looks like, multiple parallel approaches.
Maybe at the end, they want to achieve similar things.
I guess it's all about optimizing or removing that overhead of reloading everything on each request in classic PHP.
I'm more interested in Laravel Octane, since we were asked about that directly, but, yeah, it might be interesting to try other ones.
So there are a lot of Octane, frank and PHP, and then we also have Smooley, which is most likely the most advanced one, right? If they especially use…
Fibers and stuff.
**Brett McBride** 27:24 I understood Laravel Octane to be more of a…
like, the concept of running Laravel in some other you know, non-Apache FPM runtime.
Chris, do you… Sort of know more about it.
**Chris Lightfoot-Wild** 27:40 Well, I'm similar to you, I think, yeah, but it's got various Franken… you can use Swool, Road Runner, and Franken-PHP with it, like, and there's.
**Sergey** 27:49 Oh, so you think larval octane is just a middle ground, kind of like middleane bridge.
**Chris Lightfoot-Wild** 27:53 Then you need on top of it to add the cream to the thing.
**Brett McBride** 27:57 It's a brand, not a product, in this case. It's not a thing that you install, it's… it's…
Laravel paired with a modern runtime, is my understanding.
**Chris Lightfoot-Wild** 28:09 And then the framework… sorry, the other package you linked, so yeah, it looks like it's using…
Laravel's event system to just hook into the start and stop request life cycles that Octane emits.
Rather than, like, the process-based… thing that…
would currently use, hooking for. It's just using Laravel's event system.
**Sergey** 28:31 So, the current, the one… the larval instrumentation that you implemented, you relied on the… on hooking into the methods using observability API?
**Chris Lightfoot-Wild** 28:40 Yeah, I was using the observability API rather than previous… all the watches that, were kind of just, I guess, taken from Laravel Telescope, if you've looked at that before.
does a similar thing, it's just emitting and listening to Laravel events.
**Sergey** 28:56 Is it the same thing, what you mentioned? Three things, like lateral telescope, watchers, and lateral events, are those three different things, or are they somehow related to one… another?
**Chris Lightfoot-Wild** 29:05 Simil- just similar in that they're based on whatever events Laravel's framework decides to emit.
It's a lot.
**Sergey** 29:13 Relevance is kind of, like, basic thing.
And then on top of it, lateral test.
**Chris Lightfoot-Wild** 29:17 Have you heard of Lyrell Nightwatch, which is their new observability thing, but that's just using their own events.
And they've got their own little, ….
**Sergey** 29:29 Have you considered, using events, since… are they kind of, like, more chances that they will be backward compatible than hooking into methods?
**Chris Lightfoot-Wild** 29:37 There are potential, I guess. I thought… initially, I thought we were getting more out of hooks, so we could hook more parts of what was going on, because they don't always omit events.
Where you might like them to.
**Sergey** 29:48 Is it possible to combine both? It's not even at the moment. There are still watches in there that listen to….
**Chris Lightfoot-Wild** 29:54 of larval events.
So it's….
**Brett McBride** 29:58 I think we basically… well, basically, but we use, our event hook just to, know when a Laravel application is starting up, and then add watches and listen to events
A lot anyway after that, don't we, Chris?
**Chris Lightfoot-Wild** 30:15 Yeah, yeah, a bunch of this stuff is already there. It bootstraps Laravel and just inserts the watches we want.
just because… initially, I guess in my head, I was trying to think that…
It is possible that an event can…
Stop execution, so, like, if you had…
a listener for OTEL, it could be canceled before it got to run.
I obviously kind of wanted to avoid that, wanted to sort of…
Make sure that we could operate and do our work.
Regardless of whether the framework decides to stop processing an event or not.
**Sergey** 30:49 Do you mean, like, listeners to the events? When you said watchers, is this the…
Is it the same as a kind of, like, listener for the event? You can register for the event and get….
**Chris Lightfoot-Wild** 30:57 Yeah, we use the term watcher, but… and use listener interchangeably, but something that is just subscribing to an event.
….
**Sergey** 31:05 And you're saying when you subscribe and you have multiple listeners like that, watchers, then the first one can say, don't propagate it to the other ones, and then you will not get it if you are not the first one.
**Chris Lightfoot-Wild** 31:14 I believe it is possible, yeah, like, if it throws an exception, it can drop out of the….
**Sergey** 31:19 the loop. But that, technically, the solution might be still relying on events, but then instead of registering the listener, hooking into the methods that call the listener, right? So, instead of registering as one of the listeners, we will know when the listeners will be called.
Or, alternatively, always ensure that we are the first listener, right? And we'll always get.
**Chris Lightfoot-Wild** 31:37 Yeah.
**Sergey** 31:38 but….
**Chris Lightfoot-Wild** 31:39 It kind of does that at the moment, it does both. We are using the observability hook function, and then injecting events, sorry, listeners into
It's just called watches… Technically, you'.
**Sergey** 31:52 You rely on events, like, … but instead of being a listener, you're just hooking into the methods that will call listeners.
**Chris Lightfoot-Wild** 31:58 Yeah, yeah.
**Sergey** 31:59 But you rely on the events, being kind of, like, more backward compatible than trying to find the methods and implementation.
That, otherwise you would have needed to hook into to understand when important things are happening, right?
**Chris Lightfoot-Wild** 32:12 Yeah.
**Sergey** 32:14 Yeah, okay, so it sounds like, okay. Do you still need to hook, to get more information and some methods additional, or events are completely sufficient to whatever you needed to get?
**Chris Lightfoot-Wild** 32:26 From memory, I don't think events always give everything.
Book.
Obviously, if you were to look at the Laravel Nightwatch products, they've obviously got everything from events there. They've just… it's a commercial thing, isn't it? So they've just built
Their ecosystem around it, and even, like, the framework now.
is integrated for their… their commercial products, whether or not it's available or not. It sort of detects.
And then does extra work on top.
**Sergey** 32:55 Keeping those events backward compatible, even between major versions, like 10, 11, when did it appear the first time? Events feature?
**Chris Lightfoot-Wild** 33:04 Years ago, I think. Very early dose, so I think those events are still….
**Sergey** 33:10 And it's still… you can still work or compatible, like, between, like, 12 and 11, you didn't need to change anything, but, like, it's except for additional events.
**Chris Lightfoot-Wild** 33:20 I'm not sure… I don't know for certain if events change
their structure or not. Like, if there's, you know, additional properties or whatnot, or the changes to that completely, but…
Done.
**Sergey** 33:32 Only additions, like, they don't break, so, like, using events is easier. I mean, it makes work easier, right? So, essentially, you can rely, so far at least, even between major versions, they keep them compatible, so you don't need to rework, just support next major version, like….
**Chris Lightfoot-Wild** 33:48 Yeah.
**Sergey** 33:50 I guess it's, to go thin.
….
**Chris Lightfoot-Wild** 33:53 With some of these questions, do you think that…
Obviously, the asks you, but if the… are they using the… The contribute package, then, and…
Would you plan on relaying some of those just into there generally, or just bring them all onto these?
Meetings ad hoc.
Just curious, like, obviously, if someone else might.
throwing, extra ideas, going, oh yeah, I'll build that, or whatnot.
So there are a few other people that chip in as well.
**Sergey** 34:22 I'm not 100% sure, are you asking me?
**Chris Lightfoot-Wild** 34:25 Well, yeah, I guess, if you're getting support questions from consumers of your….
**Sergey** 34:31 Yeah, yeah,
**Chris Lightfoot-Wild** 34:32 But if they're using the open source package, do they….
**Sergey** 34:35 Yeah, okay, now I understood your question. This is exactly what I asked them, so I… so far, I didn't get the answer yet, so I will let you know when I will post the answer on… okay, I got the answer. They using actual customers open to any method.
Okay, I will read the response, and I will post on the Slack, but, okay, now I understand what you're asking. Are you asking to keep you guys, like, you would be interested every time we get this kind of request to… for you to… you would be interesting for us to paste this in our Slack, in the community Slack?
Yeah, we sure can do it, like, if, we definitely want to, like I said, eventually, we want it to be mostly only upstream, except maybe it's not for some holistic, so, eventually we would want then to also share the feedback.
But this one, if I understand correctly, the way they phrased it is, customer tried something.
I would need to read this. I exactly ask them what exactly did they try, because I'm not even sure if they tried OpenTelemetry. I thought maybe they even tried a classical Elastic APM, the one that we worked before, OpenTelemetry. So, I need to understand what they tried, and…
Obviously, like, it sounds like with OpenTelemetry, maybe fixes would be much easier, so definitely would want to drive into that direction.
So I will post a response, and …
if I understood you correctly, question your… Chris, that you just asked is that you would like to know more about this kind of, like.
**Chris Lightfoot-Wild** 36:08 Questions that are being raised, if we need to support something? I would personally, at least. I guess to have some insight into if anyone's using the package, and what.
**Sergey** 36:17 Yeah, yeah, understood.
**Chris Lightfoot-Wild** 36:17 way, and….
**Sergey** 36:18 Definitely, I will be glad to post anything like that, like, unfortunately, this is exactly a question that I sometimes rise to my management. I would like to get reports from the field to better understand, like, if they are losing some, you know, some sales pitches, like, why, what is missing.
From the product, but, yeah, I definitely, like, every time I will get feedback like that, that is, something that is relevant to the HP part, I will definitely be glad to post it now in community Slack as well.
So, I will, I will follow up on that one. I just saw that a couple of minutes I got response from the salesperson, if, if there will be any useful information there.
I will, I will continue that one that's read on Community Slack.
And also I will follow up with, maybe I will try to run it as well, see…
maybe find some solution that you propose to environment variables, but, yeah, sure, I mean, we will definitely… I, definitely, yeah, we will try to… every time we encounter anything like that, we will try to share it with, the group and communities, like, if it's relevant.
Yeah, if it's not something elastic-specific.
No problem there. I definitely understand the need there. Like I said, I'm also always glad to hear, like, if there are any challenges, how we can improve.
And, yeah, definitely getting feedback is very valuable from the real customers.
No problem with that.
That was a good discussion.
**Bob Strecansky** 37:55 That was a good discussion that I wasn't expecting to have today.
So, buddy.
**Chris Lightfoot-Wild** 38:02 I'm a bit jealous of anything that Brett's got such bleeding-edge tech at work. I'm still…
we've got some of this hotel stuff locally, but I'm still, like, advocating to try and, you know, get it in production, and …
Fight that fight, so, ….
**Brett McBride** 38:18 We do have some bleeding edge stuff. We also have some PHP 5.6, so….
**Bob Strecansky** 38:25 Hey.
Hey, it's okay.
Legacy code is effective code.
**Brett McBride** 38:31 It's….
**Sergey** 38:31 The extra….
**Brett McBride** 38:32 battled.
**Sergey** 38:33 I don't know about effective, but the analogy that I heard is that, like, obviously developers complain when they work on a really old legacy project, and somebody, I wasn't
I think it was a Russian conference, maybe 10 years ago. Somebody compared to be the, you know, veterinarian handling, like, old dogs, right? So, like, people really want to care about the old animals, right? So they're ready to pay a lot of money
So, kind of like, yes, you might be not in the position where it's not the coolest technology and all that, but the amount of feedback that you will get from the customer, and you know, like, appreciation when you fix it for them, and they can continue, kind of like, because, yeah, I guess it's not a direct analogy.
It's not, like, inevitable, like, with the animal, but still, like, the approach is the same. People would prefer to get, fix, local fixes of, you know, giving them some kind of, like, broad suggestions, like, just upgrade to…
Each new SPSP, which is my…
Might not have been possible, it might be a huge project, yeah?
**Bob Strecansky** 39:33 Just upgrade to a new dog.
**Sergey** 39:35 Yeah, exactly. So… so yeah, that's an interesting analogy, like, you definitely get much more appreciation from the customer when you solve that problem for them.
**Bob Strecansky** 39:45 Oh, I don't know if y'all know this, but this is a great analogy to go along with your story. Do y'all… have y'all… are y'all familiar with Old Yeller, the American Story?
**Brett McBride** 39:54 I understand.
**Sergey** 39:55 Okay, so, well, it's not the story, it's the movie, right?
**Bob Strecansky** 39:57 It's like… it's like a children's book that, like, got straight into a movie. Yeah, and it's like, they have to put the dog down at the end of the day, like, what are we old yellow ring in this situation? I think PHP has tried to Old Yellow 5-6 for a while.
**Sergey** 40:15 Yeah, huh?
**Brett McBride** 40:16 Yeah, it's an interesting calculus for us, because we're paying for extended support.
Just in case. …
at some point, it's gonna cost too much. The amount we're paying for support is worth spending on upgrading.
**Sergey** 40:33 Is that some third-party companies, or are you paying Zend? Zend provides support, different… Previously, we did buy it through Zend.
**Brett McBride** 40:40 Possibly through Red Hat now.
….
**Sergey** 40:45 Oh, really does it? Okay, interesting.
**Bob Strecansky** 40:48 I wonder… so… I'm, like, so cynical there, like, I wonder what they really do any differently than…
just letting it rip. It's like they're just, like, monitoring for security vulnerabilities and patching them, I guess.
**Sergey** 41:02 But this is what you want, like, essentially, a lot of it, you know, it's like financial advisor, right? Maybe that doesn't do anything, but the fact that it exists, a lot of people will not do stupid things because of it, right? They will just rely on the fact that somebody tells them, okay, just relax, like, okay, it's… maybe it's minus 60, but…
You'll be okay in a couple of years, right, so…
I mean, minus 60% of your portfolio, right? So, some people might say that even the existence of that support just gives them some kind of confidence that they don't need to get nervous every time they hear about some zero-day vulnerability, something like that.
**Bob Strecansky** 41:38 burning your support. Anyway.
**Sergey** 41:41 So maybe they don't do anything. I mean, technically, I assume somebody would have broken in, like, so I guess they either do something, or…
Because otherwise, we would have heard, right?
site's been broken, the ones that use speech P560. I guess they do something.
Oh, that's not happening.
**Chris Lightfoot-Wild** 41:59 Maybe they hide that somehow.
What would be good on the back of that conversation, I don't know if… I think we've been here before, but obviously we don't have in our pipeline any of these
kind of exotic runtimes and whatnot, so testing against them is…
up to the developer. I guess so, but I think it's….
**Sergey** 42:18 I think it's always a good idea to first get some real requests, right? Because otherwise, you will kind of, like…
I don't remember how it was, what is that concept? Shooting and running, or something like that? But, you know, like, you have constant barrage of new incoming technologies, just keeping abreast with all of them will just be, you know, constant full-time thing.
So instead of, you can say just, okay, let's delay it until we will get somebody who actually wants to use it in production, and wants to use it with OpenTelemetry.
Then we can at least dedicate time
But, yeah, so, I, for example… I mean, yeah, if you're into trying to test them, maybe it's… if it's a quick thing, it can be quickly added to the test that is done.
Probably a good thing, but sometimes just, you know, understanding how to use them and bringing up the environment, this is, like, sometimes even 80% of the work, right?
**Bob Strecansky** 43:09 Yeah, it's… I mean, that's… that has been a problem since the inception of this project. It's like, how do you focus your time and attention on what is quote-unquote important? Because what is important to one person is not necessarily important to another person, right? Like, I may want to use Roadrunner, and Chris may want to use
Frank and PHP, and I may want to use Woolean, like.
you have to determine how, like, how to support all of these effect… you can't support them all effectively, so you just have to make your best effort to try and support each of these silos and do what you can, but we have to remember that it is a best effort. It's not… we're not officially supporting Frank and PHP because
you know, developer X came and said, do you need to support this, right? Like, we have to be conscientious of how we're using our time and attention in our community.
**Sergey** 43:56 Yeah, I guess the expectation from Community Project is that developers don't come in and say, please support it, but instead they come in and say, okay.
please take a look, I would like to support it, can I, you know, contribute it, right? So that's, I think, the expected approach, or at least you see that there is a desire to contribute at least some part of it, right? Maybe provide an example environment and expected output.
So, some kind of, like, expertise can be already drawn upon. Because sometimes, if you have these advanced technologies, you're not always even sure what is the expected output here, like, what does it do? Like, how would you… how would you like to see, like, what is… like, what we discussed with Laravel Events, like, to even understand, like, what would you consider to be the important…
Parts of those, you know, like, of those events, or whatever happened in there, what you would like to capture, yeah?
In order to understand.
**Bob Strecansky** 44:44 8.
**Sergey** 44:45 Domain expert at some… to some degree.
**Bob Strecansky** 44:48 Exactly.
And yeah, it gets even worse when you have, like.
paid third-party providers that don't… you don't have the ability to try, like, you know, Honeycomb wants to do a PHP implementation, and then you're like, well, I don't know if this works or not, because I don't have access to Honeycomb, so…
Michael bothered me.
**Sergey** 45:06 I know that Facebook have their own thing, but …
I never heard any, but I guess they also have everything else that they own, like APM or telemetry, and they probably do everything in-house.
Because I never had any kind of, like, requests for the classical APM or anything like that.
That mentioned Facebook. Oh, it's called Hack or something like that?
**Bob Strecansky** 45:26 Yeah, that's right.
**Sergey** 45:29 So I guess they do everything in-house, they have the money.
**Bob Strecansky** 45:32 I got the money.
All right. Anything else?
**Sergey** 45:37 But anyways, let's follow up. I mean, currently, I will try to understand what they use, so if I understood correctly, Laravelock 10 by itself is just a middle thing, so they probably use some additional concrete technology on top, so I will report back on the Slack, and…
At least we'll see how we… what we do with this concrete use case.
Then we can see if we want to add a tester to it as well, so…
To, to the country, yeah.
**Chris Lightfoot-Wild** 46:03 Sounds good. Thank you.
**Sergey** 46:05 Thank you, guys.
**Bob Strecansky** 46:06 Alright, we'll see you on the internet.
**Brett McBride** 46:07 Thanks, Al. Bye.
**Bob Strecansky** 46:09 Right.
