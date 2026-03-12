SIG: Arrow SIG
Date: 2026-01-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Albert Lockett 00:01:06 Hey, Drew.
drewrelmas 00:01:09 Hello.
Albert Lockett 00:01:14 It's like we've got… Polar signals here as well.
Hey, Mike?
We're all…
Laurent Querel 00:02:12 Hi everyone, I think you will.
drewrelmas 00:02:14 Hey, Happy New Year.
Just getting it out there, I have a conflict again at 2, so I'm only gonna be here for the first half, but I wanted to hear it because we have some cool stuff going on from Albert.
So I wanted to at least make the first half.
Albert Lockett 00:02:39 Sure, sounds good. Yeah, so I guess, yeah, given that, given that we've only got Mike here for a limited time, maybe, I'll just, I'll just jump right into it. So I'll share my screen.
And I can talk about, what, what was just mentioned. Okay, so share the screen.
So, let me paint the picture here.
So, I had this PR open that adds, this new syntax to the, supported by our KQL parser, right? So this is, like an if-else type of statement that, Would be backed by the, the conditional data expression that, that got merged into the, into our ASTIL, expressions, before the holidays. So, as, as we were reviewing this, Drew pointed out, a pretty good suggestion, actually, which was that instead of just, putting this into the existing, KQL… parser, what if there's a way that we could, say, take all the, take the existing KQL parser, and sort of add… create a new parser that, extends the, extends the base language in, in a certain way. So, we see that Pest actually kind of… supports this, where, you can have your base language, and then maybe, some additional rules, when you derive the, the pest parser. And so the idea would be let's leave the, the existing KQL parser, kind of as is, and create, a new parser for our, our, kind of… Skunk Works OPL language that, supports these additional, these additional language features. So, That's the… that's the problem statement here.
And this, this kind of large and somewhat scary PR is actually, is actually what what implements that. So, so what I did was I, let's, let's, look at… the KQL parser here, so this is the existing parser. So what we can see here is now the, the… all the… all the parser rules that would be shared between the existing KQL parser and our OPL parser, which the intention of that is to support this if statement, plus a few other additional operations, like route to and fork, that we had planned.
All the… all the rule… the parser rules that are shared are in this base.pest, and then, we have… we can add overrides into either, kql.pest for… for anything that's… that's not shared, or, in, in opl.pest for anything that would be OPL-specific, and I didn't add the if-else statement in this yet, I was kind of keeping that if-else… implementation and this, splitting the parser into separate PRs, so that's why we don't see that here. So that's how the… that's how the parser rules are organized. Now, there's a lot of extra code in this, in this PR, and, let's talk about, kind of why that's necessary, because I think it'll make reviewing it easier. If anyone doesn't have any ques… sorry, anyone can stop me and ask questions at any time, otherwise I'll just keep… keep talking. I have one…
drewrelmas 00:07:27 small one, I think?
Albert Lockett 00:07:29 Sure.
drewrelmas 00:07:29 Which is, I'm just curious about what was left in kql.pest. I noticed it was the user-defined functions layer, as well as summarize. You chose not to bring into the base.
Albert Lockett 00:07:42 Yup.
So.
drewrelmas 00:07:44 And one other follow-up is I know there's a lot of stuff… I think there's a lot of stuff in the base right now that the… I know this is driving… we haven't gotten there, I know this is driving towards columnar engine, that the columnar engine doesn't necessarily support just yet. So, how did you choose what you put in base versus kql.pest? Do you not have a requirement for a summarize operation?
Albert Lockett 00:08:11 I… I'll admit that I didn't go… I didn't go too, too deeply into it, so maybe… yeah, you're right, that's a good call-out, like, maybe this… this, this, needs another pass. Currently we… like, I don't think we would support the summarize operation, right? Because as far as I know.
the, like… the summarize operation doesn't, doesn't, like, modify the actual records, does it? It just creates, like, a… like a… Like, a summary that… that…
drewrelmas 00:08:47 So, Glenn, Mike will be able to explain this better than me, but, that's… that was the intention. Our record set engine, and, like, the bridge component that we have just takes the summaries it produces, and it treats… and it converts those into actual log records, and returns that as the payload out of the processor. So… You're right that like, natively, it produces both your logs and, like, distinct summaries as a separate entity. Our requirement was take those summaries and return them as structured… as logs instead. But… I don't think we need to get too deep into the… too deep into the details.
for this discussion on that topic. It was just something I was curious about. I don't want to, derail on it.
Albert Lockett 00:09:47 Yeah, okay, that's… that's interesting. And yeah, I guess, I guess I… I didn't know that the, the, the OTTL bridge did that, and I, I left summary out, specifically, just because, A, I didn't know it did that, and B, just, like, to have, like, at least one thing that's this distinction between, like, between the KQL parser and this new parser, just to kind of prove out that, like.
we can have, like, a language feature that exists in one that, like, doesn't exist in the other, right? Yeah, okay.
drewrelmas 00:10:22 I understand it from that perspective.
Albert Lockett 00:10:24 Yeah.
Laurent Querel 00:10:25 Yeah, and we can always move the… this, summarize function in the base, if we figure out that it's interesting for the OPL language.
Like Albert said, I think the… The point is to have, A pass to let each independent language to define their own custom specific thing.
And because we are in this exploration phase between two or three languages.
Maybe things will move a little bit, but at least the infrastructure will be there.
Mike "Blanch" Blanchard 00:11:03 Yeah, I don't know, I see a lot of thumbs up there, but I… I have a feeling that's the wrong direction, because if you want OPL to be a superset of KQL, there should be nothing that the KQL parser can do that you can't do in OPL.
So I think you need to make a fun…
Laurent Querel 00:11:19 I think… I don't think that we have a particular DQA.
Mike "Blanch" Blanchard 00:11:23 A language or a superset?
Laurent Querel 00:11:26 I don't think we are… I don't think we are creating a superset.
Mike "Blanch" Blanchard 00:11:30 Maybe it's the wrong direction to mirror KQL in the first place? Just change your syntax.
Like, why… why go through… the effort to have it look like KQL if it's not gonna do what KQL does. Do you get what I'm asking?
Laurent Querel 00:11:50 Because I… So we… what we said initially was we are creating a KQL-inspired language.
Does not mean that we are doing everything that KQL is doing.
So… if your parent is saying, why not having… so I think that what Albert did here is… what we… what we think is the KQL-ish, or form.
is in base, everything that is, purely KQL that we don't want to inherit.
could end up into the pure KQL, paste grammar. I think that was the… the… let me know, Albert, if you agree with that, but I think that was the… the initial idea, and…
Mike "Blanch" Blanchard 00:12:43 That's… that's well and good for your purposes, but… you know, we're gonna have to continue work on our KQL engine.
And I don't want to have to deal with the maintenance here. This is introducing to worry about the OPL side of it.
Just fork it, if that's what you want to do.
Albert Lockett 00:13:06 Right, I mean, that… I mean, so that's… that's another option.
I guess, I guess I was thinking that, you know, there's… there's certain, There's… there are certain expressions that… that have, like, a really similar form between KQL and, an OPL, so I'm thinking things like You know, like, logical expression, and scalar expression, and And, and things like that, right? So, like, what I wanted to… avoid from a maintenance perspective is trying to say, okay, you know what, we have two separate pieces of code that are parsing, basically the same rule into the… into that… that AST slash… slash IL into that expression language. One of them's in the KQL parser, and one of them's in the, in the OPL parser. So, like, what I was trying to do with this PR is set up The structure that we could use to share those code for those common rules.
Mike "Blanch" Blanchard 00:14:20 I understand, you want to reutilize the work.
Which I'm totally fine with.
I just don't want to assume the maintenance burden.
And if we're doing all of this just because you're saying you don't want summarize.
Take my word for it, you do want sunrise. That's the killer feature in the whole thing.
Laurent Querel 00:14:41 No, I think we… it's a misinterpretation. We are not saying that we don't want summarized. We just don't know yet.
What we don't want, for example, and that is sure.
We don't want this implicit, rules for the access to some field that are sometimes field and attribute. That we don't want. We don't want to inherit of that, for example.
Well, to summarize, I think it's a totally open question.
drewrelmas 00:15:10 So.
Laurent Querel 00:15:10 And I agree, I mean, summarizing things is important also for us.
drewrelmas 00:15:15 Wha… Yeah, I… I think what would be helpful is if we understand Yeah, I think we need to look at the code a little bit more and understand what maintenance there could be that I think Mike is worried about. Another thing I'll point out is the… the part… the implicit, attributes map I think you're referring to, Laurent. That's… it's a… kind of an options thing that you can provide to the parser, if I remember correctly.
So it's… OPL can just not allow providing options, and then the default map just is ignored. I think the main part of the code for that is in… the parser abstractions subfolder, not necessarily in KQL parser or OPL parser, but the fact remains it's still up to the caller to decide if you can pass options or not. And if you don't pass options, then there will be no default map, and everything has to be explicit.
The main reason we have that is just a business requirement on our side. But I think I agree with you that it should be optional, but it's… Not necessarily in KQL parser, I'm fairly certain it's in the abstractions, layer that both would continue to share.
Laurent Querel 00:16:40 Okay.
Mike "Blanch" Blanchard 00:16:41 Yeah.
Albert Lockett 00:16:42 Yeah.
Mike "Blanch" Blanchard 00:16:43 There's a whole bunch of different modes in the parser, and what you can do when you give it schema, and how you mess with those options.
So, what Drew said is we needed that fuzzy matching for how we're consuming The parser currently.
But how it's exposed in the arrow form of the collector.
We don't have to do the fuzzy matching.
Albert Lockett 00:17:10 Yeah.
So I think that one thing that Drew said is, Maybe it makes sense to kind of, like, step a little bit more deeply into the code, and we can try to understand, like.
like, what has changed from, from a maintenance perspective, or, or, you know, like, what are the, what, like, what's the additional development burden as, as we're, evolving the KQL parser?
And I tried to implement this in a way that… that will be… As minimal as possible, so we can look at it, and then… and then we can decide whether that's, that's… that's too much overhead.
Mike "Blanch" Blanchard 00:17:53 We just throw, like, a simple case at you. Let's say somebody from our team comes and says, hey, I got a user asking for Let's say, extract red jets.
So they want to go and extend KQL to support this KQL scalar.
Do they put it in base, or do they put it in KQL?
Albert Lockett 00:18:14 Yeah, so, Okay, so, so let's, let's, let's… Let's say, for the sake of argument, that we put it in, in… in base.
Just, just for the sake of argument, then we can walk through the code. So, we could add a new rule to, to, to based.pass somewhere in here.
Mike "Blanch" Blanchard 00:18:43 It's not… it's not a question of how it's done.
The question would be, how does… how does that developer know?
They come to me and they say, Mike, Blanche, Where do I put it?
And I go, I don't know, does OPL want to utilize it?
Albert Lockett 00:18:59 I mean…
drewrelmas 00:19:02 That's fair, it's like, does anything…
Mike "Blanch" Blanchard 00:19:06 We should add, basically, a dependency into what otherwise would be just a routine work thing. You know, we're just adding a scalar, we've done it 50 times.
maybe we'd want AI to do it, I don't know, but now there's this whole new element in here where we have to worry about this other thing that has different stakeholders. You kind of get what I'm saying?
drewrelmas 00:19:33 So, yeah, it's like, if we want to add something to KQL, does it have to come through you first to decide if it's something that OPL wants to extend or not?
Albert Lockett 00:19:50 Okay, and, and… Okay, so you're thinking that, like, from the perspective.
drewrelmas 00:19:58 It's more of a logistical concern.
Mike "Blanch" Blanchard 00:20:01 Yeah, we just want to be masters of our own fate when it comes to the KQL world, and we want to be able to spin without having to worry about, you know, things that have co-opted it.
Yeah. I think it would probably be fine.
If we cross that bridge and we come to it, and just say, right now you're a superset.
And then if we do something crazy, and you're like, no, no, no, no, we don't want that, then we could do something. But I don't know if we need to… starve here, does that kind of make sense?
Albert Lockett 00:20:31 S… .
Mike "Blanch" Blanchard 00:20:33 like, let's take Summarize. Like, let's say you just consume everything. You still have the ability to override it, so you could just… You know, the pest… the KQL pests will define summary, but in your grammar, Yep.
put in an override of it, or you parse it into an error and just say, this is not supported. I don't know, you take some action to make sure that it doesn't actually get emitted. Would that be possible?
So basically, you opt out of things explicitly, and everything just comes in implicitly.
Albert Lockett 00:21:09 Okay.
Mike "Blanch" Blanchard 00:21:12 If you need to think about it, it's fine.
Albert Lockett 00:21:16 Yeah, we could do that too. So then, okay, so, so, so… The implication, then, is if we did that, the… the KQL… Syntax could just evolve without any consideration of anything that, that… Is extending it, and then it's on the… And so that cuts down the maintenance burden from the KQL side.
And then, on the… On the derivative languages side, those languages need a mechanism to say, hey, we don't… We don't support this type of expression and catch it up at the parser at the.
Mike "Blanch" Blanchard 00:21:58 Yeah, we've actually had… sorry for interrupting on… we have another team that's looking at using the record set engine in some different agent that has nothing to do with OpenTelemetry.
and correct me if I'm wrong, Drew, but they have asked for sort of a similar thing. It's like, in their queries, they don't want to allow people to call things like extractJSON.
Albert Lockett 00:22:19 So what we were thinking is.
Mike "Blanch" Blanchard 00:22:22 we would extend the options that you give the parser, and you could give it a list of things, or somehow there's some mechanism to say, like, I don't want these features to be available, and then the query would just emit, you know, oh, you've typed summarized, that's not supported.
Maybe we could just do that, and that would work for you guys.
Albert Lockett 00:22:43 Okay, so the… so, okay, so the, so instead of having… A, like… like… sort of, like, different… different pest grammars like this. We just have one… one… One big grammar, one big parser, and then you control which language which…
Mike "Blanch" Blanchard 00:23:11 So you probably still need the base grammar stuff, because you want to have your… you want to have the if-else stuff, right? So you're gonna need your own grammar.
So what I would think is, like, when you… build your OPL parser. You say, okay, use the KQL grammar.
use the OPL grammar, but then when you're calling into some of these, it looks like you refactor things so you could call into them. Maybe we just update those APIs so that, like, when you're parsing a tabular function, you can say, don't allow summary.
So as it's doing its work, and it sees in the rule tree, the pest tree, oh, user did a summary, instead of creating that in the AST, it'll just return an error saying summary is not supported.
At line 10, or whatever the heck.
drewrelmas 00:23:59 So I… if I understand correctly what you're proposing, essentially, we don't need a separate base.pest and kql.pest in our.
Mike "Blanch" Blanchard 00:24:09 You know what I'd like to see is because we just have kids who are on the list.
drewrelmas 00:24:13 We just have KQL pest, and then it's the responsibility of a derivative language to… Opt out, or ignore.
expressions that they don't want. So… I mean, essentially, this would be like a match statement with rule, and you only match against the rules that you want to support. And if there's a rule you don't want to support, you should have a default catch-all that just says, don't support. So in this way, the derivative grammar becomes an explicit.
Inheritance, where you have to If you want a rule from your bait… from the base KQL.pest, you have to explicitly handle it.
Mike "Blanch" Blanchard 00:24:55 It could be explicit, I was thinking more, you know.
I haven't seen all this code, but I'm just guessing by the refactoring that, like, the OPL dedicated parser is calling in to some of the KQL functions.
So instead of having them to write their own match, you know, with a case for everything, they would call the KQL version, and they'd pass, like, a bit mask or something that says, like.
Summary is not supported.
And then the KQL parser's match would just have a little if check, and says, oh, if that bit mask says it's not supported, I just spit out an error.
drewrelmas 00:25:31 Oh, I see.
Mike "Blanch" Blanchard 00:25:33 help a little bit. I'm down to, like, you know, we can extend our stuff to make it very easy to do this.
Because I have a feeling, like, you know, Victor's gonna need some of that, Drew.
drewrelmas 00:25:45 Laurent, your hand up.
Laurent Querel 00:25:47 Yeah, I get the sense that maybe we should share the same AST, but not sharing the same grammar at the end, based on the conversation we just had.
Because… Even with this approach that may help you… you are describing.
like, a KQL with some optionality.
I'm afraid that, would we, Again, the same conversation in a few weeks or few months, because we will have some incompatible… or incompatibility into the grammar.
So maybe it's more reasonable just to share the ASC, And we follow the initial premise of this project. We have a single AST, we have multiple engine, and we have potentially multiple language.
And the top-level language, they are independent. Okay, we are KQL-ish, but we are not 3D KQL.
We… we are coming with some different, perspective and different principle.
So I'm just… based on this conversation, I have the feeling that maybe that's the wrong direction, and maybe we should, Separate the granular.
Which will imply, duplication, some duplication of code, if I understand well.
What do you think, guys? Albert, Michael, based on that?
Albert Lockett 00:27:25 Yeah, I, I think, I think that could… That could… that could be another, another option, Yeah, I do think that, we probably would have some… Some duplication of, of code?
Unfortunately. Okay, so, you know, let's say for the sake of argument we do that.
I guess, like… If we accept that, we're going to end up, like, duplicating a bunch of the code, essentially, like, forking the, the KQL parser and having, like, two copies of… you know, parser for a logical expression, and scalar expression, and things like that.
And those can evolve independently.
If we're okay with that, then that's definitely the, the… Probably the easiest option.
Mike "Blanch" Blanchard 00:28:44 Yeah, I think the pro there is, you know.
You're your masters of your own fate, in that case.
work to… Do whatever you want. You're not inhibited by anything.
The big con would be… You know, there's a lot… of scalar functions and features in KQL that we don't currently support, and we'll probably be adding them.
So, I'm sure there's gonna be stuff we're gonna add, like the regex stuff, that you guys would like to have. So you'll have to manually, you know, merge those things and deal with that.
keep.
So you just have to kind of… The flip side would be, if you were a superset, you would just get all of that for free. And I don't… I can't say, you know, I don't have a crystal ball.
if it's gonna be more the case, we add stuff you want versus we add stuff you don't want, or if we're always adding stuff you don't want, and it's gonna be, you know, you get what I'm saying, like, there's a trade-off that has to be made, and I don't really know.
Laurent Querel 00:29:50 Yeah.
Albert Lockett 00:29:51 Yeah.
Laurent Querel 00:29:54 Yeah, I think we need to think about it.
Mike "Blanch" Blanchard 00:29:57 There are a lot, a lot of functions to find in KQL.
Albert Lockett 00:30:04 Yeah.
Laurent Querel 00:30:05 And we will have functions, so that one of the main, difference or, principle that we… we don't share, I think, between, KQL and, NOPL. KQL is, like, a generic solution.
that Microsoft is using on multiple products, multiple contexts.
OPL, the O is Open Telemetry.
We will deliver functions.
That will be, tailored, optimized for this specific context. So we will have a lot of very dedicated, very specific Signal… signal-oriented, attribute-oriented functions.
That will not, necessarily be a good fit for KQL.
So, because it's a generic solution, so they will end up with generic functions, Yeah, I'm saying that because I think, the more I'm thinking about it, the more I think we should… I obviously want to talk about that in more detail with Albert before we take a decision, but My feeling right now is… It will be better to have a different, a different grammar, and, and… and try to share the same EST as much as possible. That will reduce the, anyway, the… That will give to the end user options to go from one system to another.
Or one language to another zero. But, Yeah, it looks like a more rational approach, and… And less problematic.
Albert Lockett 00:31:56 Yeah, after… After, after hearing the feedback, I, I agree, Laurel.
Okay, sorry, Mike, I don't wanna… I know that you had a… you had a hard stop at.
Mike "Blanch" Blanchard 00:32:10 I'm good.
drewrelmas 00:32:10 That was… that was me.
Albert Lockett 00:32:12 Oh, that's true. Okay, sorry, I was…
drewrelmas 00:32:14 I sent a message in the chat, I am gonna drop in a minute, but… I just want to say thanks for the conversation. I think I'm very, very much in favor of keeping the same AST. I think this conversation is almost, as I said in my comment on Albert's PR, like a validation that that was the right direction.
I… yeah, I… lost my train of thought, but that's all I have to say, I think. So, I'm gonna drop, and I'll try and catch the… second half, if there's the recording. Thanks, everyone.
Laurent Querel 00:32:55 The…
Albert Lockett 00:32:58 Okay, cool.
Okay, cool. So I think, I think where we've landed then… is… It probably makes sense to have, for the OPL parser to have its own grammar.
And then, obviously, we're gonna keep sharing the same, the same ASC, I think that was always the plan. And then, There's just a matter of the, The code that takes the parsed.
pest rules and turns them into the, Turns them into the, Into that AST… we have a lot of code written in the KQL parser that does that already. So, you know, one option could be, okay, as a start, we just… fork the KQL parser.
keep all of that, keep all of that code, and then… and then we have, like… like, Mike pointed out, then we're each masters of our own destiny, going forward from a… from a maintenance perspective, and, And the downside there is, is… you know, not having that code shared is that, if the KQL adds something, and the OPL says, hey, that's a nice idea, I'd like to have that as well, we then end up having to… do that, do that implementation twice. But, you know, the upside of that is, the KQL site has freedom to evolve as it needs to, and doesn't have to worry about breaking that shared code, and vice versa. So, you know, maybe having that parser handling code duplicated is not so unreasonable.
Mike "Blanch" Blanchard 00:35:18 Albert, if you want to try to share it somehow, I don't have an issue with that.
Whatever you think will be easier. Yeah, it is a lot of code, and… It is pretty intricate code.
Albert Lockett 00:35:32 Yeah, so, part of, like, part of this code was… was trying to make the signatures of these functions, something that can, be generic over the, like, the derived pest rule that was, like, so, so in pests, like, with your… with your grammar for everyone, just for folks who are interested in what I'm talking about here.
When you… when you use the pest-derived parser, it, it derives a, A rule enum?
So you'll have an enum that… oh, my keyboard's not working. Hold on.
You'll have an enum with a… with a variant for every… For every rule that you've, defined in your… in your pest grammar, and then in our, in our parsing code, if I go look at one of these, We see that, okay, for, you know, this rule.
If the rule we're parsing is this variant of the rule enum, then do this, and… like Mike said, that's, that's… that's… that's intricate code that's… that hap… that's kind of spread all over the place. So part of what I tried to do in this PR was make the, was make the… Those functions generic over the, The type of, the type of rule.
And so, you can see here that, we have this trait called try as base rule that, was converting, the, the rule for For the KQL parser.
Back to a rule enum that was derived for the base rules, and then all the… The parsing code for those shared expressions, became, generic over a type of rule that can be converted into that.
base rule.
So anyway, I guess the reason I'm bringing this up is, like, A, to explain what's happening in this PR, but also to say that, like, like… it was a bit of, a complicated hoop I had to jump through to get that to actually work, because, you need to define, if I go look at that trait.
The base rule needs to have a try-from implementation for the, for the specific rule. And so… To make that try from implementation work, like, you'd essentially need, like, a big match expression, like, if it's… if it's the… this variant of the… of the KQL rule enum, then it's this variant of the base rule enum. And then so… I… Created a procedural macro that That creates that, that try from, what do you call it? That try-from, implementation. So, so anyway, So, I guess what I'm saying is, like, if… If we… if we did want to… continue to share these, like, parser, handler, The functions, like we have here. Then, it's… it's… like, we have to, like, jump through a similar hoop, if that makes sense. And if that's okay, then… then that's… then that's great, and we'll continue to do it, and if that's not okay, then, we'll… we'll probably just need to have two implementations of it.
I think I saw a hand up, but it went down.
Mike "Blanch" Blanchard 00:40:07 I had a comment, but then I realized it was wrong, so I put my hand down. I was gonna ask, Is this refactoring… generic stuff, is it one-time pain? Or, like, what's… what's the effort required when you want to put in a new rule? What do you have to do?
Albert Lockett 00:40:24 it's, it's… it's essentially a one-time pain. Yeah, so, like, befo- and then when you go to, like, write the, the, like, the parser function, instead of just writing it like we would before, where you would just, you know, write a… write a function that just takes, like, pair rule as the… as the type for the argument.
Going forward, you would have to write a function signature that's generic over… The rule, and then… Also…
Mike "Blanch" Blanchard 00:40:59 And what's…
Albert Lockett 00:41:00 implements some…
Mike "Blanch" Blanchard 00:41:02 Hypothetically.
In that list down there.
Let's say I add, I don't know, what's a new type of literal we could pretend exists, like a GUID literal?
Albert Lockett 00:41:13 Oh, yeah, so that would… there would be no, like, no huge additional maintenance burden. You would just need to do Rul, GUID, literal… parse, GUID.
Literally. For that to work, we would need…
Mike "Blanch" Blanchard 00:41:30 GUID literal would have to exist in the OPL and the KQL grammar.
Albert Lockett 00:41:36 No, it would just have to exist in the, in the, in the KQL grammar. And then, it would just have to exist in the KQL grammar. And then in the, in the, so we would probably change this. We would probably call this, like, try as KQL rule, and then, like, the implementation of this for the… for the… for the… the… the rule from the other language would just, like, throw an error here and say, hey, I can't, like… I can't convert to… Or sorry, I guess it would just… it would just never, it would just never, like, create an instance of its, of its rule that matches this variant.
Mike "Blanch" Blanchard 00:42:29 Okay.
I'm fine with that if you want to do this one-time refactoring so you can call into this code.
Albert Lockett 00:42:36 Okay.
Mike "Blanch" Blanchard 00:42:37 There's value there in, like, bug fixing, and, you know, it also makes it easier if you come around and say, oh, I actually do want a GUID literal, then correct me if I'm wrong, then you just throw in that rule in your grammar.
do that little mapping, and now you have GUIDs, right?
Albert Lockett 00:42:54 Yep.
Mike "Blanch" Blanchard 00:42:55 It seems like kind of a sweet spot.
Albert Lockett 00:42:59 Okay, cool. So, I guess… okay, yeah, I agree with that. So I guess in this case, then, what I'll do… Okay, so in terms of, like, moving this PR forward then, what I'll do, is this kind of, like, refactoring to make these, these functions generic. I'll keep that in. I'll remove, how the, How the… the grammar is… is split like this?
Because, like, from the KQL perspective, we don't want, like, a base in the KQL, We just want a, one grammar. I'll create a new grammar for the OPL parser.
And it will have a similar grammar to the kql.pest.
And then I think… I think that puts us in… in a… in a good place.
Mike "Blanch" Blanchard 00:44:07 Sounds good.
Albert Lockett 00:44:09 Okay.
Okay, cool. So then, yeah, and so then I think going forward, It's a good expression. We're masters of our own… we're masters of our own destiny, but we… we still have the… the opportunity to… Reuse, a lot of this kind of, like, code that handles these rules and turns them into a, into the AST if the opportunity to reuse that code should arise. So, I think that's, Yeah, I think that's a good thing.
Okay.
I see I get a thumb up from the one, too.
Awesome. Okay. So, yes, I'll… I'll make those changes… I'll make… all those changes first, I'll drop a message in, In, to, to, to all the folks who want to review.
That change, and then, we'll hold off merging this this PR that adds if-else1722, we'll hold off, like, adding that until that refactoring of the KQL parser is done, and we have the OPL parser, and then we can add this to the OPL parser.
So I'll mark this as a draft for now, if I can figure out how to do it.
Okay.
Cool, so that's all I had.
We didn't have anything else on the agenda. Does anyone have any, any other questions, concerns, or anything else they want to discuss?
Mike "Blanch" Blanchard 00:45:57 I can… Talk a little bit about summary. I saw your comment, Josh.
Albert Lockett 00:46:03 Oh, yeah, let's do that. I'll stop sharing.
Joshua MacDonald 00:46:06 Yeah, I want to keep it, like, light-hearted here, but… Yeah, I… I… I would be cautious about I mean… summarizes such a… it's the right verb, it's the right, you know, like, it's the right word, I think, but as for what it does, that seems like a… an area where a language has every right to experiment and, like, be unstable or, like, try to evolve. And I think OpenTelemetry is the area where I… where I want to see that land. So, like, I'd love to see a summarized operation that makes sense to OpenTelemetry.
But it would have to go through that kind of review that OpenTelemetry does, and So, so that could be a kind of target or a goal, maybe.
Mike "Blanch" Blanchard 00:46:55 Yeah, we should… this team… We should get on the same page, and then we should start working on the spec, because it's gonna take some runway, some time.
I did a really nice document that writes up how it's currently designed I think it got deleted when we switched from the proof of concept to the actual record set engine, so I need to go dig that up, but let me give you some history. So, I've talked to Josh a lot about summaries.
much of it is over my head, especially when it comes to metrics, so I really focus just on logs, but… There's all kinds of problems when we try to summarize at the edge or at an agent. You know, there could be one agent, there could be many agents, it could be forwarding to other agents, there's many hops and players before it gets to some final backend.
So… summary in general is kind of iffy, right? Somebody has to reconcile them at some point and combine them, and then we have the issue of late arriving data. So what I did in the tree and in the record set engine is I tried to solve those things for logs. I don't know if I nailed metrics, because it's… Crazy. But for logs, what happens is, when you summarize, basically you give it some aggregates, some group buys.
And the engine will track all that, and it will give you summary records.
And… a summary record is its own thing. It is not a log. The engine just says, okay, here's all the logs that got included, here's the ones I dropped, here's the summaries. And I also built it in so you could do things like sample logs. So you could say, I want a summary, you know, show me all the numbers, but take… you know, a reservoir of 20 logs. So you'll get a little bit of sample so that you can, you know, if you get a UI… like, KQL just gives you one record.
I don't really like that. I think we can do better. So what I built is a little more advanced, and I tried to take care of late-arriving data by, like.
when you get a summary back, it takes all those unique pieces of information, including the window and the range, and it gives you, like, a hash, a SHA-256 ID that's unique for that summary, it's… Dimensions, and its windows, so that they could all flow to some backend, and it could combine them.
That's what you'll find if you go in and look at the record set engine, like when you call flush batch. It's what it gives you back.
What we did for our initial integration is we used this thing called the OTLP Bridge.
That's where we put all the OpenTelemetry specifics for our implementation. So it owns the schema, it owns what to do with summaries. So what it does… is it takes all that great, rich, summary data and throws most of it away, and just emits a log record that looks like what you get in KQL.
So… that's what, kind of, we needed Drew and I for our customers, but what Josh is talking about is what I'd really like to see for open telemetry, is we take this great summary data and we put it somewhere that we've worked with the spec to say.
here's where they go. And then back-ends can understand it and do that, you know, recombination, reconciliation stuff that they need to do. In order for it all to work, we kind of need a dedicated spot to put it, if that makes sense.
So that's kind of where we need to design that, and then run it up the flagpole at the spec level, and see if we can get it in there? Does that kind of make sense? Is that where you… where you're thinking, Josh?
Joshua MacDonald 00:50:44 Yeah, I… definitely. So, so some… you may know, some of you, that I kind of run this sampling sig every other Thursday with our Thursday morning. So I've been doing sort of this conversation about sampling Which has been, like, the slowest moving thing in all of existence, or all of OpenTelemetry, but, there certainly are, more than one answer to, like, talking about sampling. You can… mostly we talk about trace sampling, but I also have nerded out many times on… weighted sampling, deterministic sampling, reservoir sampling, threshold sampling, all those things. And the reason why I like summarized as a verb is that, like, the… there's… There's lots of sampling in the world. It means many things to many people, but there's a sum being, like, computed, a summation happening.
when you sample with a weight in mind. So, like, the point of the weight in a weighted sampling arrangement is to calculate a sum.
or estimate a sum. And, so yeah, if you… if you turn… like, there's lots of ways you could represent that in an OpenTelemetry way, but none of it's really specified.
And, you know, I don't think now is the time to place… or time and place to talk about it too much more.
I've wondered whether we all, you know, I think it's worth looking at how OpenTelemetry has this exact metric exemplar concept, and whether that fits in with the model there as well. You could imagine turning.
Mike "Blanch" Blanchard 00:52:20 boo for…
Joshua MacDonald 00:52:20 Samples.
Mike "Blanch" Blanchard 00:52:22 The summary days?
Joshua MacDonald 00:52:23 sampling a bunch of exemplars with metrics.
Mike "Blanch" Blanchard 00:52:25 From the engine, it looks like metrics.
it's tempting. The only… the only reason I didn't go that road, just jump in there, is, like, on Exemplar.
something like… you can… you have a trace ID span ID, but there's no log ID. There's no way to, like, point to the log, but we could fix that. We could go to the spec for that, but anyway…
Joshua MacDonald 00:52:47 But what I'll do as an action item.
Mike "Blanch" Blanchard 00:52:49 I'll try to dig up my README that explains where we are. I'll try to PR that back into the repo so you guys can just review it.
And then we can start having conversations, I guess.
Joshua MacDonald 00:53:05 the… what Laurent just put in the chat is something I've, you know, I reserved or held back a little bit, you know.
we've got this sort of side project coming in, not represented in the room, but the Quiver project from Aaron, by our colleague.
here at Microsoft has some notion of time, that, like, it's sort of, like, future steps. We would love to be able to take your data that has timestamp data in it and, like, put it into the right bin so that, like, the, the, like, the passing of real time and event timestamp Are close and correlated with each other, so that you could actually put data into those temporal bounded, like, blocks that then let you summarize in a way that is composable, so that downstream Consumers can compose the data or combine it, like… like, aggregations that are done correctly can be combined later downstream.
So that's, like, what I would hope that we get to, is, like.
First step is we have temporal blocks.
you know, maybe we've got one Parquet file per minute, or series of Parquet files per minute.
And, you know, real time passes, you know, delayed from event time by whatever the pipeline latency is. So, like, a minute, minute and a half after your minute finishes, like, you better have completed all your collection, or else something's wrong. And you can… every collection interval is its own thing. Like, some of them are going to complete, and some of them are gonna fail, and… Like, once you bucket by time, then you can start doing really interesting summarization.
And that's when we can come back to OpenTelemetry's timestamps and stuff. Like, data model questions come after that. I think we need to build an engine that can compute those things, and then we'll talk about how to represent it.
But, it's exciting.
No, no comment required, no… take my answer off the air.
Mike "Blanch" Blanchard 00:55:10 I think… It's the untapped killer feature for OpenTelemetry.
like, I imagine this dashboard that's like, you know, here's… you got a thousand logs, and oh, here's 5 of them that had this unusual error.
go and look at those. Like, it's… It's desperate… sorely missing for anyone that's had to been on call and combed through 5,000 logs looking for something.
Laurent Querel 00:55:37 God, I mean… I totally agree that, having… Some kind of analytical capabilities part of the pipeline.
that are growing more than just filtering.
And… and reaching streams is definitively part of the… this kind of, processing language.
Either OPL or AQL.
But, that has to be done in relation with the open telemetry data model, in my view.
Because, at least for OPL, we want to deliver something that is Necessarily respecting the… the data model semantic.
Especially for the metric, which, like you mentioned, Michael, is a complex beast.
And without a good understanding of this logic.
And it's not a generic logic.
That will not be possible, and that's why I think OPL is… Tailored for open telemetry and not a generic language.
And, in addition to that.
The engine that will do this segregation, will do this summarization.
sampling… initially, for me, summarization was not necessarily sampling, but it looks like you put sampling inside the summarization, which is okay.
But, that has to be done in a way that could be achieved in a distributed environment.
Because doing that… With a single instance.
It's relatively trivial.
Doing that at scale is another… To click.
And there are multiple… Options to go in this direction.
One that, mentioned, brochure with, something like Quiver, or, A persistent queue of some kind, a distributed version of it, where we distribute the… or we partition the information, and we… we go back to a solution where aggregation could be done by one instance.
That's one approach, and there are also more complicated approaches similar to the ones that are followed by things like Flink or Spark.
Which deal with this kind of, with this kind of things, also.
Yeah, so my point is, obviously, we want to go in this direction with OPL, What we define into APL is a three-level that's… street capability level.
1… That is purely stateless.
So basically, the… the sub-language corresponding to the capability level 1, Does not involve any… State-oriented, function or stages.
And then we have the second level of capability that are introducing state only for streaming, and the third level that is introducing state, but also with fair system databases. So we are not talking, in that case, only about the stream, but potentially multiple, persistent collection, or tables, on which we can apply another superset of this OPL language To do things more complicated, like join between multiple data sources.
Which are not necessarily, supported in the capability level 2.
So the… because we are currently focusing for PL on the Cavity Level 1, that's why the Summary… summarization stuff was not a priority.
right now.
does not mean that it's… we are not considering it. We obviously consider it, but it's something for us that will imply State management in a distributed manner.
Okay, I think we reached the end of the… decision.
Albert Lockett 01:00:26 Yeah. And we reached a conclusion regarding the…
Laurent Querel 01:00:30 The grammar stuff, so that's cool.
Albert Lockett 01:00:34 Yeah, thanks, guys. I know it's a complicated problem, but, this is, this is super helpful. I think we came up with a pretty good plan.
Yep.
Yeah.
Laurent Querel 01:00:46 Brutal.
Albert Lockett 01:00:47 So, thank you.
Once again, we've done it. See you next week.
Laurent Querel 01:00:51 You, buddy.
